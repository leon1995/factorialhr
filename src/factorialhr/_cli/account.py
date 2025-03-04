import asyncio
import pathlib

import click
import cloup
import httpx

import factorialhr
from factorialhr._cli import access_token
from factorialhr._cli import common as common_cli
from factorialhr._client import ApiClient, RefreshTokenAuth, RefreshTokenAuthFile


async def _print_account_info(auth: RefreshTokenAuth, url: str):
    async with ApiClient(auth=auth, base_url=url) as api:
        credentials, _ = await factorialhr.CredentialsEndpoint(api).get()
    if len(credentials) > 1:
        raise ValueError('More than one credentials is currently not supported')
    click.echo(
        f'Logged in as {credentials[0].full_name} on {url}. Session expires at {auth.refresh_token_expiration} '
        f'{auth.created_at.tzname()}.',
    )


def get_session() -> tuple[RefreshTokenAuthFile, str]:
    if not SESSION_FILE.exists():
        raise click.ClickException('No session found. Login with "factorialhr account login".')
    auth, url = RefreshTokenAuthFile.from_file(SESSION_FILE)
    if auth.is_refresh_token_expired():
        msg = f'Session expired at {auth.refresh_token_expiration}. Login with "factorialhr account login".'
        raise click.ClickException(msg)
    return auth, url


async def _logout():
    try:
        auth, url = get_session()
    except click.ClickException:
        SESSION_FILE.unlink(missing_ok=True)
        return

    async with httpx.AsyncClient(base_url=url) as client:
        await asyncio.gather(
            client.post(
                'oauth/revoke',
                data={'client_id': auth.client_id, 'client_secret': auth.client_secret, 'token': auth.access_token},
            ),
            client.post(
                'oauth/revoke',
                data={'client_id': auth.client_id, 'client_secret': auth.client_secret, 'token': auth.refresh_token},
            ),
        )
    SESSION_FILE.unlink()


async def _login(client_id: str, client_secret: str, url: str, scope: str, redirect_url: str):
    try:
        response = await access_token.get_access_token(
            client_id=client_id,
            client_secret=client_secret,
            target_url=url,
            redirect_uri=redirect_url,
            scope=scope,
            http_server_timeout=None,
            ssl_context=None,
        )
        print(response)
    except asyncio.CancelledError:
        raise click.ClickException('Operation cancelled')  # noqa: B904
    except RuntimeError as e:
        raise click.ClickException(str(e)) from e
    auth = RefreshTokenAuthFile(
        file=SESSION_FILE,
        refresh_token=response.refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        access_token=response.access_token,
        token_type=response.token_type,
        created_at=response.created_at,
    )
    auth.to_file(url)
    await _print_account_info(auth, url)


@cloup.group(help='Manages an oauth2 session.')
def account():
    pass


APP_DIR = pathlib.Path(click.get_app_dir('factorialhr_api'))
APP_DIR.mkdir(exist_ok=True)
SESSION_FILE = APP_DIR.joinpath('session.json')


@cloup.command(help='Create an oauth2 session.')
@cloup.argument('client_id', type=str)
@cloup.argument('client_secret', type=str)
@cloup.option('--demo', help='Whether to use the production or demo api.', is_flag=True)
@cloup.option('-s', '--scope', help='Oauth2 access scope. Defaults to "read".', default='read')
@cloup.option(
    '--redirect-url',
    help='Where to redirect for oauth2 callback',
    default=f'https://redirectmeto.com/http://{access_token.HTTP_SERVER}:{access_token.HTTP_SERVER_PORT}/authorize/authorization_code',
)
@common_cli.to_async
async def login(client_id: str, client_secret: str, demo: bool, scope: str, redirect_url: str):  # noqa: FBT001
    url = 'https://api.factorialhr.com' if not demo else 'https://api.demo.factorial.dev'
    await _login(client_id=client_id, client_secret=client_secret, url=url, scope=scope, redirect_url=redirect_url)


@cloup.command(help='Get information about the current session.')
def status():
    auth, _ = get_session()
    click.echo(
        f'Session expires at {auth.refresh_token_expiration} {auth.created_at.tzname()}.',
    )


@cloup.command(help='Refresh an already created session.')
@common_cli.to_async
async def refresh():
    auth, url = get_session()
    await auth.refresh_access_token(url)
    await _print_account_info(auth, url)


@cloup.command(help='Invalidate the session.')
@common_cli.to_async
async def logout():
    await _logout()


account.add_command(login)
account.add_command(status)
account.add_command(refresh)
account.add_command(logout)
