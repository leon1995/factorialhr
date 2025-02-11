import time
import typing

import httpx


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


class RefreshTokenAuth(httpx.Auth):
    """Authorization using a refresh token which refreshes the access key automatically."""

    def __init__(  # noqa: PLR0913
        self,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        access_token: str,
        token_type: str,
        expires_at: int,
    ):
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.expires_at = expires_at
        self.token_type = token_type
        self._client = httpx.AsyncClient()

    async def async_auth_flow(self, request: httpx.Request) -> typing.AsyncGenerator[httpx.Request, httpx.Response]:
        """Implement the authentication flow."""
        if self.expires_at <= time.time():  # token expired
            await self.refresh_access_token(f'{request.url.scheme}://{request.url.host}')

        request.headers['Authorization'] = f'{self.token_type} {self.access_token}'
        yield request

    async def refresh_access_token(self, target_url: str):
        """Refresh the access token."""
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
        data = response.json()
        self.access_token = data.get('access_token')
        self.token_type = data.get('token_type')
        self.refresh_token = data.get('refresh_token')
        self.expires_at = int(data.get('expires_in')) + int(data.get('created_at'))
