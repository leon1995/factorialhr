import datetime
import enum
import typing

import pydantic

from factorialhr import _common
from factorialhr._client import Endpoint


class BreakConfiguration(pydantic.BaseModel):
    id: int
    attendance_employees_setting_id: int
    time_settings_break_configuration_id: int
    enabled: bool
    name: str | None
    paid: bool | None


class _BreakConfigurationRoot(pydantic.RootModel):
    root: list[BreakConfiguration]


class BreakConfigurationEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/attendance/break_configurations'

    async def all(self, **kwargs) -> list[BreakConfiguration]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-break-configurations."""
        return _BreakConfigurationRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, break_configuration_id: int, **kwargs) -> BreakConfiguration: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[BreakConfiguration], _common.Meta]: ...

    async def get(self, *, break_configuration_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-break-configurations-id."""
        result = await self.api.get(self.endpoint, break_configuration_id, **kwargs)
        return (
            BreakConfiguration.model_validate(result)
            if break_configuration_id is not None
            else (
                _BreakConfigurationRoot.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class EditTimesheetRequestRequestType(enum.StrEnum):
    create_shift = 'create_shift'
    delete_shift = 'delete_shift'
    update_shift = 'update_shift'


class EditTimesheetRequest(pydantic.BaseModel):
    id: int
    approved: bool | None
    request_type: EditTimesheetRequestRequestType
    employee_id: int
    workable: bool | None
    clock_in: datetime.datetime | None
    clock_out: datetime.datetime | None
    location_type: _common.LocationType | None
    reason: str | None
    attendance_shift_id: int | None
    time_settings_break_configuration_id: int | None
    observations: str | None
    date: datetime.date | None
    reference_date: str | None


class _EditTimesheetRequestRoot(pydantic.RootModel):
    root: list[EditTimesheetRequest]


class EditTimesheetRequestEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/attendance/edit_timesheet_requests'

    async def all(self, **kwargs) -> list[EditTimesheetRequest]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-edit-timesheet-requests."""
        return _EditTimesheetRequestRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, break_configuration_id: int, **kwargs) -> EditTimesheetRequest: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[EditTimesheetRequest], _common.Meta]: ...
    async def get(self, *, edit_time_sheet_request_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-edit-timesheet-requests-id."""
        result = await self.api.get(self.endpoint, edit_time_sheet_request_id, **kwargs)
        return (
            EditTimesheetRequest.model_validate(result)
            if edit_time_sheet_request_id is not None
            else (
                _EditTimesheetRequestRoot.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class EstimatedTimeSource(enum.StrEnum):
    shift_management = 'shift_management'
    work_schedule = 'work_schedule'
    contract_hours = 'contract_hours'
    none = 'none'


class EstimatedTime(pydantic.BaseModel):
    date: datetime.date
    company_id: int
    employee_id: int
    expected_minutes: int
    regular_minutes: int
    overtime_minutes: int
    breaks: list[typing.Any]  # TODO: what is the break model?
    time_unit: _common.TimeUnit
    estimated_half_days: int
    shifts: list[typing.Any]  # TODO: what is the shifts model?
    source: str
    minutes: int


class _EstimatedTimeRoot(pydantic.RootModel):
    root: list[EstimatedTime]


class EstimatedTimeEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/attendance/estimated_times'

    async def all(
        self,
        *,
        start_on: datetime.date,
        end_on: datetime.date,
        employee_ids: typing.Sequence[int],
        **kwargs,
    ) -> list[EstimatedTime]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-estimated-times."""
        params = kwargs.get('params', {})
        params.update({'start_on': start_on, 'end_on': end_on, 'employee_ids[]': employee_ids})
        return _EstimatedTimeRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    async def get(
        self,
        *,
        start_on: datetime.date,
        end_on: datetime.date,
        employee_ids: typing.Sequence[int],
        **kwargs,
    ) -> tuple[list[EstimatedTime], _common.Meta]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-estimated-times."""
        params = kwargs.get('params', {})
        params.update({'start_on': start_on, 'end_on': end_on, 'employee_ids[]': employee_ids})
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _EstimatedTimeRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class OpenShiftStatus(enum.StrEnum):
    opened = 'opened'
    closed = 'closed'
    created = 'created'


class OpenShift(pydantic.BaseModel):
    id: int
    employee_id: int
    date: str
    clock_in: datetime.datetime
    clock_out: datetime.datetime | None
    status: OpenShiftStatus
    workable: bool
    automatic_clock_in: bool
    location_type: str | None
    workplace_id: int | None
    time_settings_break_configuration_id: int | None


class _OpenShiftRoot(pydantic.RootModel):
    root: list[OpenShift]


class OpenShiftEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/attendance/open_shifts'

    async def all(self, employee_ids: typing.Sequence[int] | None = None, **kwargs) -> list[OpenShift]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-open-shifts."""
        params = kwargs.get('params', {})
        params.update({'employee_ids[]': employee_ids} if employee_ids is not None else {})
        return _OpenShiftRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    async def get(
        self,
        employee_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> tuple[list[OpenShift], _common.Meta]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-open-shifts."""
        params = kwargs.get('params', {})
        params.update({'employee_ids[]': employee_ids} if employee_ids is not None else {})
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _OpenShiftRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class OverTimeRequestStatus(enum.StrEnum):
    pending = 'pending'
    approved = 'approved'
    rejected = 'rejected'
    none = 'none'


class OverTimeRequest(pydantic.BaseModel):
    id: int
    employee_id: int
    approver_id: int
    author_id: int
    status: OverTimeRequestStatus
    description: str | None
    reason: str | None
    date: datetime.date
    hours_amount_in_cents: int
    created_at: datetime.datetime | None
    approver: bool
    approver_full_name: str | None
    is_editable: bool


class _OverTimeRequestRoot(pydantic.RootModel):
    root: list[OverTimeRequest]


class OverTimeRequestEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/attendance/overtime_requests'

    async def all(self, **kwargs) -> list[OverTimeRequest]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-overtime-requests."""
        return _OverTimeRequestRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, answer_id: int, **kwargs) -> OverTimeRequest: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[OverTimeRequest], _common.Meta]: ...

    async def get(self, *, over_time_request_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-overtime-requests-id."""
        result = await self.api.get(self.endpoint, over_time_request_id, **kwargs)
        return (
            OverTimeRequest.model_validate(result)
            if over_time_request_id is not None
            else (
                _OverTimeRequestRoot.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class ShiftHalfDay(enum.StrEnum):
    beginning_of_day = 'beginning_of_day'
    end_of_day = 'end_of_day'


class Shift(pydantic.BaseModel):
    id: int
    employee_id: int
    date: datetime.date
    reference_date: datetime.date
    clock_in: datetime.time | None
    clock_out: datetime.time | None
    in_source: str | None
    out_source: str | None
    observations: str | None
    location_type: _common.LocationType | None
    half_day: ShiftHalfDay | None
    in_location_latitude: float | None
    in_location_longitude: float | None
    in_location_accuracy: int | None
    out_location_latitude: float | None
    out_location_longitude: float | None
    out_location_accuracy: float | None
    workable: bool | None
    created_at: datetime.datetime
    workplace_id: int | None
    time_settings_break_configuration_id: int | None
    company_id: int
    updated_at: str
    minutes: int
    clock_in_with_seconds: datetime.time | None


class _ShiftRoot(pydantic.RootModel):
    root: list[Shift]


class ShiftEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/attendance/shifts'

    async def all(  # noqa: PLR0913
        self,
        *,
        employee_ids: typing.Sequence[int] | None = None,
        start_on: datetime.date | None = None,
        end_on: datetime.date | None = None,
        ids: typing.Sequence[int] | None = None,
        half_day: bool | None = None,
        workable: bool | None = None,
        latest_shift: bool | None = None,
        sort_created_at_asc: bool | None = None,
        breaks_with_time_configuration: bool | None = None,
        last_working_shift: bool | None = None,
        **kwargs,
    ) -> list[Shift]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-shifts."""
        params = kwargs.get('params', {})
        params.update(
            {
                'employee_ids[]': employee_ids,
                'start_on': start_on,
                'end_on': end_on,
                'ids[]': ids,
                'half_day': half_day,
                'workable': workable,
                'latest_shift': latest_shift,
                'sort_created_at_asc': sort_created_at_asc,
                'breaks_with_time_configuration': breaks_with_time_configuration,
                'last_working_shift': last_working_shift,
            },
        )
        return _ShiftRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, shift_id: int, **kwargs) -> Shift: ...

    @typing.overload
    async def get(
        self,
        *,
        employee_ids: typing.Sequence[int] | None = None,
        start_on: datetime.date | None = None,
        end_on: datetime.date | None = None,
        ids: typing.Sequence[int] | None = None,
        half_day: bool | None = None,
        workable: bool | None = None,
        latest_shift: bool | None = None,
        sort_created_at_asc: bool | None = None,
        breaks_with_time_configuration: bool | None = None,
        last_working_shift: bool | None = None,
        **kwargs,
    ) -> tuple[list[Shift], _common.Meta]: ...
    async def get(  # noqa: PLR0913
        self,
        *,
        shift_id: int | None = None,
        employee_ids: typing.Sequence[int] | None = None,
        start_on: datetime.date | None = None,
        end_on: datetime.date | None = None,
        ids: typing.Sequence[int] | None = None,
        half_day: bool | None = None,
        workable: bool | None = None,
        latest_shift: bool | None = None,
        sort_created_at_asc: bool | None = None,
        breaks_with_time_configuration: bool | None = None,
        last_working_shift: bool | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-shifts-id."""
        if shift_id is not None:
            return Shift.model_validate(await self.api.get(self.endpoint, shift_id, **kwargs))
        params = kwargs.get('params', {})
        params.update(
            {
                'employee_ids[]': employee_ids,
                'start_on': start_on,
                'end_on': end_on,
                'ids[]': ids,
                'half_day': half_day,
                'workable': workable,
                'latest_shift': latest_shift,
                'sort_created_at_asc': sort_created_at_asc,
                'breaks_with_time_configuration': breaks_with_time_configuration,
                'last_working_shift': last_working_shift,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _ShiftRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class WorkedTimeDayType(enum.StrEnum):
    saturday = 'saturday'
    sunday = 'sunday'
    bank_holiday = 'bank_holiday'
    workday = 'workday'


class WorkedTime(pydantic.BaseModel):
    employee_id: int
    date: datetime.date
    company_id: int
    tracked_minutes: int
    multiplied_minutes: int
    pending_minutes: int
    minutes: int
    time_unit: _common.TimeUnit
    worked_time_blocks: list[typing.Any]
    day_type: WorkedTimeDayType
    id: str


class _WorkedTimeRoot(pydantic.RootModel):
    root: list[WorkedTime]


class WorkedTimeEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/attendance/worked_times'

    async def all(
        self,
        *,
        include_time_range_category: bool,
        include_non_attendable_employees: bool,
        start_on: datetime.date | None = None,
        end_on: datetime.date | None = None,
        employee_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> list[WorkedTime]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-worked-times."""
        params = kwargs.get('params', {})
        params.update(
            {
                'include_time_range_category': include_time_range_category,
                'include_non_attendable_employees': include_non_attendable_employees,
                'start_on': start_on,
                'end_on': end_on,
                'employee_ids[]': employee_ids,
            },
        )
        return _WorkedTimeRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    async def get(
        self,
        *,
        include_time_range_category: bool,
        include_non_attendable_employees: bool,
        start_on: datetime.date | None = None,
        end_on: datetime.date | None = None,
        employee_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> tuple[list[WorkedTime], _common.Meta]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-worked-times."""
        params = kwargs.get('params', {})
        params.update(
            {
                'include_time_range_category': include_time_range_category,
                'include_non_attendable_employees': include_non_attendable_employees,
                'start_on': start_on,
                'end_on': end_on,
                'employee_ids[]': employee_ids,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _WorkedTimeRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])
