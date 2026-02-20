import datetime
import json
import math
import os
import pathlib
import typing
from collections.abc import Awaitable, Iterable, Mapping, Sequence

import anyio
import httpx
import pydantic

T = typing.TypeVar('T', bound=pydantic.BaseModel)


class PaginationMeta(pydantic.BaseModel):
    """Model for pagination metadata."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Limit of items per page (can be None sometimes, e.g. when specifying employee_ids[] in shift request)
    limit: int | None  # apparently this is can be None sometimes, e.g. when specifying employee_ids[] in shift request
    #: Total number of items
    total: int
    #: Whether there is a next page
    has_next_page: bool
    #: Whether there is a previous page
    has_previous_page: bool
    #: Start cursor for cursor-based pagination
    start_cursor: str | None = pydantic.Field(default=None)
    #: End cursor for cursor-based pagination
    end_cursor: str | None = pydantic.Field(default=None)


class ListApiResponse(pydantic.BaseModel, typing.Generic[T]):
    """Api response that returned a list of objects."""

    model_config = pydantic.ConfigDict(frozen=True)
    #: Raw data sequence from the API response
    raw_data: Sequence[Mapping[str, typing.Any]]
    #: Model type to validate the raw data against
    model_type: type[T]

    def data(self) -> Iterable[T]:
        for data in self.raw_data:
            yield pydantic.TypeAdapter(self.model_type).validate_python(data)


class MetaApiResponse(ListApiResponse[T]):
    """Response model that includes both data and meta."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Raw pagination metadata from the API response
    raw_meta: Mapping[str, typing.Any]

    @property
    def meta(self) -> PaginationMeta:
        return PaginationMeta.model_validate(self.raw_meta)


class ApiKeyAuth(httpx.Auth):
    """Authorization using an api key."""

    def __init__(self, api_key: str):
        """Initialize API key authentication.

        :param api_key: The API key to use for authentication.
        :type api_key: str
        """
        self.api_key = api_key

    def auth_flow(self, request: httpx.Request):
        """Implement the authentication flow.

        :param request: The HTTP request to authenticate.
        :type request: httpx.Request
        :yield: The authenticated request.
        :rtype: httpx.Request
        """
        request.headers['x-api-key'] = self.api_key
        yield request


class AccessTokenAuth(httpx.Auth):
    """Authorization using an access token. Not refreshing the session."""

    def __init__(self, access_token: str, token_type: str = 'Bearer'):  # noqa: S107
        """Initialize access token authentication.

        :param access_token: The access token to use for authentication.
        :type access_token: str
        :param token_type: The token type (default: 'Bearer').
        :type token_type: str
        """
        self.access_token = access_token
        self.token_type = token_type

    def auth_flow(self, request: httpx.Request):
        """Implement the authentication flow.

        :param request: The HTTP request to authenticate.
        :type request: httpx.Request
        :yield: The authenticated request.
        :rtype: httpx.Request
        """
        request.headers['Authorization'] = f'{self.token_type} {self.access_token}'
        yield request


class AccessTokenResponse(pydantic.BaseModel):
    """Access token response model."""

    model_config = pydantic.ConfigDict(frozen=True)
    #: The access token
    access_token: str
    #: The token type (e.g. 'Bearer')
    token_type: str
    #: Time until the token expires
    expires_in: datetime.timedelta
    #: The refresh token
    refresh_token: str
    #: OAuth scope granted
    scope: str
    #: When the token was created
    created_at: datetime.datetime


class RefreshTokenAuth(httpx.Auth):
    """Authorization using a refresh token which refreshes the access key automatically."""

    def __init__(  # noqa: PLR0913
        self,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        access_token: str,
        token_type: str,
        created_at: datetime.datetime,
    ):
        """Initialize refresh token authentication.

        :param refresh_token: The refresh token.
        :type refresh_token: str
        :param client_id: The OAuth client ID.
        :type client_id: str
        :param client_secret: The OAuth client secret.
        :type client_secret: str
        :param access_token: The initial access token.
        :type access_token: str
        :param token_type: The token type (e.g. 'Bearer').
        :type token_type: str
        :param created_at: When the tokens were created.
        :type created_at: datetime.datetime
        """
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.created_at = created_at
        self.token_type = token_type
        self._client = httpx.AsyncClient()

    @property
    def access_token_expiration(self) -> datetime.datetime:
        """Get the expiration date of the access token.

        :return: The expiration datetime of the access token.
        :rtype: datetime.datetime
        """
        return self.created_at + datetime.timedelta(hours=1)  # access token is valid for 1 hour

    def is_access_token_expired(self) -> bool:
        """Determine whether the access token is expired or not.

        :return: True if the access token is expired, False otherwise.
        :rtype: bool
        """
        return self.access_token_expiration <= datetime.datetime.now(self.access_token_expiration.tzinfo)

    @property
    def refresh_token_expiration(self) -> datetime.datetime:
        """Get the expiration date of the refresh token.

        :return: The expiration datetime of the refresh token.
        :rtype: datetime.datetime
        """
        return self.created_at + datetime.timedelta(weeks=1)  # refresh token is valid for 1 week

    def is_refresh_token_expired(self) -> bool:
        """Determine whether the refresh token is expired or not.

        :return: True if the refresh token is expired, False otherwise.
        :rtype: bool
        """
        return self.refresh_token_expiration <= datetime.datetime.now(self.refresh_token_expiration.tzinfo)

    async def async_auth_flow(self, request: httpx.Request) -> typing.AsyncGenerator[httpx.Request, httpx.Response]:
        """Implement the authentication flow.

        :param request: The HTTP request to authenticate.
        :type request: httpx.Request
        :yield: The authenticated request.
        :rtype: httpx.Request
        """
        if self.is_access_token_expired():  # token expired
            await self.refresh_access_token(f'{request.url.scheme}://{request.url.host}')

        request.headers['Authorization'] = f'{self.token_type} {self.access_token}'
        yield request

    async def refresh_access_token(self, target_url: str):
        """Refresh the access token.

        :param target_url: The base URL of the API (e.g. 'https://api.factorialhr.com').
        :type target_url: str
        :raises RuntimeError: When the refresh token is expired.
        :raises httpx.HTTPStatusError: When the token refresh request fails.
        """
        if self.is_refresh_token_expired():
            raise RuntimeError('Refresh token expired')
        response = await self._client.post(
            f'{target_url}/oauth/token',
            data={
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token,
            },
        )
        response.raise_for_status()
        data = AccessTokenResponse.model_validate(response.json())
        self.access_token = data.access_token
        self.token_type = data.token_type
        self.refresh_token = data.refresh_token
        self.created_at = data.created_at


class RefreshTokenAuthFile(RefreshTokenAuth):
    """Authorization using a refresh token and saves the refreshed session data in a specific json file."""

    def __init__(self, file: str | os.PathLike[str], *args, **kwargs):
        """Initialize refresh token authentication with file persistence.

        :param file: Path to the JSON file to save/load session data.
        :type file: str | os.PathLike[str]
        :param args: Positional arguments passed to RefreshTokenAuth.
        :param kwargs: Keyword arguments passed to RefreshTokenAuth.
        """
        super().__init__(*args, **kwargs)
        self.file = pathlib.Path(file)

    async def refresh_access_token(self, target_url: str):
        """Refresh the access token and save to file.

        :param target_url: The base URL of the API (e.g. 'https://api.factorialhr.com').
        :type target_url: str
        :raises RuntimeError: When the refresh token is expired.
        :raises httpx.HTTPStatusError: When the token refresh request fails.
        """
        await super().refresh_access_token(target_url)
        self.to_file(target_url)

    def to_file(self, target_url: str) -> None:
        """Save the current session data to the file.

        :param target_url: The base URL of the API (e.g. 'https://api.factorialhr.com').
        :type target_url: str
        """
        self.file.write_text(
            json.dumps(
                {
                    'refresh_token': self.refresh_token,
                    'client_id': self.client_id,
                    'client_secret': self.client_secret,
                    'access_token': self.access_token,
                    'created_at': self.created_at.isoformat(),
                    'token_type': self.token_type,
                    'target_url': target_url,
                },
            ),
        )

    @classmethod
    def from_file(
        cls,
        file: pathlib.Path,
    ) -> tuple[
        typing.Self,
        str,
    ]:
        """Load session data from a file.

        :param file: Path to the JSON file containing session data.
        :type file: pathlib.Path
        :return: A tuple of (RefreshTokenAuthFile instance, target_url).
        :rtype: tuple[typing.Self, str]
        :raises json.JSONDecodeError: When the file contains invalid JSON.
        :raises KeyError: When required keys are missing from the file.
        :raises ValueError: When datetime parsing fails.
        """
        file_content = json.loads(file.read_text())
        return cls(
            file,
            client_id=file_content['client_id'],
            client_secret=file_content['client_secret'],
            refresh_token=file_content['refresh_token'],
            created_at=datetime.datetime.fromisoformat(file_content['created_at']),
            token_type=file_content['token_type'],
            access_token=file_content['access_token'],
        ), file_content['target_url']


