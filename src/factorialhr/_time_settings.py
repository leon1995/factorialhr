import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class BreakConfiguration(pydantic.BaseModel):
    """Model for time_settings_break_configuration."""

    id: int = pydantic.Field(description='Break configuration ID')
    name: str = pydantic.Field(description='Name of the break configuration')
    paid: bool = pydantic.Field(description='Whether the break is paid')
    archived: bool | None = pydantic.Field(default=None, description='Whether the break configuration is archived')


class BreakConfigurationEndpoint(Endpoint):
    """Endpoint for time_settings/break_configurations operations."""

    endpoint = 'time_settings/break_configurations'

    async def all(self, **kwargs) -> ListApiResponse[BreakConfiguration]:
        """Get all break configurations."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=BreakConfiguration, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[BreakConfiguration]:
        """Get break configurations with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=BreakConfiguration, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, config_id: int | str, **kwargs) -> BreakConfiguration:
        """Get a specific break configuration by ID."""
        data = await self.api.get(self.endpoint, config_id, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> BreakConfiguration:
        """Create a new break configuration."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(response)

    async def update(self, config_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> BreakConfiguration:
        """Update a break configuration."""
        response = await self.api.put(self.endpoint, config_id, json=data, **kwargs)
        return pydantic.TypeAdapter(BreakConfiguration).validate_python(response)
