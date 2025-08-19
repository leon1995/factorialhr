import datetime
import typing
from collections.abc import Mapping, Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Schema(pydantic.BaseModel):
    """Model for custom_resources_schema."""

    id: int = pydantic.Field(description='Schema identifier')
    name: str = pydantic.Field(description='Schema name')
    company_id: int = pydantic.Field(description='Company identifier where this schema belongs')
    hidden: bool = pydantic.Field(description='Manages visibility of the schema')
    position: int | None = pydantic.Field(default=None, description='Schema position within employee profile')


class CustomResourcesValue(pydantic.BaseModel):
    """Model for custom_resources_value."""

    id: int = pydantic.Field(description='Value identifier')
    field_id: int = pydantic.Field(description='Identifier of the field this value belongs to')
    long_text_value: str | None = pydantic.Field(
        default=None,
        description="When the field's type is long_text_value, value for schema long_text_value custom field",
    )
    date_value: datetime.date | None = pydantic.Field(
        default=None,
        description="When the field's type is date_value, value for schema date_value custom field",
    )
    text_value: str | None = pydantic.Field(
        default=None,
        description="When the field's type is text_value, value for schema text_value custom field",
    )
    number_value: int | None = pydantic.Field(
        default=None,
        description="When the field's type is number_value, value for schema number_value custom field",
    )
    option_value: str | None = pydantic.Field(
        default=None,
        description="When the field's type is option_value, selected value for schema option_value custom field",
    )
    cents_value: int | None = pydantic.Field(
        default=None,
        description="When the field's type is cents_value, value for schema cents_value custom field",
    )
    boolean_value: bool | None = pydantic.Field(
        default=None,
        description="When the field's type is boolean_value, value for schema boolean_value custom field",
    )
    single_choice_value: str | None = pydantic.Field(
        default=None,
        description=(
            "When the field's type is single_choice_value, selected value for schema single_choice_value custom field"
        ),
    )
    multiple_choice_value: Sequence[str] | None = pydantic.Field(
        default=None,
        description=(
            "When the field's type is multiple_choice_value, "
            'selected values for schema multiple_choice_value custom field'
        ),
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
