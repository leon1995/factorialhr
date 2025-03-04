import asyncio
import ssl
import urllib.parse
import uuid
import webbrowser

import aiohttp
from aiohttp import web

from factorialhr._cli import http_server
from factorialhr._client import AccessTokenResponse

HTTP_SERVER = 'localhost'
HTTP_SERVER_PORT = 50101


async def get_authorization_code(
    target_url: str,
    client_id: str,
    redirect_uri: str,
    scope: str,
    ssl_context: ssl.SSLContext | None,
) -> str | None:
    state_secret = str(uuid.uuid4())
    code_queue: asyncio.Queue[str | None] = asyncio.Queue(1)

    async def _handler(request: web.BaseRequest) -> web.StreamResponse:
        if not (state := request.query.get('state', '')):
            await code_queue.put(None)
            return web.Response(status=400, text='state parameter is missing')
        if state != state_secret:
            await code_queue.put(None)
            return web.Response(status=401, text='state parameter is invalid')
        if not (code := request.query.get('code', '')):
            await code_queue.put(None)
            return web.Response(status=400, text='code parameter is missing')
        await code_queue.put(code)
        return web.Response(text='Authorization code received. You can close this window now')

    async with http_server.HttpServer(HTTP_SERVER, HTTP_SERVER_PORT, _handler, ssl_context):
        url = (
            f'{target_url}/oauth/authorize?'
            f'client_id={client_id}&'
            f'redirect_uri={urllib.parse.quote(redirect_uri)}&'
            'response_type=code&'
            f'scope={scope}&'
            f'state={state_secret}'
        )
        print('Open the url in a browser and log in', url)
        webbrowser.open(url)
        return await code_queue.get()


async def get_access_token(  # noqa: PLR0913
    target_url: str,
    client_id: str,
    client_secret: str,
    redirect_uri: str,
    scope: str,
    http_server_timeout: float | None,
    ssl_context: ssl.SSLContext | None,
) -> AccessTokenResponse:
    """Obtain an access token."""
    async with asyncio.timeout(http_server_timeout):
        authorization_code = await get_authorization_code(
            target_url=target_url,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
            ssl_context=ssl_context,
        )
    if authorization_code is None:
        raise RuntimeError('Authorization code could not be obtained')
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            f'{target_url}/oauth/token',
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'code': authorization_code,
                'grant_type': 'authorization_code',
                'redirect_uri': redirect_uri,
            },
        )
    response.raise_for_status()
    return AccessTokenResponse.model_validate(await response.json())
