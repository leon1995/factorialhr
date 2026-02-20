Time Settings
=============

Usage
~~~~~

Manage break configurations::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           break_config = factorialhr.BreakConfigurationEndpoint(api)
           one = await break_config.get_by_id(123)
           print(one.name, one.duration_minutes)

   asyncio.run(main())

.. autoclass:: factorialhr.BreakConfiguration
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.BreakConfigurationEndpoint
   :members:
