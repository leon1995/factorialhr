Bookkeepers Management
======================

Usage
~~~~~

Fetch bookkeeper incidences (e.g. for accounting sync)::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           bookkeepers = factorialhr.BookkeepersManagementEndpoint(api)
           response = await bookkeepers.get(params={"page": 1})
           for inc in response.data():
               print(inc.id, inc.type)

   asyncio.run(main())

.. autoclass:: factorialhr.BookkeepersManagementEndpoint
   :members:

.. autoclass:: factorialhr.BookkeepersManagementIncidence
   :members:
   :exclude-members: model_config
