import asyncio
import ssl
import urllib.parse
import uuid
import webbrowser

import aiohttp
import http_server
from aiohttp import web

HTTP_SERVER = 'localhost'
HTTP_SERVER_PORT = 50101


async def get_authorization_code(  # noqa: D103
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
        webbrowser.open(
            f'{target_url}/oauth/authorize?'
            f'client_id={client_id}&'
            f'redirect_uri={urllib.parse.quote(redirect_uri)}&'
            'response_type=code&'
            f'scope={scope}&'
            f'state={state_secret}',
        )
        return await code_queue.get()


async def main(  # noqa: PLR0913
    target_url: str,
    client_id: str,
    client_secret: str,
    redirect_uri: str,
    scope: str,
    http_server_timeout: float,
    ssl_context: ssl.SSLContext | None,
):
    """Obtain an access token."""
    async with asyncio.timeout(http_server_timeout):
        authorization_code = await get_authorization_code(
            target_url=target_url,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
            ssl_context=ssl_context,
        )
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
    data = await response.json()
    print(data)
    print(int(data.get('expires_in')) + int(data.get('created_at')))


asyncio.run(
    main(
        target_url='https://api.factorialhr.com',  # for demo use https://api.demo.factorial.dev
        client_id='<client id>',
        client_secret='<client secret>',  # noqa: S106
        redirect_uri=f'https://redirectmeto.com/http://{HTTP_SERVER}:{HTTP_SERVER_PORT}/authorize/authorization_code',
        scope='read',
        http_server_timeout=60,
        ssl_context=None,
    ),
)
