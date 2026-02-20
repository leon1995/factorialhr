Posts
=====

Usage
~~~~~

List posts, groups, and comments::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           posts = factorialhr.PostsEndpoint(api)
           response = await posts.get(params={"page": 1})
           for p in response.data():
               print(p.title, p.group_id)
           groups = factorialhr.GroupsEndpoint(api)
           for g in (await groups.all()).data():
               print(g.name)

   asyncio.run(main())

.. autoclass:: factorialhr.Comment
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CommentsEndpoint
   :members:

.. autoclass:: factorialhr.Group
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.GroupsEndpoint
   :members:

.. autoclass:: factorialhr.Post
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PostsEndpoint
   :members:
