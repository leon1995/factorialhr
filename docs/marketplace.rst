Marketplace
===========

Usage
~~~~~

List marketplace installations and settings::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           installations = factorialhr.InstallationsEndpoint(api)
           response = await installations.all()
           for inst in response.data():
               print(inst.id, inst.app_id)
           settings = factorialhr.InstallationSettingsEndpoint(api)
           for s in (await settings.get(params={"limit": 10})).data():
               print(s.installation_id)

   asyncio.run(main())

.. autoclass:: factorialhr.Installation
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.InstallationsEndpoint
   :members:

.. autoclass:: factorialhr.InstallationSettings
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.InstallationSettingsEndpoint
   :members:
