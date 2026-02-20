import datetime
import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class ItAsset(pydantic.BaseModel):
    """Model for it_management_it_asset. IT Asset (device, accessory, keys, etc)."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: IT asset identifier
    id: int = pydantic.Field(description='IT asset identifier')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: IT asset model identifier
    it_asset_model_id: int = pydantic.Field(description='IT asset model identifier')
    #: Serial number
    serial_number: str | None = pydantic.Field(default=None, description='Serial number')
    #: Status of the asset
    status: str = pydantic.Field(description='Status of the asset')
    #: Owner employee identifier
    owner_id: int | None = pydantic.Field(default=None, description='Owner employee identifier')
    #: Location identifier
    location_id: int | None = pydantic.Field(default=None, description='Location identifier')
    #: Workplace identifier
    workplace_id: int | None = pydantic.Field(default=None, description='Workplace identifier')
    #: Team identifier
    team_id: int | None = pydantic.Field(default=None, description='Team identifier')
    #: Purchase date
    purchase_date: datetime.date | None = pydantic.Field(default=None, description='Purchase date')
    #: Purchase price in cents
    purchase_price_cents: int | None = pydantic.Field(default=None, description='Purchase price in cents')
    #: Currency code
    currency: str | None = pydantic.Field(default=None, description='Currency code')
    #: Warranty end date
    warranty_end_date: datetime.date | None = pydantic.Field(default=None, description='Warranty end date')
    #: Label
    label: str | None = pydantic.Field(default=None, description='Label')
    #: Notes
    notes: str | None = pydantic.Field(default=None, description='Notes')


class ItAssetsEndpoint(Endpoint):
    """Endpoint for it_management/it_assets operations."""

    endpoint = 'it_management/it_assets'

    async def all(self, **kwargs) -> ListApiResponse[ItAsset]:
        """Get all IT assets.

        Official documentation: `it_management/it_assets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-assets>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ItAsset]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ItAsset, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ItAsset]:
        """Get IT assets with pagination metadata.

        Official documentation: `it_management/it_assets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-assets>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ItAsset]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ItAsset, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, asset_id: int | str, **kwargs) -> ItAsset:
        """Get a specific IT asset by ID.

        Official documentation: `it_management/it_assets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-assets>`_

        :param asset_id: The unique identifier.
        :type asset_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ItAsset
        """
        data = await self.api.get(self.endpoint, asset_id, **kwargs)
        raw = data['data'] if isinstance(data, dict) and 'data' in data else data
        return pydantic.TypeAdapter(ItAsset).validate_python(raw)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ItAsset:
        """Create an IT asset.

        Official documentation: `it_management/it_assets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-assets>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ItAsset
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        raw = response['data'] if isinstance(response, dict) and 'data' in response else response
        return pydantic.TypeAdapter(ItAsset).validate_python(raw)

    async def update(self, asset_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ItAsset:
        """Update an IT asset.

        Official documentation: `it_management/it_assets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-assets>`_

        :param asset_id: The unique identifier of the record to update.
        :type asset_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: ItAsset
        """
        response = await self.api.put(self.endpoint, asset_id, json=data, **kwargs)
        raw = response['data'] if isinstance(response, dict) and 'data' in response else response
        return pydantic.TypeAdapter(ItAsset).validate_python(raw)

    async def delete(self, asset_id: int | str, **kwargs) -> ItAsset:
        """Delete an IT asset.

        Official documentation: `it_management/it_assets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-assets>`_

        :param asset_id: The unique identifier of the record to delete.
        :type asset_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: ItAsset
        """
        response = await self.api.delete(self.endpoint, asset_id, **kwargs)
        raw = response['data'] if isinstance(response, dict) and 'data' in response else response
        return pydantic.TypeAdapter(ItAsset).validate_python(raw)


class ItAssetModel(pydantic.BaseModel):
    """Model for it_management_it_asset_model. IT Asset Model (make/model of device)."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: IT asset model identifier
    id: int = pydantic.Field(description='IT asset model identifier')
    #: Type name
    type_name: str = pydantic.Field(description='Type name')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Brand
    brand: str | None = pydantic.Field(default=None, description='Brand')
    #: Name
    name: str = pydantic.Field(description='Name')
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class ItAssetModelsEndpoint(Endpoint):
    """Endpoint for it_management/it_asset_models operations."""

    endpoint = 'it_management/it_asset_models'

    async def all(self, **kwargs) -> ListApiResponse[ItAssetModel]:
        """Get all IT asset models.

        Official documentation: `it_management/it_asset_models <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-asset-models>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ItAssetModel]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ItAssetModel, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ItAssetModel]:
        """Get IT asset models with pagination metadata.

        Official documentation: `it_management/it_asset_models <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-asset-models>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ItAssetModel]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ItAssetModel, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, model_id: int | str, **kwargs) -> ItAssetModel:
        """Get a specific IT asset model by ID.

        Official documentation: `it_management/it_asset_models <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-asset-models>`_

        :param model_id: The unique identifier.
        :type model_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ItAssetModel
        """
        data = await self.api.get(self.endpoint, model_id, **kwargs)
        raw = data['data'] if isinstance(data, dict) and 'data' in data else data
        return pydantic.TypeAdapter(ItAssetModel).validate_python(raw)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ItAssetModel:
        """Create an IT asset model.

        Official documentation: `it_management/it_asset_models <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-asset-models>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ItAssetModel
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        raw = response['data'] if isinstance(response, dict) and 'data' in response else response
        return pydantic.TypeAdapter(ItAssetModel).validate_python(raw)

    async def update(self, model_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ItAssetModel:
        """Update an IT asset model.

        Official documentation: `it_management/it_asset_models <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-it-management-it-asset-models>`_

        :param model_id: The unique identifier of the record to update.
        :type model_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: ItAssetModel
        """
        response = await self.api.put(self.endpoint, model_id, json=data, **kwargs)
        raw = response['data'] if isinstance(response, dict) and 'data' in response else response
        return pydantic.TypeAdapter(ItAssetModel).validate_python(raw)
