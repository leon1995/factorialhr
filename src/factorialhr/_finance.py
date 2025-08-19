import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class AccountType(StrEnum):
    """Enum for account types."""

    EQUITY = 'equity'
    NON_CURRENT_ASSET = 'non_current_asset'
    CURRENT_ASSET = 'current_asset'
    BANK = 'bank'
    NON_CURRENT_LIABILITY = 'non_current_liability'
    CURRENT_LIABILITY = 'current_liability'
    EXPENSE = 'expense'
    INCOME = 'income'


class PreferredPaymentMethod(StrEnum):
    """Enum for preferred payment methods."""

    CARD = 'card'
    BANKTRANSFER = 'banktransfer'


class FinancialDocumentStatus(StrEnum):
    """Enum for financial document status."""

    PROCESSING = 'processing'
    REVIEW = 'review'
    SENT_TO_PAY = 'sent_to_pay'
    PAID = 'paid'


class DocumentType(StrEnum):
    """Enum for document types."""

    INVOICE = 'invoice'
    RECEIPT = 'receipt'
    CREDIT_NOTE = 'credit_note'


class JournalEntryType(StrEnum):
    """Enum for journal entry types."""

    BANK = 'bank'
    BILL = 'bill'
    INVOICE = 'invoice'
    CREDIT_NOTE = 'credit_note'
    MERGED_LEDGER_ACCOUNT = 'merged_ledger_account'
    RECONCILIATION = 'reconciliation'
    TAX = 'tax'
    RECEIPT = 'receipt'
    PAYROLL_RESULT = 'payroll_result'
    EXTERNAL = 'external'


class JournalEntrySourceType(StrEnum):
    """Enum for journal entry source types."""

    BANK_TRANSACTION = 'bank_transaction'
    INVOICE = 'invoice'
    RECONCILIATION = 'reconciliation'
    FINANCE_RECONCILIATION = 'finance_reconciliation'
    ACCOUNT = 'account'
    EXPENSE = 'expense'
    PAYROLL_RESULT = 'payroll_result'
    JOURNAL_ENTRY = 'journal_entry'


class JournalEntryStatus(StrEnum):
    """Enum for journal entry status."""

    PUBLISHED = 'published'
    REVERSED = 'reversed'


class ResourceType(StrEnum):
    """Enum for ledger account resource types."""

    CUSTOMCATEGORY = 'customcategory'
    BANKACCOUNT = 'bankaccount'
    VENDOR = 'vendor'
    TAXTYPE = 'taxtype'
    INVOICE = 'invoice'
    PAYROLLCONCEPT = 'payrollconcept'


class BalanceType(StrEnum):
    """Enum for balance types."""

    CREDIT = 'credit'
    DEBIT = 'debit'


class TaxTypeCategory(StrEnum):
    """Enum for tax type categories."""

    VAT = 'vat'
    PERSONAL_INCOME = 'personal_income'


class Account(pydantic.BaseModel):
    """Model for finance_account."""

    id: int = pydantic.Field(description='Unique identifier in factorial for the ledger account')
    name: str | None = pydantic.Field(default=None, description='Name of the ledger account')
    legal_entity_id: int = pydantic.Field(description='Legal entity ID of the ledger account')
    number: str = pydantic.Field(description='Number of the ledger account')
    disabled: bool = pydantic.Field(description='Whether the ledger account is disabled')
    type: AccountType = pydantic.Field(description='Type of the ledger account')
    external_id: str | None = pydantic.Field(
        default=None,
        description='Id of the ledger account on the external system',
    )
    updated_at: datetime.datetime = pydantic.Field(description='Last updated date of the ledger account')


class AccountingSetting(pydantic.BaseModel):
    """Model for finance_accounting_setting."""

    id: int = pydantic.Field(description='Identifier for the AccountingSetting')
    external_id: str | None = pydantic.Field(default=None, description='External ID for the accounting setting')
    company_id: int = pydantic.Field(description='ID of the associated Company')
    legal_entity_id: int = pydantic.Field(description='ID of the associated Legal Entity')
    updated_at: datetime.datetime = pydantic.Field(description='Timestamp when the accounting setting was last updated')
    default_account_for_purchase_invoices_id: int | None = pydantic.Field(
        default=None,
        description='Default account for purchase invoices',
    )
    default_account_for_vendors_id: int | None = pydantic.Field(
        default=None,
        description='Default account for vendors',
    )
    default_account_for_banks_id: int | None = pydantic.Field(default=None, description='Default account for banks')
    default_account_for_suspense_id: int | None = pydantic.Field(
        default=None,
        description='Default suspense account',
    )
    default_account_for_expenses_id: int | None = pydantic.Field(
        default=None,
        description='Default account for expenses',
    )
    default_account_for_employees_id: int | None = pydantic.Field(
        default=None,
        description='Default account for employees',
    )
    default_account_for_sale_invoices_id: int | None = pydantic.Field(
        default=None,
        description='Default account for sale invoices',
    )
    default_account_for_clients_id: int | None = pydantic.Field(
        default=None,
        description='Default account for clients',
    )
    default_account_for_benefits_id: int | None = pydantic.Field(
        default=None,
        description='Default account for benefits',
    )


class Contact(pydantic.BaseModel):
    """Model for finance_contact."""

    id: int = pydantic.Field(description='Unique identifier for the Contact')
    name: str = pydantic.Field(description='The commercial name of the Contact')
    legal_name: str | None = pydantic.Field(default=None, description='The official or legal name of the Contact')
    tax_id: str | None = pydantic.Field(default=None, description='Tax identification number assigned to the Contact')
    address: Mapping[str, typing.Any] = pydantic.Field(description='The address object containing street, city, etc.')
    external_id: str | None = pydantic.Field(default=None, description='The external id of the contact')
    updated_at: datetime.datetime = pydantic.Field(description='Timestamp when the Contact was last updated')
    iban: str | None = pydantic.Field(default=None, description='International Bank Account Number if provided')
    bank_code: str | None = pydantic.Field(
        default=None,
        description='Bank or branch code for the Contact if relevant',
    )
    preferred_payment_method: PreferredPaymentMethod | None = pydantic.Field(
        default=None,
        description='Preferred payment method for the Contact (e.g. wire_transfer, paypal)',
    )


class CostCenter(pydantic.BaseModel):
    """Model for finance_cost_center."""

    id: int = pydantic.Field(description='Unique identifier for the cost center')
    name: str = pydantic.Field(description='Name of the cost center')
    company_id: int = pydantic.Field(description='Company identifier')
    legal_entity_id: int | None = pydantic.Field(default=None, description='Legal entity identifier')
    code: str | None = pydantic.Field(default=None, description='Code of the cost center')
    description: str | None = pydantic.Field(default=None, description='Description of the cost center')
    active_employees_count: int = pydantic.Field(description='Number of active employees in the cost center')
    historical_employees_count: int = pydantic.Field(description='Total historical count of employees')
    status: str = pydantic.Field(description='Status of the cost center')
    deactivation_date: str | None = pydantic.Field(
        default=None,
        description='Date when the cost center was deactivated',
    )


class CostCenterMembership(pydantic.BaseModel):
    """Model for finance_cost_center_membership."""

    id: int = pydantic.Field(description='The unique identifier of the cost center membership')
    employee_id: int = pydantic.Field(description='The identifier of the associated employee')
    cost_center_id: int = pydantic.Field(description='The identifier of the associated cost center')
    start_date: datetime.date = pydantic.Field(
        description='The date the employee started being assigned to the cost center',
    )
    end_date: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the employee stopped being assigned to the cost center',
    )
    percentage: float = pydantic.Field(description='The percentage allocation of the employee to the cost center')


class FinancialDocument(pydantic.BaseModel):
    """Model for finance_financial_document."""

    id: int = pydantic.Field(description='Factorial unique identifier')
    net_amount_cents: int | None = pydantic.Field(default=None, description='Net amount in cents')
    total_amount_cents: int | None = pydantic.Field(default=None, description='Total amount in cents')
    document_number: str | None = pydantic.Field(default=None, description='Document number')
    currency: str | None = pydantic.Field(default=None, description='Document currency')
    status: FinancialDocumentStatus = pydantic.Field(description='Current status')
    due_date: datetime.date | None = pydantic.Field(default=None, description='Due date')
    document_date: datetime.date | None = pydantic.Field(default=None, description='Document date')
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier for the legal entity of the financial document',
    )
    vendor_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier for the vendor of the financial document',
    )
    file: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='File attached')
    updated_at: datetime.datetime = pydantic.Field(description='Updation date')
    taxes: Sequence[typing.Any] = pydantic.Field(description='Taxes')
    fully_reconciled_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when was fully reconciled',
    )
    recorded_at: datetime.datetime | None = pydantic.Field(default=None, description='Date when was recorded')
    duplicate_financial_document_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier for the duplicate financial document',
    )
    validated_at: datetime.datetime | None = pydantic.Field(default=None, description='Date when was validated')
    validated_by_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier for the user who validated the financial document',
    )
    document_type: DocumentType = pydantic.Field(
        description='Type of the financial document. Using "invoice" as default',
    )
    parent_financial_document_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier for the parent financial document of the financial document',
    )
    taxes_total_amount_cents: int | None = pydantic.Field(default=None, description='Taxes total amount in cents')
    issuer_name: str | None = pydantic.Field(
        default=None,
        description='Name of the entity issuing the financial document',
    )
    issuer_address_line_1: str | None = pydantic.Field(
        default=None,
        description="First line of the issuer's address",
    )
    issuer_address_line_2: str | None = pydantic.Field(
        default=None,
        description="Second line of the issuer's address",
    )
    issuer_city: str | None = pydantic.Field(default=None, description="City of the issuer's address")
    issuer_postal_code: str | None = pydantic.Field(
        default=None,
        description="Postal code of the issuer's address",
    )
    issuer_state: str | None = pydantic.Field(
        default=None,
        description="State or province of the issuer's address",
    )
    issuer_country_code: str | None = pydantic.Field(
        default=None,
        description="Country code of the issuer's address",
    )
    issuer_tax_id: str | None = pydantic.Field(
        default=None,
        description='Tax identification number of the issuer',
    )
    recipient_name: str | None = pydantic.Field(
        default=None,
        description='Name of the entity receiving the financial document',
    )
    recipient_address_line_1: str | None = pydantic.Field(
        default=None,
        description="First line of the recipient's address",
    )
    recipient_address_line_2: str | None = pydantic.Field(
        default=None,
        description="Second line of the recipient's address",
    )
    recipient_city: str | None = pydantic.Field(default=None, description="City of the recipient's address")
    recipient_postal_code: str | None = pydantic.Field(
        default=None,
        description="Postal code of the recipient's address",
    )
    recipient_state: str | None = pydantic.Field(
        default=None,
        description="State or province of the recipient's address",
    )
    recipient_country_code: str | None = pydantic.Field(
        default=None,
        description="Country code of the recipient's address",
    )
    recipient_tax_id: str | None = pydantic.Field(
        default=None,
        description='Tax identification number of the recipient',
    )


class JournalEntry(pydantic.BaseModel):
    """Model for finance_journal_entry."""

    id: int = pydantic.Field(description='Journal entry ID')
    number: int = pydantic.Field(description='Incremental number assigned to the journal entry')
    published_at: datetime.datetime = pydantic.Field(description='Timestamp when the journal entry was published')
    type: JournalEntryType = pydantic.Field(description='Journal entry type (e.g. bank, invoice, tax)')
    source_id: int | None = pydantic.Field(default=None, description='Source id related with this journal entry')
    source_type: JournalEntrySourceType | None = pydantic.Field(
        default=None,
        description='Source type related with this journal entry',
    )
    reference_date: str = pydantic.Field(description='Date of the associate source')
    description: str | None = pydantic.Field(default=None, description='Description of the journal entry')
    legal_entity_id: int = pydantic.Field(description='The associated Legal Entity ID')
    external_id: str | None = pydantic.Field(default=None, description='External identifier for the journal entry')
    status: JournalEntryStatus = pydantic.Field(description='The status of the journal entry (draft, published, etc.)')
    updated_at: datetime.datetime = pydantic.Field(description='Timestamp when the journal entry was last updated')


class JournalLine(pydantic.BaseModel):
    """Model for finance_journal_line."""

    id: int = pydantic.Field(description='Factorial id')
    number: int = pydantic.Field(description='Sequential number assigned to the line')
    debit_amount_cents: int = pydantic.Field(description='The debit amount in cents')
    credit_amount_cents: int = pydantic.Field(description='The credit amount in cents')
    journal_entry_id: int = pydantic.Field(description='ID of the parent journal entry')
    account_id: int = pydantic.Field(description='ID of the associated account')
    fully_reconciled_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Timestamp when the journal line was reconciled',
    )
    external_id: str | None = pydantic.Field(default=None, description='External identifier for the journal line')
    updated_at: datetime.datetime = pydantic.Field(description='Timestamp when the journal line was last updated')


class LedgerAccountResource(pydantic.BaseModel):
    """Model for finance_ledger_account_resource."""

    id: int = pydantic.Field(description='Factorial unique identifier')
    resource_type: ResourceType = pydantic.Field(description='Ledger account resource type')
    resource_id: int = pydantic.Field(
        description='Factorial unique identifier of the resource associated to the ledger account resource',
    )
    account_id: int = pydantic.Field(description='Factorial Ledger Account identifier')
    balance_type: BalanceType | None = pydantic.Field(default=None, description='Ledger account balance type')
    updated_at: datetime.datetime = pydantic.Field(description='Last time the resource was updated')
    external_id: str | None = pydantic.Field(default=None, description='External identifier')
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier of the Legal entity',
    )


class TaxRate(pydantic.BaseModel):
    """Model for finance_tax_rate."""

    id: int = pydantic.Field(description='Factorial id')
    rate: float = pydantic.Field(description='Specifies the numerical percentage for the tax rate between -1 and 1')
    description: str | None = pydantic.Field(
        default=None,
        description="An optional text describing the tax rate's purpose or context",
    )
    tax_type_id: int = pydantic.Field(description='The identifier of the related TaxType record')
    external_id: str | None = pydantic.Field(default=None, description='The external id of the tax rate')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date of the tax rate')


class TaxType(pydantic.BaseModel):
    """Model for finance_tax_type."""

    id: int = pydantic.Field(description='Factorial id')
    name: str = pydantic.Field(description='The name assigned to the tax type')
    type: TaxTypeCategory = pydantic.Field(description='The tax category used to distinguish different tax kinds')
    country_code: str | None = pydantic.Field(default=None, description='The country code where this tax type applies')
    external_id: str | None = pydantic.Field(default=None, description='The external id of the tax type')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date of the tax type')


class AccountsEndpoint(Endpoint):
    """Endpoint for finance/accounts operations."""

    endpoint = 'finance/accounts'

    async def all(self, **kwargs) -> ListApiResponse[Account]:
        """Get all accounts."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Account)

    async def get(self, **kwargs) -> MetaApiResponse[Account]:
        """Get accounts with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Account)

    async def get_by_id(self, account_id: int | str, **kwargs) -> Account:
        """Get a specific account by ID."""
        data = await self.api.get(self.endpoint, account_id, **kwargs)
        return pydantic.TypeAdapter(Account).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Account:
        """Create a new account."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Account).validate_python(response)

    async def update(self, account_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Account:
        """Update an account."""
        response = await self.api.put(self.endpoint, account_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Account).validate_python(response)


class AccountingSettingsEndpoint(Endpoint):
    """Endpoint for finance/accounting_settings operations."""

    endpoint = 'finance/accounting_settings'

    async def all(self, **kwargs) -> ListApiResponse[AccountingSetting]:
        """Get all accounting settings."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=AccountingSetting)

    async def get(self, **kwargs) -> MetaApiResponse[AccountingSetting]:
        """Get accounting settings with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=AccountingSetting)

    async def get_by_id(self, setting_id: int | str, **kwargs) -> AccountingSetting:
        """Get a specific accounting setting by ID."""
        data = await self.api.get(self.endpoint, setting_id, **kwargs)
        return pydantic.TypeAdapter(AccountingSetting).validate_python(data)

    async def upsert(self, data: Mapping[str, typing.Any], **kwargs) -> AccountingSetting:
        """Upsert an accounting setting."""
        response = await self.api.post(self.endpoint, 'upsert', json=data, **kwargs)
        return pydantic.TypeAdapter(AccountingSetting).validate_python(response)


class ContactsEndpoint(Endpoint):
    """Endpoint for finance/contacts operations."""

    endpoint = 'finance/contacts'

    async def all(self, **kwargs) -> ListApiResponse[Contact]:
        """Get all contacts."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Contact)

    async def get(self, **kwargs) -> MetaApiResponse[Contact]:
        """Get contacts with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Contact)

    async def get_by_id(self, contact_id: int | str, **kwargs) -> Contact:
        """Get a specific contact by ID."""
        data = await self.api.get(self.endpoint, contact_id, **kwargs)
        return pydantic.TypeAdapter(Contact).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Contact:
        """Create a new contact."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Contact).validate_python(response)

    async def update(self, contact_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Contact:
        """Update a contact."""
        response = await self.api.put(self.endpoint, contact_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Contact).validate_python(response)


class CostCentersEndpoint(Endpoint):
    """Endpoint for finance/cost_centers operations."""

    endpoint = 'finance/cost_centers'

    async def all(self, **kwargs) -> ListApiResponse[CostCenter]:
        """Get all cost centers."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=CostCenter)

    async def get(self, **kwargs) -> MetaApiResponse[CostCenter]:
        """Get cost centers with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=CostCenter)

    async def get_by_id(self, cost_center_id: int | str, **kwargs) -> CostCenter:
        """Get a specific cost center by ID."""
        data = await self.api.get(self.endpoint, cost_center_id, **kwargs)
        return pydantic.TypeAdapter(CostCenter).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> CostCenter:
        """Create a new cost center."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(CostCenter).validate_python(response)

    async def edit(self, data: Mapping[str, typing.Any], **kwargs) -> CostCenter:
        """Edit a cost center."""
        response = await self.api.post(self.endpoint, 'edit', json=data, **kwargs)
        return pydantic.TypeAdapter(CostCenter).validate_python(response)

    async def delete(self, cost_center_id: int | str, **kwargs) -> CostCenter:
        """Delete a cost center."""
        response = await self.api.delete(self.endpoint, cost_center_id, **kwargs)
        return pydantic.TypeAdapter(CostCenter).validate_python(response)


class CostCenterMembershipsEndpoint(Endpoint):
    """Endpoint for finance/cost_center_memberships operations."""

    endpoint = 'finance/cost_center_memberships'

    async def all(self, **kwargs) -> ListApiResponse[CostCenterMembership]:
        """Get all cost center memberships."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=CostCenterMembership)

    async def get(self, **kwargs) -> MetaApiResponse[CostCenterMembership]:
        """Get cost center memberships with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=CostCenterMembership)

    async def bulk_create_update(self, data: Mapping[str, typing.Any], **kwargs) -> list[CostCenterMembership]:
        """Bulk create/update cost center memberships."""
        response = await self.api.post(self.endpoint, 'bulk_create_update', json=data, **kwargs)
        return pydantic.TypeAdapter(list[CostCenterMembership]).validate_python(response)


class FinancialDocumentsEndpoint(Endpoint):
    """Endpoint for finance/financial_documents operations."""

    endpoint = 'finance/financial_documents'

    async def all(self, **kwargs) -> ListApiResponse[FinancialDocument]:
        """Get all financial documents."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=FinancialDocument)

    async def get(self, **kwargs) -> MetaApiResponse[FinancialDocument]:
        """Get financial documents with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=FinancialDocument)

    async def get_by_id(self, document_id: int | str, **kwargs) -> FinancialDocument:
        """Get a specific financial document by ID."""
        data = await self.api.get(self.endpoint, document_id, **kwargs)
        return pydantic.TypeAdapter(FinancialDocument).validate_python(data)


class JournalEntriesEndpoint(Endpoint):
    """Endpoint for finance/journal_entries operations."""

    endpoint = 'finance/journal_entries'

    async def all(self, **kwargs) -> ListApiResponse[JournalEntry]:
        """Get all journal entries."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=JournalEntry)

    async def get(self, **kwargs) -> MetaApiResponse[JournalEntry]:
        """Get journal entries with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=JournalEntry)

    async def get_by_id(self, entry_id: int | str, **kwargs) -> JournalEntry:
        """Get a specific journal entry by ID."""
        data = await self.api.get(self.endpoint, entry_id, **kwargs)
        return pydantic.TypeAdapter(JournalEntry).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> JournalEntry:
        """Create a new journal entry."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(JournalEntry).validate_python(response)


class JournalLinesEndpoint(Endpoint):
    """Endpoint for finance/journal_lines operations."""

    endpoint = 'finance/journal_lines'

    async def all(self, **kwargs) -> ListApiResponse[JournalLine]:
        """Get all journal lines."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=JournalLine)

    async def get(self, **kwargs) -> MetaApiResponse[JournalLine]:
        """Get journal lines with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=JournalLine)

    async def get_by_id(self, line_id: int | str, **kwargs) -> JournalLine:
        """Get a specific journal line by ID."""
        data = await self.api.get(self.endpoint, line_id, **kwargs)
        return pydantic.TypeAdapter(JournalLine).validate_python(data)


class LedgerAccountResourcesEndpoint(Endpoint):
    """Endpoint for finance/ledger_account_resources operations."""

    endpoint = 'finance/ledger_account_resources'

    async def all(self, **kwargs) -> ListApiResponse[LedgerAccountResource]:
        """Get all ledger account resources."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=LedgerAccountResource)

    async def get(self, **kwargs) -> MetaApiResponse[LedgerAccountResource]:
        """Get ledger account resources with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=LedgerAccountResource)

    async def get_by_id(self, resource_id: int | str, **kwargs) -> LedgerAccountResource:
        """Get a specific ledger account resource by ID."""
        data = await self.api.get(self.endpoint, resource_id, **kwargs)
        return pydantic.TypeAdapter(LedgerAccountResource).validate_python(data)

    async def upsert(self, data: Mapping[str, typing.Any], **kwargs) -> LedgerAccountResource:
        """Upsert a ledger account resource."""
        response = await self.api.post(self.endpoint, 'upsert', json=data, **kwargs)
        return pydantic.TypeAdapter(LedgerAccountResource).validate_python(response)


class TaxRatesEndpoint(Endpoint):
    """Endpoint for finance/tax_rates operations."""

    endpoint = 'finance/tax_rates'

    async def all(self, **kwargs) -> ListApiResponse[TaxRate]:
        """Get all tax rates."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=TaxRate)

    async def get(self, **kwargs) -> MetaApiResponse[TaxRate]:
        """Get tax rates with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=TaxRate)

    async def get_by_id(self, rate_id: int | str, **kwargs) -> TaxRate:
        """Get a specific tax rate by ID."""
        data = await self.api.get(self.endpoint, rate_id, **kwargs)
        return pydantic.TypeAdapter(TaxRate).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> TaxRate:
        """Create a new tax rate."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(TaxRate).validate_python(response)

    async def update(self, rate_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> TaxRate:
        """Update a tax rate."""
        response = await self.api.put(self.endpoint, rate_id, json=data, **kwargs)
        return pydantic.TypeAdapter(TaxRate).validate_python(response)


class TaxTypesEndpoint(Endpoint):
    """Endpoint for finance/tax_types operations."""

    endpoint = 'finance/tax_types'

    async def all(self, **kwargs) -> ListApiResponse[TaxType]:
        """Get all tax types."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=TaxType)

    async def get(self, **kwargs) -> MetaApiResponse[TaxType]:
        """Get tax types with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=TaxType)

    async def get_by_id(self, type_id: int | str, **kwargs) -> TaxType:
        """Get a specific tax type by ID."""
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(TaxType).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> TaxType:
        """Create a new tax type."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(TaxType).validate_python(response)

    async def update(self, type_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> TaxType:
        """Update a tax type."""
        response = await self.api.put(self.endpoint, type_id, json=data, **kwargs)
        return pydantic.TypeAdapter(TaxType).validate_python(response)
