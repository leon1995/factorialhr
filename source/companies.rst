Companies
=========

Usage
~~~~~

List legal entities (companies)::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           entities = factorialhr.LegalEntitiesEndpoint(api)
           response = await entities.all()
           for entity in response.data():
               print(entity.name, entity.country)

   asyncio.run(main())

.. autoclass:: factorialhr.LegalEntitiesEndpoint
   :members:

.. autoclass:: factorialhr.LegalEntity
   :members:
   :exclude-members: model_config
