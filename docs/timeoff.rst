Timeoff
=======

Usage
~~~~~

List leave allowances, leaves, and policies::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           allowances = factorialhr.AllowancesEndpoint(api)
           response = await allowances.get(params={"page": 1})
           for a in response.data():
               print(a.employee_id, a.allowance_type, a.balance)
           leaves = factorialhr.LeavesEndpoint(api)
           for leave in (await leaves.all()).data():
               print(leave.employee_id, leave.starts_on, leave.ends_on)
           policies = factorialhr.PoliciesEndpoint(api)
           for p in (await policies.all()).data():
               print(p.name)

   asyncio.run(main())

.. autoclass:: factorialhr.Allowance
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.AllowanceIncidence
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.AllowanceIncidencesEndpoint
   :members:

.. autoclass:: factorialhr.AllowancesEndpoint
   :members:

.. autoclass:: factorialhr.AllowanceStatsEndpoint
   :members:

.. autoclass:: factorialhr.AllowanceStatsNew
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.BlockedPeriod
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.BlockedPeriodsEndpoint
   :members:

.. autoclass:: factorialhr.Leave
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.LeavesEndpoint
   :members:

.. autoclass:: factorialhr.LeaveType
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.LeaveTypesEndpoint
   :members:

.. autoclass:: factorialhr.PoliciesEndpoint
   :members:

.. autoclass:: factorialhr.Policy
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PolicyAssignment
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PolicyAssignmentsEndpoint
   :members:

.. autoclass:: factorialhr.PolicyTimeline
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PolicyTimelinesEndpoint
   :members:
