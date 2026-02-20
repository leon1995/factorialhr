Performance
===========

Usage
~~~~~

Work with performance agreements and reviews::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           agreements = factorialhr.AgreementsEndpoint(api)
           response = await agreements.get(params={"limit": 20})
           for a in response.data():
               print(a.employee_id, a.status)
           reviews = factorialhr.ReviewProcessesEndpoint(api)
           for r in (await reviews.all()).data():
               print(r.name, r.status)

   asyncio.run(main())

.. autoclass:: factorialhr.Agreement
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.AgreementsEndpoint
   :members:

.. autoclass:: factorialhr.CompanyEmployeeScoreScale
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CompanyEmployeeScoreScalesEndpoint
   :members:

.. autoclass:: factorialhr.EmployeeScoreScale
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EmployeeScoreScalesEndpoint
   :members:

.. autoclass:: factorialhr.ReviewEvaluation
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewEvaluationAnswer
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewEvaluationAnswersEndpoint
   :members:

.. autoclass:: factorialhr.ReviewEvaluationScore
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewEvaluationScoresEndpoint
   :members:

.. autoclass:: factorialhr.ReviewEvaluationsEndpoint
   :members:

.. autoclass:: factorialhr.ReviewOwner
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewOwnersEndpoint
   :members:

.. autoclass:: factorialhr.ReviewProcess
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewProcessCustomTemplate
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewProcessCustomTemplatesEndpoint
   :members:

.. autoclass:: factorialhr.ReviewProcessesEndpoint
   :members:

.. autoclass:: factorialhr.ReviewProcessEstimatedTarget
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewProcessEstimatedTargetsEndpoint
   :members:

.. autoclass:: factorialhr.ReviewProcessTarget
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewProcessTargetsEndpoint
   :members:

.. autoclass:: factorialhr.ReviewQuestionnaireByStrategiesEndpoint
   :members:

.. autoclass:: factorialhr.ReviewQuestionnairesByStrategy
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewVisibilitySetting
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ReviewVisibilitySettingsEndpoint
   :members:

.. autoclass:: factorialhr.TargetManager
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.TargetManagersEndpoint
   :members:
