import datetime
import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class BookkeepersManagementIncidence(pydantic.BaseModel):
    """Model for bookkeepers_management_incidence."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the incidence (aka employee update)
    id: int = pydantic.Field(description='Identifier of the incidence (aka employee update)')
    #: Identifier of employee related
    employee_id: int | None = pydantic.Field(default=None, description='Identifier of employee related')
    #: Identifier of legal entity related
    legal_entity_id: int = pydantic.Field(description='Identifier of legal entity related')
    #: Name of the incidence (aka employee update). It also represent the incidence type
    name: str = pydantic.Field(
        description='Name of the incidence (aka employee update). It also represent the incidence type',
    )
    #: Custom name of the incidence
    custom_name: str | None = pydantic.Field(default=None, description='Custom name of the incidence')
    #: The incidence is also related to another resource, for example for a leave target, the target identifier will be
    #: the leave id
    target_id: int = pydantic.Field(
        description=(
            'The incidence is also related to another resource, for example for a leave target, '
            'the target identifier will be the leave id'
        ),
    )
    #: The incidence is also related to another resource type. Examples: Employee, Contracts::ContractVersion,
    #: BookkeepersManagement::ManualIncidence, Finance::CostCenterMembership
    target_type: str = pydantic.Field(
        description=(
            'The incidence is also related to another resource type. Examples: Employee, '
            'Contracts::ContractVersion, BookkeepersManagement::ManualIncidence, Finance::CostCenterMembership'
        ),
    )
    #: The date the incidence (aka employee update) starts
    starts_on: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the incidence (aka employee update) starts',
    )
    #: The date the incidence (aka employee update) ends
    ends_on: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the incidence (aka employee update) ends',
    )
    #: The date the incidence (aka employee update) was read
    read_at: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the incidence (aka employee update) was read',
    )
    #: Status of the incidence
    status: str = pydantic.Field(description='Status of the incidence')
    #: Identifier of company related
    company_id: int = pydantic.Field(description='Identifier of company related')
    #: Indicate the message sender on the incidence (aka employee update). It can be any of 'bookkeeper', 'admin'
    message_from: str | None = pydantic.Field(
        default=None,
        description=(
            "Indicate the message sender on the incidence (aka employee update). It can be any of 'bookkeeper', 'admin'"
        ),
    )
    #: Boolean that indicates if the incidence (aka employee update) has unread messages
    has_message: bool | None = pydantic.Field(
        default=None,
        description='Boolean that indicates if the incidence (aka employee update) has unread messages',
    )
    #: Date in which incidence (aka employee update) was created
    created_at: datetime.datetime = pydantic.Field(
        description='Date in which incidence (aka employee update) was created',
    )
    #: Boolean that indicates if the incidence (aka employee update) has been reopened
    is_reopened: bool = pydantic.Field(
        description='Boolean that indicates if the incidence (aka employee update) has been reopened',
    )
    #: Legal entity name
    legal_entity_name: str | None = pydantic.Field(default=None, description='Legal entity name')
    #: Employee first name
    employee_first_name: str | None = pydantic.Field(default=None, description='Employee first name')
    #: Employee last name
    employee_last_name: str | None = pydantic.Field(default=None, description='Employee last name')


class BookkeepersManagementEndpoint(Endpoint):
    """Endpoint for bookkeepers management incidences operations."""

    endpoint = 'bookkeepers_management/incidences'

    async def all(self, **kwargs) -> ListApiResponse[BookkeepersManagementIncidence]:
        """Get all incidences records.

        Official documentation: `bookkeepers_management/incidences <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-bookkeepers-management-incidences>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[BookkeepersManagementIncidence]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=BookkeepersManagementIncidence, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[BookkeepersManagementIncidence]:
        """Get incidences with pagination metadata.

        Official documentation: `bookkeepers_management/incidences <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-bookkeepers-management-incidences>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[BookkeepersManagementIncidence]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=BookkeepersManagementIncidence,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, incidence_id: int | str, **kwargs) -> BookkeepersManagementIncidence:
        """Get a specific incidence by ID.

        Official documentation: `bookkeepers_management/incidences <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-bookkeepers-management-incidences-id>`_

        :param incidence_id: The unique identifier.
        :type incidence_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: BookkeepersManagementIncidence
        """
        data = await self.api.get(self.endpoint, incidence_id, **kwargs)
        return pydantic.TypeAdapter(BookkeepersManagementIncidence).validate_python(data)

    async def update(
        self,
        incidence_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> BookkeepersManagementIncidence:
        """Update an incidence.

        Official documentation: `bookkeepers_management/incidences <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-bookkeepers-management-incidences-id>`_

        :param incidence_id: The unique identifier of the record to update.
        :type incidence_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: BookkeepersManagementIncidence
        """
        response = await self.api.put(self.endpoint, incidence_id, json=data, **kwargs)
        return pydantic.TypeAdapter(BookkeepersManagementIncidence).validate_python(response)
