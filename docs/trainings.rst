Trainings
=========

Usage
~~~~~

List trainings, sessions, and attendance::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           trainings = factorialhr.TrainingsEndpoint(api)
           response = await trainings.get(params={"limit": 20})
           for t in response.data():
               print(t.name, t.status)
           sessions = factorialhr.SessionsEndpoint(api)
           for s in (await sessions.all()).data():
               print(s.training_id, s.starts_at)
           attendance = factorialhr.SessionAttendancesEndpoint(api)
           for a in (await attendance.get(params={"page": 1})).data():
               print(a.session_id, a.employee_id)

   asyncio.run(main())

.. autoclass:: factorialhr.Session
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SessionAccessMembership
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SessionAccessMembershipsEndpoint
   :members:

.. autoclass:: factorialhr.SessionAttendance
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SessionAttendancesEndpoint
   :members:

.. autoclass:: factorialhr.SessionsEndpoint
   :members:

.. autoclass:: factorialhr.Training
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TrainingCategoriesEndpoint
   :members:

.. autoclass:: factorialhr.TrainingCategory
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TrainingClass
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TrainingClassesEndpoint
   :members:

.. autoclass:: factorialhr.TrainingMembership
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TrainingMembershipsEndpoint
   :members:

.. autoclass:: factorialhr.TrainingsEndpoint
   :members:
