import datetime
import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class SyncableType(StrEnum):
    """Enum for syncable item types."""

    COMPENSATION = 'compensations/compensation'
    EXPENSE = 'expenses/expense'


class SyncableItem(pydantic.BaseModel):
    """Model for integrations_syncable_item."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='Syncable item identifier')
    sync_run_id: int = pydantic.Field(description='Sync run identifier')
    item_type: str = pydantic.Field(description='Type of the syncable item')
    item_id: int = pydantic.Field(description='Identifier of the item')
    status: str = pydantic.Field(description='Status of the syncable item')
    syncable_type: SyncableType = pydantic.Field(description='Type of the syncable item')
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class SyncableSyncRun(pydantic.BaseModel):
    """Model for integrations_syncable_sync_run."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='Sync run identifier')
    syncable_item_id: int = pydantic.Field(description='Syncable item identifier')
    status: str = pydantic.Field(description='Status of the sync run')
    started_at: datetime.datetime | None = pydantic.Field(default=None, description='Start date')
    completed_at: datetime.datetime | None = pydantic.Field(default=None, description='Completion date')
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class SyncableItemsEndpoint(Endpoint):
    """Endpoint for integrations/syncable_items operations."""

    endpoint = 'integrations/syncable_items'

    async def all(self, **kwargs) -> ListApiResponse[SyncableItem]:
        """Get all syncable items records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SyncableItem, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SyncableItem]:
        """Get syncable items with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=SyncableItem, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, item_id: int | str, **kwargs) -> SyncableItem:
        """Get a specific syncable item by ID."""
        data = await self.api.get(self.endpoint, item_id, **kwargs)
        return pydantic.TypeAdapter(SyncableItem).validate_python(data)


class SyncableSyncRunsEndpoint(Endpoint):
    """Endpoint for integrations/syncable_sync_runs operations."""

    endpoint = 'integrations/syncable_sync_runs'

    async def all(self, **kwargs) -> ListApiResponse[SyncableSyncRun]:
        """Get all syncable sync runs records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SyncableSyncRun, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SyncableSyncRun]:
        """Get syncable sync runs with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=SyncableSyncRun, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, run_id: int | str, **kwargs) -> SyncableSyncRun:
        """Get a specific syncable sync run by ID."""
        data = await self.api.get(self.endpoint, run_id, **kwargs)
        return pydantic.TypeAdapter(SyncableSyncRun).validate_python(data)

    async def update(self, run_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> SyncableSyncRun:
        """Update a syncable sync run."""
        response = await self.api.put(self.endpoint, run_id, json=data, **kwargs)
        return pydantic.TypeAdapter(SyncableSyncRun).validate_python(response)
