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

    model_config = pydantic.ConfigDict(frozen=True)

    #: Id of the employee
    id: int = pydantic.Field(description='Id of the employee')
    #: Access_id associated to the employee
    access_id: int = pydantic.Field(description='Access_id associated to the employee')
    #: Name of the employee
    first_name: str = pydantic.Field(description='Name of the employee')
    #: Last name of the employee
    last_name: str = pydantic.Field(description='Last name of the employee')
    #: Full name of the employee
    full_name: str = pydantic.Field(description='Full name of the employee')
    #: Nickname of the employee or a name that defines the employee better
    preferred_name: str | None = pydantic.Field(
        default=None,
        description='Nickname of the employee or a name that defines the employee better',
    )
    #: Birthname of the employee
    birth_name: str | None = pydantic.Field(default=None, description='Birthname of the employee')
    #: Gender of the employee (male | female)
    gender: str | None = pydantic.Field(default=None, description='Gender of the employee (male | female)')
    #: National identifier number
    identifier: str | None = pydantic.Field(default=None, description='National identifier number')
    #: Type of identifier (ex passport)
    identifier_type: str | None = pydantic.Field(default=None, description='Type of identifier (ex passport)')
    #: Personal email of the employee
    email: str | None = pydantic.Field(default=None, description='Personal email of the employee')
    #: Email associated to the session
    login_email: str | None = pydantic.Field(default=None, description='Email associated to the session')
    #: Birthday of the employee
    birthday_on: datetime.date | None = pydantic.Field(default=None, description='Birthday of the employee')
    #: Nationality country code of the employee (Spain ES, United Kingdom GB)
    nationality: str | None = pydantic.Field(
        default=None,
        description='Nationality country code of the employee (Spain ES, United Kingdom GB)',
    )
    #: Address of the employee
    address_line_1: str | None = pydantic.Field(default=None, description='Address of the employee')
    #: Secondary address of the employee
    address_line_2: str | None = pydantic.Field(default=None, description='Secondary address of the employee')
    #: Postal code of the employee
    postal_code: str | None = pydantic.Field(default=None, description='Postal code of the employee')
    #: City of the employee
    city: str | None = pydantic.Field(default=None, description='City of the employee')
    #: State/province/region of the employee
    state: str | None = pydantic.Field(default=None, description='State/province/region of the employee')
    #: Country code of the employee (Spain ES, United Kingdom GB)
    country: str | None = pydantic.Field(
        default=None,
        description='Country code of the employee (Spain ES, United Kingdom GB)',
    )
    #: Bank account number of the employee
    bank_number: str | None = pydantic.Field(default=None, description='Bank account number of the employee')
    #: Code to identify banks and financial institutions globally
    swift_bic: str | None = pydantic.Field(
        default=None,
        description='Code to identify banks and financial institutions globally',
    )
    #: Bank number format
    bank_number_format: BankNumberFormat | None = pydantic.Field(default=None, description='Bank number format')
    #: Id of the company to which the employee belongs (not editable)
    company_id: int = pydantic.Field(description='Id of the company to which the employee belongs (not editable)')
    #: Legal entity of the employee, references to companies/legal_entities
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='Legal entity of the employee, references to companies/legal_entities',
    )
    #: Location id of the employee, references to locations/locations
    location_id: int = pydantic.Field(description='Location id of the employee, references to locations/locations')
    #: Creation date of the employee
    created_at: datetime.datetime = pydantic.Field(description='Creation date of the employee')
    #: Date of last modification of the employee
    updated_at: datetime.datetime = pydantic.Field(description='Date of last modification of the employee')
    #: Social security number of the employee
    social_security_number: str | None = pydantic.Field(
        default=None,
        description='Social security number of the employee',
    )
    #: Is the employee being terminated?
    is_terminating: bool = pydantic.Field(description='Is the employee being terminated?')
    #: Termination date of the employee
    terminated_on: datetime.date | None = pydantic.Field(default=None, description='Termination date of the employee')
    #: Termination reason type of the employee
    termination_reason_type: str | None = pydantic.Field(
        default=None,
        description='Termination reason type of the employee',
    )
    #: A reason for the termination
    termination_reason: str | None = pydantic.Field(default=None, description='A reason for the termination')
    #: Observations about the termination
    termination_observations: str | None = pydantic.Field(
        default=None,
        description='Observations about the termination',
    )
    #: Manager id of the employee, you can get the manager id from employees endpoint
    manager_id: int | None = pydantic.Field(
        default=None,
        description='Manager id of the employee, you can get the manager id from employees endpoint',
    )
    #: Timeoff manager id of the employee
    timeoff_manager_id: int | None = pydantic.Field(default=None, description='Timeoff manager id of the employee')
    #: Phone number of the employee
    phone_number: str | None = pydantic.Field(default=None, description='Phone number of the employee')
    #: Identity number or string used inside a company to internally identify the employee
    company_identifier: str | None = pydantic.Field(
        default=None,
        description='Identity number or string used inside a company to internally identify the employee',
    )
    #: Age of the employee
    age_number: int | None = pydantic.Field(default=None, description='Age of the employee')
    #: The description of the termination type
    termination_type_description: str | None = pydantic.Field(
        default=None,
        description='The description of the termination type',
    )
    #: Name of the employee contact
    contact_name: str | None = pydantic.Field(default=None, description='Name of the employee contact')
    #: Phone number of the employee contact
    contact_number: str | None = pydantic.Field(default=None, description='Phone number of the employee contact')
    #: Personal email of the employee
    personal_email: str | None = pydantic.Field(default=None, description='Personal email of the employee')
    #: Date since when the employee is working in the company
    seniority_calculation_date: datetime.date | None = pydantic.Field(
        default=None,
        description='Date since when the employee is working in the company',
    )
    #: Pronouns that an employee uses to define themselves
    pronouns: str | None = pydantic.Field(
        default=None,
        description='Pronouns that an employee uses to define themselves',
    )
    #: Status of the employee, true when active, false when terminated
    active: bool | None = pydantic.Field(
        default=None,
        description='Status of the employee, true when active, false when terminated',
    )
    #: Officially certified level of disability granted by public administration for individuals with physical or mental
    #: impairments, expressed in cents
    disability_percentage_cents: int | None = pydantic.Field(
        default=None,
        description='Officially certified level of disability granted by public administration for individuals with physical or mental impairments, expressed in cents',  # noqa: E501
    )
    #: Identifier expiration date
    identifier_expiration_date: datetime.date | None = pydantic.Field(
        default=None,
        description='Identifier expiration date',
    )
    #: Employee included in a time tracking policy
    attendable: bool = pydantic.Field(description='Employee included in a time tracking policy')
    #: Country of birth of the employee
    country_of_birth: str | None = pydantic.Field(default=None, description='Country of birth of the employee')
    #: Birthplace of the employee
    birthplace: str | None = pydantic.Field(default=None, description='Birthplace of the employee')


class EmployeesEndpoint(Endpoint):
    """Endpoint for employees/employees operations."""

    endpoint = 'employees/employees'

    async def all(self, **kwargs) -> ListApiResponse[Employee]:
        """Get all employees records.

        Official documentation: `employees/employees <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-employees-employees>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Employee]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Employee, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Employee]:
        """Get employees with pagination metadata.

        Official documentation: `employees/employees <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-employees-employees>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Employee]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Employee, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, employee_id: int | str, **kwargs) -> Employee:
        """Get a specific employee by ID.

        Official documentation: `employees/employees <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-employees-employees-id>`_

        :param employee_id: The unique identifier.
        :type employee_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Employee
        """
        data = await self.api.get(self.endpoint, employee_id, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(data)

    async def update(self, employee_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Update an employee.

        Official documentation: `employees/employees <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-employees-employees-id>`_

        :param employee_id: The unique identifier of the record to update.
        :type employee_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Employee
        """
        response = await self.api.put(self.endpoint, employee_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)

    async def create_with_contract(self, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Create an employee with contract.

        Official documentation: `employees/employees <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-employees-employees-create-with-contract>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Employee
        """
        response = await self.api.post(self.endpoint, 'create_with_contract', json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)

    async def invite(self, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Invite an employee.

        Official documentation: `employees/employees <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-employees-employees-invite>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Employee
        """
        response = await self.api.post(self.endpoint, 'invite', json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)

    async def terminate(self, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Terminate an employee.

        Official documentation: `employees/employees <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-employees-employees-terminate>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Employee
        """
        response = await self.api.post(self.endpoint, 'terminate', json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)

    async def unterminate(self, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Unterminate an employee.

        Official documentation: `employees/employees <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-employees-employees-unterminate>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Employee
        """
        response = await self.api.post(self.endpoint, 'unterminate', json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)

    async def set_regular_access_start_date(self, data: Mapping[str, typing.Any], **kwargs) -> Employee:
        """Set regular access start date for an employee.

        Official documentation: `employees/employees <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-employees-employees-set-regular-access-start-date>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Employee
        """
        response = await self.api.post(self.endpoint, 'set_regular_access_start_date', json=data, **kwargs)
        return pydantic.TypeAdapter(Employee).validate_python(response)
