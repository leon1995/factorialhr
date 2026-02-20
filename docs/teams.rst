Teams
=====

Usage
~~~~~

List teams and memberships::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           teams = factorialhr.TeamsEndpoint(api)
           response = await teams.all()
           for team in response.data():
               print(team.name)
           memberships = factorialhr.MembershipsEndpoint(api)
           for m in (await memberships.get(params={"limit": 50})).data():
               print(m.team_id, m.employee_id)

   asyncio.run(main())

.. autoclass:: factorialhr.Membership
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.MembershipsEndpoint
   :members:

.. autoclass:: factorialhr.Team
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TeamsEndpoint
   :members:
