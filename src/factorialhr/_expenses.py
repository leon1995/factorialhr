import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class ExpensableType(StrEnum):
    """Enum for expensable types."""

    EXPENSE = 'expense'
    MILEAGE = 'mileage'
    PERDIEM = 'perdiem'


class ExpenseStatus(StrEnum):
    """Enum for expense status."""

    PENDING = 'pending'
    CHANGES_REQUESTED = 'changes_requested'
    APPROVED = 'approved'
    PAID = 'paid'
    ARCHIVED = 'archived'
    INREVIEW = 'inreview'
    REJECTED = 'rejected'
    REVERSED = 'reversed'
    DRAFT = 'draft'
    IN_PAYROLL = 'in_payroll'
    SENT_TO_PAY = 'sent_to_pay'


class ReimbursementMethod(StrEnum):
    """Enum for reimbursement methods."""

    UNKNOWN = 'unknown'
    SEPA_TRANSFER = 'sepa_transfer'
    PAYROLL = 'payroll'


class CreationType(StrEnum):
    """Enum for creation types."""

    MANUAL = 'manual'
    AUTOMATIC = 'automatic'
    TRAVELPERK = 'travelperk'


class PaymentType(StrEnum):
    """Enum for payment types."""

    REIMBURSABLE = 'reimbursable'
    NOT_REIMBURSABLE = 'not_reimbursable'


class Expensable(pydantic.BaseModel):
    """Model for expenses_expensable."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Unique identifier for the expensable
    id: int = pydantic.Field(description='Unique identifier for the expensable')
    #: Type of the expensable
    type: ExpensableType = pydantic.Field(description='Type of the expensable')
    #: The ID of the company that owns the expensable
    company_id: int = pydantic.Field(description='The ID of the company that owns the expensable')
    #: The ID of the employee that owns the expensable
    employee_id: int = pydantic.Field(description='The ID of the employee that owns the expensable')
    #: The optional ID of the group that the expensable belongs to
    group_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the group that the expensable belongs to',
    )
    #: The optional ID of the legal entity that the expensable belongs to
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the legal entity that the expensable belongs to',
    )
    #: The date and time when the expensable was created
    created_at: datetime.datetime = pydantic.Field(description='The date and time when the expensable was created')
    #: The optional amount in cents
    amount: int | None = pydantic.Field(default=None, description='The optional amount in cents')
    #: The currency code in ISO 4217 format
    currency: str = pydantic.Field(description='The currency code in ISO 4217 format')
    #: The status of the expensable
    status: ExpenseStatus = pydantic.Field(description='The status of the expensable')
    #: The optional description of the expensable
    description: str | None = pydantic.Field(default=None, description='The optional description of the expensable')
    #: The optional ID of the employee that reported the expensable
    reporter_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the employee that reported the expensable',
    )
    #: The optional date and time when the status was last updated
    status_updated_at: datetime.datetime = pydantic.Field(
        description='The optional date and time when the status was last updated',
    )
    #: The optional date and time when the expensable was effective
    effective_on: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The optional date and time when the expensable was effective',
    )
    #: The optional date and time when the expensable was requested for review
    review_request_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The optional date and time when the expensable was requested for review',
    )
    #: The optional date and time when the expensable was set as paid
    paid_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The optional date and time when the expensable was set as paid',
    )
    #: The date and time when the expensable was last updated
    updated_at: datetime.datetime = pydantic.Field(description='The date and time when the expensable was last updated')
    #: The optional reimbursable amount in cents
    reimbursable_amount: int | None = pydantic.Field(
        default=None,
        description='The optional reimbursable amount in cents',
    )
    #: The optional reimbursable currency code in ISO 4217 format
    reimbursable_currency: str | None = pydantic.Field(
        default=None,
        description='The optional reimbursable currency code in ISO 4217 format',
    )
    #: The optional reimbursement method
    reimbursement_method: ReimbursementMethod | None = pydantic.Field(
        default=None,
        description='The optional reimbursement method',
    )
    #: The optional internal reference of the expensable
    internal_reference: str | None = pydantic.Field(
        default=None,
        description='The optional internal reference of the expensable',
    )
    #: The optional ID of the expense that the expensable belongs to
    expense_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the expense that the expensable belongs to',
    )
    #: The optional ID of the mileage that the expensable belongs to
    mileage_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the mileage that the expensable belongs to',
    )
    #: The optional ID of the per_diem that the expensable belongs to
    per_diem_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the per_diem that the expensable belongs to',
    )
    #: The id of the budget
    budget_id: int | None = pydantic.Field(default=None, description='The id of the budget')
    #: The id of the project
    project_id: int | None = pydantic.Field(default=None, description='The id of the project')
    #: The ids of the cost centers
    cost_center_ids: Sequence[int] | None = pydantic.Field(
        default=None,
        description='The ids of the cost centers',
    )


class Expense(pydantic.BaseModel):
    """Model for expenses_expense."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: The id of the expense
    id: int | None = pydantic.Field(default=None, description='The id of the expense')
    #: The id of the expense's owner
    employee_id: int | None = pydantic.Field(default=None, description="The id of the expense's owner")
    #: The id of the expense's company
    company_id: int = pydantic.Field(description="The id of the expense's company")
    #: The id of the card payment
    card_payment_id: int | None = pydantic.Field(default=None, description='The id of the card payment')
    #: The id of the dispute
    dispute_id: int | None = pydantic.Field(default=None, description='The id of the dispute')
    #: The id of the expensable
    expenses_expensable_id: int | None = pydantic.Field(default=None, description='The id of the expensable')
    #: The name of the merchant
    merchant_name: str | None = pydantic.Field(default=None, description='The name of the merchant')
    #: The user merchant of the expense
    user_merchant: str | None = pydantic.Field(default=None, description='The user merchant of the expense')
    #: The tax identification number of the merchant
    merchant_tin: str | None = pydantic.Field(default=None, description='The tax identification number of the merchant')
    #: The category of the expense
    category: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='The category of the expense')
    #: The subcategory of the expense
    subcategory: str | None = pydantic.Field(default=None, description='The subcategory of the expense')
    #: How the expense was created
    creation_type: CreationType = pydantic.Field(description='How the expense was created')
    #: The reference of the expense
    reference: str | None = pydantic.Field(default=None, description='The reference of the expense')
    #: The optional amount in cents
    amount: int | None = pydantic.Field(default=None, description='The optional amount in cents')
    #: The currency of the expense
    currency: str = pydantic.Field(description='The currency of the expense')
    #: The status of the expense
    status: ExpenseStatus = pydantic.Field(description='The status of the expense')
    #: The description of the expense
    description: str | None = pydantic.Field(default=None, description='The description of the expense')
    #: The date when the expense was made
    effective_on: datetime.date = pydantic.Field(description='The date when the expense was made')
    #: The date and time when the expense was reviewed
    review_request_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The date and time when the expense was reviewed',
    )
    #: The date and time when the status was updated
    status_updated_at: datetime.datetime = pydantic.Field(description='The date and time when the status was updated')
    #: The files of the expense
    files: Sequence[typing.Any] = pydantic.Field(description='The files of the expense')
    #: The id of the external authorization
    external_authorization_id: str | None = pydantic.Field(
        default=None,
        description='The id of the external authorization',
    )
    #: The id of the card
    expenses_card_id: int | None = pydantic.Field(default=None, description='The id of the card')
    #: The card of the expense
    card: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='The card of the expense')
    #: The id of the document
    document_id: int | None = pydantic.Field(default=None, description='The id of the document')
    #: The signed document of the expense
    signed_document: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The signed document of the expense',
    )
    #: The access token of the expense
    access_token: str | None = pydantic.Field(default=None, description='The access token of the expense')
    #: The date and time when the expense was paid
    paid_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The date and time when the expense was paid',
    )
    #: Number of the financial document associated to the expense
    document_number: str | None = pydantic.Field(
        default=None,
        description='Number of the financial document associated to the expense',
    )
    #: Type of the financial document associated to the expense
    document_type: str | None = pydantic.Field(
        default=None,
        description='Type of the financial document associated to the expense',
    )
    #: The payment of the expense
    payment: PaymentType | None = pydantic.Field(default=None, description='The payment of the expense')
    #: The method of the payment
    payment_method: str | None = pydantic.Field(default=None, description='The method of the payment')
    #: The exchange rate of the payment
    exchange_rate: float | None = pydantic.Field(default=None, description='The exchange rate of the payment')
    #: The currency of the reimbursable amount
    reimbursable_currency: str | None = pydantic.Field(
        default=None,
        description='The currency of the reimbursable amount',
    )
    #: The optional reimbursable amount in cents
    reimbursable_amount: int | None = pydantic.Field(
        default=None,
        description='The optional reimbursable amount in cents',
    )
    #: The taxes of the expense
    taxes: Sequence[typing.Any] = pydantic.Field(description='The taxes of the expense')
    #: The id of the category
    category_id: int | None = pydantic.Field(default=None, description='The id of the category')
    #: The id of the ledger account
    ledger_account_id: int | None = pydantic.Field(default=None, description='The id of the ledger account')
    #: The id of the budget associated with this expense
    budget_id: int | None = pydantic.Field(
        default=None,
        description='The id of the budget associated with this expense',
    )
    #: The id of the project associated with this expense
    project_id: int | None = pydantic.Field(
        default=None,
        description='The id of the project associated with this expense',
    )
    #: Array of cost center ids associated with this expense
    cost_center_ids: Sequence[int] | None = pydantic.Field(
        default=None,
        description='Array of cost center ids associated with this expense',
    )


class Mileage(pydantic.BaseModel):
    """Model for expenses_mileage."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Mileage identifier
    id: int = pydantic.Field(description='Mileage identifier')
    #: Employee identifier
    employee_id: int | None = pydantic.Field(default=None, description='Employee identifier')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Expensable identifier
    expenses_expensable_id: int | None = pydantic.Field(default=None, description='Expensable identifier')
    #: The category of the mileage
    category: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='The category of the mileage')
    #: The subcategory of the mileage
    subcategory: str | None = pydantic.Field(default=None, description='The subcategory of the mileage')
    #: The id of the category
    category_id: int | None = pydantic.Field(default=None, description='The id of the category')
    #: The amount in cents
    amount: int | None = pydantic.Field(default=None, description='The amount in cents')
    #: The currency code
    currency: str = pydantic.Field(description='The currency code')
    #: The amount to be reimbursed for the mileage in cents
    reimbursable_amount: int | None = pydantic.Field(
        default=None,
        description='The amount to be reimbursed for the mileage in cents',
    )
    #: The currency for the reimbursable amount
    reimbursable_currency: str | None = pydantic.Field(
        default=None,
        description='The currency for the reimbursable amount',
    )
    #: The status of the mileage
    status: ExpenseStatus = pydantic.Field(description='The status of the mileage')
    #: The mileage distance
    mileage: int | None = pydantic.Field(default=None, description='The mileage distance')
    #: The units of measurement
    units: str | None = pydantic.Field(default=None, description='The units of measurement')
    #: The rate information
    rate: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='The rate information')
    #: The origin location
    from_location: str | None = pydantic.Field(default=None, alias='from', description='The origin location')
    #: The destination location
    to_location: str | None = pydantic.Field(default=None, alias='to', description='The destination location')
    #: The description of the mileage
    description: str | None = pydantic.Field(default=None, description='The description of the mileage')
    #: The effective date
    effective_on: datetime.date | None = pydantic.Field(default=None, description='The effective date')
    #: The review request date
    review_request_at: datetime.datetime | None = pydantic.Field(default=None, description='The review request date')
    #: The files attached to the mileage
    files: Sequence[typing.Any] = pydantic.Field(description='The files attached to the mileage')
    #: The date when paid
    paid_at: datetime.datetime | None = pydantic.Field(default=None, description='The date when paid')
    #: The payment type
    payment: PaymentType = pydantic.Field(description='The payment type')
    #: The ledger account identifier
    ledger_account_id: int | None = pydantic.Field(default=None, description='The ledger account identifier')
    #: Indicates if the mileage is a round trip
    round_trip: bool | None = pydantic.Field(default=None, description='Indicates if the mileage is a round trip')
    #: The longitude of the origin of the mileage
    origin_longitude: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The longitude of the origin of the mileage',
    )
    #: The latitude of the origin of the mileage
    origin_latitude: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The latitude of the origin of the mileage',
    )
    #: The longitude of the destination of the mileage
    destination_longitude: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The longitude of the destination of the mileage',
    )
    #: The latitude of the destination of the mileage
    destination_latitude: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The latitude of the destination of the mileage',
    )
    #: The calculated mileage between origin and destination in decameters/10-milers
    calculated_mileage: int | None = pydantic.Field(
        default=None,
        description='The calculated mileage between origin and destination in decameters/10-milers',
    )
    #: The id of the budget associated with this mileage
    budget_id: int | None = pydantic.Field(
        default=None,
        description='The id of the budget associated with this mileage',
    )
    #: The id of the project associated with this mileage
    project_id: int | None = pydantic.Field(
        default=None,
        description='The id of the project associated with this mileage',
    )
    #: Array of cost center ids associated with this mileage
    cost_center_ids: Sequence[int] | None = pydantic.Field(
        default=None,
        description='Array of cost center ids associated with this mileage',
    )


class PerDiem(pydantic.BaseModel):
    """Model for expenses_per_diem."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: The ID of the per diem
    id: int = pydantic.Field(description='The ID of the per diem')
    #: The ID of the employee the per diem is for
    employee_id: int | None = pydantic.Field(default=None, description='The ID of the employee the per diem is for')
    #: The ID of the company the per diem is for
    company_id: int = pydantic.Field(description='The ID of the company the per diem is for')
    #: The ID of the expensable the per diem is for
    expenses_expensable_id: int | None = pydantic.Field(
        default=None,
        description='The ID of the expensable the per diem is for',
    )
    #: The end date of the per diem
    end_date: datetime.date | None = pydantic.Field(default=None, description='The end date of the per diem')
    #: The start date of the per diem
    start_date: datetime.date | None = pydantic.Field(default=None, description='The start date of the per diem')
    #: The location the per diem is from
    from_location: str | None = pydantic.Field(
        default=None,
        alias='from',
        description='The location the per diem is from',
    )
    #: The location the per diem is to
    to_location: str | None = pydantic.Field(default=None, alias='to', description='The location the per diem is to')
    #: The ID of the ledger account the per diem is for
    ledger_account_id: int | None = pydantic.Field(
        default=None,
        description='The ID of the ledger account the per diem is for',
    )
    #: The amount of the per diem
    amount: int | None = pydantic.Field(default=None, description='The amount of the per diem')
    #: The currency for the reimbursable amount
    currency: str = pydantic.Field(description='The currency for the reimbursable amount')
    #: The amount to be reimbursed by the per diem in cents
    reimbursable_amount: int | None = pydantic.Field(
        default=None,
        description='The amount to be reimbursed by the per diem in cents',
    )
    #: The currency for the reimbursable amount
    reimbursable_currency: str | None = pydantic.Field(
        default=None,
        description='The currency for the reimbursable amount',
    )
    #: The payment method for the per diem
    payment: PaymentType = pydantic.Field(description='The payment method for the per diem')
    #: The date the per diem was paid
    paid_at: datetime.date | None = pydantic.Field(default=None, description='The date the per diem was paid')
    #: The files attached to the per diem
    files: Sequence[typing.Any] = pydantic.Field(description='The files attached to the per diem')
    #: The date the per diem was requested for review
    review_request_at: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the per diem was requested for review',
    )
    #: The date the per diem is effective on
    effective_on: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the per diem is effective on',
    )
    #: The description of the per diem
    description: str | None = pydantic.Field(default=None, description='The description of the per diem')
    #: The id of the budget associated with this per diem
    budget_id: int | None = pydantic.Field(
        default=None,
        description='The id of the budget associated with this per diem',
    )
    #: The id of the project associated with this per diem
    project_id: int | None = pydantic.Field(
        default=None,
        description='The id of the project associated with this per diem',
    )
    #: Array of cost center ids associated with this per diem
    cost_center_ids: Sequence[int] | None = pydantic.Field(
        default=None,
        description='Array of cost center ids associated with this per diem',
    )
    #: The category of the per diem
    category: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='The category of the per diem')
    #: The subcategory of the per diem
    subcategory: str | None = pydantic.Field(default=None, description='The subcategory of the per diem')
    #: The status of the per diem
    status: ExpenseStatus = pydantic.Field(description='The status of the per diem')
    #: The rates for the per diem
    rates: Sequence[typing.Any] = pydantic.Field(description='The rates for the per diem')


class ExpensablesEndpoint(Endpoint):
    """Endpoint for expenses/expensables operations."""

    endpoint = 'expenses/expensables'

    async def all(self, **kwargs) -> ListApiResponse[Expensable]:
        """Get all expensables records.

        Official documentation: `expenses/expensables <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-expensables>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Expensable]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Expensable)

    async def get(self, **kwargs) -> MetaApiResponse[Expensable]:
        """Get expensables with pagination metadata.

        Official documentation: `expenses/expensables <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-expensables>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Expensable]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Expensable)

    async def get_by_id(self, expensable_id: int | str, **kwargs) -> Expensable:
        """Get a specific expensable by ID.

        Official documentation: `expenses/expensables <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-expensables>`_

        :param expensable_id: The unique identifier.
        :type expensable_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Expensable
        """
        data = await self.api.get(self.endpoint, expensable_id, **kwargs)
        return pydantic.TypeAdapter(Expensable).validate_python(data)

    async def bulk_set_to_paid(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[Expensable]:
        """Bulk set expensables to paid status.

        Official documentation: `expenses/expensables <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-expensables>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[Expensable]
        """
        response = await self.api.post(self.endpoint, 'bulk_set_to_paid', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Expensable]).validate_python(response)


class ExpensesEndpoint(Endpoint):
    """Endpoint for expenses/expenses operations."""

    endpoint = 'expenses/expenses'

    async def all(self, **kwargs) -> ListApiResponse[Expense]:
        """Get all expenses records.

        Official documentation: `expenses/expenses <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-expenses>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Expense]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Expense)

    async def get(self, **kwargs) -> MetaApiResponse[Expense]:
        """Get expenses with pagination metadata.

        Official documentation: `expenses/expenses <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-expenses>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Expense]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Expense)

    async def get_by_id(self, expense_id: int | str, **kwargs) -> Expense:
        """Get a specific expense by ID.

        Official documentation: `expenses/expenses <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-expenses>`_

        :param expense_id: The unique identifier.
        :type expense_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Expense
        """
        data = await self.api.get(self.endpoint, expense_id, **kwargs)
        return pydantic.TypeAdapter(Expense).validate_python(data)


