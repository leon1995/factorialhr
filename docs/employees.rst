Employees
=========

Usage
~~~~~

Fetch employees and use their data::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           employees = factorialhr.EmployeesEndpoint(api)
           response = await employees.all()
           for employee in response.data():
               print(employee.first_name, employee.last_name, employee.email)
           # Or get a single employee by ID
           one = await employees.get_by_id(123)
           print(one.first_name)

   asyncio.run(main())

.. autoclass:: factorialhr.Employee
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EmployeesEndpoint
   :members:
