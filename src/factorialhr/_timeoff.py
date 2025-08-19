import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class AccruedUnitsAvailability(StrEnum):
    """Enum for when accrued units can be spent."""

    CURRENT_CYCLE = 'current_cycle'
    NEXT_CYCLE = 'next_cycle'


class AllowanceType(StrEnum):
    """Enum for allowance unit types."""

    DAYS = 'days'
    HOURS = 'hours'


class AvailableDays(StrEnum):
    """Enum for how allowance units are accrued."""

    ALL_DAYS = 'all_days'
    GENERATED_DAYS = 'generated_days'
    GENERATED_DAYS_MONTHLY = 'generated_days_monthly'
    GENERATED_DAYS_MONTHLY_FIRST_DAY = 'generated_days_monthly_first_day'
    MONTHLY_FIFTEENTH = 'monthly_fifteenth'
    MENSIVERSARY = 'mensiversary'
    BIMONTHLY_FIRST_AND_FIFTEENTH = 'bimonthly_first_and_fifteenth'
    BIMONTHLY_FIFTEENTH_AND_LAST = 'bimonthly_fifteenth_and_last'


class DaysType(StrEnum):
    """Enum for calendar days type."""

    WORKING_DAYS = 'working_days'
    NATURAL_DAYS = 'natural_days'
    NATURAL_DAYS_ONLY_RANGE = 'natural_days_only_range'
    FRENCH_CALENDAR_DAYS = 'french_calendar_days'
    FRENCH_OUVRES = 'french_ouvres'


class Frequency(StrEnum):
    """Enum for allowance cycle frequency."""

    MONTHLY_FLEXIBLE = 'monthly_flexible'
    YEARLY = 'yearly'
    LIFETIME = 'lifetime'


class NegativeCounterType(StrEnum):
    """Enum for negative counter settings."""

    NEGATIVE_COUNTER_DISABLED = 'negative_counter_disabled'
    NEGATIVE_COUNTER_ENABLED = 'negative_counter_enabled'


class ProationType(StrEnum):
    """Enum for proration settings."""

    PRORATION_ENABLED = 'proration_enabled'
    PRORATION_DISABLED = 'proration_disabled'


class RangeType(StrEnum):
    """Enum for leave duration handling."""

    EXACT_RANGE = 'exact_range'
    EXTRA_NON_WORKING_DAYS_AT_END = 'extra_non_working_days_at_end'


class Rounding(StrEnum):
    """Enum for accrued units rounding."""

    HALF_DAY = 'half_day'
    DECIMALS = 'decimals'
    QUARTERS = 'quarters'
    ROUND_UP = 'round_up'


class SourceUnits(StrEnum):
    """Enum for allowance source unit types."""

    BASE_UNITS = 'base_units'
    OVERTIME_UNITS = 'overtime_units'
    BY_WORKED_TIME = 'by_worked_time'


class TenurePeriodTransition(StrEnum):
    """Enum for tenure period transition timing."""

    BEGINNING_OF_CYCLE = 'beginning_of_cycle'
    END_OF_CYCLE = 'end_of_cycle'
    AFTER_MILESTONE = 'after_milestone'


class HalfDay(StrEnum):
    """Enum for half-day options."""

    BEGINNING_OF_DAY = 'beginning_of_day'
    END_OF_DAY = 'end_of_day'


class Allowance(pydantic.BaseModel):
    """Model for timeoff_allowance."""

    id: int = pydantic.Field(description='Unique identifier of the allowance')
    accrued_denominator_in_cents: int | None = pydantic.Field(
        default=None,
        description=(
            'Only for Allowances based on worked time. '
            'It represents how many units you need to work to be granted allowance units'
        ),
    )
    accrued_factor_in_cents: int | None = pydantic.Field(
        default=None,
        description=(
            'Only for Allowances based on worked time. '
            'It represents how many units you are given per unit of time worked'
        ),
    )
    accrued_units_availability: AccruedUnitsAvailability | None = pydantic.Field(
        default=None,
        description='When can the accrued units be spent',
    )
    allowance_type: AllowanceType = pydantic.Field(description='Sets the allowance units. Can be "days" or "hours"')
    available_days: AvailableDays = pydantic.Field(
        description=(
            'Indicates how the allowance units are accrued. '
            'For example all_days means all allowance days are given on the first day of the cycle'
        ),
    )
    carry_over_days: int | None = pydantic.Field(
        default=None,
        description='How many units can carry over between cycles',
    )
    carry_over_units_in_cents: int | None = pydantic.Field(
        default=None,
        description='How many units can carry over between cycles multiplied by 100',
    )
    count_holiday_as_workable: bool = pydantic.Field(
        description=(
            'This setting flags if units taken during a bank holiday should be deducted or not from allowance'
        ),
    )
    cycle_length: int | None = pydantic.Field(
        default=None,
        description='How many months does each allowance cycle last',
    )
    cycle_start: str | None = pydantic.Field(default=None, description='When does the cycle start')
    days_type: DaysType | None = pydantic.Field(
        default=None,
        description='Indicates if the allowance is based on working on calendar days',
    )
    employee_carry_over_starting_year: int | None = pydantic.Field(
        default=None,
        description='When does the carryover start',
    )
    expire_in_months: int | None = pydantic.Field(default=None, description='When does the carryover expire in months')
    frequency: Frequency | None = pydantic.Field(
        default=None,
        description='Defines duration of the allowance cycles. Can be "yearly", "monthly_flexible" or "lifetime"',
    )
    holiday_allowance_in_cents: int | None = pydantic.Field(
        default=None,
        description='Base amount of holiday allowance units multiplied by 100',
    )
    leave_type_ids: Sequence[int] = pydantic.Field(
        description='An array of leave type ids associated with that allowance',
    )
    maximum_amount_in_cents: int | None = pydantic.Field(
        default=None,
        description='Maximum the allowance can reach on accrued',
    )
    name: str = pydantic.Field(description='Allowance name set by the user')
    negative_counter_type: NegativeCounterType | None = pydantic.Field(
        default=None,
        description='Whether the allowance allows to request more days than available',
    )
    position: int | None = None  # Indicates the position in the allowance when rendering them in UI
    proration_type: ProationType = pydantic.Field(description='Whether the allowance has proration enabled or not')
    pto_proratio_enabled: bool | None = None  # Whether the allowance days are prorrated or not
    range_type: RangeType | None = pydantic.Field(default=None, description='Configures how leaves duration is handled')
    rounding: Rounding = pydantic.Field(
        description=(
            'How the accrued units of the allowance are rounded. It depends if the allowance is set in hours or days'
        ),
    )
    send_notification: bool | None = None
    source_units: SourceUnits | None = pydantic.Field(
        default=None,
        description='This field configures the type of allowance (fixed balance, based on worked time)',
    )
    tenure_period_transition: TenurePeriodTransition | None = pydantic.Field(
        default=None,
        description='In case the allowance has tenure periods, when is this tenure applied',
    )
    tenure_periods: Sequence[Mapping[str, typing.Any]]  # The tenure periods associated with the allowance.
    tenure_periods_enabled: bool | None = None  # Whether the allowance has tenure periods enabled or not.
    timeoff_cycle: (
        str  # Value to indicate how the allowance cycle is configured. Its an abbreviation of the first and last month.
    )
    timeoff_policy_id: int  # The Id of the policy to which the allowance belongs to
    unlimited_accrued_hours: bool | None = None  # Flag to indicate if there is unlimited accrual.
    unlimited_carry_over: bool | None = None  # Flag to indicate if there is unlimited carry over.
    unlimited_carry_over_expiration: bool | None = None  # Boolean to flag if carryover does not expire
    unlimited_holidays: bool | None = None  # Flag to indicate that the allowance has unlimited available days


class AllowanceIncidence(pydantic.BaseModel):
    """Model for timeoff_allowance_incidence."""

    id: int  # Unique identifier of the allowance incidence
    employee_id: int  # Employee id of the affected employee
    description: str | None = None  # Optional comment regarding the incidence
    days_in_cents: (
        int  # How many units * 100 does the incidence add/substract. Can be positive or negative. Example is one unit
    )
    timeoff_allowance_id: int  # To what allowance does the incidence affect. It will dictate if its days or hours
    effective_on: datetime.date  # When does the incidence take effect; this is for time off cycles calculations.
    target_balance: str | None = None  # Whether the incidence affects the Accrued or the Available counter.
    created_at: datetime.datetime  # Unix timestamp when the DB record was created
    updated_at: datetime.datetime  # Unix timestamp when the DB record was last updated


class AllowanceStatsNew(pydantic.BaseModel):
    """Model for timeoff_allowance_stats_new."""

    id: str
    allowance_id: int
    employee_id: int
    year: int
    cycles: str
    carry_overs: Sequence[typing.Any]
    accumulated_carry_over: Mapping[str, typing.Any]
    available_days: Mapping[str, typing.Any]
    total_accrued_units: Mapping[str, typing.Any]
    incidences: Mapping[str, typing.Any]
    max_balance_cap: Mapping[str, typing.Any] | None = None
    policy_allowance: Mapping[str, typing.Any]
    prorated_allowance_days: Mapping[str, typing.Any]
    total_in_decimal: Mapping[str, typing.Any] | None = None
    used_carry_over: Mapping[str, typing.Any]
    used_days: Mapping[str, typing.Any]
    used_units_until_reference_date: Mapping[str, typing.Any]
    outstanding_units: Mapping[str, typing.Any]


class BlockedPeriod(pydantic.BaseModel):
    """Model for timeoff_blocked_periods_policy."""

    id: int  # Unique identifier of the blocked period
    company_id: int  # Company id of the blocked period
    name: str  # Name of the blocked period.
    leave_type_ids: Sequence[int]  # Leave types for which absence request has been blocked
    time_periods: Sequence[Mapping[str, typing.Any]]  # The tenure periods associated with the allowance.
    strategy: str  # Type of access group
    members: Sequence[int]  # Employees whose timeoff will be affected
    location_ids: Sequence[int] | None = None  # List of locations workplace identifiers where the employees are located
    team_ids: Sequence[int] | None = None  # List of team identifiers which the selected employees belong to
    legal_entity_ids: Sequence[int] | None = (
        None  # List of legal entity identifiers which the selected employees belong to
    )


class Leave(pydantic.BaseModel):
    """Model for timeoff_leave."""

    id: int  # Identifier of the Leave
    company_id: int  # Company identifier of the employee of the leave
    employee_id: int  # Employee identifier of the leave
    start_on: datetime.date  # The start date of the leave
    finish_on: datetime.date | None = None  # The end date of the leave
    half_day: HalfDay | None = pydantic.Field(default=None, description='Indicates if the leave is taken as a half-day')
    description: str | None = None  # A description of the leave
    reason: str | None = None  # The reason provided by the employee for taking the leave
    leave_type_id: int | None = None  # The identifier for the type of leave
    leave_type_name: str | None = None  # The name of the leave type
    approved: bool | None = None  # Indicates whether the leave has been approved
    employee_full_name: str | None = None  # The full name of the employee taking the leave
    start_time: str | None = None  # The start time of the leave
    hours_amount_in_cents: int | None = None  # The total number of hours taken for the leave, represented in cents
    updated_at: datetime.datetime  # The updated at date of the leave
    created_at: datetime.datetime | None = None  # The created at date of the leave


class LeaveType(pydantic.BaseModel):
    """Model for timeoff_leave_type."""

    id: int  # Identifier of the leave type
    name: str  # Name of the leave type
    translated_name: str | None = None  # Translated name of the leave type, if available
    identifier: str  # Unique identifier of the leave type
    color: str  # The color associated with this leave type
    active: bool | None = None  # Whether the leave type is active
    editable: bool | None = None  # Whether the leave type is editable
    approval_required: bool | None = None  # Whether approval is required for this leave type
    accrues: bool | None = None  # Whether the leave type accrues over time
    attachment: bool  # Whether an attachment is required for this leave type
    allow_endless: bool | None = None  # Whether endless leave is allowed
    restricted: bool | None = None  # Whether the leave type is restricted
    visibility: bool  # Whether the leave type is visible to employees
    workable: bool  # Whether the leave type is workable
    payable: bool | None = None  # Whether the leave type is payable
    company_id: int  # Identifier of the company associated with this leave type
    is_attachment_mandatory: bool | None = None  # Whether the attachment is mandatory
    allowance_ids: Sequence[int]  # List of allowance identifiers associated with this leave type
    half_days_units_enabled: bool | None = None  # Whether half-day units are enabled for this leave type
    max_days_in_cents: int | None = None  # Maximum days in cents that can be taken
    min_days_in_cents: int | None = None  # Minimum days in cents that must be taken
    description: str | None = None  # Description of the leave type
    details_required: bool  # Whether additional details are required for the leave type


class Policy(pydantic.BaseModel):
    """Model for timeoff_policy."""

    id: int  # The policy id.
    name: str  # Policy name.
    main: bool | None = (
        None  # Is the main policy? It will return true if it's the main policy if not it will return false.
    )
    company_id: int  # The company id.
    description: str | None = None  # The policy description.


class PolicyAssignment(pydantic.BaseModel):
    """Model for timeoff_policy_assignment."""

    id: int | None = None  # Unique identifier of the policy assignment
    timeoff_policy_id: int  # The time off policy id
    employee_id: int  # The employee id
    effective_at: datetime.date  # The effective date of the policy assignment


class PolicyTimeline(pydantic.BaseModel):
    """Model for timeoff_policy_timeline."""

    employee_id: int
    start_limit_date: datetime.date
    end_limit_date: datetime.date
    items: Sequence[typing.Any]
    id: int  # This is the employee id since it's a virtual entity


class AllowancesEndpoint(Endpoint):
    """Endpoint for timeoff/allowances operations."""

    endpoint = 'timeoff/allowances'

    async def all(self, **kwargs) -> ListApiResponse[Allowance]:
        """Get all allowances records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Allowance, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Allowance]:
        """Get allowances with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Allowance, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, allowance_id: int | str, **kwargs) -> Allowance:
        """Get a specific allowance by ID."""
        data = await self.api.get(self.endpoint, allowance_id, **kwargs)
        return pydantic.TypeAdapter(Allowance).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Allowance:
        """Create a new allowance."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Allowance).validate_python(response)

    async def update(self, allowance_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Allowance:
        """Update an allowance."""
        response = await self.api.put(self.endpoint, allowance_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Allowance).validate_python(response)

    async def delete(self, allowance_id: int | str, **kwargs) -> Allowance:
        """Delete an allowance."""
        response = await self.api.delete(self.endpoint, allowance_id, **kwargs)
        return pydantic.TypeAdapter(Allowance).validate_python(response)

    async def delete_with_alt_allowance(self, data: Mapping[str, typing.Any], **kwargs) -> Allowance:
        """Delete an allowance and migrate existing incidences to alternative allowance."""
        response = await self.api.post(self.endpoint, 'delete_with_alt_allowance', json=data, **kwargs)
        return pydantic.TypeAdapter(Allowance).validate_python(response)


class AllowanceIncidencesEndpoint(Endpoint):
    """Endpoint for timeoff/allowance_incidences operations."""

    endpoint = 'timeoff/allowance_incidences'

    async def all(self, **kwargs) -> ListApiResponse[AllowanceIncidence]:
        """Get all allowance incidences records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=AllowanceIncidence, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[AllowanceIncidence]:
        """Get allowance incidences with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=AllowanceIncidence, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, incidence_id: int | str, **kwargs) -> AllowanceIncidence:
        """Get a specific allowance incidence by ID."""
        data = await self.api.get(self.endpoint, incidence_id, **kwargs)
        return pydantic.TypeAdapter(AllowanceIncidence).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> AllowanceIncidence:
        """Create a new allowance incidence."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(AllowanceIncidence).validate_python(response)

    async def update(self, incidence_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> AllowanceIncidence:
        """Update an allowance incidence."""
        response = await self.api.put(self.endpoint, incidence_id, json=data, **kwargs)
        return pydantic.TypeAdapter(AllowanceIncidence).validate_python(response)

    async def delete(self, incidence_id: int | str, **kwargs) -> AllowanceIncidence:
        """Delete an allowance incidence."""
        response = await self.api.delete(self.endpoint, incidence_id, **kwargs)
        return pydantic.TypeAdapter(AllowanceIncidence).validate_python(response)


class AllowanceStatsEndpoint(Endpoint):
    """Endpoint for timeoff/allowance_stats operations."""

    endpoint = 'timeoff/allowance_stats'

    async def all(self, **kwargs) -> ListApiResponse[AllowanceStatsNew]:
        """Get all allowance stats records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=AllowanceStatsNew, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[AllowanceStatsNew]:
        """Get allowance stats with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=AllowanceStatsNew, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, stat_id: int | str, **kwargs) -> AllowanceStatsNew:
        """Get a specific allowance stat by ID."""
        data = await self.api.get(self.endpoint, stat_id, **kwargs)
        return pydantic.TypeAdapter(AllowanceStatsNew).validate_python(data)


class BlockedPeriodsEndpoint(Endpoint):
    """Endpoint for timeoff/blocked_periods operations."""

    endpoint = 'timeoff/blocked_periods'

    async def all(self, **kwargs) -> ListApiResponse[BlockedPeriod]:
        """Get all blocked periods records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=BlockedPeriod, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[BlockedPeriod]:
        """Get blocked periods with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=BlockedPeriod, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, period_id: int | str, **kwargs) -> BlockedPeriod:
        """Get a specific blocked period by ID."""
        data = await self.api.get(self.endpoint, period_id, **kwargs)
        return pydantic.TypeAdapter(BlockedPeriod).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> BlockedPeriod:
        """Create a new blocked period."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(BlockedPeriod).validate_python(response)

    async def update(self, period_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> BlockedPeriod:
        """Update a blocked period."""
        response = await self.api.put(self.endpoint, period_id, json=data, **kwargs)
        return pydantic.TypeAdapter(BlockedPeriod).validate_python(response)

    async def delete(self, period_id: int | str, **kwargs) -> BlockedPeriod:
        """Delete a blocked period."""
        response = await self.api.delete(self.endpoint, period_id, **kwargs)
        return pydantic.TypeAdapter(BlockedPeriod).validate_python(response)


class LeavesEndpoint(Endpoint):
    """Endpoint for timeoff/leaves operations."""

    endpoint = 'timeoff/leaves'

    async def all(self, **kwargs) -> ListApiResponse[Leave]:
        """Get all leaves records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Leave, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Leave]:
        """Get leaves with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Leave, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, leave_id: int | str, **kwargs) -> Leave:
        """Get a specific leave by ID."""
        data = await self.api.get(self.endpoint, leave_id, **kwargs)
        return pydantic.TypeAdapter(Leave).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Leave:
        """Create a new leave."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Leave).validate_python(response)

    async def update(self, leave_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Leave:
        """Update a leave."""
        response = await self.api.put(self.endpoint, leave_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Leave).validate_python(response)

    async def delete(self, leave_id: int | str, **kwargs) -> Leave:
        """Delete a leave."""
        response = await self.api.delete(self.endpoint, leave_id, **kwargs)
        return pydantic.TypeAdapter(Leave).validate_python(response)

    async def approve(self, data: Mapping[str, typing.Any], **kwargs) -> Leave:
        """Approve a leave."""
        response = await self.api.post(self.endpoint, 'approve', json=data, **kwargs)
        return pydantic.TypeAdapter(Leave).validate_python(response)

    async def approve_all(self, data: Mapping[str, typing.Any], **kwargs) -> Leave:
        """Approve all steps of a leave."""
        response = await self.api.post(self.endpoint, 'approve_all', json=data, **kwargs)
        return pydantic.TypeAdapter(Leave).validate_python(response)

    async def reject(self, data: Mapping[str, typing.Any], **kwargs) -> Leave:
        """Reject a leave."""
        response = await self.api.post(self.endpoint, 'reject', json=data, **kwargs)
        return pydantic.TypeAdapter(Leave).validate_python(response)


class LeaveTypesEndpoint(Endpoint):
    """Endpoint for timeoff/leave_types operations."""

    endpoint = 'timeoff/leave_types'

    async def all(self, **kwargs) -> ListApiResponse[LeaveType]:
        """Get all leave types records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=LeaveType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[LeaveType]:
        """Get leave types with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=LeaveType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, leave_type_id: int | str, **kwargs) -> LeaveType:
        """Get a specific leave type by ID."""
        data = await self.api.get(self.endpoint, leave_type_id, **kwargs)
        return pydantic.TypeAdapter(LeaveType).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> LeaveType:
        """Create a new leave type."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(LeaveType).validate_python(response)

    async def update(self, leave_type_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> LeaveType:
        """Update a leave type."""
        response = await self.api.put(self.endpoint, leave_type_id, json=data, **kwargs)
        return pydantic.TypeAdapter(LeaveType).validate_python(response)


class PoliciesEndpoint(Endpoint):
    """Endpoint for timeoff/policies operations."""

    endpoint = 'timeoff/policies'

    async def all(self, **kwargs) -> ListApiResponse[Policy]:
        """Get all policies records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Policy, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Policy]:
        """Get policies with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Policy, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, policy_id: int | str, **kwargs) -> Policy:
        """Get a specific policy by ID."""
        data = await self.api.get(self.endpoint, policy_id, **kwargs)
        return pydantic.TypeAdapter(Policy).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Policy:
        """Create a new policy."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Policy).validate_python(response)

    async def update(self, policy_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Policy:
        """Update a policy."""
        response = await self.api.put(self.endpoint, policy_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Policy).validate_python(response)

    async def delete(self, policy_id: int | str, **kwargs) -> Policy:
        """Delete a policy."""
        response = await self.api.delete(self.endpoint, policy_id, **kwargs)
        return pydantic.TypeAdapter(Policy).validate_python(response)


class PolicyAssignmentsEndpoint(Endpoint):
    """Endpoint for timeoff/policy_assignments operations."""

    endpoint = 'timeoff/policy_assignments'

    async def all(self, **kwargs) -> ListApiResponse[PolicyAssignment]:
        """Get all policy assignments records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PolicyAssignment, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PolicyAssignment]:
        """Get policy assignments with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PolicyAssignment, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, assignment_id: int | str, **kwargs) -> PolicyAssignment:
        """Get a specific policy assignment by ID."""
        data = await self.api.get(self.endpoint, assignment_id, **kwargs)
        return pydantic.TypeAdapter(PolicyAssignment).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> PolicyAssignment:
        """Create a new policy assignment."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(PolicyAssignment).validate_python(response)

    async def update(self, assignment_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> PolicyAssignment:
        """Update a policy assignment."""
        response = await self.api.put(self.endpoint, assignment_id, json=data, **kwargs)
        return pydantic.TypeAdapter(PolicyAssignment).validate_python(response)

    async def delete(self, assignment_id: int | str, **kwargs) -> PolicyAssignment:
        """Delete a policy assignment."""
        response = await self.api.delete(self.endpoint, assignment_id, **kwargs)
        return pydantic.TypeAdapter(PolicyAssignment).validate_python(response)


class PolicyTimelinesEndpoint(Endpoint):
    """Endpoint for timeoff/policy_timelines operations."""

    endpoint = 'timeoff/policy_timelines'

    async def all(self, **kwargs) -> ListApiResponse[PolicyTimeline]:
        """Get all policy timelines records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PolicyTimeline, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PolicyTimeline]:
        """Get policy timelines with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PolicyTimeline, raw_meta=response['meta'], raw_data=response['data'])