class ApiClient:
    """Factorial api class."""

    def __init__(
        self,
        base_url: str = 'https://api.factorialhr.com',
        *,
        auth: httpx.Auth,
        **kwargs,
    ):
        """Initialize the API client.

        :param base_url: The base URL of the Factorial API (default: 'https://api.factorialhr.com').
        :type base_url: str
        :param auth: The authentication handler (e.g. AccessTokenAuth, ApiKeyAuth, RefreshTokenAuth).
        :type auth: httpx.Auth
        :param kwargs: Optional keyword arguments forwarded to httpx.AsyncClient (e.g. ``timeout``, ``headers``).
        :type kwargs: optional
        """
        headers = {'accept': 'application/json'}
        self._client = httpx.AsyncClient(
            base_url=f'{base_url}/api/{self.api_version}/resources/',
            headers=headers,
            auth=auth,
            **kwargs,
        )

    @property
    def api_version(self) -> str:
        """Get the API version.

        :return: The API version string.
        :rtype: str
        """
        return '2026-01-01'

    async def close(self):
        """Close the client session.

        :raises httpx.HTTPError: When closing the session fails.
        """
        await self._client.aclose()

    async def __aexit__(self, *_, **__):
        """Exit the async context manager.

        :param _: Exception type (ignored).
        :param __: Exception value and traceback (ignored).
        """
        await self.close()

    async def __aenter__(self) -> typing.Self:
        """Enter the async context manager.

        :return: The ApiClient instance.
        :rtype: typing.Self
        """
        await self._client.__aenter__()
        return self

    @staticmethod
    def _eval_http_method(response: httpx.Response) -> dict[str, typing.Any]:
        """Evaluate an HTTP response and return JSON data.

        :param response: The HTTP response.
        :type response: httpx.Response
        :return: The JSON data from the response.
        :rtype: dict[str, typing.Any]
        :raises httpx.HTTPStatusError: When the response status indicates an error.
        """
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _get_path(*path: str | int | None) -> str:
        """Build a URL path from path segments.

        :param path: Path segments (None values are filtered out).
        :type path: str | int | None
        :return: The joined path string.
        :rtype: str
        """
        return '/'.join(str(p) for p in path if p is not None)

    async def get(self, *path: str | int | None, **kwargs) -> dict[str, typing.Any]:
        """Perform a GET request.

        :param path: Path segments to append to the base URL.
        :type path: str | int | None
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :return: The JSON response data.
        :rtype: dict[str, typing.Any]
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        """
        resp = await self._client.get(self._get_path(*path), **kwargs)
        return self._eval_http_method(resp)

    async def get_all(self, *path: str | int | None, **kwargs) -> Sequence[Mapping[str, typing.Any]]:
        """Get all data from an endpoint via offset pagination.

        Depending on the amount of objects to query, you might want to increase the timeout by using
        `timeout=httpx.Timeout(...)`.
        More information at https://apidoc.factorialhr.com/docs/how-does-it-work#offset-pagination.

        :param path: Path segments to append to the base URL.
        :type path: str | int | None
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :return: A sequence of all records from all pages.
        :rtype: Sequence[Mapping[str, typing.Any]]
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :raises TypeError: When the response data is not a list.
        """
        query_params = kwargs.pop('params', {})
        query_params['page'] = 1  # retrieve first page
        result = await self.get(*path, params=query_params, **kwargs)
        meta = result['meta']
        data: list[Mapping[str, typing.Any]] = result['data']
        if not isinstance(data, list):
            msg = f'Expected list data, got {type(data)}'
            raise TypeError(msg)
        if not meta['has_next_page']:
            return data
        page_count = math.ceil(meta['total'] / meta['limit'])
        responses: list[list[Mapping[str, typing.Any]]] = [[]] * (page_count - 1)

        async def runner(index: int, func: Awaitable[Mapping[str, list[Mapping[str, typing.Any]]]]) -> None:
            responses[index] = (await func)['data']

        async with anyio.create_task_group() as tg:
            for i in range(2, page_count + 1):  # start at 2 because we already got the data of first page
                query_params = query_params.copy()
                query_params['page'] = i
                tg.start_soon(runner, i - 2, self.get(*path, params=query_params, **kwargs))
        return data + [x for response in responses for x in response]

    async def post(self, *path: str | int | None, **kwargs) -> typing.Any:
        """Perform a POST request.

        :param path: Path segments to append to the base URL.
        :type path: str | int | None
        :param kwargs: Optional keyword arguments (e.g. ``json``, ``data``, ``params`` for query string) forwarded
            to the HTTP request.
        :type kwargs: optional
        :return: The JSON response data.
        :rtype: typing.Any
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        """
        resp = await self._client.post(self._get_path(*path), **kwargs)
        return self._eval_http_method(resp)

    async def put(self, *path: str | int | None, **kwargs) -> typing.Any:
        """Perform a PUT request.

        :param path: Path segments to append to the base URL.
        :type path: str | int | None
        :param kwargs: Optional keyword arguments (e.g. ``json``, ``data``, ``params`` for query string) forwarded
            to the HTTP request.
        :type kwargs: optional
        :return: The JSON response data.
        :rtype: typing.Any
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        """
        resp = await self._client.put(self._get_path(*path), **kwargs)
        return self._eval_http_method(resp)

    async def delete(self, *path: str | int | None, **kwargs) -> typing.Any:
        """Perform a DELETE request.

        :param path: Path segments to append to the base URL.
        :type path: str | int | None
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :return: The JSON response data.
        :rtype: typing.Any
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        """
        resp = await self._client.delete(self._get_path(*path), **kwargs)
        return self._eval_http_method(resp)


class Endpoint:
    """Base class for all endpoints."""

    endpoint: str

    def __init__(self, api: ApiClient):
        """Initialize an endpoint instance.

        :param api: The API client instance to use for requests.
        :type api: ApiClient
        """
        self.api = api
