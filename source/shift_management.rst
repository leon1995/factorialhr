Shift Management
================

Usage
~~~~~

Manage shifts::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           shift_mgmt = factorialhr.ShiftManagementEndpoint(api)
           response = await shift_mgmt.get(params={"page": 1})
           for shift in response.data():
               print(shift.employee_id, shift.starts_at, shift.ends_at)

   asyncio.run(main())

.. autoclass:: factorialhr.ShiftManagementEndpoint
   :members:

.. autoclass:: factorialhr.ShiftManagementShift
   :members:
   :exclude-members: model_config
