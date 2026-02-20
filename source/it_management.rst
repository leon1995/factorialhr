It Management
=============

Usage
~~~~~

List IT assets and asset models::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           assets = factorialhr.ItAssetsEndpoint(api)
           response = await assets.all()
           for a in response.data():
               print(a.name, a.asset_model_id)
           models = factorialhr.ItAssetModelsEndpoint(api)
           for m in (await models.get(params={"limit": 20})).data():
               print(m.name)

   asyncio.run(main())

.. autoclass:: factorialhr.ItAsset
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ItAssetModel
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ItAssetModelsEndpoint
   :members:

.. autoclass:: factorialhr.ItAssetsEndpoint
   :members:
