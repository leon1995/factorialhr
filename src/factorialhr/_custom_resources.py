import datetime
import typing
from collections.abc import Mapping, Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Schema(pydantic.BaseModel):
    """Model for custom_resources_schema."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='Schema identifier')
    name: str = pydantic.Field(description='Schema name')
    company_id: int = pydantic.Field(description='Company identifier where this schema belongs')
    hidden: bool = pydantic.Field(description='Manages visibility of the schema')
    position: int | None = pydantic.Field(default=None, description='Schema position within employee profile')


class Resource(pydantic.BaseModel):
    """Model for custom_resources_resource."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='Resource identifier')
    name: str = pydantic.Field(description='Resource name')
    company_id: int = pydantic.Field(description='Company identifier')
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class CustomResourcesValue(pydantic.BaseModel):
    """Model for custom_resources_value."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='Value identifier')
    resource_id: int = pydantic.Field(
        description='The identifier of the resource that owns the resource value',
    )
    attachable_id: int | None = pydantic.Field(
        default=None,
        description='The id of the attached resource like an employee',
    )


class CustomResourcesSchemasEndpoint(Endpoint):
    """Endpoint for custom_resources/schemas operations."""

    endpoint = 'custom_resources/schemas'

    async def all(self, **kwargs) -> ListApiResponse[Schema]:
        """Get all schemas records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Schema)

    async def get(self, **kwargs) -> MetaApiResponse[Schema]:
        """Get schemas with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Schema)

    async def get_by_id(self, schema_id: int | str, **kwargs) -> Schema:
        """Get a specific schema by ID."""
        data = await self.api.get(self.endpoint, schema_id, **kwargs)
        return pydantic.TypeAdapter(Schema).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Schema:
        """Create a new schema."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Schema).validate_python(response)


class ResourcesEndpoint(Endpoint):
    """Endpoint for custom_resources/resources operations."""

    endpoint = 'custom_resources/resources'

    async def all(self, **kwargs) -> ListApiResponse[Resource]:
        """Get all resources records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Resource)

    async def get(self, **kwargs) -> MetaApiResponse[Resource]:
        """Get resources with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Resource)

    async def get_by_id(self, resource_id: int | str, **kwargs) -> Resource:
        """Get a specific resource by ID."""
        data = await self.api.get(self.endpoint, resource_id, **kwargs)
        return pydantic.TypeAdapter(Resource).validate_python(data)


class CustomResourcesValuesEndpoint(Endpoint):
    """Endpoint for custom_resources/values operations."""

    endpoint = 'custom_resources/values'

    async def all(self, **kwargs) -> ListApiResponse[CustomResourcesValue]:
        """Get all values records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=CustomResourcesValue)

    async def get(self, **kwargs) -> MetaApiResponse[CustomResourcesValue]:
        """Get values with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=CustomResourcesValue)

    async def get_by_id(self, value_id: int | str, **kwargs) -> CustomResourcesValue:
        """Get a specific value by ID."""
        data = await self.api.get(self.endpoint, value_id, **kwargs)
        return pydantic.TypeAdapter(CustomResourcesValue).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> CustomResourcesValue:
        """Create a new value."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(CustomResourcesValue).validate_python(response)
