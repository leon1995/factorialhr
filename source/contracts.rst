Contracts
=========

Usage
~~~~~

List contract versions and compensations::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           versions = factorialhr.ContractVersionsEndpoint(api)
           response = await versions.get(params={"page": 1})
           for v in response.data():
               print(v.employee_id, v.start_date, v.end_date)

           comps = factorialhr.CompensationsEndpoint(api)
           comp_list = await comps.all()
           for c in comp_list.data():
               print(c.concept_id, c.amount)

   asyncio.run(main())

Enums
~~~~~

.. autoclass:: factorialhr.TimeCondition
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.BankHolidayTreatment
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.AnnualWorkingTimeDistribution
   :members:
   :undoc-members:
   :show-inheritance:

Models and endpoints
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: factorialhr.Compensation
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CompensationsEndpoint
   :members:

.. autoclass:: factorialhr.ContractTemplate
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ContractTemplatesEndpoint
   :members:

.. autoclass:: factorialhr.ContractVersion
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ContractVersionHistoriesEndpoint
   :members:

.. autoclass:: factorialhr.ContractVersionHistory
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ContractVersionMetaDataEndpoint
   :members:

.. autoclass:: factorialhr.ContractVersionMetaDatum
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ContractVersionsEndpoint
   :members:

.. autoclass:: factorialhr.FrenchContractType
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.FrenchContractTypesEndpoint
   :members:

.. autoclass:: factorialhr.GermanContractType
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.GermanContractTypesEndpoint
   :members:

.. autoclass:: factorialhr.PortugueseContractType
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PortugueseContractTypesEndpoint
   :members:

.. autoclass:: factorialhr.ReferenceContractsEndpoint
   :members:

.. autoclass:: factorialhr.SpanishContractType
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SpanishContractTypesEndpoint
   :members:

.. autoclass:: factorialhr.SpanishEducationLevel
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SpanishEducationLevelsEndpoint
   :members:

.. autoclass:: factorialhr.SpanishProfessionalCategoriesEndpoint
   :members:

.. autoclass:: factorialhr.SpanishProfessionalCategory
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SpanishWorkingDayType
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.SpanishWorkingDayTypesEndpoint
   :members:

.. autoclass:: factorialhr.TaxonomiesEndpoint
   :members:

.. autoclass:: factorialhr.Taxonomy
   :members:
   :exclude-members: model_config
