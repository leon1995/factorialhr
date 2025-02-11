"""Implementation of an HTTP server using aiohttp for handling OAuth2 authorization code flow."""

import asyncio
import contextlib
import ssl
import uuid
from collections.abc import Awaitable, Callable

from aiohttp import web


class HttpServer:
    """An HTTP server for handling OAuth2 authorization code flow."""

    def __init__(
        self,
        host: str,
        port: int,
        handler: Callable[[web.Request], Awaitable[web.StreamResponse]],
        ssl_context: ssl.SSLContext | None = None,
    ):
        self.host = host
        self.port: int = port
        self.ssl_context = ssl_context
        app = web.Application()
        app.add_routes([web.get('/authorize/authorization_code', handler)])
        self.runner = web.AppRunner(app)
        self._server_task: asyncio.Task | None = None
        self._server_started = asyncio.Event()
        self._server_close_request = asyncio.Event()
        self.state_secret = uuid.uuid4().hex

    async def __aenter__(self) -> 'HttpServer':
        await self.start()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.close()

    async def _start_http_server(self):
        await self.runner.setup()
        self._site = web.TCPSite(self.runner, self.host, self.port, ssl_context=self.ssl_context)
        await self._site.start()
        self._server_started.set()
        try:
            await self._server_close_request.wait()
        finally:
            await self.runner.cleanup()

    async def start(self):
        """Start the server."""
        self._server_task = asyncio.create_task(self._start_http_server())
        await self._server_started.wait()

    async def close(self):
        """Close the server."""
        self._server_started.clear()
        self._server_close_request.set()
        if self._server_task:
            self._server_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await self._server_task
