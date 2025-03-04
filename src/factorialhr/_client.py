import asyncio
import datetime
import json
import math
import os
import pathlib
import typing
from collections.abc import AsyncIterator

import httpx
import pydantic


class ApiKeyAuth(httpx.Auth):
    """Authorization using an api key."""

    def __init__(self, api_key: str):
        self.api_key = api_key

    def auth_flow(self, request: httpx.Request):
        """Implement the authentication flow."""
        request.headers['x-api-key'] = self.api_key
        yield request


class AccessTokenAuth(httpx.Auth):
    """Authorization using an access token. Not refreshing the session."""

    def __init__(self, access_token: str, token_type: str = 'Bearer'):  # noqa: S107
        self.access_token = access_token
        self.token_type = token_type

    def auth_flow(self, request: httpx.Request):
        """Implement the authentication flow."""
        request.headers['Authorization'] = f'{self.token_type} {self.access_token}'
        yield request


class AccessTokenResponse(pydantic.BaseModel):
    access_token: str
    token_type: str
    expires_in: datetime.timedelta
    refresh_token: str
    scope: str
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
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.created_at = created_at
        self.token_type = token_type
        self._client = httpx.AsyncClient()

    @property
    def access_token_expiration(self) -> datetime.datetime:
        """Get the expiration date of the access token."""
        return self.created_at + datetime.timedelta(hours=1)  # access token is valid for 1 hour

    def is_access_token_expired(self) -> bool:
        """Determine whether the access token is expired or not."""
        return self.access_token_expiration <= datetime.datetime.now(self.access_token_expiration.tzinfo)

    @property
    def refresh_token_expiration(self) -> datetime.datetime:
        """Get the expiration date of the refresh token."""
        return self.created_at + datetime.timedelta(weeks=1)  # refresh token is valid for 1 week

    def is_refresh_token_expired(self) -> bool:
        """Determine whether the refresh token is expired or not."""
        return self.refresh_token_expiration <= datetime.datetime.now(self.refresh_token_expiration.tzinfo)

    async def async_auth_flow(self, request: httpx.Request) -> typing.AsyncGenerator[httpx.Request, httpx.Response]:
        """Implement the authentication flow."""
        if self.is_access_token_expired():  # token expired
            await self.refresh_access_token(f'{request.url.scheme}://{request.url.host}')

        request.headers['Authorization'] = f'{self.token_type} {self.access_token}'
        yield request

    async def refresh_access_token(self, target_url: str):
        """Refresh the access token."""
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
        super().__init__(*args, **kwargs)
        self.file = pathlib.Path(file)

    async def refresh_access_token(self, target_url: str):
        await super().refresh_access_token(target_url)
        self.to_file(target_url)

    def to_file(self, target_url: str) -> None:
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
    def from_file(cls, file: pathlib.Path) -> tuple['RefreshTokenAuthFile', str]:
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

    def __init__(self, base_url: str = 'https://api.factorialhr.com', *, auth: httpx.Auth, **kwargs):
        headers = {'accept': 'application/json'}
        self._client = httpx.AsyncClient(base_url=f'{base_url}/api/', headers=headers, auth=auth, **kwargs)

    async def close(self):
        """Close the client session."""
        await self._client.aclose()

    async def __aexit__(self, *_, **__):
        await self.close()

    async def __aenter__(self) -> 'ApiClient':
        await self._client.__aenter__()
        return self

    @staticmethod
    def _eval_http_method(response: httpx.Response) -> dict[str, typing.Any]:
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _get_path(*path: str | int | None) -> str:
        return '/'.join(str(p) for p in path if p is not None)

    async def get(self, *path: str | int | None, **kwargs) -> dict[str, typing.Any]:
        """Perform a get request."""
        resp = await self._client.get(self._get_path(*path), **kwargs)
        return self._eval_http_method(resp)

    async def get_all(self, *path: str | int | None, **kwargs) -> list[dict[str, typing.Any]]:
        """Get all data from an endpoint via offset pagination.

        Depending on the amount of objects to query, you might want to increase the timeout by using
        `timeout=httpx.Timeout(...)`.
        More information at https://apidoc.factorialhr.com/docs/how-does-it-work#offset-pagination.
        """
        return [data async for data in self.get_all_iter(*path, **kwargs)]

    async def get_all_iter(self, *path: str | int | None, **kwargs) -> AsyncIterator[dict[str, typing.Any]]:
        """Get all data from an endpoint via offset pagination.

        Depending on the amount of objects to query, you might want to increase the timeout by using
        `timeout=httpx.Timeout(...)`.
        More information at https://apidoc.factorialhr.com/docs/how-does-it-work#offset-pagination.
        """
        query_params = kwargs.pop('params', {})
        query_params['page'] = 1  # retrieve first page
        result = await self.get(*path, params=query_params, **kwargs)
        meta = result['meta']
        data = result['data']
        if not isinstance(data, list):
            msg = f'Expected list data, got {type(data)}'
            raise TypeError(msg)
        for d in data:
            yield d
        if not meta['has_next_page']:
            return
        page_count = math.ceil(meta['total'] / meta['limit'])
        requests = []
        for i in range(2, page_count + 1):  # start at 2 because we already got the data of first page
            query_params = query_params.copy()
            query_params['page'] = i
            requests.append(self.get(*path, params=query_params, **kwargs))
        for response in await asyncio.gather(*requests):
            for d in response['data']:
                yield d

    async def post(self, *path: str | int | None, **kwargs) -> typing.Any:
        """Perform a post request."""
        resp = await self._client.post(self._get_path(*path), **kwargs)
        return self._eval_http_method(resp)

    async def put(self, *path: str | int | None, **kwargs) -> typing.Any:
        """Perform a put request."""
        resp = await self._client.put(self._get_path(*path), **kwargs)
        return self._eval_http_method(resp)

    async def delete(self, *path: str | int | None, **kwargs) -> typing.Any:
        """Perform a delete request."""
        resp = await self._client.delete(self._get_path(*path), **kwargs)
        return self._eval_http_method(resp)


class Endpoint:
    """Base class for all endpoints."""

    endpoint: str

    def __init__(self, api: ApiClient):
        self.api = api

    async def all_raw_iter(self, **kwargs) -> AsyncIterator[dict[str, typing.Any]]:
        async for data in self.api.get_all_iter(self.endpoint, **kwargs):
            yield data

    async def all_raw(self, **kwargs) -> list[dict[str, typing.Any]]:
        return [data async for data in self.all_raw_iter(**kwargs)]
