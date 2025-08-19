import datetime
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class HalfDay(StrEnum):
    """Enum for half-day types."""

    BEGINNING_OF_DAY = 'beginning_of_day'
    END_OF_DAY = 'end_of_day'


class CompanyHoliday(pydantic.BaseModel):
    """Model for holidays_company_holiday."""

    id: int = pydantic.Field(description='Company holiday id')
    location_id: int = pydantic.Field(description='Related location id')
    summary: str | None = pydantic.Field(default=None, description='Company holiday summary')
    description: str | None = pydantic.Field(default=None, description='Company holiday description')
    date: datetime.date = pydantic.Field(description='Company holiday date')
    half_day: HalfDay | None = pydantic.Field(
        default=None,
        description='If the company holiday is half-day and which part of the day',
    )


class CompanyHolidaysEndpoint(Endpoint):
    """Endpoint for holidays/company_holidays operations."""

    endpoint = 'holidays/company_holidays'

    async def all(self, **kwargs) -> ListApiResponse[CompanyHoliday]:
        """Get all company holidays records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=CompanyHoliday, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[CompanyHoliday]:
        """Get company holidays with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=CompanyHoliday, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, holiday_id: int | str, **kwargs) -> CompanyHoliday:
        """Get a specific company holiday by ID."""
        data = await self.api.get(self.endpoint, holiday_id, **kwargs)
        return pydantic.TypeAdapter(CompanyHoliday).validate_python(data)
