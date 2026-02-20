Custom Fields
=============

Usage
~~~~~

List custom fields and their options::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           fields = factorialhr.FieldsEndpoint(api)
           response = await fields.all()
           for field in response.data():
               print(field.name, field.resource_type)

   asyncio.run(main())

.. autoclass:: factorialhr.CustomFieldsValuesEndpoint
   :members:

.. autoclass:: factorialhr.CustomFieldValue
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.Field
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.FieldsEndpoint
   :members:

.. autoclass:: factorialhr.Option
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.OptionsEndpoint
   :members:

.. autoclass:: factorialhr.ResourceField
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ResourceFieldsEndpoint
   :members:
