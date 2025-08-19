import datetime
import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class BankNumberFormat(StrEnum):
    """Enum for bank number formats."""

    IBAN = 'iban'
    SORT_CODE_AND_ACCOUNT_NUMBER = 'sort_code_and_account_number'
    ROUTING_NUMBER_AND_ACCOUNT_NUMBER = 'routing_number_and_account_number'
    CLABE = 'clabe'
    OTHER = 'other'
    BANK_NAME_AND_ACCOUNT_NUMBER = 'bank_name_and_account_number'


class Employee(pydantic.BaseModel):
    """Model for employees_employee."""

    id: int = pydantic.Field(description='Id of the employee')
    access_id: int = pydantic.Field(description='Access_id associated to the employee')
    first_name: str = pydantic.Field(description='Name of the employee')
    last_name: str = pydantic.Field(description='Last name of the employee')
    full_name: str = pydantic.Field(description='Full name of the employee')
    preferred_name: str | None = pydantic.Field(
        default=None,
        description='Nickname of the employee or a name that defines the employee better',
    )
    birth_name: str | None = pydantic.Field(default=None, description='Birthname of the employee')
    gender: str | None = pydantic.Field(default=None, description='Gender of the employee (male | female)')
    identifier: str | None = pydantic.Field(default=None, description='National identifier number')
    identifier_type: str | None = pydantic.Field(default=None, description='Type of identifier (ex passport)')
    email: str | None = pydantic.Field(default=None, description='Personal email of the employee')
    login_email: str | None = pydantic.Field(default=None, description='Email associated to the session')
    birthday_on: datetime.date | None = pydantic.Field(default=None, description='Birthday of the employee')
    nationality: str | None = pydantic.Field(
        default=None,
        description='Nationality country code of the employee (Spain ES, United Kingdom GB)',
    )
    address_line_1: str | None = pydantic.Field(default=None, description='Address of the employee')
    address_line_2: str | None = pydantic.Field(default=None, description='Secondary address of the employee')
    postal_code: str | None = pydantic.Field(default=None, description='Postal code of the employee')
    city: str | None = pydantic.Field(default=None, description='City of the employee')
    state: str | None = pydantic.Field(default=None, description='State/province/region of the employee')
    country: str | None = pydantic.Field(
        default=None,
        description='Country code of the employee (Spain ES, United Kingdom GB)',
    )
    bank_number: str | None = pydantic.Field(default=None, description='Bank account number of the employee')
    swift_bic: str | None = pydantic.Field(
        default=None,
        description='Code to identify banks and financial institutions globally',
    )
    bank_number_format: BankNumberFormat | None = pydantic.Field(default=None, description='Bank number format')
    company_id: int = pydantic.Field(description='Id of the company to which the employee belongs (not editable)')
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='Legal entity of the employee, references to companies/legal_entities',
    )
    location_id: int = pydantic.Field(description='Location id of the employee, references to locations/locations')
    created_at: datetime.datetime = pydantic.Field(description='Creation date of the employee')
    updated_at: datetime.datetime = pydantic.Field(description='Date of last modification of the employee')
    social_security_number: str | None = pydantic.Field(
        default=None,
        description='Social security number of the employee',
    )
    is_terminating: bool = pydantic.Field(description='Is the employee being terminated?')
    terminated_on: datetime.date | None = pydantic.Field(default=None, description='Termination date of the employee')
    termination_reason_type: str | None = pydantic.Field(
        default=None,
        description='Termination reason type of the employee',
    )
    termination_reason: str | None = pydantic.Field(default=None, description='A reason for the termination')
    termination_observations: str | None = pydantic.Field(
        default=None,
        description='Observations about the termination',
    )
    manager_id: int | None = pydantic.Field(
        default=None,
        description='Manager id of the employee, you can get the manager id from employees endpoint',
    )
    timeoff_manager_id: int | None = pydantic.Field(default=None, description='Timeoff manager id of the employee')
    phone_number: str | None = pydantic.Field(default=None, description='Phone number of the employee')
    company_identifier: str | None = pydantic.Field(
        default=None,
        description='Identity number or string used inside a company to internally identify the employee',
    )
    age_number: int | None = pydantic.Field(default=None, description='Age of the employee')
    termination_type_description: str | None = pydantic.Field(
        default=None,
        description='The description of the termination type',
    )
    contact_name: str | None = pydantic.Field(default=None, description='Name of the employee contact')
    contact_number: str | None = pydantic.Field(default=None, description='Phone number of the employee contact')
    personal_email: str | None = pydantic.Field(default=None, description='Personal email of the employee')
    seniority_calculation_date: datetime.date | None = pydantic.Field(
        default=None,
        description='Date since when the employee is working in the company',
    )
    pronouns: str | None = pydantic.Field(
        default=None,
        description='Pronouns that an employee uses to define themselves',
    )
    active: bool | None = pydantic.Field(
        default=None,
        description='Status of the employee, true when active, false when terminated',
    )
    disability_percentage_cents: int | None = pydantic.Field(
        default=None,
        description='Officially certified level of disability granted by public administration for individuals with physical or mental impairments, expressed in cents',  # noqa: E501
    )
    identifier_expiration_date: datetime.date | None = pydantic.Field(
        default=None,
        description='Identifier expiration date',
    )
    attendable: bool = pydantic.Field(description='Employee included in a time tracking policy')
    country_of_birth: str | None = pydantic.Field(default=None, description='Country of birth of the employee')
    birthplace: str | None = pydantic.Field(default=None, description='Birthplace of the employee')


class EmployeesEndpoint(Endpoint):
    """Endpoint for employees/employees operations."""

    endpoint = 'employees/employees'

    async def all(self, **kwargs) -> ListApiResponse[Employee]:
        """Get all employees records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Employee, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Employee]:
        """Get employees with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Employee, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, employee_id: int | str, **kwargs) -> Employee:
        """Get a specific employee by ID."""
        data = await self.api.get(self.endpoint, employee_id, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(data)

    async def update(self, employee_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Update an employee."""
        response = await self.api.put(self.endpoint, employee_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)

    async def create_with_contract(self, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Create an employee with contract."""
        response = await self.api.post(self.endpoint, 'create_with_contract', json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)

    async def invite(self, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Invite an employee."""
        response = await self.api.post(self.endpoint, 'invite', json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)

    async def terminate(self, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Terminate an employee."""
        response = await self.api.post(self.endpoint, 'terminate', json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)

    async def unterminate(self, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Unterminate an employee."""
        response = await self.api.post(self.endpoint, 'unterminate', json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)
