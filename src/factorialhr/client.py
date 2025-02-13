import asyncio
import math
import typing

import httpx


class ApiClient:
    """Factorial api class."""

    def __init__(self, base_url: str = 'https://api.factorialhr.com', *, auth: httpx.Auth, **kwargs):
        headers = {'accept': 'application/json'}
        self._client = httpx.AsyncClient(base_url=f'{base_url}/api', headers=headers, auth=auth, **kwargs)

    async def close(self):
        """Close the client session."""
        await self._client.aclose()

    async def __aexit__(self, *_, **__):
        await self.close()

    async def __aenter__(self) -> 'ApiClient':
        await self._client.__aenter__()
        return self

    @staticmethod
    def _eval_http_method(response: httpx.Response, **kwargs) -> typing.Any:
        response.raise_for_status()
        return response.json(**kwargs)

    async def get(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a get request."""
        resp = await self._client.get(endpoint, **kwargs)
        return self._eval_http_method(resp)

    async def get_all(self, endpoint: str, **kwargs) -> list:
        """Get all data from an endpoint via offset pagination.

        Depending on the amount of objects to query, you might want to increase the timeout by using
        `timeout=httpx.Timeout(...)`.
        More information at https://apidoc.factorialhr.com/docs/how-does-it-work#offset-pagination.
        """
        data, meta = (await self.get(endpoint, **kwargs)).values()
        if not meta['has_next_page']:
            return data
        page_count = math.ceil(meta['total'] / meta['limit'])
        requests = []
        for i in range(page_count):
            query_params = kwargs.get('params', {}).copy()
            query_params['page'] = i + 2
            kwargs['params'] = query_params
            requests.append(self.get(endpoint, **kwargs))
        for response in await asyncio.gather(*requests):
            data.extend(response['data'])
        assert meta['total'] == len(data), f'Got {len(data)} instead of total {meta["total"]} items'
        return data

    async def post(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a post request."""
        resp = await self._client.post(endpoint, **kwargs)
        return self._eval_http_method(resp)

    async def put(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a put request."""
        resp = await self._client.put(endpoint, **kwargs)
        return self._eval_http_method(resp)

    async def delete(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a delete request."""
        resp = await self._client.delete(endpoint, **kwargs)
        return self._eval_http_method(resp)
