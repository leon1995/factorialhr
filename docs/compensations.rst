Compensations
=============

Usage
~~~~~

Fetch compensation concepts (e.g. salary components, allowances)::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           concepts = factorialhr.ConceptsEndpoint(api)
           response = await concepts.all()
           for concept in response.data():
               print(concept.name, concept.category, concept.unit_type)

   asyncio.run(main())

Enums
~~~~~

.. autoclass:: factorialhr.ConceptCategory
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.UnitType
   :members:
   :undoc-members:
   :show-inheritance:

Models and endpoints
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: factorialhr.Concept
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ConceptsEndpoint
   :members:
