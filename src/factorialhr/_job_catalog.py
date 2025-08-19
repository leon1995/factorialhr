from collections.abc import Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Jobcataloglevel(pydantic.BaseModel):
    """Model for job_catalog_level."""

    id: int = pydantic.Field(description='Identifier for the job catalog level')
    role_id: int = pydantic.Field(description='Identifier for the job catalog role')
    name: str = pydantic.Field(description='Level name')
    role_name: str = pydantic.Field(description='Role name')
    order: int = pydantic.Field(description='Order of the level')
    archived: bool = pydantic.Field(description='Shows if the role is archived')
    is_default: bool = pydantic.Field(description='Shows if the level is the default one')


class Jobcatalogrole(pydantic.BaseModel):
    """Model for job_catalog_role."""

    id: int = pydantic.Field(description='Identifier for the job catalog role')
    company_id: int = pydantic.Field(description='Identifier for the company')
    name: str = pydantic.Field(description='Role name')
    description: str | None = pydantic.Field(default=None, description='Role description')
    legal_entities_ids: Sequence[int] = pydantic.Field(description='List of legal entities')
    supervisors_ids: Sequence[int] | None = pydantic.Field(default=None, description='List of supervisors')
    competencies_ids: Sequence[int] | None = pydantic.Field(default=None, description='List of competencies')
    archived: bool = pydantic.Field(description='Shows if the role is archived')


class LevelsEndpoint(Endpoint):
    """Endpoint for job_catalog/levels operations."""

    endpoint = 'job_catalog/levels'

    async def all(self, **kwargs) -> ListApiResponse[Jobcataloglevel]:
        """Get all job catalog levels records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Jobcataloglevel, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Jobcataloglevel]:
        """Get job catalog levels with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Jobcataloglevel, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, level_id: int | str, **kwargs) -> Jobcataloglevel:
        """Get a specific job catalog level by ID."""
        data = await self.api.get(self.endpoint, level_id, **kwargs)
        return pydantic.TypeAdapter(Jobcataloglevel).validate_python(data)


class RolesEndpoint(Endpoint):
    """Endpoint for job_catalog/roles operations."""

    endpoint = 'job_catalog/roles'

    async def all(self, **kwargs) -> ListApiResponse[Jobcatalogrole]:
        """Get all job catalog roles records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Jobcatalogrole, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Jobcatalogrole]:
        """Get job catalog roles with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Jobcatalogrole, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, role_id: int | str, **kwargs) -> Jobcatalogrole:
        """Get a specific job catalog role by ID."""
        data = await self.api.get(self.endpoint, role_id, **kwargs)
        return pydantic.TypeAdapter(Jobcatalogrole).validate_python(data)
