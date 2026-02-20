import datetime
import typing
from collections.abc import Mapping, Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Installation(pydantic.BaseModel):
    """Model for marketplace_installation."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Installation identifier
    id: int = pydantic.Field(description='Installation identifier')
    #: Installation name
    name: str = pydantic.Field(description='Installation name')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class InstallationSettings(pydantic.BaseModel):
    """Model for marketplace_installation_settings."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: List of leave types
    leave_types: Sequence[typing.Any] = pydantic.Field(description='List of leave types')
    #: List of additional compensation types
    additional_compensation_types: Sequence[typing.Any] = pydantic.Field(
        description='List of additional compensation types',
    )
    #: List of file numbers
    file_numbers: Sequence[typing.Any] = pydantic.Field(description='List of file numbers')
    #: List of establishment codes
    establishment_codes: Sequence[typing.Any] = pydantic.Field(description='List of establishment codes')
    #: List of timeoff allowance codes
    timeoff_allowance_code: Sequence[typing.Any] = pydantic.Field(description='List of timeoff allowance codes')


class InstallationsEndpoint(Endpoint):
    """Endpoint for marketplace/installations operations."""

    endpoint = 'marketplace/installations'

    async def all(self, **kwargs) -> ListApiResponse[Installation]:
        """Get all installations records.

        Official documentation: `marketplace/installations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-marketplace-installations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Installation]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Installation, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Installation]:
        """Get installations with pagination metadata.

        Official documentation: `marketplace/installations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-marketplace-installations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Installation]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Installation, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, installation_id: int | str, **kwargs) -> Installation:
        """Get a specific installation by ID.

        Official documentation: `marketplace/installations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-marketplace-installations-id>`_

        :param installation_id: The unique identifier.
        :type installation_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Installation
        """
        data = await self.api.get(self.endpoint, installation_id, **kwargs)
        return pydantic.TypeAdapter(Installation).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Installation:
        """Create a new installation.

        Official documentation: `marketplace/installations <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-marketplace-installations>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Installation
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Installation).validate_python(response)


class InstallationSettingsEndpoint(Endpoint):
    """Endpoint for marketplace/installation_settings operations."""

    endpoint = 'marketplace/installation_settings'

    async def all(self, **kwargs) -> ListApiResponse[InstallationSettings]:
        """Get all installation settings records.

        Official documentation: `marketplace/installation_settings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-marketplace-installation-settings>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[InstallationSettings]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=InstallationSettings, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[InstallationSettings]:
        """Get installation settings with pagination metadata.

        Official documentation: `marketplace/installation_settings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-marketplace-installation-settings>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[InstallationSettings]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=InstallationSettings, raw_meta=response['meta'], raw_data=response['data'])
