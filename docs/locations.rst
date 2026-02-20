Locations
=========

Usage
~~~~~

List locations and work areas::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           locations = factorialhr.LocationsEndpoint(api)
           response = await locations.all()
           for loc in response.data():
               print(loc.name, loc.location_type)
           areas = factorialhr.WorkAreasEndpoint(api)
           for area in (await areas.all()).data():
               print(area.name)

   asyncio.run(main())

.. autoclass:: factorialhr.Location
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.LocationsEndpoint
   :members:

.. autoclass:: factorialhr.WorkArea
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.WorkAreasEndpoint
   :members:
