Employee Updates
================

Usage
~~~~~

Fetch employee lifecycle events (new hires, terminations, absences)::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           absences = factorialhr.AbsencesEndpoint(api)
           for a in (await absences.all()).data():
               print(a.employee_id, a.starts_on, a.ends_on)
           terminations = factorialhr.TerminationsEndpoint(api)
           response = await terminations.get(params={"limit": 10})
           for t in response.data():
               print(t.employee_id, t.termination_date)

   asyncio.run(main())

.. autoclass:: factorialhr.AbsencesEndpoint
   :members:

.. autoclass:: factorialhr.ContractChangesEndpoint
   :members:

.. autoclass:: factorialhr.EmployeeAbsence
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EmployeeContractChange
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EmployeeNewHire
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EmployeePersonalChange
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EmployeeSummary
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EmployeeTermination
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EmployeeUpdatesEndpoint
   :members:

.. autoclass:: factorialhr.NewHiresEndpoint
   :members:

.. autoclass:: factorialhr.PersonalChangesEndpoint
   :members:

.. autoclass:: factorialhr.SummariesEndpoint
   :members:

.. autoclass:: factorialhr.TerminationsEndpoint
   :members:
