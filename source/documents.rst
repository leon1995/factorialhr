Documents
=========

Usage
~~~~~

List documents and folders::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           docs = factorialhr.DocumentsEndpoint(api)
           response = await docs.get(params={"page": 1})
           for doc in response.data():
               print(doc.name, doc.document_type)
           folders = factorialhr.FoldersEndpoint(api)
           for folder in (await folders.all()).data():
               print(folder.name)

   asyncio.run(main())

.. autoclass:: factorialhr.Document
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.DocumentsEndpoint
   :members:

.. autoclass:: factorialhr.DownloadUrl
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.DownloadUrlsEndpoint
   :members:

.. autoclass:: factorialhr.Folder
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.FoldersEndpoint
   :members:
