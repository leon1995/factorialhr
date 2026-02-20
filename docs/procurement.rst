Procurement
===========

Usage
~~~~~

List purchase orders and purchase requests::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           orders = factorialhr.PurchaseOrdersEndpoint(api)
           response = await orders.get(params={"limit": 20})
           for po in response.data():
               print(po.id, po.status, po.total_amount)
           requests = factorialhr.PurchaseRequestsEndpoint(api)
           for pr in (await requests.all()).data():
               print(pr.id, pr.status)

   asyncio.run(main())

Enums
~~~~~

.. autoclass:: factorialhr.PurchaseOrderStatus
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.PurchaseRequestStatus
   :members:
   :undoc-members:
   :show-inheritance:

Models and endpoints
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: factorialhr.ProcurementType
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ProcurementTypesEndpoint
   :members:

.. autoclass:: factorialhr.PurchaseOrder
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PurchaseOrdersEndpoint
   :members:

.. autoclass:: factorialhr.PurchaseRequest
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PurchaseRequestsEndpoint
   :members:
