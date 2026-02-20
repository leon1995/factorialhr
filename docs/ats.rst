Ats
===

Usage
~~~~~

Work with candidates, job postings, and applications::

   import asyncio
   import factorialhr

   async def main():
       auth = factorialhr.AccessTokenAuth("your_access_token")
       async with factorialhr.ApiClient(auth=auth) as api:
           # List job postings and show open positions
           job_postings = factorialhr.JobPostingsEndpoint(api)
           postings = await job_postings.all()
           for job in postings.data():
               print(job.name, job.status)

           # List candidates and inspect application stage
           candidates = factorialhr.CandidatesEndpoint(api)
           response = await candidates.get(params={"limit": 10})
           for candidate in response.data():
               print(candidate.first_name, candidate.last_name)

   asyncio.run(main())

Enums
~~~~~

.. autoclass:: factorialhr.OriginalQuestionType
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.PhaseType
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.Gender
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.CandidateSourceCategory
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.HiringStageName
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.ContractType
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.WorkplaceType
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.JobPostingStatus
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.ScheduleType
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.SalaryFormat
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.RequirementLevel
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.SalaryPeriod
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: factorialhr.DecisionMaker
   :members:
   :undoc-members:
   :show-inheritance:

Models and endpoints
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: factorialhr.Answer
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.AnswersEndpoint
   :members:

.. autoclass:: factorialhr.Application
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ApplicationPhase
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ApplicationPhasesEndpoint
   :members:

.. autoclass:: factorialhr.ApplicationsEndpoint
   :members:

.. autoclass:: factorialhr.Candidate
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CandidatesEndpoint
   :members:

.. autoclass:: factorialhr.CandidateSource
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.CandidateSourcesEndpoint
   :members:

.. autoclass:: factorialhr.EvaluationForm
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.EvaluationFormsEndpoint
   :members:

.. autoclass:: factorialhr.Feedback
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.FeedbacksEndpoint
   :members:

.. autoclass:: factorialhr.HiringStage
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.HiringStagesEndpoint
   :members:

.. autoclass:: factorialhr.JobPosting
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.JobPostingsEndpoint
   :members:

.. autoclass:: factorialhr.Message
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.MessagesEndpoint
   :members:

.. autoclass:: factorialhr.Question
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.QuestionsEndpoint
   :members:

.. autoclass:: factorialhr.RejectionReason
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.RejectionReasonsEndpoint
   :members:
