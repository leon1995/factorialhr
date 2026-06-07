Approvals
=========

Usage
~~~~~

Approve or reject a resource in a materialized approvals flow::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           flows = factorialhr.MaterializedApprovalsFlowsEndpoint(api)
           result = await flows.approve_resource(
               data={"resource_id": 123, "resource_type": "Timeoff::Leave"},
           )
           print(result.status)
           rejected = await flows.reject_resource(
               data={
                   "resource_id": 456,
                   "resource_type": "Timeoff::Leave",
                   "reason": "Does not comply with policy",
               },
           )
           print(rejected.status)

   asyncio.run(main())

Models and endpoints
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: factorialhr.MaterializedApprovalsFlow
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.MaterializedApprovalsFlowsEndpoint
   :members:
