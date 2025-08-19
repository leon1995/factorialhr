import datetime
import typing
from collections.abc import Mapping, Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class EmployeeAbsence(pydantic.BaseModel):
    """Model for employee_updates_absence."""

    id: int = pydantic.Field(description='Identifier of the absence employee update')
    status: str = pydantic.Field(description='The status of the employee update')
    employee_id: int | None = pydantic.Field(default=None, description='Employee id of the absence')
    employee_full_name: str | None = pydantic.Field(default=None, description='Full name of the employee')
    approved: bool | None = pydantic.Field(default=None, description='Indicates if the absence is approved')
    description: str | None = pydantic.Field(default=None, description='A description of the absence')
    start_on: datetime.datetime | None = pydantic.Field(default=None, description='The start date of the absence')
    prev_start_on: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The previous start date of the absence',
    )
    finish_on: datetime.datetime | None = pydantic.Field(default=None, description='The end date of the absence')
    prev_finish_on: str | None = pydantic.Field(default=None, description='The previous end date of the absence')
    half_day: str | None = pydantic.Field(default=None, description='Indicates if the absence is taken as a half-day')
    hours_amount_in_cents: int | None = pydantic.Field(
        default=None,
        description='The total number of hours taken for the absence, represented in cents',
    )
    leave_type_id: int | None = pydantic.Field(default=None, description='The id of the leave type')
    leave_type_name: str | None = pydantic.Field(default=None, description='The name of the leave type')


class EmployeeContractChange(pydantic.BaseModel):
    """Model for employee_updates_contract_change."""

    id: int = pydantic.Field(description='The id of the contract change incidence')
    status: str = pydantic.Field(description='The status of the contract change incidence')
    effective_on: datetime.date = pydantic.Field(description='The effective date of the contract')
    starts_on: datetime.date | None = pydantic.Field(default=None, description='The start date of the contract')
    ends_on: datetime.date | None = pydantic.Field(default=None, description='The end date of the contract')
    employee_id: int = pydantic.Field(description='The employee id')
    job_title: str | None = pydantic.Field(default=None, description='The job title on the contract change')
    job_role: str | None = pydantic.Field(default=None, description='The job role on the contract change')
    job_level: str | None = pydantic.Field(default=None, description='The job level on the contract change')
    has_payroll: bool = pydantic.Field(description='The payrollable status of the employee on the contract change')
    salary_amount: int | None = pydantic.Field(default=None, description='The salary amount on the contract change')
    salary_frequency: str | None = pydantic.Field(
        default=None,
        description='The salary payment frequency on the contract change',
    )
    working_week_days: str | None = pydantic.Field(
        default=None,
        description='The working week days on the contract change',
    )
    working_hours: int | None = pydantic.Field(default=None, description='The working hours on the contract change')
    working_hours_frequency: str | None = pydantic.Field(
        default=None,
        description='The working hours frequency on the contract change',
    )
    country: str | None = pydantic.Field(default=None, description='The country on the contract change')
    es_has_teleworking_contract: bool | None = pydantic.Field(
        default=None,
        description='The teleworking status on the contract change',
    )
    es_cotization_group: int | None = pydantic.Field(
        default=None,
        description='The cotization group on the contract change',
    )
    es_contract_observations: str | None = pydantic.Field(
        default=None,
        description='The contract observations on the contract change',
    )
    es_job_description: str | None = pydantic.Field(
        default=None,
        description='The job description on the contract change',
    )
    es_contract_type_id: int | None = pydantic.Field(
        default=None,
        description='The contract type id on the contract change',
    )
    es_contract_type_name: str | None = pydantic.Field(
        default=None,
        description='The contract type name on the contract change',
    )
    es_trial_period_ends_on: datetime.date | None = pydantic.Field(
        default=None,
        description='The trial period end date on the contract change',
    )
    es_working_day_type_id: int | None = pydantic.Field(
        default=None,
        description='The working day type id on the contract change',
    )
    es_education_level_id: int | None = pydantic.Field(
        default=None,
        description='The education level id on the contract change',
    )
    es_professional_category_id: int | None = pydantic.Field(
        default=None,
        description='The professional category id on the contract change',
    )
    fr_employee_type: str | None = pydantic.Field(
        default=None,
        description='The employee type on the contract change',
    )
    fr_forfait_jours: bool = pydantic.Field(description='The forfait jours status on the contract change')
    fr_jours_par_an: int | None = pydantic.Field(
        default=None,
        description='The jours par an on the contract change',
    )
    fr_coefficient: str | None = pydantic.Field(default=None, description='The coefficient on the contract change')
    fr_level_id: int | None = pydantic.Field(default=None, description='The level id on the contract change')
    fr_level_name: str | None = pydantic.Field(default=None, description='The level name on the contract change')
    fr_step_id: int | None = pydantic.Field(default=None, description='The step id on the contract change')
    fr_step_name: str | None = pydantic.Field(default=None, description='The step name on the contract change')
    fr_mutual_id: int | None = pydantic.Field(default=None, description='The mutual id on the contract change')
    fr_mutual_name: str | None = pydantic.Field(default=None, description='The mutual name on the contract change')
    fr_professional_category_id: int | None = pydantic.Field(
        default=None,
        description='The professional category id on the contract change',
    )
    fr_professional_category_name: str | None = pydantic.Field(
        default=None,
        description='The professional category name on the contract change',
    )
    fr_work_type_id: int | None = pydantic.Field(
        default=None,
        description='The work type id on the contract change',
    )
    fr_work_type_name: str | None = pydantic.Field(
        default=None,
        description='The work type name on the contract change',
    )
    compensation_ids: Sequence[int] | None = pydantic.Field(
        default=None,
        description='List of compensation identifiers',
    )
    fr_contract_type_id: int | None = pydantic.Field(
        default=None,
        description='The contract type id on the contract change',
    )
    fr_contract_type_name: str | None = pydantic.Field(
        default=None,
        description='The contract type name on the contract change',
    )
    de_contract_type_id: int | None = pydantic.Field(
        default=None,
        description='The contract type id on the contract change',
    )
    de_contract_type_name: str | None = pydantic.Field(
        default=None,
        description='The contract type name on the contract change',
    )
    pt_contract_type_id: int | None = pydantic.Field(
        default=None,
        description='The contract type id on the contract change',
    )
    pt_contract_type_name: str | None = pydantic.Field(
        default=None,
        description='The contract type name on the contract change',
    )
    created_at: datetime.datetime = pydantic.Field(description='Creation timestamp of the contract change')
    updated_at: datetime.datetime = pydantic.Field(description='Last update timestamp of the contract change')


class EmployeeNewHire(pydantic.BaseModel):
    """Model for employee_updates_new_hire."""

    id: int = pydantic.Field(description='The id of the new hire incidence')
    status: str = pydantic.Field(description='The status of the new hire incidence')
    employee_id: int = pydantic.Field(description='The employee id of the new hire')
    first_name: str = pydantic.Field(description='Name of the employee')
    last_name: str = pydantic.Field(description='Last name of the employee')
    birth_name: str | None = pydantic.Field(default=None, description='The birth name of the new hire')
    identifier: str | None = pydantic.Field(default=None, description='National identifier number')
    identifier_type: str | None = pydantic.Field(default=None, description='Type of identifier (ex passport)')
    payroll_identifier: str | None = pydantic.Field(default=None, description='Payroll identifier')
    work_email: str | None = pydantic.Field(default=None, description='Personal email of the employee')
    phone_number: str | None = pydantic.Field(default=None, description='Phone number of the employee')
    gender: str | None = pydantic.Field(default=None, description='Gender of the employee (male | female)')
    job_title: str | None = pydantic.Field(default=None, description='Job title of the employee')
    address: str = pydantic.Field(description='Address of the employee')
    city: str | None = pydantic.Field(default=None, description='City of the employee')
    country: str | None = pydantic.Field(
        default=None,
        description='Country code of the employee (Spain ES, United Kingdom GB)',
    )
    state: str | None = pydantic.Field(default=None, description='State/province/region of the employee')
    postal_code: str | None = pydantic.Field(default=None, description='Postal code of the employee')
    date_of_birth: datetime.date | None = pydantic.Field(default=None, description='Birthday of the employee')
    nationality: str | None = pydantic.Field(
        default=None,
        description='Nationality country code of the employee (Spain ES, United Kingdom GB)',
    )
    start_date: datetime.date | None = pydantic.Field(default=None, description='Start date of the employee')
    contract_effective_date: datetime.date | None = pydantic.Field(default=None, description='Contract effective date')
    contract_end_date: datetime.date | None = pydantic.Field(default=None, description='Contract end date')
    bank_account: str | None = pydantic.Field(default=None, description='Bank account number of the employee')
    salary_amount_in_cents: int | None = pydantic.Field(default=None, description='Salary amount in cents')
    salary_frequency: str | None = pydantic.Field(default=None, description='Salary payment frequency')
    working_hours: int | None = pydantic.Field(default=None, description='Working hours')
    working_hours_frequency: str | None = pydantic.Field(default=None, description='Working hours frequency')
    social_security_number: str | None = pydantic.Field(
        default=None,
        description='Social security number of the employee',
    )
    manager_id: int | None = pydantic.Field(
        default=None,
        description='Manager id of the employee, you can get the manager id from employees endpoint',
    )
    tax_id: str | None = pydantic.Field(default=None, description='Tax identification number')
    legal_entity_id: int | None = pydantic.Field(default=None, description='The legal entity id of the new hire')
    workplace_id: int | None = pydantic.Field(default=None, description='Workplace id of the employee')


class EmployeePersonalChange(pydantic.BaseModel):
    """Model for employee_updates_personal_change."""

    id: int = pydantic.Field(description='The id of the personal change incidence')
    status: str = pydantic.Field(description='The status of the personal change incidence')
    employee_id: int = pydantic.Field(description='The employee id of the personal change')
    work_email: str | None = pydantic.Field(default=None, description='Personal email of the employee')
    phone_number: str | None = pydantic.Field(default=None, description='Phone number of the employee')
    identifier_type: str | None = pydantic.Field(default=None, description='Type of identifier (ex passport)')
    identifier: str | None = pydantic.Field(default=None, description='National identifier number')
    social_security_number: str | None = pydantic.Field(
        default=None,
        description='Social security number of the employee',
    )
    tax_id: str | None = pydantic.Field(default=None, description='Tax identification number')
    first_name: str = pydantic.Field(description='Name of the employee')
    last_name: str = pydantic.Field(description='Last name of the employee')
    gender: str | None = pydantic.Field(default=None, description='Gender of the employee (male | female)')
    date_of_birth: datetime.date | None = pydantic.Field(default=None, description='Birthday of the employee')
    nationality: str | None = pydantic.Field(
        default=None,
        description='Nationality country code of the employee (Spain ES, United Kingdom GB)',
    )
    address_line_1: str | None = pydantic.Field(default=None, description='Address line 1 of the employee')
    address_line_2: str | None = pydantic.Field(default=None, description='Address line 2 of the employee')
    postal_code: str | None = pydantic.Field(default=None, description='Postal code of the employee')
    city: str | None = pydantic.Field(default=None, description='City of the employee')
    state: str | None = pydantic.Field(default=None, description='State/province/region of the employee')
    country: str | None = pydantic.Field(
        default=None,
        description='Country code of the employee (Spain ES, United Kingdom GB)',
    )
    bank_number: str | None = pydantic.Field(default=None, description='Bank account number of the employee')
    job_title: str | None = pydantic.Field(default=None, description='Job title of the employee')
    workplace_id: int | None = pydantic.Field(default=None, description='Workplace id of the employee')


class EmployeeSummary(pydantic.BaseModel):
    """Model for employee_updates_summary."""

    id: int = pydantic.Field(description='Unique identifier for the employee update summary')
    employee_id: int | None = pydantic.Field(default=None, description='Employee identifier')
    legal_entity_id: int = pydantic.Field(description='Legal entity identifier')
    status: str = pydantic.Field(description='Status of the employee update')
    type: str = pydantic.Field(description='Type of employee update')
    starts_on: datetime.date | None = pydantic.Field(default=None, description='Start date of the update')
    ends_on: datetime.date | None = pydantic.Field(default=None, description='End date of the update')
    created_at: datetime.datetime = pydantic.Field(description='Creation timestamp of the update')


class EmployeeTermination(pydantic.BaseModel):
    """Model for employee_updates_termination."""

    id: int = pydantic.Field(description='Unique identifier for the termination update')
    status: str = pydantic.Field(description='Status of the termination update')
    employee_id: int = pydantic.Field(description='Employee identifier')
    terminated_on: datetime.date | None = pydantic.Field(default=None, description='Termination date')
    termination_reason: str | None = pydantic.Field(default=None, description='Reason for termination')
    termination_observations: str | None = pydantic.Field(
        default=None,
        description='Observations about the termination',
    )
    legal_entity_id: int | None = pydantic.Field(default=None, description='Legal entity identifier')
    remaining_holidays: Sequence[typing.Any] = pydantic.Field(description='List of remaining holidays')
    termination_reason_type: str | None = pydantic.Field(default=None, description='Type of termination reason')
    termination_type_description: str | None = pydantic.Field(
        default=None,
        description='The description of the termination type',
    )


class AbsencesEndpoint(Endpoint):
    """Endpoint for employee_updates/absences operations."""

    endpoint = 'employee_updates/absences'

    async def all(self, **kwargs) -> ListApiResponse[EmployeeAbsence]:
        """Get all absences records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=EmployeeAbsence)

    async def get(self, **kwargs) -> MetaApiResponse[EmployeeAbsence]:
        """Get absences with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=EmployeeAbsence)

    async def get_by_id(self, absence_id: int | str, **kwargs) -> EmployeeAbsence:
        """Get a specific absence by ID."""
        data = await self.api.get(self.endpoint, absence_id, **kwargs)
        return pydantic.TypeAdapter(EmployeeAbsence).validate_python(data)


class ContractChangesEndpoint(Endpoint):
    """Endpoint for employee_updates/contract_changes operations."""

    endpoint = 'employee_updates/contract_changes'

    async def all(self, **kwargs) -> ListApiResponse[EmployeeContractChange]:
        """Get all contract changes records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=EmployeeContractChange)

    async def get(self, **kwargs) -> MetaApiResponse[EmployeeContractChange]:
        """Get contract changes with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=EmployeeContractChange)

    async def get_by_id(self, contract_change_id: int | str, **kwargs) -> EmployeeContractChange:
        """Get a specific contract change by ID."""
        data = await self.api.get(self.endpoint, contract_change_id, **kwargs)
        return pydantic.TypeAdapter(EmployeeContractChange).validate_python(data)


class NewHiresEndpoint(Endpoint):
    """Endpoint for employee_updates/new_hires operations."""

    endpoint = 'employee_updates/new_hires'

    async def all(self, **kwargs) -> ListApiResponse[EmployeeNewHire]:
        """Get all new hires records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=EmployeeNewHire)

    async def get(self, **kwargs) -> MetaApiResponse[EmployeeNewHire]:
        """Get new hires with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=EmployeeNewHire)

    async def get_by_id(self, new_hire_id: int | str, **kwargs) -> EmployeeNewHire:
        """Get a specific new hire by ID."""
        data = await self.api.get(self.endpoint, new_hire_id, **kwargs)
        return pydantic.TypeAdapter(EmployeeNewHire).validate_python(data)


class PersonalChangesEndpoint(Endpoint):
    """Endpoint for employee_updates/personal_changes operations."""

    endpoint = 'employee_updates/personal_changes'

    async def all(self, **kwargs) -> ListApiResponse[EmployeePersonalChange]:
        """Get all personal changes records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=EmployeePersonalChange)

    async def get(self, **kwargs) -> MetaApiResponse[EmployeePersonalChange]:
        """Get personal changes with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=EmployeePersonalChange)

    async def get_by_id(self, personal_change_id: int | str, **kwargs) -> EmployeePersonalChange:
        """Get a specific personal change by ID."""
        data = await self.api.get(self.endpoint, personal_change_id, **kwargs)
        return pydantic.TypeAdapter(EmployeePersonalChange).validate_python(data)


class SummariesEndpoint(Endpoint):
    """Endpoint for employee_updates/summaries operations."""

    endpoint = 'employee_updates/summaries'

    async def all(self, **kwargs) -> ListApiResponse[EmployeeSummary]:
        """Get all summaries records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=EmployeeSummary)

    async def get(self, **kwargs) -> MetaApiResponse[EmployeeSummary]:
        """Get summaries with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=EmployeeSummary)

    async def get_by_id(self, summary_id: int | str, **kwargs) -> EmployeeSummary:
        """Get a specific summary by ID."""
        data = await self.api.get(self.endpoint, summary_id, **kwargs)
        return pydantic.TypeAdapter(EmployeeSummary).validate_python(data)


class TerminationsEndpoint(Endpoint):
    """Endpoint for employee_updates/terminations operations."""

    endpoint = 'employee_updates/terminations'

    async def all(self, **kwargs) -> ListApiResponse[EmployeeTermination]:
        """Get all terminations records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=EmployeeTermination)

    async def get(self, **kwargs) -> MetaApiResponse[EmployeeTermination]:
        """Get terminations with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=EmployeeTermination)

    async def get_by_id(self, termination_id: int | str, **kwargs) -> EmployeeTermination:
        """Get a specific termination by ID."""
        data = await self.api.get(self.endpoint, termination_id, **kwargs)
        return pydantic.TypeAdapter(EmployeeTermination).validate_python(data)


class EmployeeUpdatesEndpoint(Endpoint):
    """Endpoint for employee_updates operations."""

    endpoint = 'employee_updates'

    async def all(self, **kwargs) -> ListApiResponse[EmployeeAbsence]:
        """Get all employee_updates records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=EmployeeAbsence)

    async def get(self, **kwargs) -> MetaApiResponse[EmployeeAbsence]:
        """Get employee_updates with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=EmployeeAbsence)

    async def get_by_id(self, employee_update_id: int | str, **kwargs) -> EmployeeAbsence:
        """Get a specific employee_updates by ID."""
        data = await self.api.get(self.endpoint, employee_update_id, **kwargs)
        return pydantic.TypeAdapter(EmployeeAbsence).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> EmployeeAbsence:
        """Create a new employee_updates."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(EmployeeAbsence).validate_python(response['data'])

    async def update(self, update_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> EmployeeAbsence:
        """Update a employee_updates."""
        response = await self.api.put(self.endpoint, update_id, json=data, **kwargs)
        return pydantic.TypeAdapter(EmployeeAbsence).validate_python(response['data'])

    async def delete(self, update_id: int | str, **kwargs) -> None:
        """Delete a employee_updates."""
        await self.api.delete(self.endpoint, update_id, **kwargs)
