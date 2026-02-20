Payroll Employees
=================

Usage
~~~~~

Fetch payroll employee identifiers::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           identifiers = factorialhr.IdentifiersEndpoint(api)
           response = await identifiers.get(params={"limit": 50})
           for ident in response.data():
               print(ident.employee_id, ident.identifier_type)

   asyncio.run(main())

.. autoclass:: factorialhr.IdentifiersEndpoint
   :members:

.. autoclass:: factorialhr.Payrollemployeesidentifier
   :members:
   :exclude-members: model_config
