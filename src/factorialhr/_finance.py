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

    model_config = pydantic.ConfigDict(frozen=True)

    #: Unique identifier in factorial for the ledger account
    id: int = pydantic.Field(description='Unique identifier in factorial for the ledger account')
    #: Name of the ledger account
    name: str | None = pydantic.Field(default=None, description='Name of the ledger account')
    #: Legal entity ID of the ledger account
    legal_entity_id: int = pydantic.Field(description='Legal entity ID of the ledger account')
    #: Number of the ledger account
    number: str = pydantic.Field(description='Number of the ledger account')
    #: Whether the ledger account is disabled
    disabled: bool = pydantic.Field(description='Whether the ledger account is disabled')
    #: Type of the ledger account
    type: AccountType = pydantic.Field(description='Type of the ledger account')
    #: Id of the ledger account on the external system
    external_id: str | None = pydantic.Field(
        default=None,
        description='Id of the ledger account on the external system',
    )
    #: Last updated date of the ledger account
    updated_at: datetime.datetime = pydantic.Field(description='Last updated date of the ledger account')


class AccountingSetting(pydantic.BaseModel):
    """Model for finance_accounting_setting."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier for the AccountingSetting
    id: int = pydantic.Field(description='Identifier for the AccountingSetting')
    #: External ID for the accounting setting
    external_id: str | None = pydantic.Field(default=None, description='External ID for the accounting setting')
    #: ID of the associated Company
    company_id: int = pydantic.Field(description='ID of the associated Company')
    #: ID of the associated Legal Entity
    legal_entity_id: int = pydantic.Field(description='ID of the associated Legal Entity')
    #: Timestamp when the accounting setting was last updated
    updated_at: datetime.datetime = pydantic.Field(description='Timestamp when the accounting setting was last updated')
    #: Default account for purchase invoices
    default_account_for_purchase_invoices_id: int | None = pydantic.Field(
        default=None,
        description='Default account for purchase invoices',
    )
    #: Default account for vendors
    default_account_for_vendors_id: int | None = pydantic.Field(
        default=None,
        description='Default account for vendors',
    )
    #: Default account for banks
    default_account_for_banks_id: int | None = pydantic.Field(default=None, description='Default account for banks')
    #: Default suspense account
    default_account_for_suspense_id: int | None = pydantic.Field(
        default=None,
        description='Default suspense account',
    )
    #: Default account for expenses
    default_account_for_expenses_id: int | None = pydantic.Field(
        default=None,
        description='Default account for expenses',
    )
    #: Default account for employees
    default_account_for_employees_id: int | None = pydantic.Field(
        default=None,
        description='Default account for employees',
    )
    #: Default account for sale invoices
    default_account_for_sale_invoices_id: int | None = pydantic.Field(
        default=None,
        description='Default account for sale invoices',
    )
    #: Default account for clients
    default_account_for_clients_id: int | None = pydantic.Field(
        default=None,
        description='Default account for clients',
    )
    #: Default account for benefits
    default_account_for_benefits_id: int | None = pydantic.Field(
        default=None,
        description='Default account for benefits',
    )


class FinanceCategory(pydantic.BaseModel):
    """Model for finance_category."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Category identifier
    id: int = pydantic.Field(description='Category identifier')
    #: Category name
    name: str = pydantic.Field(description='Category name')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class Contact(pydantic.BaseModel):
    """Model for finance_contact."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Unique identifier for the Contact
    id: int = pydantic.Field(description='Unique identifier for the Contact')
    #: The commercial name of the Contact
    name: str = pydantic.Field(description='The commercial name of the Contact')
    #: The official or legal name of the Contact
    legal_name: str | None = pydantic.Field(default=None, description='The official or legal name of the Contact')
    #: Tax identification number assigned to the Contact
    tax_id: str | None = pydantic.Field(default=None, description='Tax identification number assigned to the Contact')
    #: The address object containing street, city, etc.
    address: Mapping[str, typing.Any] = pydantic.Field(description='The address object containing street, city, etc.')
    #: The external id of the contact
    external_id: str | None = pydantic.Field(default=None, description='The external id of the contact')
    #: Contact email
    email: str | None = pydantic.Field(default=None, description='Contact email')
    #: Contact website
    website: str | None = pydantic.Field(default=None, description='Contact website')
    #: Contact phone number
    phone_number: str | None = pydantic.Field(default=None, description='Contact phone number')
    #: Timestamp when the Contact was last updated
    updated_at: datetime.datetime = pydantic.Field(description='Timestamp when the Contact was last updated')
    #: International Bank Account Number if provided
    iban: str | None = pydantic.Field(default=None, description='International Bank Account Number if provided')
    #: Bank or branch code for the Contact if relevant
    bank_code: str | None = pydantic.Field(
        default=None,
        description='Bank or branch code for the Contact if relevant',
    )
    #: Preferred payment method for the Contact (e.g. wire_transfer, paypal)
    preferred_payment_method: PreferredPaymentMethod | None = pydantic.Field(
        default=None,
        description='Preferred payment method for the Contact (e.g. wire_transfer, paypal)',
    )


class CostCenter(pydantic.BaseModel):
    """Model for finance_cost_center."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Unique identifier for the cost center
    id: int = pydantic.Field(description='Unique identifier for the cost center')
    #: Name of the cost center
    name: str = pydantic.Field(description='Name of the cost center')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Legal entity identifier
    legal_entity_id: int | None = pydantic.Field(default=None, description='Legal entity identifier')
    #: Code of the cost center
    code: str | None = pydantic.Field(default=None, description='Code of the cost center')
    #: Description of the cost center
    description: str | None = pydantic.Field(default=None, description='Description of the cost center')
    #: Number of active employees in the cost center
    active_employees_count: int = pydantic.Field(description='Number of active employees in the cost center')
    #: Total historical count of employees
    historical_employees_count: int = pydantic.Field(description='Total historical count of employees')
    #: Status of the cost center
    status: str = pydantic.Field(description='Status of the cost center')
    #: Date when the cost center was deactivated
    deactivation_date: str | None = pydantic.Field(
        default=None,
        description='Date when the cost center was deactivated',
    )


class CostCenterMembership(pydantic.BaseModel):
    """Model for finance_cost_center_membership."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: The unique identifier of the cost center membership
    id: int = pydantic.Field(description='The unique identifier of the cost center membership')
    #: The identifier of the associated employee
    employee_id: int = pydantic.Field(description='The identifier of the associated employee')
    #: The identifier of the associated cost center
    cost_center_id: int = pydantic.Field(description='The identifier of the associated cost center')
    #: The date the employee started being assigned to the cost center
    start_date: datetime.date = pydantic.Field(
        description='The date the employee started being assigned to the cost center',
    )
    #: The date the employee stopped being assigned to the cost center
    end_date: datetime.date | None = pydantic.Field(
        default=None,
        description='The date the employee stopped being assigned to the cost center',
    )
    #: The percentage allocation of the employee to the cost center
    percentage: float = pydantic.Field(description='The percentage allocation of the employee to the cost center')


class FinancialDocument(pydantic.BaseModel):
    """Model for finance_financial_document."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Factorial unique identifier
    id: int = pydantic.Field(description='Factorial unique identifier')
    #: Net amount in cents
    net_amount_cents: int | None = pydantic.Field(default=None, description='Net amount in cents')
    #: Total amount in cents
    total_amount_cents: int | None = pydantic.Field(default=None, description='Total amount in cents')
    #: Document number
    document_number: str | None = pydantic.Field(default=None, description='Document number')
    #: Document currency
    currency: str | None = pydantic.Field(default=None, description='Document currency')
    #: Current status
    status: FinancialDocumentStatus = pydantic.Field(description='Current status')
    #: Due date
    due_date: datetime.date | None = pydantic.Field(default=None, description='Due date')
    #: Document date
    document_date: datetime.date | None = pydantic.Field(default=None, description='Document date')
    #: Factorial unique identifier for the legal entity of the financial document
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier for the legal entity of the financial document',
    )
    #: Factorial unique identifier for the vendor of the financial document
    vendor_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier for the vendor of the financial document',
    )
    #: File attached
    file: Mapping[str, typing.Any] | None = pydantic.Field(default=None, description='File attached')
    #: Updation date
    updated_at: datetime.datetime = pydantic.Field(description='Updation date')
    #: Taxes
    taxes: Sequence[typing.Any] = pydantic.Field(description='Taxes')
    #: Date when was fully reconciled
    fully_reconciled_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when was fully reconciled',
    )
    #: Date when was recorded
    recorded_at: datetime.datetime | None = pydantic.Field(default=None, description='Date when was recorded')
    #: Factorial unique identifier for the duplicate financial document
    duplicate_financial_document_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier for the duplicate financial document',
    )
    #: Date when was validated
    validated_at: datetime.datetime | None = pydantic.Field(default=None, description='Date when was validated')
    #: Factorial unique identifier for the user who validated the financial document
    validated_by_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier for the user who validated the financial document',
    )
    #: Type of the financial document. Using "invoice" as default
    document_type: DocumentType = pydantic.Field(
        description='Type of the financial document. Using "invoice" as default',
    )
    #: Factorial unique identifier for the parent financial document of the financial document
    parent_financial_document_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier for the parent financial document of the financial document',
    )
    #: Taxes total amount in cents
    taxes_total_amount_cents: int | None = pydantic.Field(default=None, description='Taxes total amount in cents')
    #: Name of the entity issuing the financial document
    issuer_name: str | None = pydantic.Field(
        default=None,
        description='Name of the entity issuing the financial document',
    )
    #: First line of the issuer's address
    issuer_address_line_1: str | None = pydantic.Field(
        default=None,
        description="First line of the issuer's address",
    )
    #: Second line of the issuer's address
    issuer_address_line_2: str | None = pydantic.Field(
        default=None,
        description="Second line of the issuer's address",
    )
    #: City of the issuer's address
    issuer_city: str | None = pydantic.Field(default=None, description="City of the issuer's address")
    #: Postal code of the issuer's address
    issuer_postal_code: str | None = pydantic.Field(
        default=None,
        description="Postal code of the issuer's address",
    )
    #: State or province of the issuer's address
    issuer_state: str | None = pydantic.Field(
        default=None,
        description="State or province of the issuer's address",
    )
    #: Country code of the issuer's address
    issuer_country_code: str | None = pydantic.Field(
        default=None,
        description="Country code of the issuer's address",
    )
    #: Tax identification number of the issuer
    issuer_tax_id: str | None = pydantic.Field(
        default=None,
        description='Tax identification number of the issuer',
    )
    #: Name of the entity receiving the financial document
    recipient_name: str | None = pydantic.Field(
        default=None,
        description='Name of the entity receiving the financial document',
    )
    #: First line of the recipient's address
    recipient_address_line_1: str | None = pydantic.Field(
        default=None,
        description="First line of the recipient's address",
    )
    #: Second line of the recipient's address
    recipient_address_line_2: str | None = pydantic.Field(
        default=None,
        description="Second line of the recipient's address",
    )
    #: City of the recipient's address
    recipient_city: str | None = pydantic.Field(default=None, description="City of the recipient's address")
    #: Postal code of the recipient's address
    recipient_postal_code: str | None = pydantic.Field(
        default=None,
        description="Postal code of the recipient's address",
    )
    #: State or province of the recipient's address
    recipient_state: str | None = pydantic.Field(
        default=None,
        description="State or province of the recipient's address",
    )
    #: Country code of the recipient's address
    recipient_country_code: str | None = pydantic.Field(
        default=None,
        description="Country code of the recipient's address",
    )
    #: Tax identification number of the recipient
    recipient_tax_id: str | None = pydantic.Field(
        default=None,
        description='Tax identification number of the recipient',
    )


class JournalEntry(pydantic.BaseModel):
    """Model for finance_journal_entry."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Journal entry ID
    id: int = pydantic.Field(description='Journal entry ID')
    #: Incremental number assigned to the journal entry
    number: int = pydantic.Field(description='Incremental number assigned to the journal entry')
    #: Timestamp when the journal entry was published
    published_at: datetime.datetime = pydantic.Field(description='Timestamp when the journal entry was published')
    #: Journal entry type (e.g. bank, invoice, tax)
    type: JournalEntryType = pydantic.Field(description='Journal entry type (e.g. bank, invoice, tax)')
    #: Source id related with this journal entry
    source_id: int | None = pydantic.Field(default=None, description='Source id related with this journal entry')
    #: Source type related with this journal entry
    source_type: JournalEntrySourceType | None = pydantic.Field(
        default=None,
        description='Source type related with this journal entry',
    )
    #: Date of the associate source
    reference_date: str = pydantic.Field(description='Date of the associate source')
    #: Description of the journal entry
    description: str | None = pydantic.Field(default=None, description='Description of the journal entry')
    #: The associated Legal Entity ID
    legal_entity_id: int = pydantic.Field(description='The associated Legal Entity ID')
    #: External identifier for the journal entry
    external_id: str | None = pydantic.Field(default=None, description='External identifier for the journal entry')
    #: The status of the journal entry (draft, published, etc.)
    status: JournalEntryStatus = pydantic.Field(description='The status of the journal entry (draft, published, etc.)')
    #: Timestamp when the journal entry was last updated
    updated_at: datetime.datetime = pydantic.Field(description='Timestamp when the journal entry was last updated')


class JournalLine(pydantic.BaseModel):
    """Model for finance_journal_line."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Factorial id
    id: int = pydantic.Field(description='Factorial id')
    #: Sequential number assigned to the line
    number: int = pydantic.Field(description='Sequential number assigned to the line')
    #: The debit amount in cents
    debit_amount_cents: int = pydantic.Field(description='The debit amount in cents')
    #: The credit amount in cents
    credit_amount_cents: int = pydantic.Field(description='The credit amount in cents')
    #: ID of the parent journal entry
    journal_entry_id: int = pydantic.Field(description='ID of the parent journal entry')
    #: ID of the associated account
    account_id: int = pydantic.Field(description='ID of the associated account')
    #: Timestamp when the journal line was reconciled
    fully_reconciled_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Timestamp when the journal line was reconciled',
    )
    #: External identifier for the journal line
    external_id: str | None = pydantic.Field(default=None, description='External identifier for the journal line')
    #: Timestamp when the journal line was last updated
    updated_at: datetime.datetime = pydantic.Field(description='Timestamp when the journal line was last updated')


class LedgerAccountResource(pydantic.BaseModel):
    """Model for finance_ledger_account_resource."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Factorial unique identifier
    id: int = pydantic.Field(description='Factorial unique identifier')
    #: Ledger account resource type
    resource_type: ResourceType = pydantic.Field(description='Ledger account resource type')
    #: Factorial unique identifier of the resource associated to the ledger account resource
    resource_id: int = pydantic.Field(
        description='Factorial unique identifier of the resource associated to the ledger account resource',
    )
    #: Factorial Ledger Account identifier
    account_id: int = pydantic.Field(description='Factorial Ledger Account identifier')
    #: Ledger account balance type
    balance_type: BalanceType | None = pydantic.Field(default=None, description='Ledger account balance type')
    #: Last time the resource was updated
    updated_at: datetime.datetime = pydantic.Field(description='Last time the resource was updated')
    #: External identifier
    external_id: str | None = pydantic.Field(default=None, description='External identifier')
    #: Factorial unique identifier of the Legal entity
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='Factorial unique identifier of the Legal entity',
    )


class TaxRate(pydantic.BaseModel):
    """Model for finance_tax_rate."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Factorial id
    id: int = pydantic.Field(description='Factorial id')
    #: Specifies the numerical percentage for the tax rate between -1 and 1
    rate: float = pydantic.Field(description='Specifies the numerical percentage for the tax rate between -1 and 1')
    #: An optional text describing the tax rate's purpose or context
    description: str | None = pydantic.Field(
        default=None,
        description="An optional text describing the tax rate's purpose or context",
    )
    #: The identifier of the related TaxType record
    tax_type_id: int = pydantic.Field(description='The identifier of the related TaxType record')
    #: The external id of the tax rate
    external_id: str | None = pydantic.Field(default=None, description='The external id of the tax rate')
    #: Last update date of the tax rate
    updated_at: datetime.datetime = pydantic.Field(description='Last update date of the tax rate')


class TaxType(pydantic.BaseModel):
    """Model for finance_tax_type."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Factorial id
    id: int = pydantic.Field(description='Factorial id')
    #: The name assigned to the tax type
    name: str = pydantic.Field(description='The name assigned to the tax type')
    #: The tax category used to distinguish different tax kinds
    type: TaxTypeCategory = pydantic.Field(description='The tax category used to distinguish different tax kinds')
    #: The country code where this tax type applies
    country_code: str | None = pydantic.Field(default=None, description='The country code where this tax type applies')
    #: The external id of the tax type
    external_id: str | None = pydantic.Field(default=None, description='The external id of the tax type')
    #: Last update date of the tax type
    updated_at: datetime.datetime = pydantic.Field(description='Last update date of the tax type')


class BudgetOption(pydantic.BaseModel):
    """Model for finance_budget_option. Budget with limited information for general viewing."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Budget option identifier
    id: int = pydantic.Field(description='Budget option identifier')
    #: Name of the budget
    name: str = pydantic.Field(description='Name of the budget')
    #: Description of the budget
    description: str | None = pydantic.Field(default=None, description='Description of the budget')
    #: Currency code
    currency: str = pydantic.Field(description='Currency code')
    #: Legal entity identifier
    legal_entity_id: int = pydantic.Field(description='Legal entity identifier')


class BudgetOptionsEndpoint(Endpoint):
    """Endpoint for finance/budget_options operations."""

    endpoint = 'finance/budget_options'

    async def all(self, **kwargs) -> ListApiResponse[BudgetOption]:
        """Get all budget options.

        Official documentation: `finance/budget_options <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-budget-options>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[BudgetOption]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=BudgetOption)

    async def get(self, **kwargs) -> MetaApiResponse[BudgetOption]:
        """Get budget options with pagination metadata.

        Official documentation: `finance/budget_options <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-budget-options>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[BudgetOption]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=BudgetOption)

    async def get_by_id(self, budget_option_id: int | str, **kwargs) -> BudgetOption:
        """Get a specific budget option by ID.

        Official documentation: `finance/budget_options <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-budget-options-id>`_

        :param budget_option_id: The unique identifier.
        :type budget_option_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: BudgetOption
        """
        data = await self.api.get(self.endpoint, budget_option_id, **kwargs)
        return pydantic.TypeAdapter(BudgetOption).validate_python(data)


class AccountsEndpoint(Endpoint):
    """Endpoint for finance/accounts operations."""

    endpoint = 'finance/accounts'

    async def all(self, **kwargs) -> ListApiResponse[Account]:
        """Get all accounts.

        Official documentation: `finance/accounts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-accounts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Account]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Account)

    async def get(self, **kwargs) -> MetaApiResponse[Account]:
        """Get accounts with pagination metadata.

        Official documentation: `finance/accounts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-accounts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Account]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Account)

    async def get_by_id(self, account_id: int | str, **kwargs) -> Account:
        """Get a specific account by ID.

        Official documentation: `finance/accounts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-accounts-id>`_

        :param account_id: The unique identifier.
        :type account_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Account
        """
        data = await self.api.get(self.endpoint, account_id, **kwargs)
        return pydantic.TypeAdapter(Account).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Account:
        """Create a new account.

        Official documentation: `finance/accounts <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-finance-accounts>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Account
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Account).validate_python(response)

    async def update(self, account_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Account:
        """Update an account.

        Official documentation: `finance/accounts <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-finance-accounts-id>`_

        :param account_id: The unique identifier of the record to update.
        :type account_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Account
        """
        response = await self.api.put(self.endpoint, account_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Account).validate_python(response)


class AccountingSettingsEndpoint(Endpoint):
    """Endpoint for finance/accounting_settings operations."""

    endpoint = 'finance/accounting_settings'

    async def all(self, **kwargs) -> ListApiResponse[AccountingSetting]:
        """Get all accounting settings.

        Official documentation: `finance/accounting_settings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-accounting-settings>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[AccountingSetting]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=AccountingSetting)

    async def get(self, **kwargs) -> MetaApiResponse[AccountingSetting]:
        """Get accounting settings with pagination metadata.

        Official documentation: `finance/accounting_settings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-accounting-settings>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[AccountingSetting]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=AccountingSetting)

    async def get_by_id(self, setting_id: int | str, **kwargs) -> AccountingSetting:
        """Get a specific accounting setting by ID.

        Official documentation: `finance/accounting_settings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-accounting-settings-id>`_

        :param setting_id: The unique identifier.
        :type setting_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: AccountingSetting
        """
        data = await self.api.get(self.endpoint, setting_id, **kwargs)
        return pydantic.TypeAdapter(AccountingSetting).validate_python(data)

    async def upsert(self, data: Mapping[str, typing.Any], **kwargs) -> AccountingSetting:
        """Upsert an accounting setting.

        Official documentation: `finance/accounting_settings <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-finance-accounting-settings-upsert>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: AccountingSetting
        """
        response = await self.api.post(self.endpoint, 'upsert', json=data, **kwargs)
        return pydantic.TypeAdapter(AccountingSetting).validate_python(response)


class FinanceCategoriesEndpoint(Endpoint):
    """Endpoint for finance/categories operations."""

    endpoint = 'finance/categories'

    async def all(self, **kwargs) -> ListApiResponse[FinanceCategory]:
        """Get all categories records.

        Official documentation: `finance/categories <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-categories>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[FinanceCategory]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=FinanceCategory)

    async def get(self, **kwargs) -> MetaApiResponse[FinanceCategory]:
        """Get categories with pagination metadata.

        Official documentation: `finance/categories <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-categories>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[FinanceCategory]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=FinanceCategory)

    async def get_by_id(self, category_id: int | str, **kwargs) -> FinanceCategory:
        """Get a specific category by ID.

        Official documentation: `finance/categories <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-categories-id>`_

        :param category_id: The unique identifier.
        :type category_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: FinanceCategory
        """
        data = await self.api.get(self.endpoint, category_id, **kwargs)
        return pydantic.TypeAdapter(FinanceCategory).validate_python(data)


class ContactsEndpoint(Endpoint):
    """Endpoint for finance/contacts operations."""

    endpoint = 'finance/contacts'

    async def all(self, **kwargs) -> ListApiResponse[Contact]:
        """Get all contacts.

        Official documentation: `finance/contacts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-contacts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Contact]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Contact)

    async def get(self, **kwargs) -> MetaApiResponse[Contact]:
        """Get contacts with pagination metadata.

        Official documentation: `finance/contacts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-contacts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Contact]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Contact)

    async def get_by_id(self, contact_id: int | str, **kwargs) -> Contact:
        """Get a specific contact by ID.

        Official documentation: `finance/contacts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-contacts-id>`_

        :param contact_id: The unique identifier.
        :type contact_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Contact
        """
        data = await self.api.get(self.endpoint, contact_id, **kwargs)
        return pydantic.TypeAdapter(Contact).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Contact:
        """Create a new contact.

        Official documentation: `finance/contacts <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-finance-contacts>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Contact
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Contact).validate_python(response)

    async def update(self, contact_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Contact:
        """Update a contact.

        Official documentation: `finance/contacts <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-finance-contacts-id>`_

        :param contact_id: The unique identifier of the record to update.
        :type contact_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Contact
        """
        response = await self.api.put(self.endpoint, contact_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Contact).validate_python(response)


class CostCentersEndpoint(Endpoint):
    """Endpoint for finance/cost_centers operations."""

    endpoint = 'finance/cost_centers'

    async def all(self, **kwargs) -> ListApiResponse[CostCenter]:
        """Get all cost centers.

        Official documentation: `finance/cost_centers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-cost-centers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[CostCenter]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=CostCenter)

    async def get(self, **kwargs) -> MetaApiResponse[CostCenter]:
        """Get cost centers with pagination metadata.

        Official documentation: `finance/cost_centers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-cost-centers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[CostCenter]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=CostCenter)

    async def get_by_id(self, cost_center_id: int | str, **kwargs) -> CostCenter:
        """Get a specific cost center by ID.

        Official documentation: `finance/cost_centers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-cost-centers-id>`_

        :param cost_center_id: The unique identifier.
        :type cost_center_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: CostCenter
        """
        data = await self.api.get(self.endpoint, cost_center_id, **kwargs)
        return pydantic.TypeAdapter(CostCenter).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> CostCenter:
        """Create a new cost center.

        Official documentation: `finance/cost_centers <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-finance-cost-centers>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: CostCenter
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(CostCenter).validate_python(response)

    async def edit(self, data: Mapping[str, typing.Any], **kwargs) -> CostCenter:
        """Edit a cost center.

        Official documentation: `finance/cost_centers <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-finance-cost-centers-edit>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: CostCenter
        """
        response = await self.api.post(self.endpoint, 'edit', json=data, **kwargs)
        return pydantic.TypeAdapter(CostCenter).validate_python(response)

    async def delete(self, cost_center_id: int | str, **kwargs) -> CostCenter:
        """Delete a cost center.

        Official documentation: `finance/cost_centers <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-finance-cost-centers-id>`_

        :param cost_center_id: The unique identifier of the record to delete.
        :type cost_center_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: CostCenter
        """
        response = await self.api.delete(self.endpoint, cost_center_id, **kwargs)
        return pydantic.TypeAdapter(CostCenter).validate_python(response)


class CostCenterMembershipsEndpoint(Endpoint):
    """Endpoint for finance/cost_center_memberships operations."""

    endpoint = 'finance/cost_center_memberships'

    async def all(self, **kwargs) -> ListApiResponse[CostCenterMembership]:
        """Get all cost center memberships.

        Official documentation: `finance/cost_center_memberships <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-cost-center-memberships>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[CostCenterMembership]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=CostCenterMembership)

    async def get(self, **kwargs) -> MetaApiResponse[CostCenterMembership]:
        """Get cost center memberships with pagination metadata.

        Official documentation: `finance/cost_center_memberships <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-cost-center-memberships>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[CostCenterMembership]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=CostCenterMembership)

    async def bulk_create_update(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[CostCenterMembership]:
        """Bulk create/update cost center memberships.

        Official documentation: `finance/cost_center_memberships <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-finance-cost-center-memberships-bulk-create-update>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[CostCenterMembership]
        """
        response = await self.api.post(self.endpoint, 'bulk_create_update', json=data, **kwargs)
        return pydantic.TypeAdapter(list[CostCenterMembership]).validate_python(response)


class FinancialDocumentsEndpoint(Endpoint):
    """Endpoint for finance/financial_documents operations."""

    endpoint = 'finance/financial_documents'

    async def all(self, **kwargs) -> ListApiResponse[FinancialDocument]:
        """Get all financial documents.

        Official documentation: `finance/financial_documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-financial-documents>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[FinancialDocument]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=FinancialDocument)

    async def get(self, **kwargs) -> MetaApiResponse[FinancialDocument]:
        """Get financial documents with pagination metadata.

        Official documentation: `finance/financial_documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-financial-documents>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[FinancialDocument]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=FinancialDocument)

    async def get_by_id(self, document_id: int | str, **kwargs) -> FinancialDocument:
        """Get a specific financial document by ID.

        Official documentation: `finance/financial_documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-financial-documents-id>`_

        :param document_id: The unique identifier.
        :type document_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: FinancialDocument
        """
        data = await self.api.get(self.endpoint, document_id, **kwargs)
        return pydantic.TypeAdapter(FinancialDocument).validate_python(data)


class JournalEntriesEndpoint(Endpoint):
    """Endpoint for finance/journal_entries operations."""

    endpoint = 'finance/journal_entries'

    async def all(self, **kwargs) -> ListApiResponse[JournalEntry]:
        """Get all journal entries.

        Official documentation: `finance/journal_entries <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-journal-entries>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[JournalEntry]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=JournalEntry)

    async def get(self, **kwargs) -> MetaApiResponse[JournalEntry]:
        """Get journal entries with pagination metadata.

        Official documentation: `finance/journal_entries <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-journal-entries>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[JournalEntry]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=JournalEntry)

    async def get_by_id(self, entry_id: int | str, **kwargs) -> JournalEntry:
        """Get a specific journal entry by ID.

        Official documentation: `finance/journal_entries <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-journal-entries-id>`_

        :param entry_id: The unique identifier.
        :type entry_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: JournalEntry
        """
        data = await self.api.get(self.endpoint, entry_id, **kwargs)
        return pydantic.TypeAdapter(JournalEntry).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> JournalEntry:
        """Create a new journal entry.

        Official documentation: `finance/journal_entries <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-finance-journal-entries>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: JournalEntry
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(JournalEntry).validate_python(response)


class JournalLinesEndpoint(Endpoint):
    """Endpoint for finance/journal_lines operations."""

    endpoint = 'finance/journal_lines'

    async def all(self, **kwargs) -> ListApiResponse[JournalLine]:
        """Get all journal lines.

        Official documentation: `finance/journal_lines <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-journal-lines>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[JournalLine]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=JournalLine)

    async def get(self, **kwargs) -> MetaApiResponse[JournalLine]:
        """Get journal lines with pagination metadata.

        Official documentation: `finance/journal_lines <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-journal-lines>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[JournalLine]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=JournalLine)

    async def get_by_id(self, line_id: int | str, **kwargs) -> JournalLine:
        """Get a specific journal line by ID.

        Official documentation: `finance/journal_lines <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-journal-lines-id>`_

        :param line_id: The unique identifier.
        :type line_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: JournalLine
        """
        data = await self.api.get(self.endpoint, line_id, **kwargs)
        return pydantic.TypeAdapter(JournalLine).validate_python(data)


class LedgerAccountResourcesEndpoint(Endpoint):
    """Endpoint for finance/ledger_account_resources operations."""

    endpoint = 'finance/ledger_account_resources'

    async def all(self, **kwargs) -> ListApiResponse[LedgerAccountResource]:
        """Get all ledger account resources.

        Official documentation: `finance/ledger_account_resources <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-ledger-account-resources>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[LedgerAccountResource]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=LedgerAccountResource)

    async def get(self, **kwargs) -> MetaApiResponse[LedgerAccountResource]:
        """Get ledger account resources with pagination metadata.

        Official documentation: `finance/ledger_account_resources <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-ledger-account-resources>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[LedgerAccountResource]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=LedgerAccountResource)

    async def get_by_id(self, resource_id: int | str, **kwargs) -> LedgerAccountResource:
        """Get a specific ledger account resource by ID.

        Official documentation: `finance/ledger_account_resources <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-ledger-account-resources-id>`_

        :param resource_id: The unique identifier.
        :type resource_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: LedgerAccountResource
        """
        data = await self.api.get(self.endpoint, resource_id, **kwargs)
        return pydantic.TypeAdapter(LedgerAccountResource).validate_python(data)

    async def upsert(self, data: Mapping[str, typing.Any], **kwargs) -> LedgerAccountResource:
        """Upsert a ledger account resource.

        Official documentation: `finance/ledger_account_resources <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-finance-ledger-account-resources-upsert>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: LedgerAccountResource
        """
        response = await self.api.post(self.endpoint, 'upsert', json=data, **kwargs)
        return pydantic.TypeAdapter(LedgerAccountResource).validate_python(response)


class TaxRatesEndpoint(Endpoint):
    """Endpoint for finance/tax_rates operations."""

    endpoint = 'finance/tax_rates'

    async def all(self, **kwargs) -> ListApiResponse[TaxRate]:
        """Get all tax rates.

        Official documentation: `finance/tax_rates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-tax-rates>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[TaxRate]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=TaxRate)

    async def get(self, **kwargs) -> MetaApiResponse[TaxRate]:
        """Get tax rates with pagination metadata.

        Official documentation: `finance/tax_rates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-tax-rates>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[TaxRate]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=TaxRate)

    async def get_by_id(self, rate_id: int | str, **kwargs) -> TaxRate:
        """Get a specific tax rate by ID.

        Official documentation: `finance/tax_rates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-tax-rates-id>`_

        :param rate_id: The unique identifier.
        :type rate_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: TaxRate
        """
        data = await self.api.get(self.endpoint, rate_id, **kwargs)
        return pydantic.TypeAdapter(TaxRate).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> TaxRate:
        """Create a new tax rate.

        Official documentation: `finance/tax_rates <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-finance-tax-rates>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: TaxRate
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(TaxRate).validate_python(response)

    async def update(self, rate_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> TaxRate:
        """Update a tax rate.

        Official documentation: `finance/tax_rates <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-finance-tax-rates-id>`_

        :param rate_id: The unique identifier of the record to update.
        :type rate_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: TaxRate
        """
        response = await self.api.put(self.endpoint, rate_id, json=data, **kwargs)
        return pydantic.TypeAdapter(TaxRate).validate_python(response)


class TaxTypesEndpoint(Endpoint):
    """Endpoint for finance/tax_types operations."""

    endpoint = 'finance/tax_types'

    async def all(self, **kwargs) -> ListApiResponse[TaxType]:
        """Get all tax types.

        Official documentation: `finance/tax_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-tax-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[TaxType]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=TaxType)

    async def get(self, **kwargs) -> MetaApiResponse[TaxType]:
        """Get tax types with pagination metadata.

        Official documentation: `finance/tax_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-tax-types>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[TaxType]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=TaxType)

    async def get_by_id(self, type_id: int | str, **kwargs) -> TaxType:
        """Get a specific tax type by ID.

        Official documentation: `finance/tax_types <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-finance-tax-types-id>`_

        :param type_id: The unique identifier.
        :type type_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: TaxType
        """
        data = await self.api.get(self.endpoint, type_id, **kwargs)
        return pydantic.TypeAdapter(TaxType).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> TaxType:
        """Create a new tax type.

        Official documentation: `finance/tax_types <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-finance-tax-types>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: TaxType
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(TaxType).validate_python(response)

    async def update(self, type_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> TaxType:
        """Update a tax type.

        Official documentation: `finance/tax_types <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-finance-tax-types-id>`_

        :param type_id: The unique identifier of the record to update.
        :type type_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: TaxType
        """
        response = await self.api.put(self.endpoint, type_id, json=data, **kwargs)
        return pydantic.TypeAdapter(TaxType).validate_python(response)
