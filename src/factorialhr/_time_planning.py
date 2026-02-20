import datetime
import typing
from collections.abc import Mapping, Sequence
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

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the planned break
    id: int = pydantic.Field(description='Identifier of the planned break')
    #: Start date of the break
    start_at: datetime.datetime | None = pydantic.Field(default=None, description='Start date of the break')
    #: End date of the break
    end_at: datetime.datetime | None = pydantic.Field(default=None, description='End date of the break')
    #: Duration of the break in minutes
    duration: int | None = pydantic.Field(default=None, description='Duration of the break in minutes')
    #: Type of the break
    break_type: BreakType = pydantic.Field(description='Type of the break')
    #: Break configuration identifier
    break_configuration_id: int = pydantic.Field(description='Break configuration identifier')
    #: Name of the break configuration
    break_configuration_name: str = pydantic.Field(description='Name of the break configuration')
    #: Whether the break is paid
    break_configuration_paid: bool = pydantic.Field(description='Whether the break is paid')
    #: Default shift identifier
    default_shift_id: int | None = pydantic.Field(default=None, description='Default shift identifier')
    #: Shift configuration identifier
    shift_configuration_id: int | None = pydantic.Field(default=None, description='Shift configuration identifier')
    #: Shift identifier
    shift_id: int | None = pydantic.Field(default=None, description='Shift identifier')
    #: Day configuration identifier
    day_configuration_id: int | None = pydantic.Field(default=None, description='Day configuration identifier')


class PlanningVersion(pydantic.BaseModel):
    """Model for time_planning_planning_version."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Planning version ID
    id: int | None = pydantic.Field(default=None, description='Planning version ID')
    #: Effective date of the planning version
    effective_at: datetime.date = pydantic.Field(description='Effective date of the planning version')
    #: Type of planning tool
    planning_tool: PlanningTool = pydantic.Field(description='Type of planning tool')
    #: Number of rest days in cents
    number_of_rest_days_in_cents: int | None = pydantic.Field(default=None, description='Number of rest days in cents')
    #: Employee ID
    employee_id: int = pydantic.Field(description='Employee ID')
    #: Work schedule ID
    work_schedule_schedule_id: int | None = pydantic.Field(default=None, description='Work schedule ID')


class PlannedBreakEndpoint(Endpoint):
    """Endpoint for time_planning/planned_breaks operations."""

    endpoint = 'time_planning/planned_breaks'

    async def all(self, **kwargs) -> ListApiResponse[PlannedBreak]:
        """Get all planned breaks.

        Official documentation: `time_planning/planned_breaks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-planning-planned-breaks>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[PlannedBreak]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PlannedBreak, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PlannedBreak]:
        """Get planned breaks with pagination metadata.

        Official documentation: `time_planning/planned_breaks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-planning-planned-breaks>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[PlannedBreak]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PlannedBreak, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, break_id: int | str, **kwargs) -> PlannedBreak:
        """Get a specific planned break by ID.

        Official documentation: `time_planning/planned_breaks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-planning-planned-breaks>`_

        :param break_id: The unique identifier.
        :type break_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: PlannedBreak
        """
        data = await self.api.get(self.endpoint, break_id, **kwargs)
        return pydantic.TypeAdapter(PlannedBreak).validate_python(data)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[PlannedBreak]:
        """Bulk create planned breaks.

        Official documentation: `time_planning/planned_breaks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-planning-planned-breaks>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[PlannedBreak]
        """
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[PlannedBreak]).validate_python(response)


class PlanningVersionEndpoint(Endpoint):
    """Endpoint for time_planning/planning_versions operations."""

    endpoint = 'time_planning/planning_versions'

    async def all(self, **kwargs) -> ListApiResponse[PlanningVersion]:
        """Get all planning versions.

        Official documentation: `time_planning/planning_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-planning-planning-versions>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[PlanningVersion]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PlanningVersion, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PlanningVersion]:
        """Get planning versions with pagination metadata.

        Official documentation: `time_planning/planning_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-planning-planning-versions>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[PlanningVersion]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PlanningVersion, raw_meta=response['meta'], raw_data=response['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> PlanningVersion:
        """Create a new planning version.

        Official documentation: `time_planning/planning_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-planning-planning-versions>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: PlanningVersion
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(PlanningVersion).validate_python(response)

    async def update(self, version_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> PlanningVersion:
        """Update a planning version.

        Official documentation: `time_planning/planning_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-planning-planning-versions>`_

        :param version_id: The unique identifier of the record to update.
        :type version_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: PlanningVersion
        """
        response = await self.api.put(self.endpoint, version_id, json=data, **kwargs)
        return pydantic.TypeAdapter(PlanningVersion).validate_python(response)

    async def delete(self, version_id: int | str, **kwargs) -> PlanningVersion:
        """Delete a planning version.

        Official documentation: `time_planning/planning_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-planning-planning-versions>`_

        :param version_id: The unique identifier of the record to delete.
        :type version_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: PlanningVersion
        """
        response = await self.api.delete(self.endpoint, version_id, **kwargs)
        return pydantic.TypeAdapter(PlanningVersion).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[PlanningVersion]:
        """Bulk create planning versions.

        Official documentation: `time_planning/planning_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-planning-planning-versions>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[PlanningVersion]
        """
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[PlanningVersion]).validate_python(response)
