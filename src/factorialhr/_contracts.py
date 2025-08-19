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

    id: int = pydantic.Field(description='Compensation ID')
    contract_version_id: int = pydantic.Field(description='Contract version ID')
    contracts_taxonomy_id: int = pydantic.Field(description='Contracts taxonomy ID')
    description: str | None = pydantic.Field(default=None, description='Compensation description')
    compensation_type: str | None = pydantic.Field(
        default=None,
        description=(
            'Required field. You can only use the following options: '
            'fixed, undefined, up_to, per_worked_day, per_worked_hour'
        ),
    )
    amount: int | None = pydantic.Field(
        default=None,
        description='Required field unless your compensation type is undefined',
    )
    unit: str = pydantic.Field(description='Unit of the compensation')
    sync_with_supplements: bool | None = pydantic.Field(default=None, description='Sync with supplements')
    payroll_policy_id: int | None = pydantic.Field(default=None, description='Payroll policy ID')
    recurrence_count: int | None = pydantic.Field(default=None, description='Recurrence count')
    starts_on: datetime.date | None = pydantic.Field(default=None, description='When the compensation starts_on')
    recurrence: str | None = pydantic.Field(default=None, description='Compensation recurrence')
    first_payment_on: datetime.date | None = pydantic.Field(default=None, description='When the first payment is done')
    calculation: str | None = pydantic.Field(default=None, description='Compensation calculation')
    currency: str | None = pydantic.Field(default=None, description='Currency of the compensation')
    time_condition: TimeCondition | None = pydantic.Field(
        default=None,
        description='Time condition for the compensation',
    )
    minimum_amount_of_hours: int | None = pydantic.Field(default=None, description='Minimum amount of hours')
    minimum_amount_of_hours_in_cents: int | None = pydantic.Field(
        default=None,
        description='Compensation expected minimum amount of hours in cents',
    )


class ContractTemplate(pydantic.BaseModel):
    """Model for contracts_contract_template."""

    id: int = pydantic.Field(description='Unique identifier for the contract template')
    company_id: int | None = pydantic.Field(default=None, description='ID of the company this template belongs to')
    contract_version_type: str | None = pydantic.Field(
        default=None,
        description='Type of contract version (e.g., es for Spain, fr for France)',
    )


class ContractVersion(pydantic.BaseModel):
    """Model for contracts_contract_version."""

    id: int | None = pydantic.Field(default=None, description='Identifier for the contract version')
    company_id: int = pydantic.Field(description='Identifier for company')
    employee_id: int = pydantic.Field(description='Employee identifier, refers to /employees/employees endpoint')
    effective_on: datetime.date = pydantic.Field(
        description='The day the specific contract starts, in case of hiring the same than starts_on',
    )
    country: str | None = pydantic.Field(
        default=None,
        description='Nationality country code of the employee (Spain ES, United Kingdom GB)',
    )
    job_title: str | None = pydantic.Field(default=None, description='Job title of the employee')
    job_catalog_level_id: int | None = pydantic.Field(
        default=None,
        description='Job catalog level identifier, refers to /job_catalog/levels endpoint',
    )
    starts_on: datetime.date | None = pydantic.Field(default=None, description='The day the employee is hired')
    ends_on: datetime.date | None = pydantic.Field(default=None, description='The day the employee is terminated')
    has_payroll: bool = pydantic.Field(
        description='Boolean that indicates if the employee associated to this contract belongs to a payroll policy',
    )
    has_trial_period: bool | None = pydantic.Field(
        default=None,
        description='A flag that indicates if the employee has a trial period',
    )
    trial_period_ends_on: datetime.date | None = pydantic.Field(default=None, description='When the trial period ends')
    salary_amount: int | None = pydantic.Field(default=None, description='The amount of money the employee earns')
    salary_frequency: str | None = pydantic.Field(default=None, description='The frequency of the salary payment')
    working_week_days: str | None = pydantic.Field(default=None, description='The days of the week the employee works')
    working_hours: int | None = pydantic.Field(default=None, description='The amount of hours the employee works')
    working_hours_frequency: str | None = pydantic.Field(default=None, description='The frequency of the working hours')
    max_legal_yearly_hours: int | None = pydantic.Field(
        default=None,
        description='The maximum amount of hours the employee can work in a year',
    )
    maximum_weekly_hours: int | None = pydantic.Field(
        default=None,
        description='The maximum amount of hours the employee can work in a week',
    )
    bank_holiday_treatment: BankHolidayTreatment = pydantic.Field(
        description='Defines whether a bank holiday should be considered as a workable or non-workable day',
    )
    working_time_percentage_in_cents: int | None = pydantic.Field(
        default=None,
        description=(
            'Working time percentage in cents (e.g., when an employee is working part-time, '
            'the percentage of full-time hours they are working)'
        ),
    )
    annual_working_time_distribution: AnnualWorkingTimeDistribution | None = pydantic.Field(
        default=None,
        description=(
            'Allows companies to define how annual working hours are spread across the year '
            'to ensure compliance with legal limits'
        ),
    )
    min_rest_minutes_between_days: int | None = pydantic.Field(
        default=None,
        description='The minimum amount of minutes the employee must rest between working periods',
    )
    max_work_minutes_per_day: int | None = pydantic.Field(
        default=None,
        description='The maximum amount of minutes the employee can work in a day',
    )
    max_work_days_in_row: int | None = pydantic.Field(
        default=None,
        description='The maximum amount of days the employee can work in a row',
    )
    min_rest_hours_in_row: int | None = pydantic.Field(
        default=None,
        description='The minimum amount of hours the employee must rest in a row',
    )
    created_at: datetime.datetime = pydantic.Field(description='The date the contract version was created')
    updated_at: datetime.datetime = pydantic.Field(description='The date of the last contract version updated')
    es_has_teleworking_contract: bool | None = pydantic.Field(
        default=None,
        description='Flag that indicates if the contract has teleworking',
    )
    es_cotization_group: int | None = pydantic.Field(
        default=None,
        description='The group of cotization of the employee',
    )
    contracts_es_tariff_group_id: int | None = pydantic.Field(
        default=None,
        description='The group of cotization of the employee',
    )
    es_contract_observations: str | None = pydantic.Field(default=None, description='Observations of the contract')
    es_job_description: str | None = pydantic.Field(default=None, description='The job description of the employee')
    es_contract_type_id: int | None = pydantic.Field(default=None, description='Contract type identifier')
    es_working_day_type_id: int | None = pydantic.Field(default=None, description='Working day type identifier')
    es_education_level_id: int | None = pydantic.Field(default=None, description='Education level identifier')
    es_professional_category_id: int | None = pydantic.Field(
        default=None,
        description='Professional category identifier',
    )
    fr_employee_type: str | None = pydantic.Field(default=None, description='Employee type')
    fr_forfait_jours: bool = pydantic.Field(
        description=(
            'Flag that indicates if the employee is allowed to work within the framework of a fixed number of days'
        ),
    )
    fr_jours_par_an: int | None = pydantic.Field(
        default=None,
        description='The number of days the employee is allowed to work',
    )
    fr_coefficient: str | None = pydantic.Field(default=None, description='Coefficient for france contracts')
    fr_contract_type_id: int | None = pydantic.Field(default=None, description='Contract type identifier')
    fr_level_id: int | None = pydantic.Field(default=None, description='Level identifier')
    fr_step_id: int | None = pydantic.Field(default=None, description='Step identifier')
    fr_mutual_id: int | None = pydantic.Field(default=None, description='Mutual identifier')
    fr_professional_category_id: int | None = pydantic.Field(
        default=None,
        description='Professional category identifier',
    )
    fr_work_type_id: int | None = pydantic.Field(default=None, description='Work type identifier')
    de_contract_type_id: int | None = pydantic.Field(default=None, description='Contract type identifier')
    pt_contract_type_id: int | None = pydantic.Field(default=None, description='Contract type identifier')


class FrenchContractType(pydantic.BaseModel):
    """Model for contracts_french_contract_type."""

    id: int = pydantic.Field(description='Identifier for the contract type')
    name: str = pydantic.Field(description='Contract type name')


class GermanContractType(pydantic.BaseModel):
    """Model for contracts_german_contract_type."""

    id: int = pydantic.Field(description='Identifier for the contract type')
    name: str = pydantic.Field(description='Contract type name')


class PortugueseContractType(pydantic.BaseModel):
    """Model for contracts_portuguese_contract_type."""

    id: int = pydantic.Field(description='Identifier for the contract type')
    name: str = pydantic.Field(description='Contract type name')


class SpanishContractType(pydantic.BaseModel):
    """Model for contracts_spanish_contract_type."""

    id: int = pydantic.Field(description='Identifier for the contract type')
    name: str = pydantic.Field(description='The name of the contract type')
    default: bool | None = pydantic.Field(default=None, description='This contract type is a predefined one')
    contracts_contract_template_id: int | None = pydantic.Field(
        default=None,
        description='The contract template identifier. Refers to contracts/contract_templates',
    )


class SpanishEducationLevel(pydantic.BaseModel):
    """Model for contracts_spanish_education_level."""

    id: int = pydantic.Field(description='Education level identifier')
    name: str = pydantic.Field(description='Education level name')
    default: bool | None = pydantic.Field(default=None, description='Whether the education level is a predefined value')
    contracts_contract_template_id: int = pydantic.Field(
        description='Contract template identifier, refers to contracts/contract_templates',
    )


class SpanishProfessionalCategory(pydantic.BaseModel):
    """Model for contracts_spanish_professional_category."""

    id: int = pydantic.Field(description='Professional category identifier')
    name: str = pydantic.Field(description='Professional category name')
    default: bool | None = pydantic.Field(
        default=None,
        description='Whether the professional category is a predefined value',
    )
    contracts_contract_template_id: int = pydantic.Field(
        description='Contract template identifier, refers to contracts/contract_templates',
    )


class SpanishWorkingDayType(pydantic.BaseModel):
    """Model for contracts_spanish_working_day_type."""

    id: int = pydantic.Field(description='Working day type identifier')
    name: str = pydantic.Field(description='Working day type name')
    default: bool | None = pydantic.Field(
        default=None,
        description='Whether the Working day type is a predefined value',
    )
    contracts_contract_template_id: int | None = pydantic.Field(
        default=None,
        description='Contract template identifier, refers to contracts/contract_templates',
    )


class Taxonomy(pydantic.BaseModel):
    """Model for contracts_taxonomy."""

    id: int = pydantic.Field(description='Taxonomy identifier')
    name: str = pydantic.Field(description='Taxonomy name')
    archived: bool = pydantic.Field(description='Whether the taxonomy is archived')
    default: bool = pydantic.Field(description='Whether the taxonomy is a default value')
    legal_entity_id: int = pydantic.Field(description='Legal entity identifier')


class CompensationsEndpoint(Endpoint):
    """Endpoint for contract compensations."""

    endpoint = '/contracts/compensations'

    async def all(self, **kwargs) -> ListApiResponse[Compensation]:
        """Get all compensations."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Compensation, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Compensation]:
        """Get compensations with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Compensation, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, compensation_id: int | str, **kwargs) -> Compensation:
        """Get a specific compensation by ID."""
        data = await self.api.get(self.endpoint, compensation_id, **kwargs)
        return pydantic.TypeAdapter(Compensation).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Compensation:
        """Create a new compensation."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Compensation).validate_python(response['data'])

    async def update(self, compensation_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Compensation:
        """Update a compensation."""
        response = await self.api.put(self.endpoint, compensation_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Compensation).validate_python(response['data'])

    async def delete(self, compensation_id: int | str, **kwargs) -> None:
        """Delete a compensation."""
        await self.api.delete(self.endpoint, compensation_id, **kwargs)


class ContractTemplatesEndpoint(Endpoint):
    """Endpoint for contract templates."""

    endpoint = '/contracts/contract_templates'

    async def all(self, **kwargs) -> ListApiResponse[ContractTemplate]:
        """Get all contract templates."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ContractTemplate, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ContractTemplate]:
        """Get contract templates with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ContractTemplate, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, template_id: int | str, **kwargs) -> ContractTemplate:
        """Get a specific contract template by ID."""
        data = await self.api.get(self.endpoint, template_id, **kwargs)
        return pydantic.TypeAdapter(ContractTemplate).validate_python(data['data'])


class ContractVersionsEndpoint(Endpoint):
    """Endpoint for contract versions."""

    endpoint = '/contracts/contract_versions'

    async def all(self, **kwargs) -> ListApiResponse[ContractVersion]:
        """Get all contract versions."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ContractVersion, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ContractVersion]:
        """Get contract versions with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ContractVersion, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, version_id: int | str, **kwargs) -> ContractVersion:
        """Get a specific contract version by ID."""
        data = await self.api.get(self.endpoint, version_id, **kwargs)
        return pydantic.TypeAdapter(ContractVersion).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ContractVersion:
        """Create a new contract version."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ContractVersion).validate_python(response['data'])

    async def update(self, version_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ContractVersion:
        """Update a contract version."""
        response = await self.api.put(self.endpoint, version_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ContractVersion).validate_python(response['data'])

    async def delete(self, version_id: int | str, **kwargs) -> None:
        """Delete a contract version."""
        await self.api.delete(self.endpoint, version_id, **kwargs)


class SpanishContractTypesEndpoint(Endpoint):
    """Endpoint for Spanish contract types."""

    endpoint = '/contracts/spanish_contract_types'

    async def all(self, **kwargs) -> ListApiResponse[SpanishContractType]:
        """Get all Spanish contract types."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SpanishContractType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SpanishContractType]:
        """Get Spanish contract types with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=SpanishContractType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> SpanishContractType:
        """Get a specific Spanish contract type by ID."""
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(SpanishContractType).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> SpanishContractType:
        """Create a new Spanish contract type."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(SpanishContractType).validate_python(response['data'])


class FrenchContractTypesEndpoint(Endpoint):
    """Endpoint for French contract types."""

    endpoint = '/contracts/french_contract_types'

    async def all(self, **kwargs) -> ListApiResponse[FrenchContractType]:
        """Get all French contract types."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=FrenchContractType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[FrenchContractType]:
        """Get French contract types with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=FrenchContractType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> FrenchContractType:
        """Get a specific French contract type by ID."""
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(FrenchContractType).validate_python(data['data'])


class GermanContractTypesEndpoint(Endpoint):
    """Endpoint for German contract types."""

    endpoint = '/contracts/german_contract_types'

    async def all(self, **kwargs) -> ListApiResponse[GermanContractType]:
        """Get all German contract types."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=GermanContractType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[GermanContractType]:
        """Get German contract types with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=GermanContractType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> GermanContractType:
        """Get a specific German contract type by ID."""
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(GermanContractType).validate_python(data['data'])


class PortugueseContractTypesEndpoint(Endpoint):
    """Endpoint for Portuguese contract types."""

    endpoint = '/contracts/portuguese_contract_types'

    async def all(self, **kwargs) -> ListApiResponse[PortugueseContractType]:
        """Get all Portuguese contract types."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PortugueseContractType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PortugueseContractType]:
        """Get Portuguese contract types with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PortugueseContractType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> PortugueseContractType:
        """Get a specific Portuguese contract type by ID."""
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(PortugueseContractType).validate_python(data['data'])


class ReferenceContractsEndpoint(Endpoint):
    """Endpoint for reference contracts."""

    endpoint = '/contracts/reference_contracts'

    async def all(self, **kwargs) -> ListApiResponse[ContractVersion]:
        """Get all reference contracts."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ContractVersion, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ContractVersion]:
        """Get reference contracts with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ContractVersion, raw_meta=response['meta'], raw_data=response['data'])


class SpanishEducationLevelsEndpoint(Endpoint):
    """Endpoint for Spanish education levels."""

    endpoint = '/contracts/spanish_education_levels'

    async def all(self, **kwargs) -> ListApiResponse[SpanishEducationLevel]:
        """Get all Spanish education levels."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SpanishEducationLevel, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SpanishEducationLevel]:
        """Get Spanish education levels with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=SpanishEducationLevel, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, level_id: int | str, **kwargs) -> SpanishEducationLevel:
        """Get a specific Spanish education level by ID."""
        data = await self.api.get(self.endpoint, level_id, **kwargs)
        return pydantic.TypeAdapter(SpanishEducationLevel).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> SpanishEducationLevel:
        """Create a new Spanish education level."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(SpanishEducationLevel).validate_python(response['data'])


class SpanishProfessionalCategoriesEndpoint(Endpoint):
    """Endpoint for Spanish professional categories."""

    endpoint = '/contracts/spanish_professional_categories'

    async def all(self, **kwargs) -> ListApiResponse[SpanishProfessionalCategory]:
        """Get all Spanish professional categories."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SpanishProfessionalCategory, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SpanishProfessionalCategory]:
        """Get Spanish professional categories with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=SpanishProfessionalCategory,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, category_id: int | str, **kwargs) -> SpanishProfessionalCategory:
        """Get a specific Spanish professional category by ID."""
        data = await self.api.get(self.endpoint, category_id, **kwargs)
        return pydantic.TypeAdapter(SpanishProfessionalCategory).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> SpanishProfessionalCategory:
        """Create a new Spanish professional category."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(SpanishProfessionalCategory).validate_python(response['data'])


class SpanishWorkingDayTypesEndpoint(Endpoint):
    """Endpoint for Spanish working day types."""

    endpoint = '/contracts/spanish_working_day_types'

    async def all(self, **kwargs) -> ListApiResponse[SpanishWorkingDayType]:
        """Get all Spanish working day types."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SpanishWorkingDayType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SpanishWorkingDayType]:
        """Get Spanish working day types with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=SpanishWorkingDayType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> SpanishWorkingDayType:
        """Get a specific Spanish working day type by ID."""
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(SpanishWorkingDayType).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> SpanishWorkingDayType:
        """Create a new Spanish working day type."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(SpanishWorkingDayType).validate_python(response['data'])


class TaxonomiesEndpoint(Endpoint):
    """Endpoint for contract taxonomies."""

    endpoint = '/contracts/taxonomies'

    async def all(self, **kwargs) -> ListApiResponse[Taxonomy]:
        """Get all taxonomies."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Taxonomy, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Taxonomy]:
        """Get taxonomies with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Taxonomy, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, taxonomy_id: int | str, **kwargs) -> Taxonomy:
        """Get a specific taxonomy by ID."""
        data = await self.api.get(self.endpoint, taxonomy_id, **kwargs)
        return pydantic.TypeAdapter(Taxonomy).validate_python(data['data'])
