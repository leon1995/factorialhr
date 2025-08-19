import datetime
import typing
from collections.abc import Mapping, Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class WorkScheduleDayConfiguration(pydantic.BaseModel):
    """Model for work_schedule_day_configuration."""

    id: int = pydantic.Field(description='Day configuration ID')
    overlap_period_id: int = pydantic.Field(description='Overlap period ID')
    weekday: str = pydantic.Field(description='Day of the week')
    start_at: datetime.date | None = pydantic.Field(default=None, description='Start time')
    duration_in_seconds: int = pydantic.Field(description='Duration in seconds')


class WorkScheduleOverlapPeriod(pydantic.BaseModel):
    """Model for work_schedule_overlap_period."""

    id: int = pydantic.Field(description='Overlap period ID')
    default: bool = pydantic.Field(description='Whether this is the default period')
    schedule_id: int = pydantic.Field(description='Schedule ID')
    start_month: int = pydantic.Field(description='Start month')
    start_day: int = pydantic.Field(description='Start day')
    end_month: int = pydantic.Field(description='End month')
    end_day: int = pydantic.Field(description='End day')
    schedule_type: str = pydantic.Field(description='Type of schedule')


class WorkScheduleSchedule(pydantic.BaseModel):
    """Model for work_schedule_schedule."""

    id: int = pydantic.Field(description='Schedule ID')
    name: str = pydantic.Field(description='Schedule name')
    archived_at: datetime.datetime | None = pydantic.Field(default=None, description='Archive date')
    company_id: int = pydantic.Field(description='Company ID')
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')
    employee_ids: Sequence[int] = pydantic.Field(description='List of employee IDs')
    periods: Sequence[typing.Any] = pydantic.Field(description='Schedule periods')


class DayConfigurationEndpoint(Endpoint):
    """Endpoint for work_schedule/day_configurations operations."""

    endpoint = 'work_schedule/day_configurations'

    async def all(self, **kwargs) -> ListApiResponse[WorkScheduleDayConfiguration]:
        """Get all day configuration records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=WorkScheduleDayConfiguration)

    async def get(self, **kwargs) -> MetaApiResponse[WorkScheduleDayConfiguration]:
        """Get day configurations with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            raw_meta=response['meta'],
            raw_data=response['data'],
            model_type=WorkScheduleDayConfiguration,
        )

    async def get_by_id(self, day_config_id: int | str, **kwargs) -> WorkScheduleDayConfiguration:
        """Get a specific day configuration by ID."""
        data = await self.api.get(self.endpoint, day_config_id, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleDayConfiguration).validate_python(data)

    async def bulk_cud(self, data: Mapping[str, typing.Any], **kwargs) -> WorkScheduleDayConfiguration:
        """Bulk create/update/delete day configurations."""
        response = await self.api.post(self.endpoint, 'bulk_cud', json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleDayConfiguration).validate_python(response)


class OverlapPeriodEndpoint(Endpoint):
    """Endpoint for work_schedule/overlap_periods operations."""

    endpoint = 'work_schedule/overlap_periods'

    async def all(self, **kwargs) -> ListApiResponse[WorkScheduleOverlapPeriod]:
        """Get all overlap period records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=WorkScheduleOverlapPeriod)

    async def get(self, **kwargs) -> MetaApiResponse[WorkScheduleOverlapPeriod]:
        """Get overlap periods with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            raw_meta=response['meta'],
            raw_data=response['data'],
            model_type=WorkScheduleOverlapPeriod,
        )

    async def get_by_id(self, overlap_period_id: int | str, **kwargs) -> WorkScheduleOverlapPeriod:
        """Get a specific overlap period by ID."""
        data = await self.api.get(self.endpoint, overlap_period_id, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleOverlapPeriod).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> WorkScheduleOverlapPeriod:
        """Create a new overlap period."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleOverlapPeriod).validate_python(response)

    async def update(
        self,
        overlap_period_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> WorkScheduleOverlapPeriod:
        """Update an overlap period."""
        response = await self.api.put(self.endpoint, overlap_period_id, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleOverlapPeriod).validate_python(response)

    async def delete(self, overlap_period_id: int | str, **kwargs) -> WorkScheduleOverlapPeriod:
        """Delete an overlap period."""
        response = await self.api.delete(self.endpoint, overlap_period_id, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleOverlapPeriod).validate_python(response)


class ScheduleEndpoint(Endpoint):
    """Endpoint for work_schedule/schedules operations."""

    endpoint = 'work_schedule/schedules'

    async def all(self, **kwargs) -> ListApiResponse[WorkScheduleSchedule]:
        """Get all schedule records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=WorkScheduleSchedule)

    async def get(self, **kwargs) -> MetaApiResponse[WorkScheduleSchedule]:
        """Get schedules with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=WorkScheduleSchedule)

    async def get_by_id(self, schedule_id: int | str, **kwargs) -> WorkScheduleSchedule:
        """Get a specific schedule by ID."""
        data = await self.api.get(self.endpoint, schedule_id, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleSchedule).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> WorkScheduleSchedule:
        """Create a new schedule."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleSchedule).validate_python(response)

    async def update(
        self,
        schedule_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> WorkScheduleSchedule:
        """Update a schedule."""
        response = await self.api.put(self.endpoint, schedule_id, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleSchedule).validate_python(response)

    async def toggle_archive(self, data: Mapping[str, typing.Any], **kwargs) -> WorkScheduleSchedule:
        """Toggle archive status of a schedule."""
        response = await self.api.post(self.endpoint, 'toggle_archive', json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleSchedule).validate_python(response)