class MileagesEndpoint(Endpoint):
    """Endpoint for expenses/mileages operations."""

    endpoint = 'expenses/mileages'

    async def all(self, **kwargs) -> ListApiResponse[Mileage]:
        """Get all mileages records.

        Official documentation: `expenses/mileages <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-mileages>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Mileage]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Mileage)

    async def get(self, **kwargs) -> MetaApiResponse[Mileage]:
        """Get mileages with pagination metadata.

        Official documentation: `expenses/mileages <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-mileages>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Mileage]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Mileage)

    async def get_by_id(self, mileage_id: int | str, **kwargs) -> Mileage:
        """Get a specific mileage by ID.

        Official documentation: `expenses/mileages <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-mileages>`_

        :param mileage_id: The unique identifier.
        :type mileage_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Mileage
        """
        data = await self.api.get(self.endpoint, mileage_id, **kwargs)
        return pydantic.TypeAdapter(Mileage).validate_python(data)


class PerDiemsEndpoint(Endpoint):
    """Endpoint for expenses/per_diems operations."""

    endpoint = 'expenses/per_diems'

    async def all(self, **kwargs) -> ListApiResponse[PerDiem]:
        """Get all per diems records.

        Official documentation: `expenses/per_diems <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-per-diems>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[PerDiem]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=PerDiem)

    async def get(self, **kwargs) -> MetaApiResponse[PerDiem]:
        """Get per diems with pagination metadata.

        Official documentation: `expenses/per_diems <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-per-diems>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[PerDiem]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=PerDiem)

    async def get_by_id(self, per_diem_id: int | str, **kwargs) -> PerDiem:
        """Get a specific per diem by ID.

        Official documentation: `expenses/per_diems <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-expenses-per-diems>`_

        :param per_diem_id: The unique identifier.
        :type per_diem_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: PerDiem
        """
        data = await self.api.get(self.endpoint, per_diem_id, **kwargs)
        return pydantic.TypeAdapter(PerDiem).validate_python(data)
