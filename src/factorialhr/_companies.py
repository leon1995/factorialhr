import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class LegalEntity(pydantic.BaseModel):
    """Model for companies_legal_entity."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the legal entity
    id: int = pydantic.Field(description='Identifier of the legal entity')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Country code of the legal entity
    country: str = pydantic.Field(description='Country code of the legal entity')
    #: Legal name of the legal entity
    legal_name: str = pydantic.Field(description='Legal name of the legal entity')
    #: The currency code in ISO 4217 format
    currency: str = pydantic.Field(description='The currency code in ISO 4217 format')
    #: Tax identification number
    tin: str | None = pydantic.Field(default=None, description='Tax identification number')
    #: City of the legal entity
    city: str | None = pydantic.Field(default=None, description='City of the legal entity')
    #: State of the legal entity
    state: str | None = pydantic.Field(default=None, description='State of the legal entity')
    #: Postal code of the legal entity
    postal_code: str | None = pydantic.Field(default=None, description='Postal code of the legal entity')
    #: Address line 1 of the legal entity
    address_line_1: str | None = pydantic.Field(default=None, description='Address line 1 of the legal entity')
    #: Address line 2 of the legal entity
    address_line_2: str | None = pydantic.Field(default=None, description='Address line 2 of the legal entity')


class LegalEntitiesEndpoint(Endpoint):
    """Endpoint for legal entities."""

    endpoint = 'companies/legal_entities'

    async def all(self, **kwargs) -> ListApiResponse[LegalEntity]:
        """Get all companies records.

        Official documentation: `companies/legal_entities <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-companies-legal-entities>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[LegalEntity]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=LegalEntity, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[LegalEntity]:
        """Get companies with pagination metadata.

        Official documentation: `companies/legal_entities <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-companies-legal-entities>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[LegalEntity]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=LegalEntity, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, legal_entity_id: int | str, **kwargs) -> LegalEntity:
        """Get a specific companies by ID.

        Official documentation: `companies/legal_entities <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-companies-legal-entities-id>`_

        :param legal_entity_id: The unique identifier.
        :type legal_entity_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: LegalEntity
        """
        data = await self.api.get(self.endpoint, legal_entity_id, **kwargs)
        return pydantic.TypeAdapter(LegalEntity).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> LegalEntity:
        """Create a new companies.

        Official documentation: `companies/legal_entities <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-companies-legal-entities>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: LegalEntity
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(LegalEntity).validate_python(response['data'])
