Payroll Integrations Base
=========================

Usage
~~~~~

Fetch payroll integration codes::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           codes = factorialhr.CodesEndpoint(api)
           response = await codes.all()
           for code in response.data():
               print(code.code, code.description)

   asyncio.run(main())

.. autoclass:: factorialhr.CodesEndpoint
   :members:

.. autoclass:: factorialhr.Payrollintegrationsbasecode
   :members:
   :exclude-members: model_config
