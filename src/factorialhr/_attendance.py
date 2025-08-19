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

    id: int = pydantic.Field(description='Break configuration identifier')
    attendance_employees_setting_id: int = pydantic.Field(description='Id of the attendance employee setting')
    time_settings_break_configuration_id: int = pydantic.Field(
        description='Id of the time settings break configuration',
    )
    enabled: bool = pydantic.Field(description='Status of the break configuration if enabled or not')
    name: str | None = pydantic.Field(default=None, description='Name of the break configuration')
    paid: bool | None = pydantic.Field(default=None, description='Check the break configuration is paid or not')


class BreakConfigurationsEndpoint(Endpoint):
    """Endpoint for break configurations operations."""

    endpoint = '/attendance/break_configurations'

    async def all(self, **kwargs) -> ListApiResponse[BreakConfiguration]:
        """Get all break configurations records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=BreakConfiguration, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[BreakConfiguration]:
        """Get break configurations with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=BreakConfiguration, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, break_configuration_id: int | str, **kwargs) -> BreakConfiguration:
        """Get a specific break configuration by ID."""
        data = await self.api.get(self.endpoint, break_configuration_id, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> BreakConfiguration:
        """Create a new break configuration."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(response)

    async def update(
        self,
        break_configuration_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> BreakConfiguration:
        """Update a break configuration."""
        response = await self.api.put(self.endpoint, break_configuration_id, json=data, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(response)


class EditTimesheetRequest(pydantic.BaseModel):
    """Model for attendance_edit_timesheet_request."""

    id: int = pydantic.Field(description='Unique identifier for the edit timesheet request')
    approved: bool | None = pydantic.Field(default=None, description='Status of the edit timesheet request')
    request_type: RequestType = pydantic.Field(description='Type of the request')
    employee_id: int = pydantic.Field(description="Id of the shift's employee")
    workable: bool | None = pydantic.Field(default=None, description='Indicates if the shift is workable or a break')
    clock_in: datetime.time | None = pydantic.Field(default=None, description='Clock in of the shift')
    clock_out: datetime.time | None = pydantic.Field(default=None, description='Clock out of the shift')
    location_type: LocationType | None = pydantic.Field(default=None, description='Location of the shift')
    reason: str | None = pydantic.Field(default=None, description='Approve or reject reason')
    attendance_shift_id: int | None = pydantic.Field(default=None, description='Id of the shift for the request')
    time_settings_break_configuration_id: int | None = pydantic.Field(
        default=None,
        description='Id of the type of break for the request',
    )
    observations: str | None = pydantic.Field(default=None, description='Additional observations for the shift')
    date: datetime.date | None = pydantic.Field(default=None, description='Date of the shift')
    reference_date: datetime.date | None = pydantic.Field(default=None, description='Reference date for the shift')


class EditTimesheetRequestsEndpoint(Endpoint):
    """Endpoint for edit timesheet requests operations."""

    endpoint = '/attendance/edit_timesheet_requests'

    async def all(self, **kwargs) -> ListApiResponse[EditTimesheetRequest]:
        """Get all edit timesheet requests records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=EditTimesheetRequest, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[EditTimesheetRequest]:
        """Get edit timesheet requests with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=EditTimesheetRequest, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, edit_timesheet_request_id: int | str, **kwargs) -> EditTimesheetRequest:
        """Get a specific edit timesheet request by ID."""
        data = await self.api.get(self.endpoint, edit_timesheet_request_id, **kwargs)
        return pydantic.TypeAdapter(EditTimesheetRequest).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> EditTimesheetRequest:
        """Create a new edit timesheet request."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(EditTimesheetRequest).validate_python(response)

    async def update(
        self,
        edit_timesheet_request_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> EditTimesheetRequest:
        """Update an edit timesheet request."""
        response = await self.api.put(self.endpoint, edit_timesheet_request_id, json=data, **kwargs)
        return pydantic.TypeAdapter(EditTimesheetRequest).validate_python(response)

    async def delete(self, edit_timesheet_request_id: int | str, **kwargs) -> EditTimesheetRequest:
        """Delete an edit timesheet request."""
        response = await self.api.delete(self.endpoint, edit_timesheet_request_id, **kwargs)
        return pydantic.TypeAdapter(EditTimesheetRequest).validate_python(response)


class EstimatedTime(pydantic.BaseModel):
    """Model for attendance_estimated_time."""

    date: datetime.date = pydantic.Field(description='Date of the estimated time')
    company_id: int = pydantic.Field(description='Company identifier')
    employee_id: int = pydantic.Field(description='Employee identifier')
    expected_minutes: float = pydantic.Field(
        description=(
            'Amount of minutes the employee has to work without taking into '
            'consideration time off leaves and bank holidays'
        ),
    )
    regular_minutes: float = pydantic.Field(description='Amount of regular minutes the employee has to work')
    overtime_minutes: float = pydantic.Field(
        description='Amount of overtime minutes the employee has to work (only available with Shift Management)',
    )
    breaks: Sequence[typing.Any] = pydantic.Field(description='List of breaks')
    time_unit: TimeUnit = pydantic.Field(description='Time unit for the estimation')
    estimated_half_days: int = pydantic.Field(description='Number of estimated half days')
    shifts: Sequence[typing.Any] = pydantic.Field(description='List of shifts')
    source: str = pydantic.Field(
        description="Source of the estimated time. Could be employee's contract, work schedule or shift management",
    )
    id: str = pydantic.Field(description='ID to specify the estimation time it includes the employee_id and date')
    minutes: float = pydantic.Field(description='Amount of minutes the employee has to work')


class OpenShift(pydantic.BaseModel):
    """Model for attendance_open_shift."""

    id: int = pydantic.Field(description='Open Shift identifier')
    employee_id: int = pydantic.Field(description='Employee identifier from the open shift')
    date: datetime.date = pydantic.Field(description='Date of the open shift')
    reference_date: datetime.date = pydantic.Field(description='Reference date for the shift')
    clock_in: datetime.datetime = pydantic.Field(description='Clock in time from the shift. Ignore the date part')
    clock_out: datetime.datetime | None = pydantic.Field(
        default=None,
        description='For open shifts, this field is null',
    )
    status: OpenShiftStatus = pydantic.Field(description='Status of the shift')
    workable: bool = pydantic.Field(description='Indicates if the shift is a break or a workable shift')
    automatic_clock_in: bool = pydantic.Field(description='Indicates if the shift is automatic or not')
    location_type: LocationType | None = pydantic.Field(
        default=None,
        description='String representing the location type of the shift. Examples work_from_home, office, etc',
    )
    workplace_id: int | None = pydantic.Field(
        default=None,
        description='Identifier for the workplace assigned to the shift',
    )
    time_settings_break_configuration_id: int | None = pydantic.Field(
        default=None,
        description='If the shift is a break, this field will have the break configuration id',
    )


class OvertimeRequest(pydantic.BaseModel):
    """Model for attendance_overtime_request."""

    id: int = pydantic.Field(description='Overtime request identifier')
    employee_id: int = pydantic.Field(description='Employee identifier')
    approver_id: int | None = pydantic.Field(default=None, description='Approver identifier')
    author_id: int = pydantic.Field(description='Author identifier')
    status: OvertimeStatus = pydantic.Field(description='Status of the overtime request')
    description: str | None = pydantic.Field(default=None, description='Description of the overtime request')
    reason: str | None = pydantic.Field(default=None, description='Reason for the overtime request')
    date: datetime.date = pydantic.Field(description='Date of the overtime request')
    hours_amount_in_cents: int = pydantic.Field(description='Hours amount in cents')
    created_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Creation date of the overtime request',
    )
    approver: bool = pydantic.Field(description='Whether the request has an approver')
    approver_full_name: str | None = pydantic.Field(default=None, description='Full name of the approver')
    is_editable: bool = pydantic.Field(description='Defines if the overtime request can be edited')


class AttendanceShift(pydantic.BaseModel):
    """Model for attendance_shift."""

    id: int = pydantic.Field(description='Unique identifier for the shift')
    employee_id: int = pydantic.Field(description='Identifier for the employee assigned to the shift')
    date: datetime.date = pydantic.Field(description='Date of the shift')
    reference_date: datetime.date = pydantic.Field(description='Reference date for the shift')
    clock_in: datetime.time | None = pydantic.Field(default=None, description='Time when the employee clocked in')
    clock_out: datetime.time | None = pydantic.Field(default=None, description='Time when the employee clocked out')
    in_source: str | None = pydantic.Field(default=None, description='Source of the clock-in time')
    out_source: str | None = pydantic.Field(default=None, description='Source of the clock-out time')
    observations: str | None = pydantic.Field(default=None, description='Additional observations about the shift')
    location_type: LocationType | None = pydantic.Field(default=None, description='Type of location for the shift')
    half_day: HalfDay | None = pydantic.Field(default=None, description='Indicates which worked part of the day')
    in_location_latitude: float | None = pydantic.Field(default=None, description='Latitude of the clock-in location')
    in_location_longitude: float | None = pydantic.Field(default=None, description='Longitude of the clock-in location')
    in_location_accuracy: float | None = pydantic.Field(default=None, description='Accuracy of the clock-in location')
    out_location_latitude: float | None = pydantic.Field(default=None, description='Latitude of the clock-out location')
    out_location_longitude: float | None = pydantic.Field(
        default=None,
        description='Longitude of the clock-out location',
    )
    out_location_accuracy: float | None = pydantic.Field(default=None, description='Accuracy of the clock-out location')
    workable: bool | None = pydantic.Field(default=None, description='Indicates if the shift is workable')
    created_at: datetime.datetime = pydantic.Field(description='Timestamp when the shift record was created')
    workplace_id: int | None = pydantic.Field(default=None, description='Identifier for the location')
    time_settings_break_configuration_id: int | None = pydantic.Field(
        default=None,
        description='Identifier for the break configuration',
    )
    company_id: int = pydantic.Field(description='Identifier for the company')
    updated_at: datetime.datetime = pydantic.Field(description='Timestamp when the shift record was updated')
    minutes: int = pydantic.Field(description='Number in minutes of the shift')
    clock_in_with_seconds: datetime.time | None = pydantic.Field(default=None, description='Clock in time with seconds')


class WorkedTime(pydantic.BaseModel):
    """Model for attendance_worked_time."""

    employee_id: int = pydantic.Field(description='Employee identifier')
    date: datetime.date = pydantic.Field(description='Date of the worked time')
    company_id: int = pydantic.Field(description='Company identifier')
    tracked_minutes: int = pydantic.Field(description='Number of tracked minutes')
    multiplied_minutes: int = pydantic.Field(description='Number of multiplied minutes')
    pending_minutes: int = pydantic.Field(description='Number of pending minutes')
    minutes: int = pydantic.Field(description='Total number of minutes')
    time_unit: TimeUnit = pydantic.Field(description='Time unit for the worked time')
    worked_time_blocks: Sequence[typing.Any] = pydantic.Field(description='List of worked time blocks')
    day_type: DayType = pydantic.Field(description='Type of day')
    id: str = pydantic.Field(description='ID to specify the worked time it includes the employee_id and date')


class EstimatedTimesEndpoint(Endpoint):
    """Endpoint for estimated times operations."""

    endpoint = '/attendance/estimated_times'

    async def get(self, **kwargs) -> MetaApiResponse[EstimatedTime]:
        """Get estimated times with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=EstimatedTime, raw_meta=response['meta'], raw_data=response['data'])

    async def all(self, **kwargs) -> ListApiResponse[EstimatedTime]:
        """Get all estimated times records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=EstimatedTime, raw_data=data)


class OpenShiftsEndpoint(Endpoint):
    """Endpoint for open shifts operations."""

    endpoint = '/attendance/open_shifts'

    async def get(self, **kwargs) -> MetaApiResponse[OpenShift]:
        """Get open shifts with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=OpenShift, raw_meta=response['meta'], raw_data=response['data'])

    async def all(self, **kwargs) -> ListApiResponse[OpenShift]:
        """Get all open shifts records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=OpenShift, raw_data=data)


class OvertimeRequestsEndpoint(Endpoint):
    """Endpoint for overtime requests operations."""

    endpoint = '/attendance/overtime_requests'

    async def all(self, **kwargs) -> ListApiResponse[OvertimeRequest]:
        """Get all overtime requests records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=OvertimeRequest, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[OvertimeRequest]:
        """Get overtime requests with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=OvertimeRequest, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, overtime_request_id: int | str, **kwargs) -> OvertimeRequest:
        """Get a specific overtime request by ID."""
        data = await self.api.get(self.endpoint, overtime_request_id, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> OvertimeRequest:
        """Create a new overtime request."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(response)

    async def update(
        self,
        overtime_request_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> OvertimeRequest:
        """Update an overtime request."""
        response = await self.api.put(self.endpoint, overtime_request_id, json=data, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(response)

    async def delete(self, overtime_request_id: int | str, **kwargs) -> OvertimeRequest:
        """Delete an overtime request."""
        response = await self.api.delete(self.endpoint, overtime_request_id, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(response)

    async def approve(self, data: Mapping[str, typing.Any], **kwargs) -> OvertimeRequest:
        """Approve an overtime request."""
        response = await self.api.post(self.endpoint, 'approve', json=data, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(response)

    async def reject(self, data: Mapping[str, typing.Any], **kwargs) -> OvertimeRequest:
        """Reject an overtime request."""
        response = await self.api.post(self.endpoint, 'reject', json=data, **kwargs)
        return pydantic.TypeAdapter(OvertimeRequest).validate_python(response)


class ShiftsEndpoint(Endpoint):
    """Endpoint for shifts operations."""

    endpoint = '/attendance/shifts'

    async def all(self, **kwargs) -> ListApiResponse[AttendanceShift]:
        """Get all shifts records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=AttendanceShift)

    async def get(self, **kwargs) -> MetaApiResponse[AttendanceShift]:
        """Get shifts with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=AttendanceShift)

    async def get_by_id(self, shift_id: int | str, **kwargs) -> AttendanceShift:
        """Get a specific shift by ID."""
        data = await self.api.get(self.endpoint, shift_id, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """Create a new shift."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def update(
        self,
        shift_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> AttendanceShift:
        """Update a shift."""
        response = await self.api.put(self.endpoint, shift_id, json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def delete(self, shift_id: int | str, **kwargs) -> AttendanceShift:
        """Delete a shift."""
        response = await self.api.delete(self.endpoint, shift_id, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def autofill(self, data: Mapping[str, typing.Any], **kwargs) -> list[AttendanceShift]:
        """Autofill shifts."""
        response = await self.api.post(self.endpoint, 'autofill', json=data, **kwargs)
        return pydantic.TypeAdapter(list[AttendanceShift]).validate_python(response)

    async def break_start(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """Start a break in a shift."""
        response = await self.api.post(self.endpoint, 'break_start', json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def break_end(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """End a break in a shift."""
        response = await self.api.post(self.endpoint, 'break_end', json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def clock_in(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """Clock in a shift."""
        response = await self.api.post(self.endpoint, 'clock_in', json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def clock_out(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """Clock out a shift."""
        response = await self.api.post(self.endpoint, 'clock_out', json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)

    async def toggle_clock(self, data: Mapping[str, typing.Any], **kwargs) -> AttendanceShift:
        """Toggle clock (clock in/out) a shift."""
        response = await self.api.post(self.endpoint, 'toggle_clock', json=data, **kwargs)
        return pydantic.TypeAdapter(AttendanceShift).validate_python(response)


class WorkedTimesEndpoint(Endpoint):
    """Endpoint for worked times operations."""

    endpoint = '/attendance/worked_times'

    async def get(self, **kwargs) -> MetaApiResponse[WorkedTime]:
        """Get worked times with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=WorkedTime, raw_meta=response['meta'], raw_data=response['data'])

    async def all(self, **kwargs) -> ListApiResponse[WorkedTime]:
        """Get all worked times records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=WorkedTime, raw_data=data)
