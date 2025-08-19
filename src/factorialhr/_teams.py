import typing
from collections.abc import Mapping, Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Membership(pydantic.BaseModel):
    """Model for teams_membership."""

    id: int = pydantic.Field(description='Membership ID')
    company_id: int | None = pydantic.Field(default=None, description='Company ID of the membership')
    employee_id: int = pydantic.Field(description='Employee ID of the membership')
    team_id: int = pydantic.Field(description='Team ID of the membership')
    lead: bool = pydantic.Field(description='Whether the employee is a lead of the team or not')


class Team(pydantic.BaseModel):
    """Model for teams_team."""

    id: int = pydantic.Field(description='Team ID')
    name: str = pydantic.Field(description='Team name')
    description: str | None = pydantic.Field(default=None, description='Team description')
    avatar: str | None = pydantic.Field(default=None, description='Team avatar URL')
    employee_ids: Sequence[int] | None = pydantic.Field(default=None, description='List of employee IDs in the team')
    lead_ids: Sequence[int] | None = pydantic.Field(default=None, description='List of team lead employee IDs')
    company_id: int = pydantic.Field(description='Company ID')


class MembershipsEndpoint(Endpoint):
    """Endpoint for teams/memberships operations."""

    endpoint = 'teams/memberships'

    async def all(self, **kwargs) -> ListApiResponse[Membership]:
        """Get all memberships records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Membership, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Membership]:
        """Get memberships with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Membership, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, membership_id: int | str, **kwargs) -> Membership:
        """Get a specific team membership by ID."""
        data = await self.api.get(self.endpoint, membership_id, **kwargs)
        return pydantic.TypeAdapter(Membership).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Membership:
        """Create a new membership."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Membership).validate_python(response)

    async def update(self, membership_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Membership:
        """Update a membership."""
        response = await self.api.put(self.endpoint, membership_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Membership).validate_python(response)

    async def delete(self, membership_id: int | str, **kwargs) -> Membership:
        """Delete a membership."""
        response = await self.api.delete(self.endpoint, membership_id, **kwargs)
        return pydantic.TypeAdapter(Membership).validate_python(response)


class TeamsEndpoint(Endpoint):
    """Endpoint for teams/teams operations."""

    endpoint = 'teams/teams'

    async def all(self, **kwargs) -> ListApiResponse[Team]:
        """Get all teams records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Team, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Team]:
        """Get teams with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Team, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, team_id: int | str, **kwargs) -> Team:
        """Get a specific team by ID."""
        data = await self.api.get(self.endpoint, team_id, **kwargs)
        return pydantic.TypeAdapter(Team).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Team:
        """Create a new team."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Team).validate_python(response)

    async def update(self, team_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Team:
        """Update a team."""
        response = await self.api.put(self.endpoint, team_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Team).validate_python(response)

    async def delete(self, team_id: int | str, **kwargs) -> Team:
        """Delete a team."""
        response = await self.api.delete(self.endpoint, team_id, **kwargs)
        return pydantic.TypeAdapter(Team).validate_python(response)
