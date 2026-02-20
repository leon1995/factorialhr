import datetime
import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class TimeCondition(StrEnum):
    """Enum for time conditions."""

    FULL_DAY = 'full_day'
    HALF_DAY = 'half_day'
    CUSTOM = 'custom'


class BankHolidayTreatment(StrEnum):
    """Enum for bank holiday treatment."""

    WORKABLE = 'workable'
    NON_WORKABLE = 'non_workable'


class AnnualWorkingTimeDistribution(StrEnum):
    """Enum for annual working time distribution."""

    LIMIT_WORKDAYS = 'limit_workdays'
    LIMIT_DAILY_HOURS = 'limit_daily_hours'


class Compensation(pydantic.BaseModel):
    """Model for contracts_compensation."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Compensation ID
    id: int = pydantic.Field(description='Compensation ID')
    #: Contract version ID
    contract_version_id: int = pydantic.Field(description='Contract version ID')
    #: Contracts taxonomy ID
    contracts_taxonomy_id: int = pydantic.Field(description='Contracts taxonomy ID')
    #: Compensation description
    description: str | None = pydantic.Field(default=None, description='Compensation description')
    #: Required field. You can only use the following options: fixed, undefined, up_to, per_worked_day, per_worked_hour
    compensation_type: str | None = pydantic.Field(
        default=None,
        description=(
            'Required field. You can only use the following options: '
            'fixed, undefined, up_to, per_worked_day, per_worked_hour'
        ),
    )
    #: Required field unless your compensation type is undefined
    amount: int | None = pydantic.Field(
        default=None,
        description='Required field unless your compensation type is undefined',
    )
    #: Unit of the compensation
    unit: str = pydantic.Field(description='Unit of the compensation')
    #: Sync with supplements
    sync_with_supplements: bool | None = pydantic.Field(default=None, description='Sync with supplements')
    #: Payroll policy ID
    payroll_policy_id: int | None = pydantic.Field(default=None, description='Payroll policy ID')
    #: Recurrence count
    recurrence_count: int | None = pydantic.Field(default=None, description='Recurrence count')
    #: When the compensation starts_on
    starts_on: datetime.date | None = pydantic.Field(default=None, description='When the compensation starts_on')
    #: Compensation recurrence
    recurrence: str | None = pydantic.Field(default=None, description='Compensation recurrence')
    #: When the first payment is done
    first_payment_on: datetime.date | None = pydantic.Field(default=None, description='When the first payment is done')
    #: Compensation calculation
    calculation: str | None = pydantic.Field(default=None, description='Compensation calculation')
    #: Currency of the compensation
    currency: str | None = pydantic.Field(default=None, description='Currency of the compensation')
    #: Time condition for the compensation
    time_condition: TimeCondition | None = pydantic.Field(
        default=None,
        description='Time condition for the compensation',
    )
    #: Minimum amount of hours
    minimum_amount_of_hours: int | None = pydantic.Field(default=None, description='Minimum amount of hours')
    #: Compensation expected minimum amount of hours in cents
    minimum_amount_of_hours_in_cents: int | None = pydantic.Field(
        default=None,
        description='Compensation expected minimum amount of hours in cents',
    )


class ContractTemplate(pydantic.BaseModel):
    """Model for contracts_contract_template."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Unique identifier for the contract template
    id: int = pydantic.Field(description='Unique identifier for the contract template')
    #: ID of the company this template belongs to
    company_id: int | None = pydantic.Field(default=None, description='ID of the company this template belongs to')
    #: Type of contract version (e.g., es for Spain, fr for France)
    contract_version_type: str | None = pydantic.Field(
        default=None,
        description='Type of contract version (e.g., es for Spain, fr for France)',
    )


class ContractVersion(pydantic.BaseModel):
    """Model for contracts_contract_version."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier for the contract version
    id: int | None = pydantic.Field(default=None, description='Identifier for the contract version')
    #: Identifier for company
    company_id: int = pydantic.Field(description='Identifier for company')
    #: Employee identifier, refers to /employees/employees endpoint
    employee_id: int = pydantic.Field(description='Employee identifier, refers to /employees/employees endpoint')
    #: The day the specific contract starts, in case of hiring the same than starts_on
    effective_on: datetime.date = pydantic.Field(
        description='The day the specific contract starts, in case of hiring the same than starts_on',
    )
    #: Nationality country code of the employee (Spain ES, United Kingdom GB)
    country: str | None = pydantic.Field(
        default=None,
        description='Nationality country code of the employee (Spain ES, United Kingdom GB)',
    )
    #: Job title of the employee
    job_title: str | None = pydantic.Field(default=None, description='Job title of the employee')
    #: Job catalog level identifier, refers to /job_catalog/levels endpoint
    job_catalog_level_id: int | None = pydantic.Field(
        default=None,
        description='Job catalog level identifier, refers to /job_catalog/levels endpoint',
    )
    #: The day the employee is hired
    starts_on: datetime.date | None = pydantic.Field(default=None, description='The day the employee is hired')
    #: The day the employee is terminated
    ends_on: datetime.date | None = pydantic.Field(default=None, description='The day the employee is terminated')
    #: Boolean that indicates if the employee associated to this contract belongs to a payroll policy
    has_payroll: bool = pydantic.Field(
        description='Boolean that indicates if the employee associated to this contract belongs to a payroll policy',
    )
    #: A flag that indicates if the employee has a trial period
    has_trial_period: bool | None = pydantic.Field(
        default=None,
        description='A flag that indicates if the employee has a trial period',
    )
    #: When the trial period ends
    trial_period_ends_on: datetime.date | None = pydantic.Field(default=None, description='When the trial period ends')
    #: The amount of money the employee earns
    salary_amount: int | None = pydantic.Field(default=None, description='The amount of money the employee earns')
    #: The frequency of the salary payment
    salary_frequency: str | None = pydantic.Field(default=None, description='The frequency of the salary payment')
    #: The days of the week the employee works
    working_week_days: str | None = pydantic.Field(default=None, description='The days of the week the employee works')
    #: The amount of hours the employee works
    working_hours: int | None = pydantic.Field(default=None, description='The amount of hours the employee works')
    #: The frequency of the working hours
    working_hours_frequency: str | None = pydantic.Field(default=None, description='The frequency of the working hours')
    #: The maximum amount of hours the employee can work in a year
    max_legal_yearly_hours: int | None = pydantic.Field(
        default=None,
        description='The maximum amount of hours the employee can work in a year',
    )
    #: The maximum amount of hours the employee can work in a week
    maximum_weekly_hours: int | None = pydantic.Field(
        default=None,
        description='The maximum amount of hours the employee can work in a week',
    )
    #: Defines whether a bank holiday should be considered as a workable or non-workable day
    bank_holiday_treatment: BankHolidayTreatment = pydantic.Field(
        description='Defines whether a bank holiday should be considered as a workable or non-workable day',
    )
    #: Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time hours
    #: they are working)
    working_time_percentage_in_cents: int | None = pydantic.Field(
        default=None,
        description=(
            'Working time percentage in cents (e.g., when an employee is working part-time, '
            'the percentage of full-time hours they are working)'
        ),
    )
    #: Allows companies to define how annual working hours are spread across the year to ensure compliance with legal
    #: limits
    annual_working_time_distribution: AnnualWorkingTimeDistribution | None = pydantic.Field(
        default=None,
        description=(
            'Allows companies to define how annual working hours are spread across the year '
            'to ensure compliance with legal limits'
        ),
    )
    #: The minimum amount of minutes the employee must rest between working periods
    min_rest_minutes_between_days: int | None = pydantic.Field(
        default=None,
        description='The minimum amount of minutes the employee must rest between working periods',
    )
    #: The maximum amount of minutes the employee can work in a day
    max_work_minutes_per_day: int | None = pydantic.Field(
        default=None,
        description='The maximum amount of minutes the employee can work in a day',
    )
    #: The maximum amount of days the employee can work in a row
    max_work_days_in_row: int | None = pydantic.Field(
        default=None,
        description='The maximum amount of days the employee can work in a row',
    )
    #: The minimum amount of hours the employee must rest in a row
    min_rest_hours_in_row: int | None = pydantic.Field(
        default=None,
        description='The minimum amount of hours the employee must rest in a row',
    )
    #: The date the contract version was created
    created_at: datetime.datetime = pydantic.Field(description='The date the contract version was created')
    #: The date of the last contract version updated
    updated_at: datetime.datetime = pydantic.Field(description='The date of the last contract version updated')
    #: Flag that indicates if the contract has teleworking
    es_has_teleworking_contract: bool | None = pydantic.Field(
        default=None,
        description='Flag that indicates if the contract has teleworking',
    )
    #: The group of cotization of the employee
    es_cotization_group: int | None = pydantic.Field(
        default=None,
        description='The group of cotization of the employee',
    )
    #: The group of cotization of the employee
    contracts_es_tariff_group_id: int | None = pydantic.Field(
        default=None,
        description='The group of cotization of the employee',
    )
    #: Observations of the contract
    es_contract_observations: str | None = pydantic.Field(default=None, description='Observations of the contract')
    #: The job description of the employee
    es_job_description: str | None = pydantic.Field(default=None, description='The job description of the employee')
    #: Contract type identifier
    es_contract_type_id: int | None = pydantic.Field(default=None, description='Contract type identifier')
    #: Working day type identifier
    es_working_day_type_id: int | None = pydantic.Field(default=None, description='Working day type identifier')
    #: Education level identifier
    es_education_level_id: int | None = pydantic.Field(default=None, description='Education level identifier')
    #: Professional category identifier
    es_professional_category_id: int | None = pydantic.Field(
        default=None,
        description='Professional category identifier',
    )
    #: Employee type
    fr_employee_type: str | None = pydantic.Field(default=None, description='Employee type')
    #: Flag that indicates if the employee is allowed to work within the framework of a fixed number of days
    fr_forfait_jours: bool = pydantic.Field(
        description=(
            'Flag that indicates if the employee is allowed to work within the framework of a fixed number of days'
        ),
    )
    #: The number of days the employee is allowed to work
    fr_jours_par_an: int | None = pydantic.Field(
        default=None,
        description='The number of days the employee is allowed to work',
    )
    #: Coefficient for france contracts
    fr_coefficient: str | None = pydantic.Field(default=None, description='Coefficient for france contracts')
    #: Contract type identifier
    fr_contract_type_id: int | None = pydantic.Field(default=None, description='Contract type identifier')
    #: Level identifier
    fr_level_id: int | None = pydantic.Field(default=None, description='Level identifier')
    #: Step identifier
    fr_step_id: int | None = pydantic.Field(default=None, description='Step identifier')
    #: Mutual identifier
    fr_mutual_id: int | None = pydantic.Field(default=None, description='Mutual identifier')
    #: Professional category identifier
    fr_professional_category_id: int | None = pydantic.Field(
        default=None,
        description='Professional category identifier',
    )
    #: Work type identifier
    fr_work_type_id: int | None = pydantic.Field(default=None, description='Work type identifier')
    #: Contract type identifier
    de_contract_type_id: int | None = pydantic.Field(default=None, description='Contract type identifier')
    #: Contract type identifier
    pt_contract_type_id: int | None = pydantic.Field(default=None, description='Contract type identifier')
    #: The role id of the employee in the job catalog
    job_catalog_role_id: int | None = pydantic.Field(
        default=None,
        description='The role id of the employee in the job catalog',
    )
    #: The uuid node in the job catalog tree. For now it only supports level nodes. From this point in the job catalog
    #: tree you can get the full ancestor path to the root node including the role. Refer to job_catalog/tree_nodes
    #: endpoint.
    job_catalog_tree_node_uuid: str | None = pydantic.Field(
        default=None,
        description=(
            'The uuid node in the job catalog tree. For now it only supports level nodes. '
            'From this point in the job catalog tree you can get the full ancestor path to the root node including the '
            'role. Refer to job_catalog/tree_nodes endpoint.'
        ),
    )
    #: Whether it is the reference contract today or not. It is important to remark that reference contract does not
    #: mean active
    is_reference: bool | None = pydantic.Field(
        default=None,
        description='Whether it is the reference contract today or not. It is important to remark that '
        'reference contract does not mean active',
    )


class FrenchContractType(pydantic.BaseModel):
    """Model for contracts_french_contract_type."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier for the contract type
    id: int = pydantic.Field(description='Identifier for the contract type')
    #: Contract type name
    name: str = pydantic.Field(description='Contract type name')
    #: Whether to show archived types or not
    archived: bool | None = pydantic.Field(default=None, description='Whether to show archived types or not')


class GermanContractType(pydantic.BaseModel):
    """Model for contracts_german_contract_type."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier for the contract type
    id: int = pydantic.Field(description='Identifier for the contract type')
    #: Contract type name
    name: str = pydantic.Field(description='Contract type name')
    #: Whether to show archived types or not
    archived: bool | None = pydantic.Field(default=None, description='Whether to show archived types or not')


class PortugueseContractType(pydantic.BaseModel):
    """Model for contracts_portuguese_contract_type."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier for the contract type
    id: int = pydantic.Field(description='Identifier for the contract type')
    #: Contract type name
    name: str = pydantic.Field(description='Contract type name')
    #: Whether to show archived types or not
    archived: bool | None = pydantic.Field(default=None, description='Whether to show archived types or not')


class SpanishContractType(pydantic.BaseModel):
    """Model for contracts_spanish_contract_type."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier for the contract type
    id: int = pydantic.Field(description='Identifier for the contract type')
    #: The name of the contract type
    name: str = pydantic.Field(description='The name of the contract type')
    #: This contract type is a predefined one
    default: bool | None = pydantic.Field(default=None, description='This contract type is a predefined one')
    #: The contract template identifier. Refers to contracts/contract_templates
    contracts_contract_template_id: int | None = pydantic.Field(
        default=None,
        description='The contract template identifier. Refers to contracts/contract_templates',
    )


class SpanishEducationLevel(pydantic.BaseModel):
    """Model for contracts_spanish_education_level."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Education level identifier
    id: int = pydantic.Field(description='Education level identifier')
    #: Education level name
    name: str = pydantic.Field(description='Education level name')
    #: Whether the education level is a predefined value
    default: bool | None = pydantic.Field(default=None, description='Whether the education level is a predefined value')
    #: Contract template identifier, refers to contracts/contract_templates
    contracts_contract_template_id: int = pydantic.Field(
        description='Contract template identifier, refers to contracts/contract_templates',
    )


class SpanishProfessionalCategory(pydantic.BaseModel):
    """Model for contracts_spanish_professional_category."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Professional category identifier
    id: int = pydantic.Field(description='Professional category identifier')
    #: Professional category name
    name: str = pydantic.Field(description='Professional category name')
    #: Whether the professional category is a predefined value
    default: bool | None = pydantic.Field(
        default=None,
        description='Whether the professional category is a predefined value',
    )
    #: Contract template identifier, refers to contracts/contract_templates
    contracts_contract_template_id: int = pydantic.Field(
        description='Contract template identifier, refers to contracts/contract_templates',
    )


class SpanishWorkingDayType(pydantic.BaseModel):
    """Model for contracts_spanish_working_day_type."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Working day type identifier
    id: int = pydantic.Field(description='Working day type identifier')
    #: Working day type name
    name: str = pydantic.Field(description='Working day type name')
    #: Whether the Working day type is a predefined value
    default: bool | None = pydantic.Field(
        default=None,
        description='Whether the Working day type is a predefined value',
    )
    #: Contract template identifier, refers to contracts/contract_templates
    contracts_contract_template_id: int | None = pydantic.Field(
        default=None,
        description='Contract template identifier, refers to contracts/contract_templates',
    )


class Taxonomy(pydantic.BaseModel):
    """Model for contracts_taxonomy."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Taxonomy identifier
    id: int = pydantic.Field(description='Taxonomy identifier')
    #: Taxonomy name
    name: str = pydantic.Field(description='Taxonomy name')
    #: Whether the taxonomy is archived
    archived: bool = pydantic.Field(description='Whether the taxonomy is archived')
    #: Whether the taxonomy is a default value
    default: bool = pydantic.Field(description='Whether the taxonomy is a default value')
    #: Legal entity identifier
    legal_entity_id: int = pydantic.Field(description='Legal entity identifier')


class CompensationsEndpoint(Endpoint):
    """Endpoint for contract compensations."""

    endpoint = 'contracts/compensations'

    async def all(self, **kwargs) -> ListApiResponse[Compensation]:
        """Get all compensations.

        Official documentation: `contracts/compensations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-compensations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Compensation]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Compensation, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Compensation]:
        """Get compensations with pagination metadata.

        Official documentation: `contracts/compensations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-compensations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Compensation]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Compensation, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, compensation_id: int | str, **kwargs) -> Compensation:
        """Get a specific compensation by ID.

        Official documentation: `contracts/compensations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-compensations>`_

        :param compensation_id: The unique identifier.
        :type compensation_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Compensation
        """
        data = await self.api.get(self.endpoint, compensation_id, **kwargs)
        return pydantic.TypeAdapter(Compensation).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Compensation:
        """Create a new compensation.

        Official documentation: `contracts/compensations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-compensations>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Compensation
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Compensation).validate_python(response['data'])

    async def update(self, compensation_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Compensation:
        """Update a compensation.

        Official documentation: `contracts/compensations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-compensations>`_

        :param compensation_id: The unique identifier of the record to update.
        :type compensation_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Compensation
        """
        response = await self.api.put(self.endpoint, compensation_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Compensation).validate_python(response['data'])

    async def delete(self, compensation_id: int | str, **kwargs) -> None:
        """Delete a compensation.

        Official documentation: `contracts/compensations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-compensations>`_

        :param compensation_id: The unique identifier of the record to delete.
        :type compensation_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: None.
        :rtype: None
        """
        await self.api.delete(self.endpoint, compensation_id, **kwargs)


class ContractTemplatesEndpoint(Endpoint):
    """Endpoint for contract templates."""

    endpoint = 'contracts/contract_templates'

    async def all(self, **kwargs) -> ListApiResponse[ContractTemplate]:
        """Get all contract templates.

        Official documentation: `contracts/contract_templates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-templates>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ContractTemplate]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ContractTemplate, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ContractTemplate]:
        """Get contract templates with pagination metadata.

        Official documentation: `contracts/contract_templates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-templates>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ContractTemplate]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ContractTemplate, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, template_id: int | str, **kwargs) -> ContractTemplate:
        """Get a specific contract template by ID.

        Official documentation: `contracts/contract_templates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-templates>`_

        :param template_id: The unique identifier.
        :type template_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ContractTemplate
        """
        data = await self.api.get(self.endpoint, template_id, **kwargs)
        return pydantic.TypeAdapter(ContractTemplate).validate_python(data['data'])


class ContractVersionsEndpoint(Endpoint):
    """Endpoint for contract versions."""

    endpoint = 'contracts/contract_versions'

    async def all(self, **kwargs) -> ListApiResponse[ContractVersion]:
        """Get all contract versions.

        Official documentation: `contracts/contract_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-versions>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ContractVersion]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ContractVersion, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ContractVersion]:
        """Get contract versions with pagination metadata.

        Official documentation: `contracts/contract_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-versions>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ContractVersion]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ContractVersion, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, version_id: int | str, **kwargs) -> ContractVersion:
        """Get a specific contract version by ID.

        Official documentation: `contracts/contract_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-versions>`_

        :param version_id: The unique identifier.
        :type version_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ContractVersion
        """
        data = await self.api.get(self.endpoint, version_id, **kwargs)
        return pydantic.TypeAdapter(ContractVersion).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ContractVersion:
        """Create a new contract version.

        Official documentation: `contracts/contract_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-versions>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ContractVersion
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ContractVersion).validate_python(response['data'])

    async def update(self, version_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ContractVersion:
        """Update a contract version.

        Official documentation: `contracts/contract_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-versions>`_

        :param version_id: The unique identifier of the record to update.
        :type version_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: ContractVersion
        """
        response = await self.api.put(self.endpoint, version_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ContractVersion).validate_python(response['data'])

    async def delete(self, version_id: int | str, **kwargs) -> None:
        """Delete a contract version.

        Official documentation: `contracts/contract_versions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-versions>`_

        :param version_id: The unique identifier of the record to delete.
        :type version_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: None.
        :rtype: None
        """
        await self.api.delete(self.endpoint, version_id, **kwargs)


class SpanishContractTypesEndpoint(Endpoint):
    """Endpoint for Spanish contract types."""

    endpoint = 'contracts/spanish_contract_types'

    async def all(self, **kwargs) -> ListApiResponse[SpanishContractType]:
        """Get all Spanish contract types.

        Official documentation: `contracts/spanish_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-contract-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[SpanishContractType]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SpanishContractType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SpanishContractType]:
        """Get Spanish contract types with pagination metadata.

        Official documentation: `contracts/spanish_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-contract-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[SpanishContractType]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=SpanishContractType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> SpanishContractType:
        """Get a specific Spanish contract type by ID.

        Official documentation: `contracts/spanish_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-contract-types>`_

        :param type_id: The unique identifier.
        :type type_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: SpanishContractType
        """
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(SpanishContractType).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> SpanishContractType:
        """Create a new Spanish contract type.

        Official documentation: `contracts/spanish_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-contract-types>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: SpanishContractType
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(SpanishContractType).validate_python(response['data'])


class FrenchContractTypesEndpoint(Endpoint):
    """Endpoint for French contract types."""

    endpoint = 'contracts/french_contract_types'

    async def all(self, **kwargs) -> ListApiResponse[FrenchContractType]:
        """Get all French contract types.

        Official documentation: `contracts/french_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-french-contract-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[FrenchContractType]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=FrenchContractType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[FrenchContractType]:
        """Get French contract types with pagination metadata.

        Official documentation: `contracts/french_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-french-contract-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[FrenchContractType]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=FrenchContractType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> FrenchContractType:
        """Get a specific French contract type by ID.

        Official documentation: `contracts/french_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-french-contract-types>`_

        :param type_id: The unique identifier.
        :type type_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: FrenchContractType
        """
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(FrenchContractType).validate_python(data['data'])


class GermanContractTypesEndpoint(Endpoint):
    """Endpoint for German contract types."""

    endpoint = 'contracts/german_contract_types'

    async def all(self, **kwargs) -> ListApiResponse[GermanContractType]:
        """Get all German contract types.

        Official documentation: `contracts/german_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-german-contract-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[GermanContractType]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=GermanContractType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[GermanContractType]:
        """Get German contract types with pagination metadata.

        Official documentation: `contracts/german_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-german-contract-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[GermanContractType]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=GermanContractType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> GermanContractType:
        """Get a specific German contract type by ID.

        Official documentation: `contracts/german_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-german-contract-types>`_

        :param type_id: The unique identifier.
        :type type_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: GermanContractType
        """
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(GermanContractType).validate_python(data['data'])


class PortugueseContractTypesEndpoint(Endpoint):
    """Endpoint for Portuguese contract types."""

    endpoint = 'contracts/portuguese_contract_types'

    async def all(self, **kwargs) -> ListApiResponse[PortugueseContractType]:
        """Get all Portuguese contract types.

        Official documentation: `contracts/portuguese_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-portuguese-contract-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[PortugueseContractType]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PortugueseContractType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PortugueseContractType]:
        """Get Portuguese contract types with pagination metadata.

        Official documentation: `contracts/portuguese_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-portuguese-contract-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[PortugueseContractType]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PortugueseContractType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> PortugueseContractType:
        """Get a specific Portuguese contract type by ID.

        Official documentation: `contracts/portuguese_contract_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-portuguese-contract-types>`_

        :param type_id: The unique identifier.
        :type type_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: PortugueseContractType
        """
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(PortugueseContractType).validate_python(data['data'])


class ReferenceContractsEndpoint(Endpoint):
    """Endpoint for reference contracts."""

    endpoint = 'contracts/reference_contracts'

    async def all(self, **kwargs) -> ListApiResponse[ContractVersion]:
        """Get all reference contracts.

        Official documentation: `contracts/reference_contracts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-reference-contracts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ContractVersion]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ContractVersion, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ContractVersion]:
        """Get reference contracts with pagination metadata.

        Official documentation: `contracts/reference_contracts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-reference-contracts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ContractVersion]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ContractVersion, raw_meta=response['meta'], raw_data=response['data'])


class SpanishEducationLevelsEndpoint(Endpoint):
    """Endpoint for Spanish education levels."""

    endpoint = 'contracts/spanish_education_levels'

    async def all(self, **kwargs) -> ListApiResponse[SpanishEducationLevel]:
        """Get all Spanish education levels.

        Official documentation: `contracts/spanish_education_levels <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-education-levels>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[SpanishEducationLevel]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SpanishEducationLevel, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SpanishEducationLevel]:
        """Get Spanish education levels with pagination metadata.

        Official documentation: `contracts/spanish_education_levels <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-education-levels>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[SpanishEducationLevel]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=SpanishEducationLevel, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, level_id: int | str, **kwargs) -> SpanishEducationLevel:
        """Get a specific Spanish education level by ID.

        Official documentation: `contracts/spanish_education_levels <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-education-levels>`_

        :param level_id: The unique identifier.
        :type level_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: SpanishEducationLevel
        """
        data = await self.api.get(self.endpoint, level_id, **kwargs)
        return pydantic.TypeAdapter(SpanishEducationLevel).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> SpanishEducationLevel:
        """Create a new Spanish education level.

        Official documentation: `contracts/spanish_education_levels <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-education-levels>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: SpanishEducationLevel
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(SpanishEducationLevel).validate_python(response['data'])


class SpanishProfessionalCategoriesEndpoint(Endpoint):
    """Endpoint for Spanish professional categories."""

    endpoint = 'contracts/spanish_professional_categories'

    async def all(self, **kwargs) -> ListApiResponse[SpanishProfessionalCategory]:
        """Get all Spanish professional categories.

        Official documentation: `contracts/spanish_professional_categories <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-professional-categories>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[SpanishProfessionalCategory]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SpanishProfessionalCategory, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SpanishProfessionalCategory]:
        """Get Spanish professional categories with pagination metadata.

        Official documentation: `contracts/spanish_professional_categories <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-professional-categories>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[SpanishProfessionalCategory]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=SpanishProfessionalCategory,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, category_id: int | str, **kwargs) -> SpanishProfessionalCategory:
        """Get a specific Spanish professional category by ID.

        Official documentation: `contracts/spanish_professional_categories <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-professional-categories>`_

        :param category_id: The unique identifier.
        :type category_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: SpanishProfessionalCategory
        """
        data = await self.api.get(self.endpoint, category_id, **kwargs)
        return pydantic.TypeAdapter(SpanishProfessionalCategory).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> SpanishProfessionalCategory:
        """Create a new Spanish professional category.

        Official documentation: `contracts/spanish_professional_categories <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-professional-categories>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: SpanishProfessionalCategory
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(SpanishProfessionalCategory).validate_python(response['data'])


class SpanishWorkingDayTypesEndpoint(Endpoint):
    """Endpoint for Spanish working day types."""

    endpoint = 'contracts/spanish_working_day_types'

    async def all(self, **kwargs) -> ListApiResponse[SpanishWorkingDayType]:
        """Get all Spanish working day types.

        Official documentation: `contracts/spanish_working_day_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-working-day-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[SpanishWorkingDayType]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SpanishWorkingDayType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SpanishWorkingDayType]:
        """Get Spanish working day types with pagination metadata.

        Official documentation: `contracts/spanish_working_day_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-working-day-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[SpanishWorkingDayType]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=SpanishWorkingDayType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> SpanishWorkingDayType:
        """Get a specific Spanish working day type by ID.

        Official documentation: `contracts/spanish_working_day_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-working-day-types>`_

        :param type_id: The unique identifier.
        :type type_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: SpanishWorkingDayType
        """
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(SpanishWorkingDayType).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> SpanishWorkingDayType:
        """Create a new Spanish working day type.

        Official documentation: `contracts/spanish_working_day_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-spanish-working-day-types>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: SpanishWorkingDayType
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(SpanishWorkingDayType).validate_python(response['data'])


class ContractVersionHistory(pydantic.BaseModel):
    """Model for contracts_contract_version_history."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Contract version history identifier
    id: int = pydantic.Field(description='Contract version history identifier')
    #: Contract version identifier
    contract_version_id: int = pydantic.Field(description='Contract version identifier')
    #: Description of changes made
    changes: str = pydantic.Field(description='Description of changes made')
    #: The uuid node in the job catalog tree. For now it only supports level nodes. From this point in the job catalog
    #: tree you can get the full ancestor path to the root node including the role. Refer to job_catalog/tree_nodes
    #: endpoint.
    job_catalog_tree_node_uuid: str | None = pydantic.Field(
        default=None,
        description=(
            'The uuid node in the job catalog tree. For now it only supports level nodes. '
            'From this point in the job catalog tree you can get the full ancestor path to the root node including the '
            'role. Refer to job_catalog/tree_nodes endpoint.'
        ),
    )
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class ContractVersionMetaDatum(pydantic.BaseModel):
    """Model for contracts_contract_version_meta_datum."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Contract version meta datum identifier
    id: int = pydantic.Field(description='Contract version meta datum identifier')
    #: Contract version identifier
    contract_version_id: int = pydantic.Field(description='Contract version identifier')
    #: Meta data key
    key: str = pydantic.Field(description='Meta data key')
    #: Meta data value
    value: str = pydantic.Field(description='Meta data value')
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class ContractVersionHistoriesEndpoint(Endpoint):
    """Endpoint for contract version histories."""

    endpoint = 'contracts/contract_version_histories'

    async def all(self, **kwargs) -> ListApiResponse[ContractVersionHistory]:
        """Get all contract version histories.

        Official documentation: `contracts/contract_version_histories <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-version-histories>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ContractVersionHistory]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ContractVersionHistory, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ContractVersionHistory]:
        """Get contract version histories with pagination metadata.

        Official documentation: `contracts/contract_version_histories <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-version-histories>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ContractVersionHistory]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ContractVersionHistory, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, history_id: int | str, **kwargs) -> ContractVersionHistory:
        """Get a specific contract version history by ID.

        Official documentation: `contracts/contract_version_histories <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-version-histories>`_

        :param history_id: The unique identifier.
        :type history_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ContractVersionHistory
        """
        data = await self.api.get(self.endpoint, history_id, **kwargs)
        return pydantic.TypeAdapter(ContractVersionHistory).validate_python(data['data'])


class ContractVersionMetaDataEndpoint(Endpoint):
    """Endpoint for contract version meta data."""

    endpoint = 'contracts/contract_version_meta_data'

    async def all(self, **kwargs) -> ListApiResponse[ContractVersionMetaDatum]:
        """Get all contract version meta data.

        Official documentation: `contracts/contract_version_meta_data <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-version-meta-data>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ContractVersionMetaDatum]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ContractVersionMetaDatum, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ContractVersionMetaDatum]:
        """Get contract version meta data with pagination metadata.

        Official documentation: `contracts/contract_version_meta_data <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-version-meta-data>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ContractVersionMetaDatum]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=ContractVersionMetaDatum,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, meta_datum_id: int | str, **kwargs) -> ContractVersionMetaDatum:
        """Get a specific contract version meta datum by ID.

        Official documentation: `contracts/contract_version_meta_data <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-contract-version-meta-data>`_

        :param meta_datum_id: The unique identifier.
        :type meta_datum_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ContractVersionMetaDatum
        """
        data = await self.api.get(self.endpoint, meta_datum_id, **kwargs)
        return pydantic.TypeAdapter(ContractVersionMetaDatum).validate_python(data['data'])


class TaxonomiesEndpoint(Endpoint):
    """Endpoint for contract taxonomies."""

    endpoint = 'contracts/taxonomies'

    async def all(self, **kwargs) -> ListApiResponse[Taxonomy]:
        """Get all taxonomies.

        Official documentation: `contracts/taxonomies <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-taxonomies>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Taxonomy]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Taxonomy, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Taxonomy]:
        """Get taxonomies with pagination metadata.

        Official documentation: `contracts/taxonomies <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-taxonomies>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Taxonomy]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Taxonomy, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, taxonomy_id: int | str, **kwargs) -> Taxonomy:
        """Get a specific taxonomy by ID.

        Official documentation: `contracts/taxonomies <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-contracts-taxonomies>`_

        :param taxonomy_id: The unique identifier.
        :type taxonomy_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Taxonomy
        """
        data = await self.api.get(self.endpoint, taxonomy_id, **kwargs)
        return pydantic.TypeAdapter(Taxonomy).validate_python(data['data'])
