Integrations
============

Usage
~~~~~

List syncable items and sync runs::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           items = factorialhr.SyncableItemsEndpoint(api)
           response = await items.get(params={"limit": 10})
           for item in response.data():
               print(item.syncable_type, item.external_id)
           runs = factorialhr.SyncableSyncRunsEndpoint(api)
           for run in (await runs.all()).data():
               print(run.started_at, run.status)

   asyncio.run(main())

Enums
~~~~~

.. autoclass:: factorialhr.SyncableType
   :members:
   :undoc-members:
   :show-inheritance:

Models and endpoints
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: factorialhr.SyncableItem
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SyncableItemsEndpoint
   :members:

.. autoclass:: factorialhr.SyncableSyncRun
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SyncableSyncRunsEndpoint
   :members:
