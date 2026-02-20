Custom Resources
================

Usage
~~~~~

Work with custom resource definitions and values::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           schemas = factorialhr.CustomResourcesSchemasEndpoint(api)
           for schema in (await schemas.all()).data():
               print(schema.name)
           resources = factorialhr.ResourcesEndpoint(api)
           response = await resources.get(params={"limit": 20})
           for r in response.data():
               print(r.resource_field_id, r.value)

   asyncio.run(main())

.. autoclass:: factorialhr.CustomResourcesSchemasEndpoint
   :members:

.. autoclass:: factorialhr.CustomResourcesValue
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CustomResourcesValuesEndpoint
   :members:

.. autoclass:: factorialhr.Resource
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ResourcesEndpoint
   :members:

.. autoclass:: factorialhr.Schema
   :members:
   :exclude-members: model_config
