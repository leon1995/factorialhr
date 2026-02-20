import datetime
import typing
from collections.abc import Mapping, Sequence
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

    model_config = pydantic.ConfigDict(frozen=True)

    #: Shift identifier
    id: int = pydantic.Field(description='Shift identifier')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Name of the shift, doing a fallback to the default shift title or template week name
    name: str | None = pydantic.Field(
        default=None,
        description='Name of the shift, doing a fallback to the default shift title or template week name',
    )
    #: The state of the shift
    state: ShiftState = pydantic.Field(description='The state of the shift')
    #: Shift location identifier
    location_id: int | None = pydantic.Field(default=None, description='Shift location identifier')
    #: Shift work area identifier
    locations_work_area_id: int | None = pydantic.Field(default=None, description='Shift work area identifier')
    #: Employee identifier
    employee_id: int = pydantic.Field(description='Employee identifier')
    #: Start date of the shift
    start_at: datetime.datetime = pydantic.Field(description='Start date of the shift')
    #: End date of the shift
    end_at: datetime.datetime = pydantic.Field(description='End date of the shift')
    #: Shift notes
    notes: str | None = pydantic.Field(default=None, description='Shift notes')
    #: Flag to indicate if the shift has extra hours
    extra_hours: bool | None = pydantic.Field(default=None, description='Flag to indicate if the shift has extra hours')
    #: Default shift title
    default_shift_title: str | None = pydantic.Field(default=None, description='Default shift title')
    #: Shift timezone
    timezone: str = pydantic.Field(description='Shift timezone')
    #: Local start date of the shift
    local_start_at: datetime.datetime = pydantic.Field(description='Local start date of the shift')
    #: Local end date of the shift
    local_end_at: datetime.datetime = pydantic.Field(description='Local end date of the shift')


class ShiftManagementEndpoint(Endpoint):
    """Endpoint for shift_management/shifts operations."""

    endpoint = 'shift_management/shifts'

    async def all(self, **kwargs) -> ListApiResponse[ShiftManagementShift]:
        """Get all shifts records.

        Official documentation: `shift_management/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-shift-management-shifts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ShiftManagementShift]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ShiftManagementShift, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ShiftManagementShift]:
        """Get shifts with pagination metadata.

        Official documentation: `shift_management/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-shift-management-shifts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ShiftManagementShift]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ShiftManagementShift, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, shift_id: int | str, **kwargs) -> ShiftManagementShift:
        """Get a specific shift by ID.

        Official documentation: `shift_management/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-shift-management-shifts>`_

        :param shift_id: The unique identifier.
        :type shift_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ShiftManagementShift
        """
        data = await self.api.get(self.endpoint, shift_id, **kwargs)
        return pydantic.TypeAdapter(ShiftManagementShift).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ShiftManagementShift:
        """Create a new shift.

        Official documentation: `shift_management/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-shift-management-shifts>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ShiftManagementShift
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ShiftManagementShift).validate_python(response)

    async def update(self, shift_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ShiftManagementShift:
        """Update a shift.

        Official documentation: `shift_management/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-shift-management-shifts>`_

        :param shift_id: The unique identifier of the record to update.
        :type shift_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: ShiftManagementShift
        """
        response = await self.api.put(self.endpoint, shift_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ShiftManagementShift).validate_python(response)

    async def delete(self, shift_id: int | str, **kwargs) -> ShiftManagementShift:
        """Delete a shift.

        Official documentation: `shift_management/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-shift-management-shifts>`_

        :param shift_id: The unique identifier of the record to delete.
        :type shift_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: ShiftManagementShift
        """
        response = await self.api.delete(self.endpoint, shift_id, **kwargs)
        return pydantic.TypeAdapter(ShiftManagementShift).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[ShiftManagementShift]:
        """Bulk create shifts.

        Official documentation: `shift_management/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-shift-management-shifts>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[ShiftManagementShift]
        """
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ShiftManagementShift]).validate_python(response)

    async def bulk_delete(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[ShiftManagementShift]:
        """Bulk delete shifts.

        Official documentation: `shift_management/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-shift-management-shifts>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[ShiftManagementShift]
        """
        response = await self.api.post(self.endpoint, 'bulk_delete', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ShiftManagementShift]).validate_python(response)
