import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class CountryCode(StrEnum):
    """Enum for payroll employee country codes."""

    PORTUGAL = 'pt'
    GERMANY = 'de'
    ITALY = 'it'


class Payrollemployeesidentifier(pydantic.BaseModel):
    """Model for payroll_employees_identifier."""

    id: int = pydantic.Field(description='Payroll employee identifier')
    employee_id: int = pydantic.Field(description='Identifier of the employee')
    social_security_number: str | None = pydantic.Field(
        default=None,
        description='Social security number of the employee',
    )
    tax_id: str | None = pydantic.Field(default=None, description='Tax id of the employee')
    country: CountryCode = pydantic.Field(description='Country code of the employee (pt | it | de)')


class IdentifiersEndpoint(Endpoint):
    """Endpoint for payroll_employees/identifiers operations."""

    endpoint = 'payroll_employees/identifiers'

    async def all(self, **kwargs) -> ListApiResponse[Payrollemployeesidentifier]:
        """Get all payroll employee identifiers records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Payrollemployeesidentifier, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Payrollemployeesidentifier]:
        """Get payroll employee identifiers with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=Payrollemployeesidentifier,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, identifier_id: int | str, **kwargs) -> Payrollemployeesidentifier:
        """Get a specific payroll employee identifier by ID."""
        data = await self.api.get(self.endpoint, identifier_id, **kwargs)
        return pydantic.TypeAdapter(Payrollemployeesidentifier).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Payrollemployeesidentifier:
        """Create a new payroll employee identifier."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Payrollemployeesidentifier).validate_python(response)

    async def update(
        self,
        identifier_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> Payrollemployeesidentifier:
        """Update a payroll employee identifier."""
        response = await self.api.put(self.endpoint, identifier_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Payrollemployeesidentifier).validate_python(response)

    async def delete(self, identifier_id: int | str, **kwargs) -> Payrollemployeesidentifier:
        """Delete a payroll employee identifier."""
        response = await self.api.delete(self.endpoint, identifier_id, **kwargs)
        return pydantic.TypeAdapter(Payrollemployeesidentifier).validate_python(response)
