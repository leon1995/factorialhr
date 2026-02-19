import datetime
import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class ItAsset(pydantic.BaseModel):
    """Model for it_management_it_asset. IT Asset (device, accessory, keys, etc)."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='IT asset identifier')
    company_id: int = pydantic.Field(description='Company identifier')
    it_asset_model_id: int = pydantic.Field(description='IT asset model identifier')
    serial_number: str | None = pydantic.Field(default=None, description='Serial number')
    status: str = pydantic.Field(description='Status of the asset')
    owner_id: int | None = pydantic.Field(default=None, description='Owner employee identifier')
    location_id: int | None = pydantic.Field(default=None, description='Location identifier')
    workplace_id: int | None = pydantic.Field(default=None, description='Workplace identifier')
    team_id: int | None = pydantic.Field(default=None, description='Team identifier')
    purchase_date: datetime.date | None = pydantic.Field(default=None, description='Purchase date')
    purchase_price_cents: int | None = pydantic.Field(default=None, description='Purchase price in cents')
    currency: str | None = pydantic.Field(default=None, description='Currency code')
    warranty_end_date: datetime.date | None = pydantic.Field(default=None, description='Warranty end date')
    label: str | None = pydantic.Field(default=None, description='Label')
    notes: str | None = pydantic.Field(default=None, description='Notes')


class ItAssetsEndpoint(Endpoint):
    """Endpoint for it_management/it_assets operations."""

    endpoint = 'it_management/it_assets'

    async def all(self, **kwargs) -> ListApiResponse[ItAsset]:
        """Get all IT assets."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ItAsset, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ItAsset]:
        """Get IT assets with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ItAsset, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, asset_id: int | str, **kwargs) -> ItAsset:
        """Get a specific IT asset by ID."""
        data = await self.api.get(self.endpoint, asset_id, **kwargs)
        raw = data['data'] if isinstance(data, dict) and 'data' in data else data
        return pydantic.TypeAdapter(ItAsset).validate_python(raw)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ItAsset:
        """Create an IT asset."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        raw = response['data'] if isinstance(response, dict) and 'data' in response else response
        return pydantic.TypeAdapter(ItAsset).validate_python(raw)

    async def update(self, asset_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ItAsset:
        """Update an IT asset."""
        response = await self.api.put(self.endpoint, asset_id, json=data, **kwargs)
        raw = response['data'] if isinstance(response, dict) and 'data' in response else response
        return pydantic.TypeAdapter(ItAsset).validate_python(raw)

    async def delete(self, asset_id: int | str, **kwargs) -> ItAsset:
        """Delete an IT asset."""
        response = await self.api.delete(self.endpoint, asset_id, **kwargs)
        raw = response['data'] if isinstance(response, dict) and 'data' in response else response
        return pydantic.TypeAdapter(ItAsset).validate_python(raw)


class ItAssetModel(pydantic.BaseModel):
    """Model for it_management_it_asset_model. IT Asset Model (make/model of device)."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='IT asset model identifier')
    type_name: str = pydantic.Field(description='Type name')
    company_id: int = pydantic.Field(description='Company identifier')
    brand: str | None = pydantic.Field(default=None, description='Brand')
    name: str = pydantic.Field(description='Name')
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class ItAssetModelsEndpoint(Endpoint):
    """Endpoint for it_management/it_asset_models operations."""

    endpoint = 'it_management/it_asset_models'

    async def all(self, **kwargs) -> ListApiResponse[ItAssetModel]:
        """Get all IT asset models."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ItAssetModel, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ItAssetModel]:
        """Get IT asset models with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ItAssetModel, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, model_id: int | str, **kwargs) -> ItAssetModel:
        """Get a specific IT asset model by ID."""
        data = await self.api.get(self.endpoint, model_id, **kwargs)
        raw = data['data'] if isinstance(data, dict) and 'data' in data else data
        return pydantic.TypeAdapter(ItAssetModel).validate_python(raw)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ItAssetModel:
        """Create an IT asset model."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        raw = response['data'] if isinstance(response, dict) and 'data' in response else response
        return pydantic.TypeAdapter(ItAssetModel).validate_python(raw)

    async def update(self, model_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ItAssetModel:
        """Update an IT asset model."""
        response = await self.api.put(self.endpoint, model_id, json=data, **kwargs)
        raw = response['data'] if isinstance(response, dict) and 'data' in response else response
        return pydantic.TypeAdapter(ItAssetModel).validate_python(raw)
