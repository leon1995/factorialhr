import datetime
import typing
from collections.abc import Mapping, Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class WorkScheduleDayConfiguration(pydantic.BaseModel):
    """Model for work_schedule_day_configuration."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Day configuration ID
    id: int = pydantic.Field(description='Day configuration ID')
    #: Overlap period ID
    overlap_period_id: int = pydantic.Field(description='Overlap period ID')
    #: Day of the week
    weekday: str = pydantic.Field(description='Day of the week')
    #: Start time
    start_at: datetime.date | None = pydantic.Field(default=None, description='Start time')
    #: Duration in seconds
    duration_in_seconds: int = pydantic.Field(description='Duration in seconds')


class WorkScheduleOverlapPeriod(pydantic.BaseModel):
    """Model for work_schedule_overlap_period."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Overlap period ID
    id: int = pydantic.Field(description='Overlap period ID')
    #: Whether this is the default period
    default: bool = pydantic.Field(description='Whether this is the default period')
    #: Schedule ID
    schedule_id: int = pydantic.Field(description='Schedule ID')
    #: Start month
    start_month: int = pydantic.Field(description='Start month')
    #: Start day
    start_day: int = pydantic.Field(description='Start day')
    #: End month
    end_month: int = pydantic.Field(description='End month')
    #: End day
    end_day: int = pydantic.Field(description='End day')
    #: Type of schedule
    schedule_type: str = pydantic.Field(description='Type of schedule')


class WorkScheduleSchedule(pydantic.BaseModel):
    """Model for work_schedule_schedule."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Schedule ID
    id: int = pydantic.Field(description='Schedule ID')
    #: Schedule name
    name: str = pydantic.Field(description='Schedule name')
    #: Archive date
    archived_at: datetime.datetime | None = pydantic.Field(default=None, description='Archive date')
    #: Company ID
    company_id: int = pydantic.Field(description='Company ID')
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')
    #: List of employee IDs
    employee_ids: Sequence[int] = pydantic.Field(description='List of employee IDs')
    #: Schedule periods
    periods: Sequence[typing.Any] = pydantic.Field(description='Schedule periods')


class DayConfigurationEndpoint(Endpoint):
    """Endpoint for work_schedule/day_configurations operations."""

    endpoint = 'work_schedule/day_configurations'

    async def all(self, **kwargs) -> ListApiResponse[WorkScheduleDayConfiguration]:
        """Get all day configuration records.

        Official documentation: `work_schedule/day_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-day-configurations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[WorkScheduleDayConfiguration]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=WorkScheduleDayConfiguration)

    async def get(self, **kwargs) -> MetaApiResponse[WorkScheduleDayConfiguration]:
        """Get day configurations with pagination metadata.

        Official documentation: `work_schedule/day_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-day-configurations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[WorkScheduleDayConfiguration]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            raw_meta=response['meta'],
            raw_data=response['data'],
            model_type=WorkScheduleDayConfiguration,
        )

    async def get_by_id(self, day_config_id: int | str, **kwargs) -> WorkScheduleDayConfiguration:
        """Get a specific day configuration by ID.

        Official documentation: `work_schedule/day_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-day-configurations>`_

        :param day_config_id: The unique identifier.
        :type day_config_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: WorkScheduleDayConfiguration
        """
        data = await self.api.get(self.endpoint, day_config_id, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleDayConfiguration).validate_python(data)

    async def bulk_cud(self, data: Mapping[str, typing.Any], **kwargs) -> WorkScheduleDayConfiguration:
        """Bulk create/update/delete day configurations.

        Official documentation: `work_schedule/day_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-day-configurations>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: WorkScheduleDayConfiguration
        """
        response = await self.api.post(self.endpoint, 'bulk_cud', json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleDayConfiguration).validate_python(response)


