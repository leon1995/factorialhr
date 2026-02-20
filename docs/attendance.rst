Attendance
==========

Usage
~~~~~

Fetch shifts, worked time, and overtime requests::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           # List attendance shifts for a period
           shifts = factorialhr.ShiftsEndpoint(api)
           response = await shifts.get(params={"page": 1, "limit": 20})
           for shift in response.data():
               print(shift.employee_id, shift.starts_at, shift.ends_at)

           # Get worked time entries (e.g. for payroll or reports)
           worked = factorialhr.WorkedTimesEndpoint(api)
           all_worked = await worked.all()
           for w in all_worked.data():
               print(w.employee_id, w.date, w.seconds)

   asyncio.run(main())

Enums
~~~~~

.. autoclass:: factorialhr.LocationType
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.TimeUnit
   :members:
   :undoc-members:
   :show-inheritance:

Models and endpoints
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: factorialhr.AttendanceShift
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.BreakConfigurationsEndpoint
   :members:

.. autoclass:: factorialhr.EditTimesheetRequest
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EditTimesheetRequestsEndpoint
   :members:

.. autoclass:: factorialhr.EstimatedTime
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EstimatedTimesEndpoint
   :members:

.. autoclass:: factorialhr.OpenShift
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.OpenShiftsEndpoint
   :members:

.. autoclass:: factorialhr.OvertimeRequest
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.OvertimeRequestsEndpoint
   :members:

.. autoclass:: factorialhr.Review
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewsEndpoint
   :members:

.. autoclass:: factorialhr.ShiftsEndpoint
   :members:

.. autoclass:: factorialhr.WorkedTime
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.WorkedTimesEndpoint
   :members:
