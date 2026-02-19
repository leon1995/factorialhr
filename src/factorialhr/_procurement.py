import datetime
import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class PurchaseOrderStatus(StrEnum):
    """Enum for purchase order statuses."""

    DRAFT = 'draft'
    PENDING = 'pending'
    ORDERED = 'ordered'
    RECEIVED = 'received'
    PARTIAL = 'partial'
    CLOSED = 'closed'


class PurchaseOrder(pydantic.BaseModel):
    """Model for procurement_purchase_order."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='Unique identifier of the purchase order')
    po_number: int = pydantic.Field(description='Purchase order number assigned to this order')
    description: str = pydantic.Field(description='Description or notes about the purchase order')
    status: PurchaseOrderStatus = pydantic.Field(description='Current status of the purchase order')
    cost: Mapping[str, typing.Any] = pydantic.Field(description='Total cost of the purchase order')
    date: str = pydantic.Field(description='Date when the purchase order was created')
    purchase_request_id: int = pydantic.Field(
        description='Identifier of the purchase request that generated this purchase order',
    )
    legal_entity_id: int = pydantic.Field(description='Identifier of the legal entity that owns this purchase order')
    company_id: int = pydantic.Field(description='Identifier of the company that owns this purchase order')
    formatted_po_number: str = pydantic.Field(
        description='Formatted purchase order number with prefix (e.g., PO-00001)',
    )
    vendor_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the vendor (contact) associated with this purchase order',
    )


class PurchaseOrdersEndpoint(Endpoint):
    """Endpoint for procurement/purchase_orders operations."""

    endpoint = 'procurement/purchase_orders'

    async def all(self, **kwargs) -> ListApiResponse[PurchaseOrder]:
        """Get all purchase orders records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PurchaseOrder, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PurchaseOrder]:
        """Get purchase orders with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PurchaseOrder, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, purchase_order_id: int | str, **kwargs) -> PurchaseOrder:
        """Get a specific purchase order by ID."""
        data = await self.api.get(self.endpoint, purchase_order_id, **kwargs)
        return pydantic.TypeAdapter(PurchaseOrder).validate_python(data['data'])


class PurchaseRequestStatus(StrEnum):
    """Enum for purchase request statuses."""

    DRAFT = 'draft'
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    CHANGES_REQUESTED = 'changes_requested'


class PurchaseRequest(pydantic.BaseModel):
    """Model for procurement_purchase_request."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='Unique identifier of the purchase request')
    description: str = pydantic.Field(description='Description or notes about the purchase request')
    type_id: int = pydantic.Field(description='The id of the referred type')
    cost: Mapping[str, typing.Any] = pydantic.Field(description='Total cost of the purchase request')
    date: str = pydantic.Field(description='Date when the purchase request was created')
    requester_employee_id: int = pydantic.Field(description='Identifier of the employee who requested this purchase')
    status: PurchaseRequestStatus = pydantic.Field(description='Current status of the purchase request')
    company_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the company that owns this purchase request',
    )
    vendor_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the vendor (contact) associated with this purchase request',
    )
    url: str | None = pydantic.Field(
        default=None,
        description='URL related to the purchase request (e.g., product link)',
    )
    additional_information: str | None = pydantic.Field(
        default=None,
        description='Additional information or notes about the purchase request',
    )
    deadline: datetime.date | None = pydantic.Field(default=None, description='Deadline date for the purchase request')


class PurchaseRequestsEndpoint(Endpoint):
    """Endpoint for procurement/purchase_requests operations."""

    endpoint = 'procurement/purchase_requests'

    async def all(self, **kwargs) -> ListApiResponse[PurchaseRequest]:
        """Get all purchase requests records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PurchaseRequest, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PurchaseRequest]:
        """Get purchase requests with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PurchaseRequest, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, purchase_request_id: int | str, **kwargs) -> PurchaseRequest:
        """Get a specific purchase request by ID."""
        data = await self.api.get(self.endpoint, purchase_request_id, **kwargs)
        return pydantic.TypeAdapter(PurchaseRequest).validate_python(data['data'])


class ProcurementType(pydantic.BaseModel):
    """Model for procurement_type."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='The id of the type')
    company_id: int = pydantic.Field(description='Identifier of the company that owns this type')
    name: str = pydantic.Field(description='Name of the procurement type')
    created_at: datetime.datetime = pydantic.Field(description='Time the procurement type was created')
    updated_at: datetime.datetime = pydantic.Field(description='Time the procurement type was last updated')
    author_id: int | None = pydantic.Field(
        default=None,
        description='Employee ID who created this type (null for system types)',
    )
    description: str | None = pydantic.Field(default=None, description='Description of the procurement type')
    enabled: bool | None = pydantic.Field(default=None, description='Defines if a type is enabled')
    identifier: str | None = pydantic.Field(default=None, description='System identifier for default types')


class ProcurementTypesEndpoint(Endpoint):
    """Endpoint for procurement/types operations."""

    endpoint = 'procurement/types'

    async def all(self, **kwargs) -> ListApiResponse[ProcurementType]:
        """Get all procurement types records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ProcurementType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ProcurementType]:
        """Get procurement types with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ProcurementType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> ProcurementType:
        """Get a specific procurement type by ID."""
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(ProcurementType).validate_python(data['data'])
