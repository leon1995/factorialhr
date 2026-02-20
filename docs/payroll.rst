Payroll
=======

Usage
~~~~~

Fetch payroll-related data (family situations, supplements, policy periods)::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           family = factorialhr.FamilySituationsEndpoint(api)
           for f in (await family.all()).data():
               print(f.name)
           supplements = factorialhr.SupplementsEndpoint(api)
           response = await supplements.get(params={"page": 1})
           for s in response.data():
               print(s.employee_id, s.amount)

   asyncio.run(main())

.. autoclass:: factorialhr.EmployeesIdentifier
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.FamilySituation
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.FamilySituationsEndpoint
   :members:

.. autoclass:: factorialhr.IntegrationsBaseCode
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PolicyPeriod
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PolicyPeriodsEndpoint
   :members:

.. autoclass:: factorialhr.Supplement
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SupplementsEndpoint
   :members:
