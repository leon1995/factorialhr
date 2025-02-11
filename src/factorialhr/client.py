import typing

import httpx


class ApiClient:
    """Factorial api class."""

    def __init__(self, authorizer: httpx.Auth, base_url: str = 'https://api.factorialhr.com'):
        headers = {'accept': 'application/json'}
        self._client = httpx.AsyncClient(base_url=base_url, headers=headers, auth=authorizer)

    async def close(self):
        """Close the client session."""
        await self._client.aclose()

    async def __aexit__(self, *_, **__):
        await self.close()

    async def __aenter__(self) -> 'ApiClient':
        return self

    async def get(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a get request."""
        resp = await self._client.get('/api' + endpoint, **kwargs)
        resp.raise_for_status()
        return resp.json()

    async def post(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a post request."""
        resp = await self._client.post('/api' + endpoint, **kwargs)
        resp.raise_for_status()
        return resp.json()

    async def put(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a put request."""
        resp = await self._client.put('/api' + endpoint, **kwargs)
        resp.raise_for_status()
        return resp.json()

    async def delete(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a delete request."""
        resp = await self._client.delete('/api' + endpoint, **kwargs)
        resp.raise_for_status()
        return resp.json()
