import datetime
import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class BookkeepersManagementIncidence(pydantic.BaseModel):
    """Model for bookkeepers_management_incidence."""

    id: int = pydantic.Field(description='Identifier of the incidence (aka employee update)')
    employee_id: int | None = pydantic.Field(default=None, description='Identifier of employee related')
    legal_entity_id: int = pydantic.Field(description='Identifier of legal entity related')
    name: str = pydantic.Field(
        description='Name of the incidence (aka employee update). It also represent the incidence type',
    )
    custom_name: str | None = pydantic.Field(default=None, description='Custom name of the incidence')
    target_id: int = pydantic.Field(
        description=(
            'The incidence is also related to another resource, for example for a leave target, '
            'the target identifier will be the leave id'
        ),
    )
    target_type: str = pydantic.Field(
        description=(
            'The incidence is also related to another resource type. Examples: Employee, '
            'Contracts::ContractVersion, BookkeepersManagement::ManualIncidence, Finance::CostCenterMembership'
        ),
    )
    starts_on: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the incidence (aka employee update) starts',
    )
    ends_on: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the incidence (aka employee update) ends',
    )
    read_at: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the incidence (aka employee update) was read',
    )
    status: str = pydantic.Field(description='Status of the incidence')
    company_id: int = pydantic.Field(description='Identifier of company related')
    message_from: str | None = pydantic.Field(
        default=None,
        description=(
            "Indicate the message sender on the incidence (aka employee update). It can be any of 'bookkeeper', 'admin'"
        ),
    )
    has_message: bool | None = pydantic.Field(
        default=None,
        description='Boolean that indicates if the incidence (aka employee update) has unread messages',
    )
    created_at: datetime.datetime = pydantic.Field(
        description='Date in which incidence (aka employee update) was created',
    )
    is_reopened: bool = pydantic.Field(
        description='Boolean that indicates if the incidence (aka employee update) has been reopened',
    )
    legal_entity_name: str | None = pydantic.Field(default=None, description='Legal entity name')
    employee_first_name: str | None = pydantic.Field(default=None, description='Employee first name')
    employee_last_name: str | None = pydantic.Field(default=None, description='Employee last name')


class BookkeepersManagementEndpoint(Endpoint):
    """Endpoint for bookkeepers management incidences operations."""

    endpoint = '/bookkeepers_management/incidences'

    async def all(self, **kwargs) -> ListApiResponse[BookkeepersManagementIncidence]:
        """Get all incidences records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=BookkeepersManagementIncidence, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[BookkeepersManagementIncidence]:
        """Get incidences with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=BookkeepersManagementIncidence,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, incidence_id: int | str, **kwargs) -> BookkeepersManagementIncidence:
        """Get a specific incidence by ID."""
        data = await self.api.get(self.endpoint, incidence_id, **kwargs)
        return pydantic.TypeAdapter(BookkeepersManagementIncidence).validate_python(data)

    async def update(
        self,
        incidence_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> BookkeepersManagementIncidence:
        """Update an incidence."""
        response = await self.api.put(self.endpoint, incidence_id, json=data, **kwargs)
        return pydantic.TypeAdapter(BookkeepersManagementIncidence).validate_python(response)
