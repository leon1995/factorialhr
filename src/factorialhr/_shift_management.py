import datetime
import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class ShiftState(StrEnum):
    """Enum for shift state."""

    DRAFT = 'draft'
    PUBLISHED = 'published'
    BACKUP = 'backup'


class ShiftManagementShift(pydantic.BaseModel):
    """Model for shift_management_shift."""

    id: int = pydantic.Field(description='Shift identifier')
    company_id: int = pydantic.Field(description='Company identifier')
    name: str | None = pydantic.Field(
        default=None,
        description='Name of the shift, doing a fallback to the default shift title or template week name',
    )
    state: ShiftState = pydantic.Field(description='The state of the shift')
    location_id: int | None = pydantic.Field(default=None, description='Shift location identifier')
    locations_work_area_id: int | None = pydantic.Field(default=None, description='Shift work area identifier')
    employee_id: int = pydantic.Field(description='Employee identifier')
    start_at: datetime.datetime = pydantic.Field(description='Start date of the shift')
    end_at: datetime.datetime = pydantic.Field(description='End date of the shift')
    notes: str | None = pydantic.Field(default=None, description='Shift notes')
    extra_hours: bool | None = pydantic.Field(default=None, description='Flag to indicate if the shift has extra hours')
    default_shift_title: str | None = pydantic.Field(default=None, description='Default shift title')
    timezone: str = pydantic.Field(description='Shift timezone')
    local_start_at: datetime.datetime = pydantic.Field(description='Local start date of the shift')
    local_end_at: datetime.datetime = pydantic.Field(description='Local end date of the shift')


class ShiftManagementEndpoint(Endpoint):
    """Endpoint for shift_management/shifts operations."""

    endpoint = 'shift_management/shifts'

    async def all(self, **kwargs) -> ListApiResponse[ShiftManagementShift]:
        """Get all shifts records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ShiftManagementShift, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ShiftManagementShift]:
        """Get shifts with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ShiftManagementShift, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, shift_id: int | str, **kwargs) -> ShiftManagementShift:
        """Get a specific shift by ID."""
        data = await self.api.get(self.endpoint, shift_id, **kwargs)
        return pydantic.TypeAdapter(ShiftManagementShift).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ShiftManagementShift:
        """Create a new shift."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ShiftManagementShift).validate_python(response)

    async def update(self, shift_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ShiftManagementShift:
        """Update a shift."""
        response = await self.api.put(self.endpoint, shift_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ShiftManagementShift).validate_python(response)

    async def delete(self, shift_id: int | str, **kwargs) -> ShiftManagementShift:
        """Delete a shift."""
        response = await self.api.delete(self.endpoint, shift_id, **kwargs)
        return pydantic.TypeAdapter(ShiftManagementShift).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> list[ShiftManagementShift]:
        """Bulk create shifts."""
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ShiftManagementShift]).validate_python(response)

    async def bulk_delete(self, data: Mapping[str, typing.Any], **kwargs) -> list[ShiftManagementShift]:
        """Bulk delete shifts."""
        response = await self.api.post(self.endpoint, 'bulk_delete', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ShiftManagementShift]).validate_python(response)
