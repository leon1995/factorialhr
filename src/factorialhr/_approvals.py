import datetime
import typing
from collections.abc import Mapping, Sequence

import pydantic

from factorialhr._client import Endpoint


class MaterializedApprovalsFlow(pydantic.BaseModel):
    """Model for approvals_materialized_approvals_flow."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Materialized approvals flow identifier
    id: int = pydantic.Field(description='Materialized approvals flow identifier')
    #: Author identifier
    author_id: int | None = pydantic.Field(default=None, description='Author identifier')
    #: Author employee identifier
    author_employee_id: int | None = pydantic.Field(default=None, description='Author employee identifier')
    #: Owner identifier
    owner_id: int | None = pydantic.Field(default=None, description='Owner identifier')
    #: Owner employee identifier
    owner_employee_id: int | None = pydantic.Field(default=None, description='Owner employee identifier')
    #: Type of the resource (e.g. Timeoff::Leave)
    resource_type: str | None = pydantic.Field(default=None, description='Type of the resource (e.g. Timeoff::Leave)')
    #: Id of the resource
    resource_id: int | None = pydantic.Field(default=None, description='Id of the resource')
    #: URL of the resource
    resource_url: str | None = pydantic.Field(default=None, description='URL of the resource')
    #: Status of the approval flow
    status: str | None = pydantic.Field(default=None, description='Status of the approval flow')
    #: Expiration timestamp
    expires_at: datetime.datetime | None = pydantic.Field(default=None, description='Expiration timestamp')
    #: Final decision timestamp
    final_decision_at: datetime.datetime | None = pydantic.Field(default=None, description='Final decision timestamp')
    #: Approval flow identifier
    approval_flow_id: int | None = pydantic.Field(default=None, description='Approval flow identifier')
    #: List of approvers
    approvers: Sequence[typing.Any] = pydantic.Field(default_factory=list, description='List of approvers')
    #: Email detail blocks
    email_detail_blocks: Sequence[typing.Any] = pydantic.Field(
        default_factory=list,
        description='Email detail blocks',
    )
    #: Override approver identifier
    override_approver_id: int | None = pydantic.Field(default=None, description='Override approver identifier')
    #: Override approver employee identifier
    override_approver_employee_id: int | None = pydantic.Field(
        default=None,
        description='Override approver employee identifier',
    )
    #: Rules decision
    rules_decision: str | None = pydantic.Field(default=None, description='Rules decision')
    #: Auto approval description
    auto_approval_description: str | None = pydantic.Field(default=None, description='Auto approval description')
    #: Action type
    action_type: str | None = pydantic.Field(default=None, description='Action type')
    #: Reason for rejection
    reason: str | None = pydantic.Field(default=None, description='Reason for rejection')


class MaterializedApprovalsFlowsEndpoint(Endpoint):
    """Endpoint for approvals/materialized_approvals_flows operations."""

    endpoint = 'approvals/materialized_approvals_flows'

    async def approve_resource(self, data: Mapping[str, typing.Any], **kwargs) -> MaterializedApprovalsFlow:
        """Approve resources in a materialized approvals flow.

        Official documentation: `approvals/materialized_approvals_flows <https://apidoc.factorialhr.com/reference/post_api-2026-04-01-resources-approvals-materialized-approvals-flows-approve-resource>`_

        :param data: Payload with ``resource_id`` and ``resource_type`` (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated approval flow.
        :rtype: MaterializedApprovalsFlow
        """
        response = await self.api.post(self.endpoint, 'approve_resource', json=data, **kwargs)
        return pydantic.TypeAdapter(MaterializedApprovalsFlow).validate_python(response['data'])

    async def reject_resource(self, data: Mapping[str, typing.Any], **kwargs) -> MaterializedApprovalsFlow:
        """Reject resources in a materialized approvals flow.

        Official documentation: `approvals/materialized_approvals_flows <https://apidoc.factorialhr.com/reference/post_api-2026-04-01-resources-approvals-materialized-approvals-flows-reject-resource>`_

        :param data: Payload with ``resource_id``, ``resource_type``, and optional ``reason`` (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated approval flow.
        :rtype: MaterializedApprovalsFlow
        """
        response = await self.api.post(self.endpoint, 'reject_resource', json=data, **kwargs)
        return pydantic.TypeAdapter(MaterializedApprovalsFlow).validate_python(response['data'])