class OverlapPeriodEndpoint(Endpoint):
    """Endpoint for work_schedule/overlap_periods operations."""

    endpoint = 'work_schedule/overlap_periods'

    async def all(self, **kwargs) -> ListApiResponse[WorkScheduleOverlapPeriod]:
        """Get all overlap period records.

        Official documentation: `work_schedule/overlap_periods <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-overlap-periods>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[WorkScheduleOverlapPeriod]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=WorkScheduleOverlapPeriod)

    async def get(self, **kwargs) -> MetaApiResponse[WorkScheduleOverlapPeriod]:
        """Get overlap periods with pagination metadata.

        Official documentation: `work_schedule/overlap_periods <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-overlap-periods>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[WorkScheduleOverlapPeriod]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            raw_meta=response['meta'],
            raw_data=response['data'],
            model_type=WorkScheduleOverlapPeriod,
        )

    async def get_by_id(self, overlap_period_id: int | str, **kwargs) -> WorkScheduleOverlapPeriod:
        """Get a specific overlap period by ID.

        Official documentation: `work_schedule/overlap_periods <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-overlap-periods>`_

        :param overlap_period_id: The unique identifier.
        :type overlap_period_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: WorkScheduleOverlapPeriod
        """
        data = await self.api.get(self.endpoint, overlap_period_id, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleOverlapPeriod).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> WorkScheduleOverlapPeriod:
        """Create a new overlap period.

        Official documentation: `work_schedule/overlap_periods <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-overlap-periods>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: WorkScheduleOverlapPeriod
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleOverlapPeriod).validate_python(response)

    async def update(
        self,
        overlap_period_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> WorkScheduleOverlapPeriod:
        """Update an overlap period.

        :param overlap_period_id: The unique identifier of the record to update.
        :type overlap_period_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: WorkScheduleOverlapPeriod
        """
        response = await self.api.put(self.endpoint, overlap_period_id, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleOverlapPeriod).validate_python(response)

    async def delete(self, overlap_period_id: int | str, **kwargs) -> WorkScheduleOverlapPeriod:
        """Delete an overlap period.

        Official documentation: `work_schedule/overlap_periods <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-overlap-periods>`_

        :param overlap_period_id: The unique identifier of the record to delete.
        :type overlap_period_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: WorkScheduleOverlapPeriod
        """
        response = await self.api.delete(self.endpoint, overlap_period_id, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleOverlapPeriod).validate_python(response)


class ScheduleEndpoint(Endpoint):
    """Endpoint for work_schedule/schedules operations."""

    endpoint = 'work_schedule/schedules'

    async def all(self, **kwargs) -> ListApiResponse[WorkScheduleSchedule]:
        """Get all schedule records.

        Official documentation: `work_schedule/schedules <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-schedules>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[WorkScheduleSchedule]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=WorkScheduleSchedule)

    async def get(self, **kwargs) -> MetaApiResponse[WorkScheduleSchedule]:
        """Get schedules with pagination metadata.

        Official documentation: `work_schedule/schedules <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-schedules>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[WorkScheduleSchedule]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=WorkScheduleSchedule)

    async def get_by_id(self, schedule_id: int | str, **kwargs) -> WorkScheduleSchedule:
        """Get a specific schedule by ID.

        Official documentation: `work_schedule/schedules <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-schedules>`_

        :param schedule_id: The unique identifier.
        :type schedule_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: WorkScheduleSchedule
        """
        data = await self.api.get(self.endpoint, schedule_id, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleSchedule).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> WorkScheduleSchedule:
        """Create a new schedule.

        Official documentation: `work_schedule/schedules <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-schedules>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: WorkScheduleSchedule
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleSchedule).validate_python(response)

    async def update(
        self,
        schedule_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> WorkScheduleSchedule:
        """Update a schedule.

        :param schedule_id: The unique identifier of the record to update.
        :type schedule_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: WorkScheduleSchedule
        """
        response = await self.api.put(self.endpoint, schedule_id, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleSchedule).validate_python(response)

    async def toggle_archive(self, data: Mapping[str, typing.Any], **kwargs) -> WorkScheduleSchedule:
        """Toggle archive status of a schedule.

        Official documentation: `work_schedule/schedules <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-work-schedule-schedules>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: WorkScheduleSchedule
        """
        response = await self.api.post(self.endpoint, 'toggle_archive', json=data, **kwargs)
        return pydantic.TypeAdapter(WorkScheduleSchedule).validate_python(response)
