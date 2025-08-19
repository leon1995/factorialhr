import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Location(pydantic.BaseModel):
    """Model for locations_location."""

    id: int = pydantic.Field(description='Identifier of the location')
    company_id: int = pydantic.Field(description='Company identifier')
    name: str = pydantic.Field(description='Name of the location')
    timezone: str | None = pydantic.Field(default=None, description='Timezone of the location')
    country: str | None = pydantic.Field(default=None, description='Country code of the location')
    state: str | None = pydantic.Field(default=None, description='State of the location')
    city: str | None = pydantic.Field(default=None, description='City of the location')
    address_line_1: str | None = pydantic.Field(default=None, description='Address line 1 of the location')
    address_line_2: str | None = pydantic.Field(default=None, description='Address line 2 of the location')
    postal_code: str | None = pydantic.Field(default=None, description='Postal code of the location')
    phone_number: str | None = pydantic.Field(default=None, description='Phone number of the location')
    main: bool = pydantic.Field(description='Whether the location is the main one')
    latitude: float | None = pydantic.Field(default=None, description='Latitude of the location')
    longitude: float | None = pydantic.Field(default=None, description='Longitude of the location')
    radius: float | None = pydantic.Field(default=None, description='Radius of the location')
    siret: str | None = pydantic.Field(default=None, description='SIRET of the location (only for France)')


class WorkArea(pydantic.BaseModel):
    """Model for locations_work_area."""

    id: int = pydantic.Field(description='Work area identifier')
    location_id: int = pydantic.Field(description='Location identifier')
    name: str = pydantic.Field(description='Name of the work area')
    archived_at: str | None = pydantic.Field(default=None, description='Archival timestamp of the work area')


class LocationsEndpoint(Endpoint):
    """Endpoint for locations/locations operations."""

    endpoint = 'locations/locations'

    async def all(self, **kwargs) -> ListApiResponse[Location]:
        """Get all locations records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Location, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Location]:
        """Get locations with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Location, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, location_id: int | str, **kwargs) -> Location:
        """Get a specific location by ID."""
        data = await self.api.get(self.endpoint, location_id, **kwargs)
        return pydantic.TypeAdapter(Location).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Location:
        """Create a new location."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Location).validate_python(response)

    async def update(self, location_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Location:
        """Update a location."""
        response = await self.api.put(self.endpoint, location_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Location).validate_python(response)

    async def delete(self, location_id: int | str, **kwargs) -> Location:
        """Delete a location."""
        response = await self.api.delete(self.endpoint, location_id, **kwargs)
        return pydantic.TypeAdapter(Location).validate_python(response)


class WorkAreasEndpoint(Endpoint):
    """Endpoint for locations/work_areas operations."""

    endpoint = 'locations/work_areas'

    async def all(self, **kwargs) -> ListApiResponse[WorkArea]:
        """Get all work areas records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=WorkArea, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[WorkArea]:
        """Get work areas with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=WorkArea, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, work_area_id: int | str, **kwargs) -> WorkArea:
        """Get a specific work area by ID."""
        data = await self.api.get(self.endpoint, work_area_id, **kwargs)
        return pydantic.TypeAdapter(WorkArea).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> WorkArea:
        """Create a new work area."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkArea).validate_python(response)

    async def update(self, work_area_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> WorkArea:
        """Update a work area."""
        response = await self.api.put(self.endpoint, work_area_id, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkArea).validate_python(response)

    async def archive(self, data: Mapping[str, typing.Any], **kwargs) -> WorkArea:
        """Archive a work area."""
        response = await self.api.post(self.endpoint, 'archive', json=data, **kwargs)
        return pydantic.TypeAdapter(WorkArea).validate_python(response)

    async def unarchive(self, data: Mapping[str, typing.Any], **kwargs) -> WorkArea:
        """Unarchive a work area."""
        response = await self.api.post(self.endpoint, 'unarchive', json=data, **kwargs)
        return pydantic.TypeAdapter(WorkArea).validate_python(response)
