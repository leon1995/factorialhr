Holidays
========

Usage
~~~~~

List company holidays::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           holidays = factorialhr.CompanyHolidaysEndpoint(api)
           response = await holidays.all()
           for h in response.data():
               print(h.name, h.date, h.half_day)

   asyncio.run(main())

.. autoclass:: factorialhr.CompanyHoliday
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CompanyHolidaysEndpoint
   :members:
