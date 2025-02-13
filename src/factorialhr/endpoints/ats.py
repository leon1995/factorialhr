from factorialhr.endpoints import _base


class Answer(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/answers'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-answers."""
        return await self.api.get(self.endpoint, **kwargs)

    async def single(self, *, answer_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-answers-id."""
        return await self.api.get(f'{self.endpoint}/{answer_id}', **kwargs)


class Application(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/applications'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-applications."""
        return await self.api.get(self.endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-ats-applications."""
        return await self.api.post(self.endpoint, **kwargs)

    async def delete(self, *, application_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-ats-applications-id."""
        return await self.api.delete(f'{self.endpoint}/{application_id}', **kwargs)

    async def update(self, *, application_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-ats-applications-id."""
        return await self.api.put(f'{self.endpoint}/{application_id}', **kwargs)

    async def single(self, *, application_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-applications-id."""
        return await self.api.get(f'{self.endpoint}/{application_id}', **kwargs)

    async def apply(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-ats-applications-apply."""
        return await self.api.post(self.endpoint, **kwargs)


class ApplicationPhase(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/application_phases'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-application-phases."""
        return await self.api.get(self.endpoint, **kwargs)

    async def single(self, *, application_phase: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-application-phases-id."""
        return await self.api.get(f'{self.endpoint}/{application_phase}', **kwargs)


class Candidate(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/candidates'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-candidates."""
        return await self.api.get(self.endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-ats-candidates."""
        return await self.api.post(self.endpoint, **kwargs)

    async def delete(self, *, candidate_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-ats-candidates-id."""
        return await self.api.delete(f'{self.endpoint}/{candidate_id}', **kwargs)

    async def update(self, *, candidate_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-ats-candidates-id."""
        return await self.api.put(f'{self.endpoint}/{candidate_id}', **kwargs)

    async def single(self, *, candidate_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-candidates-id."""
        return await self.api.get(f'{self.endpoint}/{candidate_id}', **kwargs)


class CandidateSource(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/candidate_sources'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-candidate-sources."""
        return await self.api.get(self.endpoint, **kwargs)

    async def single(self, *, candidate_source_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-candidate-sources-id."""
        return await self.api.get(f'{self.endpoint}/{candidate_source_id}', **kwargs)


class EvaluationForm(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/evaluation_forms'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-evaluation-forms."""
        return await self.api.get(self.endpoint, **kwargs)

    async def single(self, *, evaluation_form_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-evaluation-forms-id."""
        return await self.api.get(f'{self.endpoint}/{evaluation_form_id}', **kwargs)

    async def save_as_template(self, *, evaluation_form_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-ats-evaluation-forms-save-as-template."""
        return await self.api.put(f'{self.endpoint}/{evaluation_form_id}', **kwargs)


class Feedback(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/feedbacks'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-feedbacks."""
        return await self.api.get(self.endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-ats-feedbacks."""
        return await self.api.post(self.endpoint, **kwargs)

    async def delete(self, *, feedback_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-ats-feedbacks-id."""
        return await self.api.delete(f'{self.endpoint}/{feedback_id}', **kwargs)

    async def update(self, *, feedback_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-ats-feedbacks-id."""
        return await self.api.put(f'{self.endpoint}/{feedback_id}', **kwargs)

    async def single(self, *, feedback_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-feedbacks-id."""
        return await self.api.get(f'{self.endpoint}/{feedback_id}', **kwargs)


class HiringStages(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/hiring_stages'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-hiring-stages."""
        return await self.api.get(self.endpoint, **kwargs)

    async def single(self, *, hiring_stage_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-hiring-stages-id."""
        return await self.api.get(f'{self.endpoint}/{hiring_stage_id}', **kwargs)


class JobPosting(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/job_postings'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-job-postings."""
        return await self.api.get(self.endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-ats-job-postings."""
        return await self.api.post(self.endpoint, **kwargs)

    async def delete(self, *, job_posting_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-ats-job-postings-id."""
        return await self.api.delete(f'{self.endpoint}/{job_posting_id}', **kwargs)

    async def update(self, *, job_posting_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-ats-job-postings-id."""
        return await self.api.put(f'{self.endpoint}/{job_posting_id}', **kwargs)

    async def single(self, *, job_posting_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-job-postings-id."""
        return await self.api.get(f'{self.endpoint}/{job_posting_id}', **kwargs)

    async def duplicate(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-ats-job-postings-duplicate."""
        return await self.api.post(f'{self.endpoint}/duplicate', **kwargs)


class Message(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/messages'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-messages."""
        return await self.api.get(self.endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-ats-messages."""
        return await self.api.post(self.endpoint, **kwargs)

    async def single(self, *, evaluation_form_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-messages-id."""
        return await self.api.get(f'{self.endpoint}/{evaluation_form_id}', **kwargs)


class RejectReason(_base.Endpoint):
    endpoint = '/2025-01-01/resources/ats/rejection_reasons'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-rejection-reasons."""
        return await self.api.get(self.endpoint, **kwargs)

    async def single(self, *, reject_reason_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-rejection-reasons-id."""
        return await self.api.get(f'{self.endpoint}/{reject_reason_id}', **kwargs)
