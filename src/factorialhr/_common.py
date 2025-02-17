import enum
import typing

import pydantic


class Meta(pydantic.BaseModel):
    has_next_page: bool
    has_previous_page: bool
    start_cursor: str | None = pydantic.Field(default=None)
    end_cursor: str | None = pydantic.Field(default=None)
    limit: int | None  # apparently this is can be None sometimes, e.g. when specifying employee_ids[] in shift request
    total: int


class LocationType(enum.StrEnum):
    office = 'office'
    business_trip = 'business_trip'
    work_from_home = 'work_from_home'


class TimeUnit(enum.StrEnum):
    minute = 'minute'
    half_day = 'half_day'
    none = 'none'


def build_params(**kwargs) -> dict[str, typing.Any]:
    """Remove None values from kwargs."""
    return {key: value for key, value in kwargs.items() if value is not None}
