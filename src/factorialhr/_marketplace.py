import datetime
import typing
from collections.abc import Mapping, Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Installation(pydantic.BaseModel):
    """Model for marketplace_installation."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='Installation identifier')
    name: str = pydantic.Field(description='Installation name')
    company_id: int = pydantic.Field(description='Company identifier')
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class InstallationSettings(pydantic.BaseModel):
    """Model for marketplace_installation_settings."""

    model_config = pydantic.ConfigDict(frozen=True)

    leave_types: Sequence[typing.Any] = pydantic.Field(description='List of leave types')
    additional_compensation_types: Sequence[typing.Any] = pydantic.Field(
        description='List of additional compensation types',
    )
    file_numbers: Sequence[typing.Any] = pydantic.Field(description='List of file numbers')
    establishment_codes: Sequence[typing.Any] = pydantic.Field(description='List of establishment codes')
    timeoff_allowance_code: Sequence[typing.Any] = pydantic.Field(description='List of timeoff allowance codes')


class InstallationsEndpoint(Endpoint):
    """Endpoint for marketplace/installations operations."""

    endpoint = 'marketplace/installations'

    async def all(self, **kwargs) -> ListApiResponse[Installation]:
        """Get all installations records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Installation, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Installation]:
        """Get installations with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Installation, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, installation_id: int | str, **kwargs) -> Installation:
        """Get a specific installation by ID."""
        data = await self.api.get(self.endpoint, installation_id, **kwargs)
        return pydantic.TypeAdapter(Installation).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Installation:
        """Create a new installation."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Installation).validate_python(response)


class InstallationSettingsEndpoint(Endpoint):
    """Endpoint for marketplace/installation_settings operations."""

    endpoint = 'marketplace/installation_settings'

    async def all(self, **kwargs) -> ListApiResponse[InstallationSettings]:
        """Get all installation settings records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=InstallationSettings, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[InstallationSettings]:
        """Get installation settings with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=InstallationSettings, raw_meta=response['meta'], raw_data=response['data'])
