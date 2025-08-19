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

    id: int = pydantic.Field(description='Unique identifier for the expensable')
    type: ExpensableType = pydantic.Field(description='Type of the expensable')
    company_id: int = pydantic.Field(description='The ID of the company that owns the expensable')
    employee_id: int = pydantic.Field(description='The ID of the employee that owns the expensable')
    group_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the group that the expensable belongs to',
    )
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the legal entity that the expensable belongs to',
    )
    created_at: datetime.datetime = pydantic.Field(description='The date and time when the expensable was created')
    amount: int | None = pydantic.Field(default=None, description='The optional amount in cents')
    currency: str = pydantic.Field(description='The currency code in ISO 4217 format')
    status: ExpenseStatus = pydantic.Field(description='The status of the expensable')
    description: str | None = pydantic.Field(default=None, description='The optional description of the expensable')
    reporter_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the employee that reported the expensable',
    )
    status_updated_at: datetime.datetime = pydantic.Field(
        description='The optional date and time when the status was last updated',
    )
    effective_on: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The optional date and time when the expensable was effective',
    )
    review_request_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The optional date and time when the expensable was requested for review',
    )
    paid_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The optional date and time when the expensable was set as paid',
    )
    updated_at: datetime.datetime = pydantic.Field(description='The date and time when the expensable was last updated')
    reimbursable_amount: int | None = pydantic.Field(
        default=None,
        description='The optional reimbursable amount in cents',
    )
    reimbursable_currency: str | None = pydantic.Field(
        default=None,
        description='The optional reimbursable currency code in ISO 4217 format',
    )
    reimbursement_method: ReimbursementMethod | None = pydantic.Field(
        default=None,
        description='The optional reimbursement method',
    )
    internal_reference: str | None = pydantic.Field(
        default=None,
        description='The optional internal reference of the expensable',
    )
    expense_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the expense that the expensable belongs to',
    )
    mileage_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the mileage that the expensable belongs to',
    )
    per_diem_id: int | None = pydantic.Field(
        default=None,
        description='The optional ID of the per_diem that the expensable belongs to',
    )


class Expense(pydantic.BaseModel):
    """Model for expenses_expense."""

    id: int | None = pydantic.Field(default=None, description='The id of the expense')
    employee_id: int | None = pydantic.Field(default=None, description="The id of the expense's owner")
    company_id: int = pydantic.Field(description="The id of the expense's company")
    card_payment_id: int | None = pydantic.Field(default=None, description='The id of the card payment')
    dispute_id: int | None = pydantic.Field(default=None, description='The id of the dispute')
    expenses_expensable_id: int | None = pydantic.Field(default=None, description='The id of the expensable')
    merchant_name: str | None = pydantic.Field(default=None, description='The name of the merchant')
    user_merchant: str | None = pydantic.Field(default=None, description='The user merchant of the expense')
    merchant_tin: str | None = pydantic.Field(default=None, description='The tax identification number of the merchant')
    category: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='The category of the expense')
    subcategory: str | None = pydantic.Field(default=None, description='The subcategory of the expense')
    creation_type: CreationType = pydantic.Field(description='How the expense was created')
    reference: str | None = pydantic.Field(default=None, description='The reference of the expense')
    amount: int | None = pydantic.Field(default=None, description='The optional amount in cents')
    currency: str = pydantic.Field(description='The currency of the expense')
    status: ExpenseStatus = pydantic.Field(description='The status of the expense')
    description: str | None = pydantic.Field(default=None, description='The description of the expense')
    effective_on: datetime.date = pydantic.Field(description='The date when the expense was made')
    review_request_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The date and time when the expense was reviewed',
    )
    status_updated_at: datetime.datetime = pydantic.Field(description='The date and time when the status was updated')
    files: Sequence[typing.Any] = pydantic.Field(description='The files of the expense')
    external_authorization_id: str | None = pydantic.Field(
        default=None,
        description='The id of the external authorization',
    )
    expenses_card_id: int | None = pydantic.Field(default=None, description='The id of the card')
    card: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='The card of the expense')
    document_id: int | None = pydantic.Field(default=None, description='The id of the document')
    signed_document: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The signed document of the expense',
    )
    access_token: str | None = pydantic.Field(default=None, description='The access token of the expense')
    paid_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='The date and time when the expense was paid',
    )
    document_number: str | None = pydantic.Field(
        default=None,
        description='Number of the financial document associated to the expense',
    )
    document_type: str | None = pydantic.Field(
        default=None,
        description='Type of the financial document associated to the expense',
    )
    payment: PaymentType | None = pydantic.Field(default=None, description='The payment of the expense')
    payment_method: str | None = pydantic.Field(default=None, description='The method of the payment')
    exchange_rate: float | None = pydantic.Field(default=None, description='The exchange rate of the payment')
    reimbursable_currency: str | None = pydantic.Field(
        default=None,
        description='The currency of the reimbursable amount',
    )
    reimbursable_amount: int | None = pydantic.Field(
        default=None,
        description='The optional reimbursable amount in cents',
    )
    taxes: Sequence[typing.Any] = pydantic.Field(description='The taxes of the expense')
    category_id: int | None = pydantic.Field(default=None, description='The id of the category')
    ledger_account_id: int | None = pydantic.Field(default=None, description='The id of the ledger account')


class Mileage(pydantic.BaseModel):
    """Model for expenses_mileage."""

    id: int = pydantic.Field(description='Mileage identifier')
    employee_id: int | None = pydantic.Field(default=None, description='Employee identifier')
    company_id: int = pydantic.Field(description='Company identifier')
    expenses_expensable_id: int | None = pydantic.Field(default=None, description='Expensable identifier')
    category: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='The category of the mileage')
    subcategory: str | None = pydantic.Field(default=None, description='The subcategory of the mileage')
    category_id: int | None = pydantic.Field(default=None, description='The id of the category')
    amount: int | None = pydantic.Field(default=None, description='The amount in cents')
    currency: str = pydantic.Field(description='The currency code')
    reimbursable_amount: int | None = pydantic.Field(
        default=None,
        description='The amount to be reimbursed for the mileage in cents',
    )
    reimbursable_currency: str | None = pydantic.Field(
        default=None,
        description='The currency for the reimbursable amount',
    )
    status: ExpenseStatus = pydantic.Field(description='The status of the mileage')
    mileage: int | None = pydantic.Field(default=None, description='The mileage distance')
    units: str | None = pydantic.Field(default=None, description='The units of measurement')
    rate: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='The rate information')
    from_location: str | None = pydantic.Field(default=None, alias='from', description='The origin location')
    to_location: str | None = pydantic.Field(default=None, alias='to', description='The destination location')
    description: str | None = pydantic.Field(default=None, description='The description of the mileage')
    effective_on: datetime.date | None = pydantic.Field(default=None, description='The effective date')
    review_request_at: datetime.datetime | None = pydantic.Field(default=None, description='The review request date')
    files: Sequence[typing.Any] = pydantic.Field(description='The files attached to the mileage')
    paid_at: datetime.datetime | None = pydantic.Field(default=None, description='The date when paid')
    payment: PaymentType = pydantic.Field(description='The payment type')
    ledger_account_id: int | None = pydantic.Field(default=None, description='The ledger account identifier')
    round_trip: bool | None = pydantic.Field(default=None, description='Indicates if the mileage is a round trip')
    origin_longitude: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The longitude of the origin of the mileage',
    )
    origin_latitude: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The latitude of the origin of the mileage',
    )
    destination_longitude: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The longitude of the destination of the mileage',
    )
    destination_latitude: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The latitude of the destination of the mileage',
    )
    calculated_mileage: int | None = pydantic.Field(
        default=None,
        description='The calculated mileage between origin and destination in decameters/10-milers',
    )


class PerDiem(pydantic.BaseModel):
    """Model for expenses_per_diem."""

    id: int = pydantic.Field(description='The ID of the per diem')
    employee_id: int | None = pydantic.Field(default=None, description='The ID of the employee the per diem is for')
    company_id: int = pydantic.Field(description='The ID of the company the per diem is for')
    expenses_expensable_id: int | None = pydantic.Field(
        default=None,
        description='The ID of the expensable the per diem is for',
    )
    end_date: datetime.date | None = pydantic.Field(default=None, description='The end date of the per diem')
    start_date: datetime.date | None = pydantic.Field(default=None, description='The start date of the per diem')
    from_location: str | None = pydantic.Field(
        default=None,
        alias='from',
        description='The location the per diem is from',
    )
    to_location: str | None = pydantic.Field(default=None, alias='to', description='The location the per diem is to')
    ledger_account_id: int | None = pydantic.Field(
        default=None,
        description='The ID of the ledger account the per diem is for',
    )
    amount: int | None = pydantic.Field(default=None, description='The amount of the per diem')
    currency: str = pydantic.Field(description='The currency for the reimbursable amount')
    reimbursable_amount: int | None = pydantic.Field(
        default=None,
        description='The amount to be reimbursed by the per diem in cents',
    )
    reimbursable_currency: str | None = pydantic.Field(
        default=None,
        description='The currency for the reimbursable amount',
    )
    payment: PaymentType = pydantic.Field(description='The payment method for the per diem')
    paid_at: datetime.date | None = pydantic.Field(default=None, description='The date the per diem was paid')
    files: Sequence[typing.Any] = pydantic.Field(description='The files attached to the per diem')
    review_request_at: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the per diem was requested for review',
    )
    effective_on: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the per diem is effective on',
    )
    description: str | None = pydantic.Field(default=None, description='The description of the per diem')
    category: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='The category of the per diem')
    subcategory: str | None = pydantic.Field(default=None, description='The subcategory of the per diem')
    status: ExpenseStatus = pydantic.Field(description='The status of the per diem')
    rates: Sequence[typing.Any] = pydantic.Field(description='The rates for the per diem')


class ExpensablesEndpoint(Endpoint):
    """Endpoint for expenses/expensables operations."""

    endpoint = 'expenses/expensables'

    async def all(self, **kwargs) -> ListApiResponse[Expensable]:
        """Get all expensables records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Expensable)

    async def get(self, **kwargs) -> MetaApiResponse[Expensable]:
        """Get expensables with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Expensable)

    async def get_by_id(self, expensable_id: int | str, **kwargs) -> Expensable:
        """Get a specific expensable by ID."""
        data = await self.api.get(self.endpoint, expensable_id, **kwargs)
        return pydantic.TypeAdapter(Expensable).validate_python(data)


class ExpensesEndpoint(Endpoint):
    """Endpoint for expenses/expenses operations."""

    endpoint = 'expenses/expenses'

    async def all(self, **kwargs) -> ListApiResponse[Expense]:
        """Get all expenses records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Expense)

    async def get(self, **kwargs) -> MetaApiResponse[Expense]:
        """Get expenses with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Expense)

    async def get_by_id(self, expense_id: int | str, **kwargs) -> Expense:
        """Get a specific expense by ID."""
        data = await self.api.get(self.endpoint, expense_id, **kwargs)
        return pydantic.TypeAdapter(Expense).validate_python(data)


class MileagesEndpoint(Endpoint):
    """Endpoint for expenses/mileages operations."""

    endpoint = 'expenses/mileages'

    async def all(self, **kwargs) -> ListApiResponse[Mileage]:
        """Get all mileages records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Mileage)

    async def get(self, **kwargs) -> MetaApiResponse[Mileage]:
        """Get mileages with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Mileage)

    async def get_by_id(self, mileage_id: int | str, **kwargs) -> Mileage:
        """Get a specific mileage by ID."""
        data = await self.api.get(self.endpoint, mileage_id, **kwargs)
        return pydantic.TypeAdapter(Mileage).validate_python(data)


class PerDiemsEndpoint(Endpoint):
    """Endpoint for expenses/per_diems operations."""

    endpoint = 'expenses/per_diems'

    async def all(self, **kwargs) -> ListApiResponse[PerDiem]:
        """Get all per diems records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=PerDiem)

    async def get(self, **kwargs) -> MetaApiResponse[PerDiem]:
        """Get per diems with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=PerDiem)

    async def get_by_id(self, per_diem_id: int | str, **kwargs) -> PerDiem:
        """Get a specific per diem by ID."""
        data = await self.api.get(self.endpoint, per_diem_id, **kwargs)
        return pydantic.TypeAdapter(PerDiem).validate_python(data)
