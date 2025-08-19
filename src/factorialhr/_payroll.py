import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class CivilStatus(StrEnum):
    """Enum for civil status."""

    SINGLE = 'single'
    COHABITATING = 'cohabitating'
    DIVORCED = 'divorced'
    MARRIED = 'married'
    UNKNOWN = 'unknown'
    CIVIL_PARTNERSHIP = 'civil_partnership'
    SEPARATED = 'separated'
    WIDOW = 'widow'
    NOT_APPLICABLE = 'not_applicable'


class Unit(StrEnum):
    """Enum for supplement unit types."""

    MONEY = 'money'
    UNITS = 'units'
    TIME = 'time'


class CountryCode(StrEnum):
    """Enum for payroll employee country codes."""

    PORTUGAL = 'pt'
    GERMANY = 'de'
    ITALY = 'it'


class Integration(StrEnum):
    """Enum for payroll integration types."""

    A3INNUVA = 'a3innuva'
    A3NOM = 'a3nom'
    PAIERH = 'paierh'
    YEAP_PAIERH = 'yeap_paierh'
    SILAE = 'silae'
    SILAE_API = 'silae_api'
    DATEV = 'datev'
    DATEV_API = 'datev_api'
    DATEV_LUG_API = 'datev_lug_api'
    DATEV_LAUDS = 'datev_lauds'
    ZUCCHETTI = 'zucchetti'
    GISPAGHE = 'gispaghe'


class FamilySituation(pydantic.BaseModel):
    """Model for payroll_family_situation."""

    id: int = pydantic.Field(description='ID of the family situation')
    employee_id: int = pydantic.Field(description='Employee id of the family situation')
    civil_status: CivilStatus | None = pydantic.Field(default=None, description='Civil status of the employee')
    number_of_dependants: int | None = pydantic.Field(default=None, description='Number of dependants of the employee')


class PolicyPeriod(pydantic.BaseModel):
    """Model for payroll_policy_period."""

    id: int = pydantic.Field(description='Policy period id')
    name: str | None = pydantic.Field(default=None, description='Policy name with start and end date')
    starts_on: datetime.date = pydantic.Field(description='The start date of the policy period')
    policy_id: int = pydantic.Field(description='The id of the policy associated with the policy period')
    company_id: int = pydantic.Field(description='The id of the company')
    ends_on: datetime.date = pydantic.Field(description='The end date of the policy period')
    period: str = pydantic.Field(description='Period for the policy')
    status: str | None = pydantic.Field(default=None, description='Policy period status')
    policy_name: str | None = pydantic.Field(default=None, description='Policy name')
    calculation_started_at: datetime.date | None = pydantic.Field(
        default=None,
        description='The date and time the calculation started',
    )


class Supplement(pydantic.BaseModel):
    """Model for payroll_supplement."""

    id: int = pydantic.Field(description='The identifier of the supplement')
    employee_id: int = pydantic.Field(description='The identifier of the employee associated with the supplement')
    company_id: int = pydantic.Field(description='The identifier of the company associated with the supplement')
    contracts_compensation_id: int | None = pydantic.Field(
        default=None,
        description='The contract compensation identifier associated with the supplement',
    )
    contracts_taxonomy_id: int | None = pydantic.Field(
        default=None,
        description='The taxonomy identifier associated with the supplement',
    )
    amount_in_cents: int | None = pydantic.Field(default=None, description='The amount of the supplement in cents')
    unit: Unit = pydantic.Field(description='The unit of the supplement')
    effective_on: str | None = pydantic.Field(
        default=None,
        description='The date on which the supplement becomes effective',
    )
    created_at: bool | None = pydantic.Field(
        default=None,
        description='The created at date when the supplement was created',
    )
    updated_at: bool | None = pydantic.Field(
        default=None,
        description='The last updated at date when the supplement was last updated',
    )
    description: str | None = pydantic.Field(default=None, description='The description of the supplement')
    payroll_policy_period_id: int | None = pydantic.Field(
        default=None,
        description='The payroll policy period identifier associated with the supplement',
    )
    employee_observations: Sequence[str] | None = pydantic.Field(
        default=None,
        description='Observations on the employee made by the admin or manager',
    )
    raw_minutes_in_cents: int | None = pydantic.Field(
        default=None,
        description='The raw value of minutes in cents associated with the supplement',
    )
    minutes_in_cents: int | None = pydantic.Field(
        default=None,
        description='The value of minutes in cents after adjustments',
    )
    equivalent_minutes_in_cents: int | None = pydantic.Field(
        default=None,
        description='The equivalent value of minutes in cents for payroll processing',
    )
    currency: str | None = pydantic.Field(
        default=None,
        description='The currency used for the supplement, typically in ISO 4217 format',
    )
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='The legal entity identifier associated with the supplement',
    )


class EmployeesIdentifier(pydantic.BaseModel):
    """Model for payroll_employees_identifier."""

    id: int = pydantic.Field(description='Payroll employee identifier')
    employee_id: int = pydantic.Field(description='Identifier of the employee')
    social_security_number: str | None = pydantic.Field(
        default=None,
        description='Social security number of the employee',
    )
    tax_id: str | None = pydantic.Field(default=None, description='Tax id of the employee')
    country: CountryCode = pydantic.Field(description='Country code of the employee (pt | it | de)')


class IntegrationsBaseCode(pydantic.BaseModel):
    """Model for payroll_integrations_base_code."""

    id: int = pydantic.Field(description='Code identifier')
    company_id: int = pydantic.Field(description='Company ID where the code belongs to')
    code: str = pydantic.Field(description='Code value')
    codeable_id: int = pydantic.Field(description='Related object ID. Used together with codeable_type')
    codeable_type: str = pydantic.Field(
        description=(
            'Related object type. Used together with codeable_id '
            '(Employee | Company | LegalEntity | Location | TimeoffLeaveType)'
        ),
    )
    integration: Integration = pydantic.Field(description='Integration name')


class FamilySituationsEndpoint(Endpoint):
    """Endpoint for payroll/family_situations operations."""

    endpoint = 'payroll/family_situations'

    async def all(self, **kwargs) -> ListApiResponse[FamilySituation]:
        """Get all family situations records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=FamilySituation, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[FamilySituation]:
        """Get family situations with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=FamilySituation, raw_meta=response['meta'], raw_data=response['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> FamilySituation:
        """Create a new family situation."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(FamilySituation).validate_python(response)

    async def update(self, family_situation_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> FamilySituation:
        """Update a family situation."""
        response = await self.api.put(self.endpoint, family_situation_id, json=data, **kwargs)
        return pydantic.TypeAdapter(FamilySituation).validate_python(response)


class PolicyPeriodsEndpoint(Endpoint):
    """Endpoint for payroll/policy_periods operations."""

    endpoint = 'payroll/policy_periods'

    async def change_status(self, data: Mapping[str, typing.Any], **kwargs) -> PolicyPeriod:
        """Change status of a policy period."""
        response = await self.api.post(self.endpoint, 'change_status', json=data, **kwargs)
        return pydantic.TypeAdapter(PolicyPeriod).validate_python(response)


class SupplementsEndpoint(Endpoint):
    """Endpoint for payroll/supplements operations."""

    endpoint = 'payroll/supplements'

    async def all(self, **kwargs) -> ListApiResponse[Supplement]:
        """Get all supplements records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Supplement, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Supplement]:
        """Get supplements with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Supplement, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, supplement_id: int | str, **kwargs) -> Supplement:
        """Get a specific supplement by ID."""
        data = await self.api.get(self.endpoint, supplement_id, **kwargs)
        return pydantic.TypeAdapter(Supplement).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Supplement:
        """Create a new supplement."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Supplement).validate_python(response)

    async def update(self, supplement_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Supplement:
        """Update a supplement."""
        response = await self.api.put(self.endpoint, supplement_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Supplement).validate_python(response)

    async def delete(self, supplement_id: int | str, **kwargs) -> Supplement:
        """Delete a supplement."""
        response = await self.api.delete(self.endpoint, supplement_id, **kwargs)
        return pydantic.TypeAdapter(Supplement).validate_python(response)
