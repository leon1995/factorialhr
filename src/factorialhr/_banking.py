import datetime
import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class AccountNumberType(StrEnum):
    """Enum for bank account number types."""

    IBAN = 'iban'
    SORT_CODE_AND_ACCOUNT_NUMBER = 'sort_code_and_account_number'
    ROUTING_NUMBER_AND_ACCOUNT_NUMBER = 'routing_number_and_account_number'
    CLABE = 'clabe'
    OTHER = 'other'
    BANK_NAME_AND_ACCOUNT_NUMBER = 'bank_name_and_account_number'


class CardPaymentStatus(StrEnum):
    """Enum for card payment status."""

    PENDING = 'pending'
    CLOSED = 'closed'
    REVERSED = 'reversed'
    REJECTED = 'rejected'


class CardPaymentType(StrEnum):
    """Enum for card payment type."""

    PAYMENT = 'payment'
    REFUND = 'refund'


class RejectedReason(StrEnum):
    """Enum for card payment rejected reasons."""

    ACCOUNT_DISABLED = 'account_disabled'
    CARD_ACTIVE = 'card_active'
    CARD_CANCELED = 'card_canceled'
    CARD_EXPIRED = 'card_expired'
    CARD_INACTIVE = 'card_inactive'
    CARDHOLDER_BLOCKED = 'cardholder_blocked'
    CARDHOLDER_INACTIVE = 'cardholder_inactive'
    CARDHOLDER_VERIFICATION_REQUIRED = 'cardholder_verification_required'
    INSECURE_AUTHORIZATION_METHOD = 'insecure_authorization_method'
    INSUFFICIENT_FUNDS = 'insufficient_funds'
    NOT_ALLOWED = 'not_allowed'
    PIN_BLOCKED = 'pin_blocked'
    SPENDING_CONTROLS = 'spending_controls'
    SUSPECTED_FRAUD = 'suspected_fraud'
    VERIFICATION_FAILED = 'verification_failed'


class TransactionType(StrEnum):
    """Enum for transaction types."""

    PAYROLL = 'payroll'
    PAYMENT = 'payment'
    TOPUP = 'topup'
    UNKNOWN = 'unknown'
    CARD_PAYMENT = 'card_payment'
    DISPUTE = 'dispute'
    CARD_REFUND = 'card_refund'
    FEES = 'fees'
    OUTGOING_TRANSFER = 'outgoing_transfer'
    INCOMING_TRANSFER = 'incoming_transfer'
    OUTGOING = 'outgoing'
    INCOMING = 'incoming'


class BankAccount(pydantic.BaseModel):
    """Model for banking_bank_account."""

    id: int = pydantic.Field(description='Factorial unique identifier')
    external_id: str = pydantic.Field(description='External ID for the bank account')
    currency: str = pydantic.Field(description='Currency')
    country: str = pydantic.Field(description='Country')
    account_number: str = pydantic.Field(description='Account number')
    account_number_type: AccountNumberType = pydantic.Field(description='Account number type')
    sort_code: str | None = pydantic.Field(default=None, description='Sort code')
    bic: str | None = pydantic.Field(default=None, description='Bank Identifier Code')
    iban: str | None = pydantic.Field(default=None, description='International Bank Account Number')
    routing_number: str | None = pydantic.Field(default=None, description='Routing number')
    account_balance_cents: int = pydantic.Field(description='Account balance in cents')
    available_balance_cents: int = pydantic.Field(description='Available balance in cents')
    pending_balance_cents: int = pydantic.Field(description='Pending balance in cents')
    beneficiary_name: str | None = pydantic.Field(default=None, description='Beneficiary name')
    bank_name: str | None = pydantic.Field(default=None, description='Bank name')
    account_alias: str | None = pydantic.Field(default=None, description='Account alias')
    updated_at: datetime.datetime = pydantic.Field(description='Last updated date')
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier of the legal entity',
    )


class CardPayment(pydantic.BaseModel):
    """Model for banking_card_payment."""

    id: int = pydantic.Field(description='The ID of the card payment')
    card_id: int = pydantic.Field(description='The ID of the card')
    amount_cents: int = pydantic.Field(description='The amount of the card payment')
    currency: str = pydantic.Field(description='The currency of the card payment')
    merchant_name: str = pydantic.Field(description='The name of the merchant')
    merchant_amount_cents: int = pydantic.Field(description='The amount of the merchant')
    merchant_currency: str = pydantic.Field(description='The currency of the merchant')
    approved: bool = pydantic.Field(description='Whether the card payment was approved')
    external_created_at: datetime.datetime = pydantic.Field(
        description='The date and time the card payment was created in the external system',
    )
    status: CardPaymentStatus = pydantic.Field(description='The status of the card payment')
    type: CardPaymentType = pydantic.Field(description='The type of the card payment')
    exchange_rate: float = pydantic.Field(description='The exchange rate of the card payment')
    rejected_reason: RejectedReason | None = pydantic.Field(
        default=None,
        description='The reason the card payment was rejected',
    )
    created_at: datetime.datetime = pydantic.Field(
        description='The date and time the card payment was created in factorial',
    )


class Transaction(pydantic.BaseModel):
    """Model for banking_transaction."""

    id: int = pydantic.Field(description='Factorial unique identifier')
    bank_account_id: int = pydantic.Field(description='Factorial Banking Bank Account unique identifier')
    amount_cents: int = pydantic.Field(description='Amount in cents')
    balance_after_cents: int | None = pydantic.Field(default=None, description='Balance after the transaction in cents')
    currency: str = pydantic.Field(description='Currency')
    type: TransactionType = pydantic.Field(description='Type of transaction')
    description: str | None = pydantic.Field(default=None, description='Description of the transaction')
    booking_date: datetime.datetime = pydantic.Field(description='Booking date of the transaction')
    value_date: datetime.datetime = pydantic.Field(description='Value date of the transaction')
    card_payment_id: int = pydantic.Field(description='Factorial unique identifier of the card payment')
    updated_at: datetime.datetime = pydantic.Field(description='Date when the transaction was last updated')


class BankAccountNumber(pydantic.BaseModel):
    """Model for banking_bank_account_number."""

    id: str  # Employee id.
    company_id: int  # Company identifier
    account_number: str  # Account number
    complementary_data: str | None = None  # Additional banking information, depending on the selected format.
    format: str  # The format of the account number.


class BankAccountsEndpoint(Endpoint):
    """Endpoint for bank accounts operations."""

    endpoint = '/banking/bank_accounts'

    async def all(self, **kwargs) -> ListApiResponse[BankAccount]:
        """Get all bank accounts records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=BankAccount, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[BankAccount]:
        """Get bank accounts with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=BankAccount, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, bank_account_id: int | str, **kwargs) -> BankAccount:
        """Get a specific bank account by ID."""
        data = await self.api.get(self.endpoint, bank_account_id, **kwargs)
        return pydantic.TypeAdapter(BankAccount).validate_python(data)

    async def create_manual(self, data: Mapping[str, typing.Any], **kwargs) -> BankAccount:
        """Create a manual bank account."""
        response = await self.api.post(self.endpoint, 'create_manual', json=data, **kwargs)
        return pydantic.TypeAdapter(BankAccount).validate_python(response)


class CardPaymentsEndpoint(Endpoint):
    """Endpoint for card payments operations."""

    endpoint = '/banking/card_payments'

    async def all(self, **kwargs) -> ListApiResponse[CardPayment]:
        """Get all card payments records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=CardPayment, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[CardPayment]:
        """Get card payments with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=CardPayment, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, card_payment_id: int | str, **kwargs) -> CardPayment:
        """Get a specific card payment by ID."""
        data = await self.api.get(self.endpoint, card_payment_id, **kwargs)
        return pydantic.TypeAdapter(CardPayment).validate_python(data)


class TransactionsEndpoint(Endpoint):
    """Endpoint for transactions operations."""

    endpoint = '/banking/transactions'

    async def all(self, **kwargs) -> ListApiResponse[Transaction]:
        """Get all transactions records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Transaction, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Transaction]:
        """Get transactions with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Transaction, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, transaction_id: int | str, **kwargs) -> Transaction:
        """Get a specific transaction by ID."""
        data = await self.api.get(self.endpoint, transaction_id, **kwargs)
        return pydantic.TypeAdapter(Transaction).validate_python(data)
