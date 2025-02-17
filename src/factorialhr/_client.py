import asyncio
import math
import typing

import httpx


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
        query_params = kwargs.pop('params', {})
        query_params['page'] = 1  # retrieve first page
        result = await self.get(*path, params=query_params, **kwargs)
        meta = result['meta']
        data = result['data']
        if not isinstance(data, list):
            msg = f'Expected list data, got {type(data)}'
            raise TypeError(msg)
        if not meta['has_next_page']:
            return data

        page_count = math.ceil(meta['total'] / meta['limit'])
        requests = []
        for i in range(2, page_count + 1):  # start at 2 because we already got the data of first page
            query_params = query_params.copy()
            query_params['page'] = i
            requests.append(self.get(*path, params=query_params, **kwargs))
        for response in await asyncio.gather(*requests):
            data.extend(response['data'])
        assert meta['total'] == len(data), f'Got {len(data)} instead of total {meta["total"]} items'
        return data

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

    def __init__(self, api: ApiClient):
        self.api = api
