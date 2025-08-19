import datetime
import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class BreakType(StrEnum):
    """Enum for break types."""

    FLEXIBLE = 'flexible'
    FIXED = 'fixed'
    SEMI_FLEXIBLE = 'semi_flexible'


class PlanningTool(StrEnum):
    """Enum for planning tool types."""

    SHIFT_MANAGEMENT = 'shift_management'
    WORK_SCHEDULE = 'work_schedule'
    CONTRACT_HOURS = 'contract_hours'
    NONE = 'none'


class PlannedBreak(pydantic.BaseModel):
    """Represents a planned break in time planning."""

    id: int = pydantic.Field(description='Identifier of the planned break')
    start_at: datetime.datetime | None = pydantic.Field(default=None, description='Start date of the break')
    end_at: datetime.datetime | None = pydantic.Field(default=None, description='End date of the break')
    duration: int | None = pydantic.Field(default=None, description='Duration of the break in minutes')
    break_type: BreakType = pydantic.Field(description='Type of the break')
    break_configuration_id: int = pydantic.Field(description='Break configuration identifier')
    break_configuration_name: str = pydantic.Field(description='Name of the break configuration')
    break_configuration_paid: bool = pydantic.Field(description='Whether the break is paid')
    default_shift_id: int | None = pydantic.Field(default=None, description='Default shift identifier')
    shift_configuration_id: int | None = pydantic.Field(default=None, description='Shift configuration identifier')
    shift_id: int | None = pydantic.Field(default=None, description='Shift identifier')
    day_configuration_id: int | None = pydantic.Field(default=None, description='Day configuration identifier')


class PlanningVersion(pydantic.BaseModel):
    """Model for time_planning_planning_version."""

    id: int | None = pydantic.Field(default=None, description='Planning version ID')
    effective_at: datetime.date = pydantic.Field(description='Effective date of the planning version')
    planning_tool: PlanningTool = pydantic.Field(description='Type of planning tool')
    number_of_rest_days_in_cents: int | None = pydantic.Field(default=None, description='Number of rest days in cents')
    employee_id: int = pydantic.Field(description='Employee ID')
    work_schedule_schedule_id: int | None = pydantic.Field(default=None, description='Work schedule ID')


class PlannedBreakEndpoint(Endpoint):
    """Endpoint for time_planning/planned_breaks operations."""

    endpoint = 'time_planning/planned_breaks'

    async def all(self, **kwargs) -> ListApiResponse[PlannedBreak]:
        """Get all planned breaks."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PlannedBreak, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PlannedBreak]:
        """Get planned breaks with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PlannedBreak, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, break_id: int | str, **kwargs) -> PlannedBreak:
        """Get a specific planned break by ID."""
        data = await self.api.get(self.endpoint, break_id, **kwargs)
        return pydantic.TypeAdapter(PlannedBreak).validate_python(data)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> list[PlannedBreak]:
        """Bulk create planned breaks."""
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[PlannedBreak]).validate_python(response)


class PlanningVersionEndpoint(Endpoint):
    """Endpoint for time_planning/planning_versions operations."""

    endpoint = 'time_planning/planning_versions'

    async def all(self, **kwargs) -> ListApiResponse[PlanningVersion]:
        """Get all planning versions."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PlanningVersion, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PlanningVersion]:
        """Get planning versions with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PlanningVersion, raw_meta=response['meta'], raw_data=response['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> PlanningVersion:
        """Create a new planning version."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(PlanningVersion).validate_python(response)

    async def update(self, version_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> PlanningVersion:
        """Update a planning version."""
        response = await self.api.put(self.endpoint, version_id, json=data, **kwargs)
        return pydantic.TypeAdapter(PlanningVersion).validate_python(response)

    async def delete(self, version_id: int | str, **kwargs) -> PlanningVersion:
        """Delete a planning version."""
        response = await self.api.delete(self.endpoint, version_id, **kwargs)
        return pydantic.TypeAdapter(PlanningVersion).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> list[PlanningVersion]:
        """Bulk create planning versions."""
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[PlanningVersion]).validate_python(response)
