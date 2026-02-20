import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class BreakConfiguration(pydantic.BaseModel):
    """Model for time_settings_break_configuration."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Break configuration ID
    id: int = pydantic.Field(description='Break configuration ID')
    #: Name of the break configuration
    name: str = pydantic.Field(description='Name of the break configuration')
    #: Whether the break is paid
    paid: bool = pydantic.Field(description='Whether the break is paid')
    #: Whether the break configuration is archived
    archived: bool | None = pydantic.Field(default=None, description='Whether the break configuration is archived')


class BreakConfigurationEndpoint(Endpoint):
    """Endpoint for time_settings/break_configurations operations."""

    endpoint = 'time_settings/break_configurations'

    async def all(self, **kwargs) -> ListApiResponse[BreakConfiguration]:
        """Get all break configurations.

        Official documentation: `time_settings/break_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-settings-break-configurations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[BreakConfiguration]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=BreakConfiguration, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[BreakConfiguration]:
        """Get break configurations with pagination metadata.

        Official documentation: `time_settings/break_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-settings-break-configurations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[BreakConfiguration]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=BreakConfiguration, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, config_id: int | str, **kwargs) -> BreakConfiguration:
        """Get a specific break configuration by ID.

        Official documentation: `time_settings/break_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-settings-break-configurations>`_

        :param config_id: The unique identifier.
        :type config_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: BreakConfiguration
        """
        data = await self.api.get(self.endpoint, config_id, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> BreakConfiguration:
        """Create a new break configuration.

        Official documentation: `time_settings/break_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-settings-break-configurations>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: BreakConfiguration
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(response)

    async def update(self, config_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> BreakConfiguration:
        """Update a break configuration.

        Official documentation: `time_settings/break_configurations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-time-settings-break-configurations>`_

        :param config_id: The unique identifier of the record to update.
        :type config_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: BreakConfiguration
        """
        response = await self.api.put(self.endpoint, config_id, json=data, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(response)
