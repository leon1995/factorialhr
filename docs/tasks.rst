Tasks
=====

Usage
~~~~~

List tasks and task files::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           tasks = factorialhr.TasksEndpoint(api)
           response = await tasks.get(params={"limit": 20})
           for t in response.data():
               print(t.title, t.status, t.due_date)
           files = factorialhr.TaskFilesEndpoint(api)
           for f in (await files.all()).data():
               print(f.task_id, f.filename)

   asyncio.run(main())

.. autoclass:: factorialhr.Task
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TaskFile
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TaskFilesEndpoint
   :members:

.. autoclass:: factorialhr.TasksEndpoint
   :members:
