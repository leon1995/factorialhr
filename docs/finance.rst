Finance
=======

Usage
~~~~~

List accounts, contacts, and journal entries::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           accounts = factorialhr.AccountsEndpoint(api)
           for acc in (await accounts.all()).data():
               print(acc.name, acc.account_type)
           contacts = factorialhr.ContactsEndpoint(api)
           response = await contacts.get(params={"limit": 20})
           for c in response.data():
               print(c.name)
           entries = factorialhr.JournalEntriesEndpoint(api)
           for e in (await entries.get(params={"page": 1})).data():
               print(e.date, e.journal_entry_type)

   asyncio.run(main())

.. autoclass:: factorialhr.Account
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.AccountingSetting
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.AccountingSettingsEndpoint
   :members:

.. autoclass:: factorialhr.AccountsEndpoint
   :members:

.. autoclass:: factorialhr.BudgetOption
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.BudgetOptionsEndpoint
   :members:

.. autoclass:: factorialhr.Contact
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ContactsEndpoint
   :members:

.. autoclass:: factorialhr.CostCenter
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CostCenterMembership
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CostCenterMembershipsEndpoint
   :members:

.. autoclass:: factorialhr.CostCentersEndpoint
   :members:

.. autoclass:: factorialhr.FinanceCategoriesEndpoint
   :members:

.. autoclass:: factorialhr.FinanceCategory
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.FinancialDocument
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.FinancialDocumentsEndpoint
   :members:

.. autoclass:: factorialhr.JournalEntriesEndpoint
   :members:

.. autoclass:: factorialhr.JournalEntry
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.JournalLine
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.JournalLinesEndpoint
   :members:

.. autoclass:: factorialhr.LedgerAccountResource
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.LedgerAccountResourcesEndpoint
   :members:

.. autoclass:: factorialhr.TaxRate
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TaxRatesEndpoint
   :members:

.. autoclass:: factorialhr.TaxType
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TaxTypesEndpoint
   :members:
