import typing

import pydantic

from factorialhr import _common
from factorialhr._client import Endpoint


class Membership(pydantic.BaseModel):
    id: int
    company_id: int | None
    employee_id: int
    team_id: int
    lead: bool


class _MembershipRoot(pydantic.RootModel):
    root: list[Membership]


class MembershipEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/teams/memberships'

    async def all(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        lead: bool | None = None,
        team_ids: typing.Sequence[int] | None = None,
        employee_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> list[Membership]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-teams-memberships."""
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'lead': lead,
                'team_ids[]': team_ids,
                'employee_ids[]': employee_ids,
            },
        )
        return _MembershipRoot.model_validate(
            await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, membership_id: int, **kwargs) -> Membership: ...

    @typing.overload
    async def get(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        lead: bool | None = None,
        team_ids: typing.Sequence[int] | None = None,
        employee_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> tuple[list[Membership], _common.Meta]: ...
    async def get(
        self,
        *,
        membership_id: int | None = None,
        ids: typing.Sequence[int] | None = None,
        lead: bool | None = None,
        team_ids: typing.Sequence[int] | None = None,
        employee_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-teams-memberships-id."""
        if membership_id is not None:
            return Membership.model_validate(await self.api.get(self.endpoint, membership_id, **kwargs))
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'lead': lead,
                'team_ids[]': team_ids,
                'employee_ids[]': employee_ids,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _MembershipRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class Team(pydantic.BaseModel):
    id: int
    name: str
    description: str | None
    avatar: str | None
    employee_ids: list[int] | None
    lead_ids: list[int] | None
    company_id: int


class _TeamRoot(pydantic.RootModel):
    root: list[Team]


class TeamEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/teams/teams'

    async def all(self, *, ids: typing.Sequence[int] | None = None, **kwargs) -> list[Team]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-teams-teams."""
        params = kwargs.get('params', {})
        params.update({'ids[]': ids})
        return _TeamRoot.model_validate(
            await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, team_id: int, **kwargs) -> Team: ...

    @typing.overload
    async def get(self, *, ids: typing.Sequence[int] | None = None, **kwargs) -> tuple[list[Team], _common.Meta]: ...

    async def get(self, *, team_id: int | None = None, ids: typing.Sequence[int] | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-teams-teams-id."""
        if team_id is not None:
            return Team.model_validate(await self.api.get(self.endpoint, team_id, **kwargs))
        params = kwargs.get('params', {})
        params.update({'ids[]': ids})
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _TeamRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])
