Expenses
========

Usage
~~~~~

List expenses and expensables::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           expenses = factorialhr.ExpensesEndpoint(api)
           response = await expenses.get(params={"page": 1})
           for e in response.data():
               print(e.employee_id, e.amount, e.status)
           expensables = factorialhr.ExpensablesEndpoint(api)
           for ex in (await expensables.all()).data():
               print(ex.name, ex.expensable_type)

   asyncio.run(main())

.. autoclass:: factorialhr.Expensable
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ExpensablesEndpoint
   :members:

.. autoclass:: factorialhr.Expense
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ExpensesEndpoint
   :members:

.. autoclass:: factorialhr.Mileage
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.MileagesEndpoint
   :members:

.. autoclass:: factorialhr.PerDiem
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PerDiemsEndpoint
   :members:
