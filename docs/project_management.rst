Project Management
==================

Usage
~~~~~

Fetch projects, time records, and expense records::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           projects = factorialhr.ProjectEndpoint(api)
           response = await projects.get(params={"page": 1})
           for proj in response.data():
               print(proj.name, proj.status)
           time_records = factorialhr.TimeRecordEndpoint(api)
           records = await time_records.get(params={"limit": 20})
           for r in records.data():
               print(r.employee_id, r.date, r.seconds)
           expenses = factorialhr.ExpenseRecordEndpoint(api)
           for e in (await expenses.all()).data():
               print(e.amount, e.project_id)

   asyncio.run(main())

Enums
~~~~~

.. autoclass:: factorialhr.ProjectStatus
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.ProjectEmployeeAssignment
   :members:
   :undoc-members:
   :show-inheritance:

Models and endpoints
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: factorialhr.ExpenseRecord
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ExpenseRecordEndpoint
   :members:

.. autoclass:: factorialhr.ExportableExpense
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ExportableExpenseEndpoint
   :members:

.. autoclass:: factorialhr.ExportableProject
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ExportableProjectEndpoint
   :members:

.. autoclass:: factorialhr.FlexibleTimeRecord
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.FlexibleTimeRecordComment
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.FlexibleTimeRecordCommentEndpoint
   :members:

.. autoclass:: factorialhr.FlexibleTimeRecordEndpoint
   :members:

.. autoclass:: factorialhr.PlannedRecord
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PlannedRecordsEndpoint
   :members:

.. autoclass:: factorialhr.Project
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ProjectEndpoint
   :members:

.. autoclass:: factorialhr.ProjectTask
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ProjectTaskEndpoint
   :members:

.. autoclass:: factorialhr.ProjectWorker
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ProjectWorkerEndpoint
   :members:

.. autoclass:: factorialhr.Subproject
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SubprojectEndpoint
   :members:

.. autoclass:: factorialhr.TimeRecord
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TimeRecordEndpoint
   :members:
