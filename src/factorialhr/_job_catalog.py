from enum import StrEnum
import datetime
import typing
from collections.abc import Sequence

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Jobcataloglevel(pydantic.BaseModel):
    """Model for job_catalog_level."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='Identifier for the job catalog level')
    role_id: int = pydantic.Field(description='Identifier for the job catalog role')
    name: str = pydantic.Field(description='Level name')
    role_name: str = pydantic.Field(description='Role name')
    order: int = pydantic.Field(description='Order of the level')
    archived: bool = pydantic.Field(description='Shows if the role is archived')
    is_default: bool = pydantic.Field(description='Shows if the level is the default one')


class Jobcatalogrole(pydantic.BaseModel):
    """Model for job_catalog_role."""

    model_config = pydantic.ConfigDict(frozen=True)

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


class NodeAttribute(pydantic.BaseModel):
    """Model for job_catalog_node_attribute. JobCatalog Node Attributes."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='Node attribute identifier')
    type: str = pydantic.Field(description='Type of the attribute')
    attribute_id: int = pydantic.Field(description='Attribute identifier')
    value_competency: typing.Any | None = pydantic.Field(default=None, description='Value when type is competency')
    value_it_management_asset: typing.Any | None = pydantic.Field(default=None, description='Value when type is it_management_asset')
    value_salary_range: typing.Any | None = pydantic.Field(default=None, description='Value when type is salary_range')
    value_working_conditions: typing.Any | None = pydantic.Field(default=None, description='Value when type is working_conditions')


class NodeAttributesEndpoint(Endpoint):
    """Endpoint for job_catalog/node_attributes operations."""

    endpoint = 'job_catalog/node_attributes'

    async def all(self, **kwargs) -> ListApiResponse[NodeAttribute]:
        """Get all node attributes."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=NodeAttribute, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[NodeAttribute]:
        """Get node attributes with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=NodeAttribute, raw_meta=response['meta'], raw_data=response['data'])


class JobCatalogNodeType(StrEnum):
    """Enum for job catalog node types."""

    ROOT = 'jobcatalog_treeroot'
    FAMILY = 'jobcatalog_treefamily'
    FUNCTION = 'jobcatalog_treefunction'
    ROLE = 'jobcatalog_treerole'
    LEVEL = 'jobcatalog_treelevel'

class JobCatalogNode(pydantic.BaseModel):
    """Model for job_catalog_node. JobCatalog Tree Node."""

    model_config = pydantic.ConfigDict(frozen=True)

    type: JobCatalogNodeType = pydantic.Field(description='Node type')
    uuid: str = pydantic.Field(description='Node UUID')
    ancestor_uuid: str | None = pydantic.Field(default=None, description='Parent node UUID')
    name: str = pydantic.Field(description='Node name')
    description: str | None = pydantic.Field(default=None, description='Description')
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')
    full_path_to_root: Sequence[str] | None = pydantic.Field(default=None, description='Full path from root to this node')
    job_catalog_title: str | None = pydantic.Field(
        default=None,
        description='Full title that represents the job position',
    )


class TreeNodesEndpoint(Endpoint):
    """Endpoint for job_catalog/tree_nodes operations."""

    endpoint = 'job_catalog/tree_nodes'

    async def all(self, **kwargs) -> ListApiResponse[JobCatalogNode]:
        """Get all tree nodes."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=JobCatalogNode, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[JobCatalogNode]:
        """Get tree nodes with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=JobCatalogNode, raw_meta=response['meta'], raw_data=response['data'])
