Time Planning
=============

Usage
~~~~~

Work with planning versions and planned breaks::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           versions = factorialhr.PlanningVersionEndpoint(api)
           response = await versions.get(params={"limit": 10})
           for v in response.data():
               print(v.id, v.name)
           breaks = factorialhr.PlannedBreakEndpoint(api)
           for b in (await breaks.all()).data():
               print(b.planning_version_id, b.break_type)

   asyncio.run(main())

.. autoclass:: factorialhr.PlannedBreak
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PlannedBreakEndpoint
   :members:

.. autoclass:: factorialhr.PlanningVersion
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PlanningVersionEndpoint
   :members:
