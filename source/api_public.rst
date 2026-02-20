Api Public
==========

Usage
~~~~~

Create credentials for OAuth or manage webhook subscriptions::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           creds = factorialhr.CredentialsEndpoint(api)
           # List credentials (e.g. to inspect OAuth clients)
           response = await creds.get()
           for c in response.data():
               print(c.client_id, c.scope)

           subs = factorialhr.WebhookSubscriptionEndpoint(api)
           # List webhook subscriptions and filter by event
           all_subs = await subs.all()
           for sub in all_subs.data():
               print(sub.event, sub.callback_url)

   asyncio.run(main())

.. autoclass:: factorialhr.Credentials
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CredentialsEndpoint
   :members:

.. autoclass:: factorialhr.WebhookSubscription
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.WebhookSubscriptionEndpoint
   :members:
