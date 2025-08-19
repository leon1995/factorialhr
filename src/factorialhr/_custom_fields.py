import datetime
import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class FieldType(StrEnum):
    """Enum for custom field types."""

    TEXT = 'text'
    LONG_TEXT = 'long_text'
    DATE = 'date'
    RATING = 'rating'
    CHECKBOX = 'checkbox'
    SINGLE_CHOICE = 'single_choice'
    MULTIPLE_CHOICE = 'multiple_choice'
    MONEY = 'money'
    CENTS = 'cents'


class Field(pydantic.BaseModel):
    """Model for custom_fields_field."""

    id: int = pydantic.Field(description='Field identifier')
    field_type: FieldType = pydantic.Field(description="The type of the field's value")
    label_text: str = pydantic.Field(description='Field label')
    position: int | None = pydantic.Field(default=None, description='Field position within employee profile')
    required: bool | None = pydantic.Field(default=None, description='Requirement to fill this field')
    min_value: int | None = pydantic.Field(default=None, description='Minimum value in range field type')
    max_value: int | None = pydantic.Field(default=None, description='Maximum value in range field type')
    legal_entity_name: str | None = pydantic.Field(
        default=None,
        description='Legal entity name where this field belongs',
    )
    legal_entity_id: int | None = pydantic.Field(default=None, description='Legal entity id where this field belongs')
    slug: str | None = pydantic.Field(default=None, description='Custom field slug')


class Option(pydantic.BaseModel):
    """Model for custom_fields_option."""

    id: int = pydantic.Field(description='Option identifier')
    label: str | None = pydantic.Field(default=None, description='Title for option')
    value: str | None = pydantic.Field(default=None, description='Option value')
    is_active: bool | None = pydantic.Field(default=None, description='Flag to make the option available')
    field_id: int | None = pydantic.Field(default=None, description='Custom Fields identifier')


class ResourceField(pydantic.BaseModel):
    """Model for custom_fields_resource_field."""

    id: int = pydantic.Field(description='Resource field identifier')
    field_id: int | None = pydantic.Field(default=None, description='Custom Field identifier')


class CustomFieldValue(pydantic.BaseModel):
    """Model for custom_fields_value."""

    id: int = pydantic.Field(description='Unique identifier for the custom field value')
    value: bool | None = pydantic.Field(default=None, description='Custom Fields value')
    long_text_value: str | None = pydantic.Field(default=None, description='Custom field text value')
    custom_field_identifier: str = pydantic.Field(description='Custom field identifier')
    date_value: datetime.date | None = pydantic.Field(default=None, description='Custom field date value')
    single_choice_value: str | None = pydantic.Field(default=None, description='Custom field single choice value')
    cents_value: int | None = pydantic.Field(default=None, description='Custom field number value')
    valuable_id: int = pydantic.Field(description='Valuable identifier')
    field_id: int = pydantic.Field(description='Field identifier')
    valuable_type: str = pydantic.Field(description='Valuable type')
    label: str | None = pydantic.Field(default=None, description='Field label')
    required: bool | None = pydantic.Field(default=None, description='Whether field is required')
    usage_group_id: int | None = pydantic.Field(default=None, description='Usage group identifier')
    usage_group_slug: str | None = pydantic.Field(default=None, description='Usage group slug')


class FieldsEndpoint(Endpoint):
    """Endpoint for custom fields fields."""

    endpoint = '/custom_fields/fields'

    async def all(self, **kwargs) -> ListApiResponse[Field]:
        """Get all custom fields."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Field)

    async def get(self, **kwargs) -> MetaApiResponse[Field]:
        """Get custom fields with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Field)

    async def get_by_id(self, field_id: int | str, **kwargs) -> Field:
        """Get a specific custom field by ID."""
        data = await self.api.get(f'{self.endpoint}/{field_id}', **kwargs)
        return pydantic.TypeAdapter(Field).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Field:
        """Create a new custom field."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Field).validate_python(response['data'])

    async def delete(self, field_id: int | str, **kwargs) -> None:
        """Delete a custom field."""
        await self.api.delete(f'{self.endpoint}/{field_id}', **kwargs)


class OptionsEndpoint(Endpoint):
    """Endpoint for custom fields options."""

    endpoint = '/custom_fields/options'

    async def all(self, **kwargs) -> ListApiResponse[Option]:
        """Get all custom field options."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Option)

    async def get(self, **kwargs) -> MetaApiResponse[Option]:
        """Get custom field options with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Option)

    async def get_by_id(self, option_id: int | str, **kwargs) -> Option:
        """Get a specific custom field option by ID."""
        data = await self.api.get(f'{self.endpoint}/{option_id}', **kwargs)
        return pydantic.TypeAdapter(Option).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Option:
        """Create a new custom field option."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Option).validate_python(response['data'])


class ResourceFieldsEndpoint(Endpoint):
    """Endpoint for custom fields resource fields."""

    endpoint = '/custom_fields/resource_fields'

    async def all(self, **kwargs) -> ListApiResponse[ResourceField]:
        """Get all custom resource fields."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=ResourceField)

    async def get(self, **kwargs) -> MetaApiResponse[ResourceField]:
        """Get custom resource fields with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=ResourceField)

    async def get_by_id(self, resource_field_id: int | str, **kwargs) -> ResourceField:
        """Get a specific custom resource field by ID."""
        data = await self.api.get(f'{self.endpoint}/{resource_field_id}', **kwargs)
        return pydantic.TypeAdapter(ResourceField).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ResourceField:
        """Create a new custom resource field."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ResourceField).validate_python(response['data'])


class CustomFieldsValuesEndpoint(Endpoint):
    """Endpoint for custom fields values."""

    endpoint = '/custom_fields/values'

    async def all(self, **kwargs) -> ListApiResponse[CustomFieldValue]:
        """Get all custom field values."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=CustomFieldValue)

    async def get(self, **kwargs) -> MetaApiResponse[CustomFieldValue]:
        """Get custom field values with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=CustomFieldValue)

    async def get_by_id(self, value_id: int | str, **kwargs) -> CustomFieldValue:
        """Get a specific custom field value by ID."""
        data = await self.api.get(f'{self.endpoint}/{value_id}', **kwargs)
        return pydantic.TypeAdapter(CustomFieldValue).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> CustomFieldValue:
        """Create a new custom field value."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(CustomFieldValue).validate_python(response['data'])

    async def update(self, value_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> CustomFieldValue:
        """Update a custom field value."""
        response = await self.api.put(f'{self.endpoint}/{value_id}', json=data, **kwargs)
        return pydantic.TypeAdapter(CustomFieldValue).validate_python(response['data'])
