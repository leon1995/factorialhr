import datetime
import typing
from collections.abc import Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Jobcataloglevel(pydantic.BaseModel):
    """Model for job_catalog_level."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier for the job catalog level
    id: int = pydantic.Field(description='Identifier for the job catalog level')
    #: Identifier for the job catalog role
    role_id: int = pydantic.Field(description='Identifier for the job catalog role')
    #: Level name
    name: str = pydantic.Field(description='Level name')
    #: Role name
    role_name: str = pydantic.Field(description='Role name')
    #: Order of the level
    order: int = pydantic.Field(description='Order of the level')
    #: Shows if the role is archived
    archived: bool = pydantic.Field(description='Shows if the role is archived')
    #: Shows if the level is the default one
    is_default: bool = pydantic.Field(description='Shows if the level is the default one')


class Jobcatalogrole(pydantic.BaseModel):
    """Model for job_catalog_role."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier for the job catalog role
    id: int = pydantic.Field(description='Identifier for the job catalog role')
    #: Identifier for the company
    company_id: int = pydantic.Field(description='Identifier for the company')
    #: Role name
    name: str = pydantic.Field(description='Role name')
    #: Role description
    description: str | None = pydantic.Field(default=None, description='Role description')
    #: List of legal entities
    legal_entities_ids: Sequence[int] = pydantic.Field(description='List of legal entities')
    #: List of supervisors
    supervisors_ids: Sequence[int] | None = pydantic.Field(default=None, description='List of supervisors')
    #: List of competencies
    competencies_ids: Sequence[int] | None = pydantic.Field(default=None, description='List of competencies')
    #: Shows if the role is archived
    archived: bool = pydantic.Field(description='Shows if the role is archived')


class LevelsEndpoint(Endpoint):
    """Endpoint for job_catalog/levels operations."""

    endpoint = 'job_catalog/levels'

    async def all(self, **kwargs) -> ListApiResponse[Jobcataloglevel]:
        """Get all job catalog levels records.

        Official documentation: `job_catalog/levels <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-job-catalog-levels>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Jobcataloglevel]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Jobcataloglevel, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Jobcataloglevel]:
        """Get job catalog levels with pagination metadata.

        Official documentation: `job_catalog/levels <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-job-catalog-levels>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Jobcataloglevel]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Jobcataloglevel, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, level_id: int | str, **kwargs) -> Jobcataloglevel:
        """Get a specific job catalog level by ID.

        Official documentation: `job_catalog/levels <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-job-catalog-levels-id>`_

        :param level_id: The unique identifier.
        :type level_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Jobcataloglevel
        """
        data = await self.api.get(self.endpoint, level_id, **kwargs)
        return pydantic.TypeAdapter(Jobcataloglevel).validate_python(data)


class RolesEndpoint(Endpoint):
    """Endpoint for job_catalog/roles operations."""

    endpoint = 'job_catalog/roles'

    async def all(self, **kwargs) -> ListApiResponse[Jobcatalogrole]:
        """Get all job catalog roles records.

        Official documentation: `job_catalog/roles <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-job-catalog-roles>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Jobcatalogrole]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Jobcatalogrole, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Jobcatalogrole]:
        """Get job catalog roles with pagination metadata.

        Official documentation: `job_catalog/roles <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-job-catalog-roles>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Jobcatalogrole]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Jobcatalogrole, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, role_id: int | str, **kwargs) -> Jobcatalogrole:
        """Get a specific job catalog role by ID.

        Official documentation: `job_catalog/roles <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-job-catalog-roles-id>`_

        :param role_id: The unique identifier.
        :type role_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Jobcatalogrole
        """
        data = await self.api.get(self.endpoint, role_id, **kwargs)
        return pydantic.TypeAdapter(Jobcatalogrole).validate_python(data)


class NodeAttribute(pydantic.BaseModel):
    """Model for job_catalog_node_attribute. JobCatalog Node Attributes."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Node attribute identifier
    id: int = pydantic.Field(description='Node attribute identifier')
    #: Type of the attribute
    type: str = pydantic.Field(description='Type of the attribute')
    #: Attribute identifier
    attribute_id: int = pydantic.Field(description='Attribute identifier')
    #: Value when type is competency
    value_competency: typing.Any | None = pydantic.Field(default=None, description='Value when type is competency')
    #: Value when type is it_management_asset
    value_it_management_asset: typing.Any | None = pydantic.Field(
        default=None,
        description='Value when type is it_management_asset',
    )
    #: Value when type is salary_range
    value_salary_range: typing.Any | None = pydantic.Field(default=None, description='Value when type is salary_range')
    #: Value when type is working_conditions
    value_working_conditions: typing.Any | None = pydantic.Field(
        default=None,
        description='Value when type is working_conditions',
    )


class NodeAttributesEndpoint(Endpoint):
    """Endpoint for job_catalog/node_attributes operations."""

    endpoint = 'job_catalog/node_attributes'

    async def all(self, **kwargs) -> ListApiResponse[NodeAttribute]:
        """Get all node attributes.

        Official documentation: `job_catalog/node_attributes <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-job-catalog-node-attributes>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[NodeAttribute]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=NodeAttribute, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[NodeAttribute]:
        """Get node attributes with pagination metadata.

        Official documentation: `job_catalog/node_attributes <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-job-catalog-node-attributes>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[NodeAttribute]
        """
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

    #: Node type
    type: JobCatalogNodeType = pydantic.Field(description='Node type')
    #: Node UUID
    uuid: str = pydantic.Field(description='Node UUID')
    #: Parent node UUID
    ancestor_uuid: str | None = pydantic.Field(default=None, description='Parent node UUID')
    #: Node name
    name: str = pydantic.Field(description='Node name')
    #: Description
    description: str | None = pydantic.Field(default=None, description='Description')
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')
    #: Full path from root to this node
    full_path_to_root: Sequence[str] | None = pydantic.Field(
        default=None,
        description='Full path from root to this node',
    )
    #: Full title that represents the job position
    job_catalog_title: str | None = pydantic.Field(
        default=None,
        description='Full title that represents the job position',
    )


class TreeNodesEndpoint(Endpoint):
    """Endpoint for job_catalog/tree_nodes operations."""

    endpoint = 'job_catalog/tree_nodes'

    async def all(self, **kwargs) -> ListApiResponse[JobCatalogNode]:
        """Get all tree nodes.

        Official documentation: `job_catalog/tree_nodes <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-job-catalog-tree-nodes>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[JobCatalogNode]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=JobCatalogNode, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[JobCatalogNode]:
        """Get tree nodes with pagination metadata.

        Official documentation: `job_catalog/tree_nodes <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-job-catalog-tree-nodes>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[JobCatalogNode]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=JobCatalogNode, raw_meta=response['meta'], raw_data=response['data'])
