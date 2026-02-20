import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class LocationType(StrEnum):
    office = 'office'
    business_trip = 'business_trip'
    work_from_home = 'work_from_home'


class TimeUnit(StrEnum):
    minute = 'minute'
    half_day = 'half_day'
    none = 'none'


class RequestType(StrEnum):
    """Enum for edit timesheet request types."""

    CREATE_SHIFT = 'create_shift'
    DELETE_SHIFT = 'delete_shift'
    UPDATE_SHIFT = 'update_shift'


class OpenShiftStatus(StrEnum):
    """Enum for open shift status."""

    OPENED = 'opened'
    CLOSED = 'closed'
    CREATED = 'created'


class OvertimeStatus(StrEnum):
    """Enum for overtime request status."""

    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    NONE = 'none'


class HalfDay(StrEnum):
    """Enum for half day types."""

    BEGINNING_OF_DAY = 'beginning_of_day'
    END_OF_DAY = 'end_of_day'


class DayType(StrEnum):
    """Enum for day types."""

    SATURDAY = 'saturday'
    SUNDAY = 'sunday'
    BANK_HOLIDAY = 'bank_holiday'
    WORKDAY = 'workday'


class BreakConfiguration(pydantic.BaseModel):
    """Model for attendance_break_configuration."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Break configuration identifier
    id: int = pydantic.Field(description='Break configuration identifier')
    #: Id of the attendance employee setting
    attendance_employees_setting_id: int = pydantic.Field(description='Id of the attendance employee setting')
    #: Id of the time settings break configuration
    time_settings_break_configuration_id: int = pydantic.Field(
        description='Id of the time settings break configuration',
    )
    #: Status of the break configuration if enabled or not
    enabled: bool = pydantic.Field(description='Status of the break configuration if enabled or not')
    #: Name of the break configuration
    name: str | None = pydantic.Field(default=None, description='Name of the break configuration')
    #: Check the break configuration is paid or not
    paid: bool | None = pydantic.Field(default=None, description='Check the break configuration is paid or not')


class BreakConfigurationsEndpoint(Endpoint):
    """Endpoint for break configurations operations."""

    endpoint = 'attendance/break_configurations'

    async def all(self, **kwargs) -> ListApiResponse[BreakConfiguration]:
        """Get all break configurations records.

        Official documentation: `attendance/break_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-break-configurations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[BreakConfiguration]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=BreakConfiguration, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[BreakConfiguration]:
        """Get break configurations with pagination metadata.

        Official documentation: `attendance/break_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-break-configurations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[BreakConfiguration]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=BreakConfiguration, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, break_configuration_id: int | str, **kwargs) -> BreakConfiguration:
        """Get a specific break configuration by ID.

        Official documentation: `attendance/break_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-break-configurations-id>`_

        :param break_configuration_id: The unique identifier.
        :type break_configuration_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: BreakConfiguration
        """
        data = await self.api.get(self.endpoint, break_configuration_id, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> BreakConfiguration:
        """Create a new break configuration.

        Official documentation: `attendance/break_configurations <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-break-configurations>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: BreakConfiguration
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(response)

    async def update(
        self,
        break_configuration_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> BreakConfiguration:
        """Update a break configuration.

        Official documentation: `attendance/break_configurations <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-attendance-break-configurations-id>`_

        :param break_configuration_id: The unique identifier of the record to update.
        :type break_configuration_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: BreakConfiguration
        """
        response = await self.api.put(self.endpoint, break_configuration_id, json=data, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(response)


class EditTimesheetRequest(pydantic.BaseModel):
    """Model for attendance_edit_timesheet_request."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Unique identifier for the edit timesheet request
    id: int = pydantic.Field(description='Unique identifier for the edit timesheet request')
    #: Status of the edit timesheet request
    approved: bool | None = pydantic.Field(default=None, description='Status of the edit timesheet request')
    #: Type of the request
    request_type: RequestType = pydantic.Field(description='Type of the request')
    #: Id of the shift's employee
    employee_id: int = pydantic.Field(description="Id of the shift's employee")
    #: Indicates if the shift is workable or a break
    workable: bool | None = pydantic.Field(default=None, description='Indicates if the shift is workable or a break')
    #: Clock in of the shift
    clock_in: datetime.time | None = pydantic.Field(default=None, description='Clock in of the shift')
    #: Clock out of the shift
    clock_out: datetime.time | None = pydantic.Field(default=None, description='Clock out of the shift')
    #: Location of the shift
    location_type: LocationType | None = pydantic.Field(default=None, description='Location of the shift')
    #: Approve or reject reason
    reason: str | None = pydantic.Field(default=None, description='Approve or reject reason')
    #: Id of the shift for the request
    attendance_shift_id: int | None = pydantic.Field(default=None, description='Id of the shift for the request')
    #: Id of the type of break for the request
    time_settings_break_configuration_id: int | None = pydantic.Field(
        default=None,
        description='Id of the type of break for the request',
    )
    #: Additional observations for the shift
    observations: str | None = pydantic.Field(default=None, description='Additional observations for the shift')
    #: Date of the shift
    date: datetime.date | None = pydantic.Field(default=None, description='Date of the shift')
    #: Reference date for the shift
    reference_date: datetime.date | None = pydantic.Field(default=None, description='Reference date for the shift')


class EditTimesheetRequestsEndpoint(Endpoint):
    """Endpoint for edit timesheet requests operations."""

    endpoint = 'attendance/edit_timesheet_requests'

    async def all(self, **kwargs) -> ListApiResponse[EditTimesheetRequest]:
        """Get all edit timesheet requests records.

        Official documentation: `attendance/edit_timesheet_requests <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-edit-timesheet-requests>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[EditTimesheetRequest]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=EditTimesheetRequest, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[EditTimesheetRequest]:
        """Get edit timesheet requests with pagination metadata.

        Official documentation: `attendance/edit_timesheet_requests <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-edit-timesheet-requests>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[EditTimesheetRequest]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=EditTimesheetRequest, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, edit_timesheet_request_id: int | str, **kwargs) -> EditTimesheetRequest:
        """Get a specific edit timesheet request by ID.

        Official documentation: `attendance/edit_timesheet_requests <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-edit-timesheet-requests-id>`_

        :param edit_timesheet_request_id: The unique identifier.
        :type edit_timesheet_request_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: EditTimesheetRequest
        """
        data = await self.api.get(self.endpoint, edit_timesheet_request_id, **kwargs)
        return pydantic.TypeAdapter(EditTimesheetRequest).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> EditTimesheetRequest:
        """Create a new edit timesheet request.

        Official documentation: `attendance/edit_timesheet_requests <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-edit-timesheet-requests>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: EditTimesheetRequest
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(EditTimesheetRequest).validate_python(response)

    async def update(
        self,
        edit_timesheet_request_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> EditTimesheetRequest:
        """Update an edit timesheet request.

        Official documentation: `attendance/edit_timesheet_requests <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-attendance-edit-timesheet-requests-id>`_

        :param edit_timesheet_request_id: The unique identifier of the record to update.
        :type edit_timesheet_request_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: EditTimesheetRequest
        """
        response = await self.api.put(self.endpoint, edit_timesheet_request_id, json=data, **kwargs)
        return pydantic.TypeAdapter(EditTimesheetRequest).validate_python(response)

    async def delete(self, edit_timesheet_request_id: int | str, **kwargs) -> EditTimesheetRequest:
        """Delete an edit timesheet request.

        Official documentation: `attendance/edit_timesheet_requests <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-attendance-edit-timesheet-requests-id>`_

        :param edit_timesheet_request_id: The unique identifier of the record to delete.
        :type edit_timesheet_request_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: EditTimesheetRequest
        """
        response = await self.api.delete(self.endpoint, edit_timesheet_request_id, **kwargs)
        return pydantic.TypeAdapter(EditTimesheetRequest).validate_python(response)


class EstimatedTime(pydantic.BaseModel):
    """Model for attendance_estimated_time."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Date of the estimated time
    date: datetime.date = pydantic.Field(description='Date of the estimated time')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Employee identifier
    employee_id: int = pydantic.Field(description='Employee identifier')
    #: Amount of minutes the employee has to work without taking into consideration time off leaves and bank holidays
    expected_minutes: float = pydantic.Field(
        description=(
            'Amount of minutes the employee has to work without taking into '
            'consideration time off leaves and bank holidays'
        ),
    )
    #: Amount of regular minutes the employee has to work
    regular_minutes: float = pydantic.Field(description='Amount of regular minutes the employee has to work')
    #: Amount of overtime minutes the employee has to work (only available with Shift Management)
    overtime_minutes: float = pydantic.Field(
        description='Amount of overtime minutes the employee has to work (only available with Shift Management)',
    )
    #: List of breaks
    breaks: Sequence[typing.Any] = pydantic.Field(description='List of breaks')
    #: Time unit for the estimation
    time_unit: TimeUnit = pydantic.Field(description='Time unit for the estimation')
    #: Number of estimated half days
    estimated_half_days: int = pydantic.Field(description='Number of estimated half days')
    #: List of shifts
    shifts: Sequence[typing.Any] = pydantic.Field(description='List of shifts')
    #: Source of the estimated time. Could be employee's contract, work schedule or shift management
    source: str = pydantic.Field(
        description="Source of the estimated time. Could be employee's contract, work schedule or shift management",
    )
    #: ID to specify the estimation time it includes the employee_id and date
    id: str = pydantic.Field(description='ID to specify the estimation time it includes the employee_id and date')
    #: Amount of minutes the employee has to work
    minutes: float = pydantic.Field(description='Amount of minutes the employee has to work')


class OpenShift(pydantic.BaseModel):
    """Model for attendance_open_shift."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Open Shift identifier
    id: int = pydantic.Field(description='Open Shift identifier')
    #: Employee identifier from the open shift
    employee_id: int = pydantic.Field(description='Employee identifier from the open shift')
    #: Date of the open shift
    date: datetime.date = pydantic.Field(description='Date of the open shift')
    #: Reference date for the shift
    reference_date: datetime.date = pydantic.Field(description='Reference date for the shift')
    #: Clock in time from the shift. Ignore the date part
    clock_in: datetime.datetime = pydantic.Field(description='Clock in time from the shift. Ignore the date part')
    #: For open shifts, this field is null
    clock_out: datetime.datetime | None = pydantic.Field(
        default=None,
        description='For open shifts, this field is null',
    )
    #: Status of the shift
    status: OpenShiftStatus = pydantic.Field(description='Status of the shift')
    #: Indicates if the shift is a break or a workable shift
    workable: bool = pydantic.Field(description='Indicates if the shift is a break or a workable shift')
    #: Indicates if the shift is automatic or not
    automatic_clock_in: bool = pydantic.Field(description='Indicates if the shift is automatic or not')
    #: String representing the location type of the shift. Examples work_from_home, office, etc
    location_type: LocationType | None = pydantic.Field(
        default=None,
        description='String representing the location type of the shift. Examples work_from_home, office, etc',
    )
    #: Identifier for the workplace assigned to the shift
    workplace_id: int | None = pydantic.Field(
        default=None,
        description='Identifier for the workplace assigned to the shift',
    )
    #: If the shift is a break, this field will have the break configuration id
    time_settings_break_configuration_id: int | None = pydantic.Field(
        default=None,
        description='If the shift is a break, this field will have the break configuration id',
    )


class OvertimeRequest(pydantic.BaseModel):
    """Model for attendance_overtime_request."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Overtime request identifier
    id: int = pydantic.Field(description='Overtime request identifier')
    #: Employee identifier
    employee_id: int = pydantic.Field(description='Employee identifier')
    #: Approver identifier
    approver_id: int | None = pydantic.Field(default=None, description='Approver identifier')
    #: Author identifier
    author_id: int = pydantic.Field(description='Author identifier')
    #: Status of the overtime request
    status: OvertimeStatus = pydantic.Field(description='Status of the overtime request')
    #: Description of the overtime request
    description: str | None = pydantic.Field(default=None, description='Description of the overtime request')
    #: Reason for the overtime request
    reason: str | None = pydantic.Field(default=None, description='Reason for the overtime request')
    #: Date of the overtime request
    date: datetime.date = pydantic.Field(description='Date of the overtime request')
    #: Hours amount in cents
    hours_amount_in_cents: int = pydantic.Field(description='Hours amount in cents')
    #: Creation date of the overtime request
    created_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Creation date of the overtime request',
    )
    #: Whether the request has an approver
    approver: bool = pydantic.Field(description='Whether the request has an approver')
    #: Full name of the approver
    approver_full_name: str | None = pydantic.Field(default=None, description='Full name of the approver')
    #: Defines if the overtime request can be edited
    is_editable: bool = pydantic.Field(description='Defines if the overtime request can be edited')


class AttendanceShift(pydantic.BaseModel):
    """Model for attendance_shift."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Unique identifier for the shift
    id: int = pydantic.Field(description='Unique identifier for the shift')
    #: Identifier for the employee assigned to the shift
    employee_id: int = pydantic.Field(description='Identifier for the employee assigned to the shift')
    #: Date of the shift
    date: datetime.date = pydantic.Field(description='Date of the shift')
    #: Reference date for the shift
    reference_date: datetime.date = pydantic.Field(description='Reference date for the shift')
    #: Time when the employee clocked in
    clock_in: datetime.time | None = pydantic.Field(default=None, description='Time when the employee clocked in')
    #: Time when the employee clocked out
    clock_out: datetime.time | None = pydantic.Field(default=None, description='Time when the employee clocked out')
    #: Source of the clock-in time
    in_source: str | None = pydantic.Field(default=None, description='Source of the clock-in time')
    #: Source of the clock-out time
    out_source: str | None = pydantic.Field(default=None, description='Source of the clock-out time')
    #: Additional observations about the shift
    observations: str | None = pydantic.Field(default=None, description='Additional observations about the shift')
    #: Type of location for the shift
    location_type: LocationType | None = pydantic.Field(default=None, description='Type of location for the shift')
    #: Indicates which worked part of the day
    half_day: HalfDay | None = pydantic.Field(default=None, description='Indicates which worked part of the day')
    #: Latitude of the clock-in location
    in_location_latitude: float | None = pydantic.Field(default=None, description='Latitude of the clock-in location')
    #: Longitude of the clock-in location
    in_location_longitude: float | None = pydantic.Field(default=None, description='Longitude of the clock-in location')
    #: Accuracy of the clock-in location
    in_location_accuracy: float | None = pydantic.Field(default=None, description='Accuracy of the clock-in location')
    #: Latitude of the clock-out location
    out_location_latitude: float | None = pydantic.Field(default=None, description='Latitude of the clock-out location')
    #: Longitude of the clock-out location
    out_location_longitude: float | None = pydantic.Field(
        default=None,
        description='Longitude of the clock-out location',
    )
    #: Accuracy of the clock-out location
    out_location_accuracy: float | None = pydantic.Field(default=None, description='Accuracy of the clock-out location')
    #: Indicates if the shift is workable
    workable: bool | None = pydantic.Field(default=None, description='Indicates if the shift is workable')
    #: Timestamp when the shift record was created
    created_at: datetime.datetime = pydantic.Field(description='Timestamp when the shift record was created')
    #: Identifier for the location
    workplace_id: int | None = pydantic.Field(default=None, description='Identifier for the location')
    #: Identifier for the break configuration
    time_settings_break_configuration_id: int | None = pydantic.Field(
        default=None,
        description='Identifier for the break configuration',
    )
    #: Identifier for the company
    company_id: int = pydantic.Field(description='Identifier for the company')
    #: Timestamp when the shift record was updated
    updated_at: datetime.datetime = pydantic.Field(description='Timestamp when the shift record was updated')
    #: Number in minutes of the shift
    minutes: int = pydantic.Field(description='Number in minutes of the shift')
    #: Clock in time with seconds
    clock_in_with_seconds: datetime.time | None = pydantic.Field(default=None, description='Clock in time with seconds')


class WorkedTime(pydantic.BaseModel):
    """Model for attendance_worked_time."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Employee identifier
    employee_id: int = pydantic.Field(description='Employee identifier')
    #: Date of the worked time
    date: datetime.date = pydantic.Field(description='Date of the worked time')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Number of tracked minutes
    tracked_minutes: int = pydantic.Field(description='Number of tracked minutes')
    #: Number of multiplied minutes
    multiplied_minutes: int = pydantic.Field(description='Number of multiplied minutes')
    #: Number of pending minutes
    pending_minutes: int = pydantic.Field(description='Number of pending minutes')
    #: Total number of minutes
    minutes: int = pydantic.Field(description='Total number of minutes')
    #: Time unit for the worked time
    time_unit: TimeUnit = pydantic.Field(description='Time unit for the worked time')
    #: List of worked time blocks
    worked_time_blocks: Sequence[typing.Any] = pydantic.Field(description='List of worked time blocks')
    #: Type of day
    day_type: DayType = pydantic.Field(description='Type of day')
    #: ID to specify the worked time it includes the employee_id and date
    id: str = pydantic.Field(description='ID to specify the worked time it includes the employee_id and date')


class EstimatedTimesEndpoint(Endpoint):
    """Endpoint for estimated times operations."""

    endpoint = 'attendance/estimated_times'

    async def get(self, **kwargs) -> MetaApiResponse[EstimatedTime]:
        """Get estimated times with pagination metadata.

        Official documentation: `attendance/estimated_times <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-estimated-times>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[EstimatedTime]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=EstimatedTime, raw_meta=response['meta'], raw_data=response['data'])

    async def all(self, **kwargs) -> ListApiResponse[EstimatedTime]:
        """Get all estimated times records.

        Official documentation: `attendance/estimated_times <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-estimated-times>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[EstimatedTime]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=EstimatedTime, raw_data=data)


class OpenShiftsEndpoint(Endpoint):
    """Endpoint for open shifts operations."""

    endpoint = 'attendance/open_shifts'

    async def get(self, **kwargs) -> MetaApiResponse[OpenShift]:
        """Get open shifts with pagination metadata.

        Official documentation: `attendance/open_shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-open-shifts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[OpenShift]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=OpenShift, raw_meta=response['meta'], raw_data=response['data'])

    async def all(self, **kwargs) -> ListApiResponse[OpenShift]:
        """Get all open shifts records.

        Official documentation: `attendance/open_shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-open-shifts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[OpenShift]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=OpenShift, raw_data=data)


class OvertimeRequestsEndpoint(Endpoint):
    """Endpoint for overtime requests operations."""

    endpoint = 'attendance/overtime_requests'

    async def all(self, **kwargs) -> ListApiResponse[OvertimeRequest]:
        """Get all overtime requests records.

        Official documentation: `attendance/overtime_requests <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-overtime-requests>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[OvertimeRequest]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=OvertimeRequest, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[OvertimeRequest]:
        """Get overtime requests with pagination metadata.

        Official documentation: `attendance/overtime_requests <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-overtime-requests>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[OvertimeRequest]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=OvertimeRequest, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, overtime_request_id: int | str, **kwargs) -> OvertimeRequest:
        """Get a specific overtime request by ID.

        Official documentation: `attendance/overtime_requests <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-overtime-requests-id>`_

        :param overtime_request_id: The unique identifier.
        :type overtime_request_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: OvertimeRequest
        """
        data = await self.api.get(self.endpoint, overtime_request_id, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> OvertimeRequest:
        """Create a new overtime request.

        Official documentation: `attendance/overtime_requests <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-overtime-requests>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: OvertimeRequest
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(response)

    async def update(
        self,
        overtime_request_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> OvertimeRequest:
        """Update an overtime request.

        Official documentation: `attendance/overtime_requests <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-attendance-overtime-requests-id>`_

        :param overtime_request_id: The unique identifier of the record to update.
        :type overtime_request_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: OvertimeRequest
        """
        response = await self.api.put(self.endpoint, overtime_request_id, json=data, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(response)

    async def delete(self, overtime_request_id: int | str, **kwargs) -> OvertimeRequest:
        """Delete an overtime request.

        Official documentation: `attendance/overtime_requests <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-attendance-overtime-requests-id>`_

        :param overtime_request_id: The unique identifier of the record to delete.
        :type overtime_request_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: OvertimeRequest
        """
        response = await self.api.delete(self.endpoint, overtime_request_id, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(response)

    async def approve(self, data: Mapping[str, typing.Any], **kwargs) -> OvertimeRequest:
        """Approve an overtime request.

        Official documentation: `attendance/overtime_requests <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-overtime-requests-approve>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: OvertimeRequest
        """
        response = await self.api.post(self.endpoint, 'approve', json=data, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(response)

    async def reject(self, data: Mapping[str, typing.Any], **kwargs) -> OvertimeRequest:
        """Reject an overtime request.

        Official documentation: `attendance/overtime_requests <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-overtime-requests-reject>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: OvertimeRequest
        """
        response = await self.api.post(self.endpoint, 'reject', json=data, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(response)


class ShiftsEndpoint(Endpoint):
    """Endpoint for shifts operations."""

    endpoint = 'attendance/shifts'

    async def all(self, **kwargs) -> ListApiResponse[AttendanceShift]:
        """Get all shifts records.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-shifts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[AttendanceShift]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=AttendanceShift)

    async def get(self, **kwargs) -> MetaApiResponse[AttendanceShift]:
        """Get shifts with pagination metadata.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-shifts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[AttendanceShift]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=AttendanceShift)

    async def get_by_id(self, shift_id: int | str, **kwargs) -> AttendanceShift:
        """Get a specific shift by ID.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-shifts-id>`_

        :param shift_id: The unique identifier.
        :type shift_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: AttendanceShift
        """
        data = await self.api.get(self.endpoint, shift_id, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """Create a new shift.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-shifts>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: AttendanceShift
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def update(
        self,
        shift_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> AttendanceShift:
        """Update a shift.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-attendance-shifts-id>`_

        :param shift_id: The unique identifier of the record to update.
        :type shift_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: AttendanceShift
        """
        response = await self.api.put(self.endpoint, shift_id, json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def delete(self, shift_id: int | str, **kwargs) -> AttendanceShift:
        """Delete a shift.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-attendance-shifts-id>`_

        :param shift_id: The unique identifier of the record to delete.
        :type shift_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: AttendanceShift
        """
        response = await self.api.delete(self.endpoint, shift_id, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def autofill(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[AttendanceShift]:
        """Autofill shifts.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-shifts-autofill>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[AttendanceShift]
        """
        response = await self.api.post(self.endpoint, 'autofill', json=data, **kwargs)
        return pydantic.TypeAdapter(list[AttendanceShift]).validate_python(response)

    async def break_start(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """Start a break in a shift.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-shifts-break-start>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: AttendanceShift
        """
        response = await self.api.post(self.endpoint, 'break_start', json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def break_end(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """End a break in a shift.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-shifts-break-end>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: AttendanceShift
        """
        response = await self.api.post(self.endpoint, 'break_end', json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def clock_in(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """Clock in a shift.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-shifts-clock-in>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: AttendanceShift
        """
        response = await self.api.post(self.endpoint, 'clock_in', json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def clock_out(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """Clock out a shift.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-shifts-clock-out>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: AttendanceShift
        """
        response = await self.api.post(self.endpoint, 'clock_out', json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def toggle_clock(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """Toggle clock (clock in/out) a shift.

        Official documentation: `attendance/shifts <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-shifts-toggle-clock>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: AttendanceShift
        """
        response = await self.api.post(self.endpoint, 'toggle_clock', json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)


class Review(pydantic.BaseModel):
    """Model for attendance_review."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Review identifier
    id: int = pydantic.Field(description='Review identifier')
    #: Employee identifier
    employee_id: int = pydantic.Field(description='Employee identifier')
    #: Review date
    date: datetime.date = pydantic.Field(description='Review date')
    #: Whether the review is approved
    approved: bool = pydantic.Field(description='Whether the review is approved')
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class ReviewsEndpoint(Endpoint):
    """Endpoint for attendance reviews operations."""

    endpoint = 'attendance/reviews'

    async def all(self, **kwargs) -> ListApiResponse[Review]:
        """Get all reviews records.

        Official documentation: `attendance/reviews <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-reviews>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Review]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Review, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Review]:
        """Get reviews with pagination metadata.

        Official documentation: `attendance/reviews <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-reviews>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Review]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Review, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, review_id: int | str, **kwargs) -> Review:
        """Get a specific review by ID.

        Official documentation: `attendance/reviews <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-reviews-id>`_

        :param review_id: The unique identifier.
        :type review_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Review
        """
        data = await self.api.get(self.endpoint, review_id, **kwargs)
        return pydantic.TypeAdapter(Review).validate_python(data)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[Review]:
        """Bulk create reviews.

        Official documentation: `attendance/reviews <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-reviews-bulk-create>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[Review]
        """
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Review]).validate_python(response)

    async def bulk_destroy(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[Review]:
        """Bulk destroy reviews.

        Official documentation: `attendance/reviews <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-attendance-reviews-bulk-destroy>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[Review]
        """
        response = await self.api.post(self.endpoint, 'bulk_destroy', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Review]).validate_python(response)


class WorkedTimesEndpoint(Endpoint):
    """Endpoint for worked times operations."""

    endpoint = 'attendance/worked_times'

    async def get(self, **kwargs) -> MetaApiResponse[WorkedTime]:
        """Get worked times with pagination metadata.

        Official documentation: `attendance/worked_times <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-worked-times>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[WorkedTime]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=WorkedTime, raw_meta=response['meta'], raw_data=response['data'])

    async def all(self, **kwargs) -> ListApiResponse[WorkedTime]:
        """Get all worked times records.

        Official documentation: `attendance/worked_times <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-attendance-worked-times>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[WorkedTime]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=WorkedTime, raw_data=data)
