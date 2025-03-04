import asyncio
import datetime
import functools
import typing
from collections.abc import Callable

import click
import cloup
import dateutil.rrule


class DateType(click.ParamType):
    name = 'iso 8601 date'

    def convert(self, value: typing.Any, param: click.Parameter | None, ctx: click.Context | None) -> typing.Any:  # noqa: ARG002
        if isinstance(value, datetime.date):
            return value
        try:
            return datetime.date.fromisoformat(value)
        except ValueError as e:
            self.fail(str(e))


DATE = DateType()


def to_async(func: Callable) -> Callable:
    @functools.wraps(func)
    def _call(*args, **kwargs):
        asyncio.run(func(*args, **kwargs))

    return _call


def _set_logging(_: click.Context, __: click.Parameter, value: bool):  # noqa: FBT001
    if not value:
        return
    import logging.config

    logging.config.dictConfig(
        {
            'version': 1,
            'handlers': {
                'default': {'class': 'logging.StreamHandler', 'formatter': 'http', 'stream': 'ext://sys.stderr'},
            },
            'formatters': {
                'http': {
                    'format': '[%(asctime)s] %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S',
                },
            },
            'loggers': {
                'httpx': {
                    'handlers': ['default'],
                    'level': 'DEBUG',
                },
            },
        },
    )


generic_options = cloup.option_group(
    'Generic options',
    cloup.option('--less', is_flag=True, help='Print paginated'),
    cloup.option('--http-timeout', type=click.IntRange(min=0), help='Set the http timeout'),
    cloup.option('-v', '--verbose', is_flag=True, callback=_set_logging, is_eager=True, help='Increase verbosity'),
)

upper_lower_bounds = (
    cloup.option('--start', type=DATE, help='Lower included bound date'),
    cloup.option(
        '--end',
        type=DATE,
        default=datetime.datetime.now(tz=datetime.UTC).date(),
        help='Upper included bound date. Defaults to today',
    ),
)


def get_months_in(start: datetime.date, end: datetime.date) -> dateutil.rrule.rrule:
    return dateutil.rrule.rrule(dateutil.rrule.MONTHLY, dtstart=start, until=end)
