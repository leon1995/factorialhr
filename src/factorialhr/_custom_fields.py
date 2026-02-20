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

    model_config = pydantic.ConfigDict(frozen=True)

    #: Field identifier
    id: int = pydantic.Field(description='Field identifier')
    #: The type of the field's value
    field_type: FieldType = pydantic.Field(description="The type of the field's value")
    #: Field label
    label_text: str = pydantic.Field(description='Field label')
    #: Field position within employee profile
    position: int | None = pydantic.Field(default=None, description='Field position within employee profile')
    #: Requirement to fill this field
    required: bool | None = pydantic.Field(default=None, description='Requirement to fill this field')
    #: Minimum value in range field type
    min_value: int | None = pydantic.Field(default=None, description='Minimum value in range field type')
    #: Maximum value in range field type
    max_value: int | None = pydantic.Field(default=None, description='Maximum value in range field type')
    #: Legal entity name where this field belongs
    legal_entity_name: str | None = pydantic.Field(
        default=None,
        description='Legal entity name where this field belongs',
    )
    #: Legal entity id where this field belongs
    legal_entity_id: int | None = pydantic.Field(default=None, description='Legal entity id where this field belongs')
    #: Custom field slug
    slug: str | None = pydantic.Field(default=None, description='Custom field slug')


class Option(pydantic.BaseModel):
    """Model for custom_fields_option."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Option identifier
    id: int = pydantic.Field(description='Option identifier')
    #: Title for option
    label: str | None = pydantic.Field(default=None, description='Title for option')
    #: Option value
    value: str | None = pydantic.Field(default=None, description='Option value')
    #: Flag to make the option available
    is_active: bool | None = pydantic.Field(default=None, description='Flag to make the option available')
    #: Custom Fields identifier
    field_id: int | None = pydantic.Field(default=None, description='Custom Fields identifier')


class ResourceField(pydantic.BaseModel):
    """Model for custom_fields_resource_field."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Resource field identifier
    id: int = pydantic.Field(description='Resource field identifier')
    #: Custom Field identifier
    field_id: int | None = pydantic.Field(default=None, description='Custom Field identifier')


class CustomFieldValue(pydantic.BaseModel):
    """Model for custom_fields_value."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Unique identifier for the custom field value
    id: int = pydantic.Field(description='Unique identifier for the custom field value')
    #: Custom Fields value
    value: bool | None = pydantic.Field(default=None, description='Custom Fields value')
    #: Custom field text value
    long_text_value: str | None = pydantic.Field(default=None, description='Custom field text value')
    #: Custom field identifier
    custom_field_identifier: str = pydantic.Field(description='Custom field identifier')
    #: Custom field date value
    date_value: datetime.date | None = pydantic.Field(default=None, description='Custom field date value')
    #: Custom field single choice value
    single_choice_value: str | None = pydantic.Field(default=None, description='Custom field single choice value')
    #: Custom field number value
    cents_value: int | None = pydantic.Field(default=None, description='Custom field number value')
    #: Valuable identifier
    valuable_id: int = pydantic.Field(description='Valuable identifier')
    #: Field identifier
    field_id: int = pydantic.Field(description='Field identifier')
    #: Valuable type
    valuable_type: str = pydantic.Field(description='Valuable type')
    #: Field label
    label: str | None = pydantic.Field(default=None, description='Field label')
    #: Whether field is required
    required: bool | None = pydantic.Field(default=None, description='Whether field is required')
    #: Usage group identifier
    usage_group_id: int | None = pydantic.Field(default=None, description='Usage group identifier')
    #: Usage group slug
    usage_group_slug: str | None = pydantic.Field(default=None, description='Usage group slug')
    #: The date and time the custom field value was last updated
    updated_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The date and time the custom field value was last updated',
    )


class FieldsEndpoint(Endpoint):
    """Endpoint for custom fields fields."""

    endpoint = 'custom_fields/fields'

    async def all(self, **kwargs) -> ListApiResponse[Field]:
        """Get all custom fields.

        Official documentation: `custom_fields/fields <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-fields>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Field]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Field)

    async def get(self, **kwargs) -> MetaApiResponse[Field]:
        """Get custom fields with pagination metadata.

        Official documentation: `custom_fields/fields <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-fields>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Field]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Field)

    async def get_by_id(self, field_id: int | str, **kwargs) -> Field:
        """Get a specific custom field by ID.

        Official documentation: `custom_fields/fields <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-field-id>`_

        :param field_id: The unique identifier.
        :type field_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Field
        """
        data = await self.api.get(f'{self.endpoint}/{field_id}', **kwargs)
        return pydantic.TypeAdapter(Field).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Field:
        """Create a new custom field.

        Official documentation: `custom_fields/fields <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-custom-fields-fields>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Field
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Field).validate_python(response['data'])

    async def delete(self, field_id: int | str, **kwargs) -> None:
        """Delete a custom field.

        Official documentation: `custom_fields/fields <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-custom-fields-fields-id>`_

        :param field_id: The unique identifier of the record to delete.
        :type field_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: None.
        :rtype: None
        """
        await self.api.delete(f'{self.endpoint}/{field_id}', **kwargs)


class OptionsEndpoint(Endpoint):
    """Endpoint for custom fields options."""

    endpoint = 'custom_fields/options'

    async def all(self, **kwargs) -> ListApiResponse[Option]:
        """Get all custom field options.

        Official documentation: `custom_fields/options <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-options>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Option]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Option)

    async def get(self, **kwargs) -> MetaApiResponse[Option]:
        """Get custom field options with pagination metadata.

        Official documentation: `custom_fields/options <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-options>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Option]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Option)

    async def get_by_id(self, option_id: int | str, **kwargs) -> Option:
        """Get a specific custom field option by ID.

        Official documentation: `custom_fields/options <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-options-id>`_

        :param option_id: The unique identifier.
        :type option_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Option
        """
        data = await self.api.get(f'{self.endpoint}/{option_id}', **kwargs)
        return pydantic.TypeAdapter(Option).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Option:
        """Create a new custom field option.

        Official documentation: `custom_fields/options <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-custom-fields-options>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Option
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Option).validate_python(response['data'])


class ResourceFieldsEndpoint(Endpoint):
    """Endpoint for custom fields resource fields."""

    endpoint = 'custom_fields/resource_fields'

    async def all(self, **kwargs) -> ListApiResponse[ResourceField]:
        """Get all custom resource fields.

        Official documentation: `custom_fields/resource_fields <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-resource-fields>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ResourceField]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=ResourceField)

    async def get(self, **kwargs) -> MetaApiResponse[ResourceField]:
        """Get custom resource fields with pagination metadata.

        Official documentation: `custom_fields/resource_fields <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-resource-fields>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ResourceField]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=ResourceField)

    async def get_by_id(self, resource_field_id: int | str, **kwargs) -> ResourceField:
        """Get a specific custom resource field by ID.

        Official documentation: `custom_fields/resource_fields <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-resource-fields-id>`_

        :param resource_field_id: The unique identifier.
        :type resource_field_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ResourceField
        """
        data = await self.api.get(f'{self.endpoint}/{resource_field_id}', **kwargs)
        return pydantic.TypeAdapter(ResourceField).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ResourceField:
        """Create a new custom resource field.

        Official documentation: `custom_fields/resource_fields <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-custom-fields-resource-fields>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ResourceField
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ResourceField).validate_python(response['data'])


class CustomFieldsValuesEndpoint(Endpoint):
    """Endpoint for custom fields values."""

    endpoint = 'custom_fields/values'

    async def all(self, **kwargs) -> ListApiResponse[CustomFieldValue]:
        """Get all custom field values.

        Official documentation: `custom_fields/values <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-values>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[CustomFieldValue]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=CustomFieldValue)

    async def get(self, **kwargs) -> MetaApiResponse[CustomFieldValue]:
        """Get custom field values with pagination metadata.

        Official documentation: `custom_fields/values <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-values>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[CustomFieldValue]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=CustomFieldValue)

    async def get_by_id(self, value_id: int | str, **kwargs) -> CustomFieldValue:
        """Get a specific custom field value by ID.

        Official documentation: `custom_fields/values <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-custom-fields-values-id>`_

        :param value_id: The unique identifier.
        :type value_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: CustomFieldValue
        """
        data = await self.api.get(f'{self.endpoint}/{value_id}', **kwargs)
        return pydantic.TypeAdapter(CustomFieldValue).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> CustomFieldValue:
        """Create a new custom field value.

        Official documentation: `custom_fields/values <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-custom-fields-values>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: CustomFieldValue
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(CustomFieldValue).validate_python(response['data'])

    async def update(self, value_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> CustomFieldValue:
        """Update a custom field value.

        Official documentation: `custom_fields/values <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-custom-fields-values-id>`_

        :param value_id: The unique identifier of the record to update.
        :type value_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: CustomFieldValue
        """
        response = await self.api.put(f'{self.endpoint}/{value_id}', json=data, **kwargs)
        return pydantic.TypeAdapter(CustomFieldValue).validate_python(response['data'])
