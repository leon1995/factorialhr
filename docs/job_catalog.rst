Job Catalog
===========

Usage
~~~~~

Fetch job catalog levels, roles, and nodes::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           levels = factorialhr.LevelsEndpoint(api)
           for level in (await levels.all()).data():
               print(level.name)
           roles = factorialhr.RolesEndpoint(api)
           response = await roles.get(params={"page": 1})
           for role in response.data():
               print(role.name)
           tree = factorialhr.TreeNodesEndpoint(api)
           for node in (await tree.all()).data():
               print(node.name, node.node_type)

   asyncio.run(main())

Enums
~~~~~

.. autoclass:: factorialhr.JobCatalogNodeType
   :members:
   :undoc-members:
   :show-inheritance:

Models and endpoints
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: factorialhr.Jobcataloglevel
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.JobCatalogNode
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.Jobcatalogrole
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.LevelsEndpoint
   :members:

.. autoclass:: factorialhr.NodeAttribute
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.NodeAttributesEndpoint
   :members:

.. autoclass:: factorialhr.RolesEndpoint
   :members:

.. autoclass:: factorialhr.TreeNodesEndpoint
   :members:
