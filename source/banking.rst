Banking
=======

Usage
~~~~~

List bank accounts and transactions::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           accounts = factorialhr.BankAccountsEndpoint(api)
           response = await accounts.all()
           for account in response.data():
               print(account.name, account.currency)

           # List card payments or transactions
           transactions = factorialhr.TransactionsEndpoint(api)
           txs = await transactions.get(params={"limit": 50})
           for t in txs.data():
               print(t.amount, t.description)

   asyncio.run(main())

.. autoclass:: factorialhr.BankAccount
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.BankAccountNumber
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.BankAccountsEndpoint
   :members:

.. autoclass:: factorialhr.CardPayment
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CardPaymentsEndpoint
   :members:

.. autoclass:: factorialhr.Transaction
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TransactionsEndpoint
   :members:
