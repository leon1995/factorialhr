import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Location(pydantic.BaseModel):
    """Model for locations_location."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the location
    id: int = pydantic.Field(description='Identifier of the location')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Name of the location
    name: str = pydantic.Field(description='Name of the location')
    #: Timezone of the location
    timezone: str | None = pydantic.Field(default=None, description='Timezone of the location')
    #: Country code of the location
    country: str | None = pydantic.Field(default=None, description='Country code of the location')
    #: State of the location
    state: str | None = pydantic.Field(default=None, description='State of the location')
    #: City of the location
    city: str | None = pydantic.Field(default=None, description='City of the location')
    #: Address line 1 of the location
    address_line_1: str | None = pydantic.Field(default=None, description='Address line 1 of the location')
    #: Address line 2 of the location
    address_line_2: str | None = pydantic.Field(default=None, description='Address line 2 of the location')
    #: Postal code of the location
    postal_code: str | None = pydantic.Field(default=None, description='Postal code of the location')
    #: Phone number of the location
    phone_number: str | None = pydantic.Field(default=None, description='Phone number of the location')
    #: Whether the location is the main one
    main: bool = pydantic.Field(description='Whether the location is the main one')
    #: Latitude of the location
    latitude: float | None = pydantic.Field(default=None, description='Latitude of the location')
    #: Longitude of the location
    longitude: float | None = pydantic.Field(default=None, description='Longitude of the location')
    #: Radius of the location
    radius: float | None = pydantic.Field(default=None, description='Radius of the location')
    #: SIRET of the location (only for France)
    siret: str | None = pydantic.Field(default=None, description='SIRET of the location (only for France)')


class WorkArea(pydantic.BaseModel):
    """Model for locations_work_area."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Work area identifier
    id: int = pydantic.Field(description='Work area identifier')
    #: Location identifier
    location_id: int = pydantic.Field(description='Location identifier')
    #: Name of the work area
    name: str = pydantic.Field(description='Name of the work area')
    #: Archival timestamp of the work area
    archived_at: str | None = pydantic.Field(default=None, description='Archival timestamp of the work area')


class LocationsEndpoint(Endpoint):
    """Endpoint for locations/locations operations."""

    endpoint = 'locations/locations'

    async def all(self, **kwargs) -> ListApiResponse[Location]:
        """Get all locations records.

        Official documentation: `locations/locations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-locations-locations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Location]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Location, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Location]:
        """Get locations with pagination metadata.

        Official documentation: `locations/locations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-locations-locations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Location]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Location, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, location_id: int | str, **kwargs) -> Location:
        """Get a specific location by ID.

        Official documentation: `locations/locations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-locations-locations-id>`_

        :param location_id: The unique identifier.
        :type location_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Location
        """
        data = await self.api.get(self.endpoint, location_id, **kwargs)
        return pydantic.TypeAdapter(Location).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Location:
        """Create a new location.

        Official documentation: `locations/locations <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-locations-locations>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Location
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Location).validate_python(response)

    async def update(self, location_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Location:
        """Update a location.

        Official documentation: `locations/locations <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-locations-locations-id>`_

        :param location_id: The unique identifier of the record to update.
        :type location_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Location
        """
        response = await self.api.put(self.endpoint, location_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Location).validate_python(response)

    async def delete(self, location_id: int | str, **kwargs) -> Location:
        """Delete a location.

        Official documentation: `locations/locations <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-locations-locations-id>`_

        :param location_id: The unique identifier of the record to delete.
        :type location_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: Location
        """
        response = await self.api.delete(self.endpoint, location_id, **kwargs)
        return pydantic.TypeAdapter(Location).validate_python(response)


class WorkAreasEndpoint(Endpoint):
    """Endpoint for locations/work_areas operations."""

    endpoint = 'locations/work_areas'

    async def all(self, **kwargs) -> ListApiResponse[WorkArea]:
        """Get all work areas records.

        Official documentation: `locations/work_areas <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-locations-work-areas>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[WorkArea]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=WorkArea, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[WorkArea]:
        """Get work areas with pagination metadata.

        Official documentation: `locations/work_areas <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-locations-work-areas>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[WorkArea]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=WorkArea, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, work_area_id: int | str, **kwargs) -> WorkArea:
        """Get a specific work area by ID.

        Official documentation: `locations/work_areas <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-locations-work-areas-id>`_

        :param work_area_id: The unique identifier.
        :type work_area_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: WorkArea
        """
        data = await self.api.get(self.endpoint, work_area_id, **kwargs)
        return pydantic.TypeAdapter(WorkArea).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> WorkArea:
        """Create a new work area.

        Official documentation: `locations/work_areas <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-locations-work-areas>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: WorkArea
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkArea).validate_python(response)

    async def update(self, work_area_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> WorkArea:
        """Update a work area.

        Official documentation: `locations/work_areas <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-locations-work-areas-id>`_

        :param work_area_id: The unique identifier of the record to update.
        :type work_area_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: WorkArea
        """
        response = await self.api.put(self.endpoint, work_area_id, json=data, **kwargs)
        return pydantic.TypeAdapter(WorkArea).validate_python(response)

    async def archive(self, data: Mapping[str, typing.Any], **kwargs) -> WorkArea:
        """Archive a work area.

        Official documentation: `locations/work_areas <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-locations-work-areas-archive>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: WorkArea
        """
        response = await self.api.post(self.endpoint, 'archive', json=data, **kwargs)
        return pydantic.TypeAdapter(WorkArea).validate_python(response)

    async def unarchive(self, data: Mapping[str, typing.Any], **kwargs) -> WorkArea:
        """Unarchive a work area.

        Official documentation: `locations/work_areas <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-locations-work-areas-unarchive>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: WorkArea
        """
        response = await self.api.post(self.endpoint, 'unarchive', json=data, **kwargs)
        return pydantic.TypeAdapter(WorkArea).validate_python(response)
