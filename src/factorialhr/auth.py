"""Authorization for api calls."""

import queue
import threading
import time
import typing
import urllib.parse
import uuid
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer

import httpx

HTTP_UNAUTHORIZED = 401
HTTP_SERVER = "localhost"
HTTP_SERVER_PORT = 50101


def _get_authorization_code(target_url: str,
                            client_id: str,
                            redirect_uri: str,
                            scope: str,
                            timeout: int) -> str | None:
    state_secret = str(uuid.uuid4())
    code_queue = queue.Queue(1)

    class GetRequestHandler(BaseHTTPRequestHandler):

        def do_GET(self):  # noqa: N802
            path = urllib.parse.urlparse(self.path)
            if path.path != '/authorize/authorization_code':
                return
            queries = urllib.parse.parse_qs(path.query)
            states = queries.get('state', [])
            if len(states) != 1 or states[0] != state_secret:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(
                    bytes('<html><b>ERROR: invalid state parameter. Repeat login process</b></html>', 'utf-8'))
                code_queue.put(None)
                return
            codes = queries.get('code', [])
            if len(codes) != 1 or not (code := codes[0]):
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes('<html><b>ERROR: authorization code is missing. '
                                       'Repeat login process</b></html>', 'utf-8'))
                code_queue.put(None)
                return
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes('<html><b>SUCCESS. You can close this window now</b></html>', 'utf-8'))
            code_queue.put(code)

    web_server = HTTPServer((HTTP_SERVER, HTTP_SERVER_PORT), GetRequestHandler)
    t = threading.Thread(target=web_server.serve_forever, daemon=True)
    t.start()
    webbrowser.open(f'{target_url}/oauth/authorize?'
                    f'client_id={client_id}&'
                    f'redirect_uri={urllib.parse.quote(redirect_uri)}&'
                    'response_type=code&'
                    f'{scope}&'
                    f'state={state_secret}')
    try:
        return code_queue.get(timeout=timeout)
    except queue.Empty:  # code has not been delivered in time
        return None
    finally:
        web_server.shutdown()
        web_server.server_close()
        t.join()


class ApiKeyAuth(httpx.Auth):
    """Authorization using an api key."""

    def __init__(self, api_key: str):
        self.api_key = api_key

    def auth_flow(self, request: httpx.Request):
        """Implement the authentication flow."""
        request.headers['x-api-key'] = self.api_key
        yield request


class OAuth2Auth(httpx.Auth):
    """Authorization using oauth2 flow."""

    requires_response_body = True

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scope: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope

        self.authorization_code: str | None = None
        self.access_token: str | None = None
        self.token_type: str | None = None
        self.expires_in: int | None = None
        self.refresh_token: str | None = None
        self.created_at: int | None = None

    def auth_flow(self, request: httpx.Request) -> typing.Generator[httpx.Request, httpx.Response, None]:
        """Implement the authentication flow."""
        if not self.authorization_code:
            self.authorization_code = _get_authorization_code(
                target_url=f'{request.url.scheme}://{request.url.host}',
                client_id=self.client_id,
                redirect_uri=self.redirect_uri,
                scope=self.scope,
                timeout=60)
            if not self.authorization_code:
                raise httpx.RequestError('Authorization code could not be obtained')
            self.access_token = None  # requires to be regenerated
        if not self.access_token:
            response = yield self.build_access_token_request(f'{request.url.scheme}://{request.url.host}')
            self.update_access_token(response)

        if self.created_at + self.expires_in <= time.time():
            response = yield self.build_refresh_request(f'{request.url.scheme}://{request.url.host}')
            self.update_access_token(response)

        request.headers['Authorization'] = f'{self.token_type} {self.access_token}'
        yield request

    def build_access_token_request(self, target_url: str) -> httpx.Request:
        """Build a request to obtain a new access token."""
        return httpx.Request(
            "POST",
            f"{target_url}/oauth/token",
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                'code': self.authorization_code,
                "grant_type": "authorization_code",
                'redirect_uri': self.redirect_uri,
            },
        )

    def build_refresh_request(self, target_url: str) -> httpx.Request:
        """Build a request to obtain a new access token."""
        return httpx.Request(
            "POST",
            f"{target_url}/oauth/token",
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
            },
        )

    def update_access_token(self, response: httpx.Response):
        """Update the member variables."""
        response.raise_for_status()
        response_data = dict(response.json())
        self.access_token = response_data.get('access_token')
        self.token_type = response_data.get('token_type')
        self.expires_in = response_data.get('expires_in')
        self.refresh_token = response_data.get('refresh_token')
        self.created_at = response_data.get('created_at')
