import typing
from collections.abc import Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class InstallationSettings(pydantic.BaseModel):
    """Model for marketplace_installation_settings."""

    leave_types: Sequence[typing.Any] = pydantic.Field(description='List of leave types')
    additional_compensation_types: Sequence[typing.Any] = pydantic.Field(
        description='List of additional compensation types',
    )
    file_numbers: Sequence[typing.Any] = pydantic.Field(description='List of file numbers')
    establishment_codes: Sequence[typing.Any] = pydantic.Field(description='List of establishment codes')
    timeoff_allowance_code: Sequence[typing.Any] = pydantic.Field(description='List of timeoff allowance codes')


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
