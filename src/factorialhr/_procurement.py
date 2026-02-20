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

    #: Unique identifier of the purchase order
    id: int = pydantic.Field(description='Unique identifier of the purchase order')
    #: Purchase order number assigned to this order
    po_number: int = pydantic.Field(description='Purchase order number assigned to this order')
    #: Description or notes about the purchase order
    description: str = pydantic.Field(description='Description or notes about the purchase order')
    #: Current status of the purchase order
    status: PurchaseOrderStatus = pydantic.Field(description='Current status of the purchase order')
    #: Total cost of the purchase order
    cost: Mapping[str, typing.Any] = pydantic.Field(description='Total cost of the purchase order')
    #: Date when the purchase order was created
    date: str = pydantic.Field(description='Date when the purchase order was created')
    #: Identifier of the purchase request that generated this purchase order
    purchase_request_id: int = pydantic.Field(
        description='Identifier of the purchase request that generated this purchase order',
    )
    #: Identifier of the legal entity that owns this purchase order
    legal_entity_id: int = pydantic.Field(description='Identifier of the legal entity that owns this purchase order')
    #: Identifier of the company that owns this purchase order
    company_id: int = pydantic.Field(description='Identifier of the company that owns this purchase order')
    #: Formatted purchase order number with prefix (e.g., PO-00001)
    formatted_po_number: str = pydantic.Field(
        description='Formatted purchase order number with prefix (e.g., PO-00001)',
    )
    #: Identifier of the vendor (contact) associated with this purchase order
    vendor_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the vendor (contact) associated with this purchase order',
    )


class PurchaseOrdersEndpoint(Endpoint):
    """Endpoint for procurement/purchase_orders operations."""

    endpoint = 'procurement/purchase_orders'

    async def all(self, **kwargs) -> ListApiResponse[PurchaseOrder]:
        """Get all purchase orders records.

        Official documentation: `procurement/purchase_orders <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-procurement-purchase-orders>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[PurchaseOrder]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PurchaseOrder, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PurchaseOrder]:
        """Get purchase orders with pagination metadata.

        Official documentation: `procurement/purchase_orders <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-procurement-purchase-orders>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[PurchaseOrder]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PurchaseOrder, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, purchase_order_id: int | str, **kwargs) -> PurchaseOrder:
        """Get a specific purchase order by ID.

        Official documentation: `procurement/purchase_orders <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-procurement-purchase-orders-id>`_

        :param purchase_order_id: The unique identifier.
        :type purchase_order_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: PurchaseOrder
        """
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

    #: Unique identifier of the purchase request
    id: int = pydantic.Field(description='Unique identifier of the purchase request')
    #: Description or notes about the purchase request
    description: str = pydantic.Field(description='Description or notes about the purchase request')
    #: The id of the referred type
    type_id: int = pydantic.Field(description='The id of the referred type')
    #: Total cost of the purchase request
    cost: Mapping[str, typing.Any] = pydantic.Field(description='Total cost of the purchase request')
    #: Date when the purchase request was created
    date: str = pydantic.Field(description='Date when the purchase request was created')
    #: Identifier of the employee who requested this purchase
    requester_employee_id: int = pydantic.Field(description='Identifier of the employee who requested this purchase')
    #: Current status of the purchase request
    status: PurchaseRequestStatus = pydantic.Field(description='Current status of the purchase request')
    #: Identifier of the company that owns this purchase request
    company_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the company that owns this purchase request',
    )
    #: Identifier of the vendor (contact) associated with this purchase request
    vendor_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the vendor (contact) associated with this purchase request',
    )
    #: URL related to the purchase request (e.g., product link)
    url: str | None = pydantic.Field(
        default=None,
        description='URL related to the purchase request (e.g., product link)',
    )
    #: Additional information or notes about the purchase request
    additional_information: str | None = pydantic.Field(
        default=None,
        description='Additional information or notes about the purchase request',
    )
    #: Deadline date for the purchase request
    deadline: datetime.date | None = pydantic.Field(default=None, description='Deadline date for the purchase request')


class PurchaseRequestsEndpoint(Endpoint):
    """Endpoint for procurement/purchase_requests operations."""

    endpoint = 'procurement/purchase_requests'

    async def all(self, **kwargs) -> ListApiResponse[PurchaseRequest]:
        """Get all purchase requests records.

        Official documentation: `procurement/purchase_requests <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-procurement-purchase-requests>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[PurchaseRequest]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PurchaseRequest, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PurchaseRequest]:
        """Get purchase requests with pagination metadata.

        Official documentation: `procurement/purchase_requests <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-procurement-purchase-requests>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[PurchaseRequest]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PurchaseRequest, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, purchase_request_id: int | str, **kwargs) -> PurchaseRequest:
        """Get a specific purchase request by ID.

        Official documentation: `procurement/purchase_requests <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-procurement-purchase-requests-id>`_

        :param purchase_request_id: The unique identifier.
        :type purchase_request_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: PurchaseRequest
        """
        data = await self.api.get(self.endpoint, purchase_request_id, **kwargs)
        return pydantic.TypeAdapter(PurchaseRequest).validate_python(data['data'])


class ProcurementType(pydantic.BaseModel):
    """Model for procurement_type."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: The id of the type
    id: int = pydantic.Field(description='The id of the type')
    #: Identifier of the company that owns this type
    company_id: int = pydantic.Field(description='Identifier of the company that owns this type')
    #: Name of the procurement type
    name: str = pydantic.Field(description='Name of the procurement type')
    #: Time the procurement type was created
    created_at: datetime.datetime = pydantic.Field(description='Time the procurement type was created')
    #: Time the procurement type was last updated
    updated_at: datetime.datetime = pydantic.Field(description='Time the procurement type was last updated')
    #: Employee ID who created this type (null for system types)
    author_id: int | None = pydantic.Field(
        default=None,
        description='Employee ID who created this type (null for system types)',
    )
    #: Description of the procurement type
    description: str | None = pydantic.Field(default=None, description='Description of the procurement type')
    #: Defines if a type is enabled
    enabled: bool | None = pydantic.Field(default=None, description='Defines if a type is enabled')
    #: System identifier for default types
    identifier: str | None = pydantic.Field(default=None, description='System identifier for default types')


class ProcurementTypesEndpoint(Endpoint):
    """Endpoint for procurement/types operations."""

    endpoint = 'procurement/types'

    async def all(self, **kwargs) -> ListApiResponse[ProcurementType]:
        """Get all procurement types records.

        Official documentation: `procurement/types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-procurement-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ProcurementType]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ProcurementType, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ProcurementType]:
        """Get procurement types with pagination metadata.

        Official documentation: `procurement/types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-procurement-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ProcurementType]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ProcurementType, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, type_id: int | str, **kwargs) -> ProcurementType:
        """Get a specific procurement type by ID.

        Official documentation: `procurement/types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-procurement-types-id>`_

        :param type_id: The unique identifier.
        :type type_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ProcurementType
        """
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(ProcurementType).validate_python(data['data'])
