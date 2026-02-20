import datetime
import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Schema(pydantic.BaseModel):
    """Model for custom_resources_schema."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Schema identifier
    id: int = pydantic.Field(description='Schema identifier')
    #: Schema name
    name: str = pydantic.Field(description='Schema name')
    #: Company identifier where this schema belongs
    company_id: int = pydantic.Field(description='Company identifier where this schema belongs')
    #: Manages visibility of the schema
    hidden: bool = pydantic.Field(description='Manages visibility of the schema')
    #: Schema position within employee profile
    position: int | None = pydantic.Field(default=None, description='Schema position within employee profile')


class Resource(pydantic.BaseModel):
    """Model for custom_resources_resource."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Resource identifier
    id: int = pydantic.Field(description='Resource identifier')
    #: Resource name
    name: str = pydantic.Field(description='Resource name')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class CustomResourcesValue(pydantic.BaseModel):
    """Model for custom_resources_value."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Value identifier
    id: int = pydantic.Field(description='Value identifier')
    #: The identifier of the resource that owns the resource value
    resource_id: int = pydantic.Field(
        description='The identifier of the resource that owns the resource value',
    )
    #: The id of the attached resource like an employee
    attachable_id: int | None = pydantic.Field(
        default=None,
        description='The id of the attached resource like an employee',
    )


class CustomResourcesSchemasEndpoint(Endpoint):
    """Endpoint for custom_resources/schemas operations."""

    endpoint = 'custom_resources/schemas'

    async def all(self, **kwargs) -> ListApiResponse[Schema]:
        """Get all schemas records.

        Official documentation: `custom_resources/schemas <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-schemas>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Schema]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Schema)

    async def get(self, **kwargs) -> MetaApiResponse[Schema]:
        """Get schemas with pagination metadata.

        Official documentation: `custom_resources/schemas <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-schemas>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Schema]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Schema)

    async def get_by_id(self, schema_id: int | str, **kwargs) -> Schema:
        """Get a specific schema by ID.

        Official documentation: `custom_resources/schemas <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-schemas>`_

        :param schema_id: The unique identifier.
        :type schema_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Schema
        """
        data = await self.api.get(self.endpoint, schema_id, **kwargs)
        return pydantic.TypeAdapter(Schema).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Schema:
        """Create a new schema.

        Official documentation: `custom_resources/schemas <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-schemas>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Schema
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Schema).validate_python(response)


class ResourcesEndpoint(Endpoint):
    """Endpoint for custom_resources/resources operations."""

    endpoint = 'custom_resources/resources'

    async def all(self, **kwargs) -> ListApiResponse[Resource]:
        """Get all resources records.

        Official documentation: `custom_resources/resources <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-resources>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Resource]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Resource)

    async def get(self, **kwargs) -> MetaApiResponse[Resource]:
        """Get resources with pagination metadata.

        Official documentation: `custom_resources/resources <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-resources>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Resource]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Resource)

    async def get_by_id(self, resource_id: int | str, **kwargs) -> Resource:
        """Get a specific resource by ID.

        Official documentation: `custom_resources/resources <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-resources>`_

        :param resource_id: The unique identifier.
        :type resource_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Resource
        """
        data = await self.api.get(self.endpoint, resource_id, **kwargs)
        return pydantic.TypeAdapter(Resource).validate_python(data)


class CustomResourcesValuesEndpoint(Endpoint):
    """Endpoint for custom_resources/values operations."""

    endpoint = 'custom_resources/values'

    async def all(self, **kwargs) -> ListApiResponse[CustomResourcesValue]:
        """Get all values records.

        Official documentation: `custom_resources/values <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-values>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[CustomResourcesValue]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=CustomResourcesValue)

    async def get(self, **kwargs) -> MetaApiResponse[CustomResourcesValue]:
        """Get values with pagination metadata.

        Official documentation: `custom_resources/values <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-values>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[CustomResourcesValue]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=CustomResourcesValue)

    async def get_by_id(self, value_id: int | str, **kwargs) -> CustomResourcesValue:
        """Get a specific value by ID.

        Official documentation: `custom_resources/values <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-values>`_

        :param value_id: The unique identifier.
        :type value_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: CustomResourcesValue
        """
        data = await self.api.get(self.endpoint, value_id, **kwargs)
        return pydantic.TypeAdapter(CustomResourcesValue).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> CustomResourcesValue:
        """Create a new value.

        Official documentation: `custom_resources/values <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-resources-values>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: CustomResourcesValue
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(CustomResourcesValue).validate_python(response)
