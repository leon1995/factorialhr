import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class LegalEntity(pydantic.BaseModel):
    """Model for companies_legal_entity."""

    id: int = pydantic.Field(description='Identifier of the legal entity')
    company_id: int = pydantic.Field(description='Company identifier')
    country: str = pydantic.Field(description='Country code of the legal entity')
    legal_name: str = pydantic.Field(description='Legal name of the legal entity')
    currency: str = pydantic.Field(description='The currency code in ISO 4217 format')
    tin: str | None = pydantic.Field(default=None, description='Tax identification number')
    city: str | None = pydantic.Field(default=None, description='City of the legal entity')
    state: str | None = pydantic.Field(default=None, description='State of the legal entity')
    postal_code: str | None = pydantic.Field(default=None, description='Postal code of the legal entity')
    address_line_1: str | None = pydantic.Field(default=None, description='Address line 1 of the legal entity')
    address_line_2: str | None = pydantic.Field(default=None, description='Address line 2 of the legal entity')


class LegalEntitiesEndpoint(Endpoint):
    """Endpoint for legal entities."""

    endpoint = '/companies/legal_entities'

    async def all(self, **kwargs) -> ListApiResponse[LegalEntity]:
        """Get all companies records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=LegalEntity, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[LegalEntity]:
        """Get companies with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=LegalEntity, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, legal_entity_id: int | str, **kwargs) -> LegalEntity:
        """Get a specific companies by ID."""
        data = await self.api.get(self.endpoint, legal_entity_id, **kwargs)
        return pydantic.TypeAdapter(LegalEntity).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> LegalEntity:
        """Create a new companies."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(LegalEntity).validate_python(response['data'])
