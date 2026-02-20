Work Schedule
=============

Usage
~~~~~

Fetch work schedule configuration::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           schedule = factorialhr.ScheduleEndpoint(api)
           one = await schedule.get_by_id(123)
           print(one.name)
           day_config = factorialhr.DayConfigurationEndpoint(api)
           config = await day_config.get_by_id(456)
           print(config.schedule_id)

   asyncio.run(main())

.. autoclass:: factorialhr.DayConfigurationEndpoint
   :members:

.. autoclass:: factorialhr.OverlapPeriodEndpoint
   :members:

.. autoclass:: factorialhr.ScheduleEndpoint
   :members:

.. autoclass:: factorialhr.WorkScheduleDayConfiguration
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.WorkScheduleOverlapPeriod
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.WorkScheduleSchedule
   :members:
   :exclude-members: model_config
