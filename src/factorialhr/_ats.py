import datetime
import enum
import typing

import pydantic

from factorialhr import _common
from factorialhr._client import Endpoint


class AnswerOriginalQuestionType(enum.StrEnum):
    text = 'text'
    long_text = 'long_text'
    single_choice = 'single_choice'
    multiple_choice = 'multiple_choice'
    file = 'file'


class Answer(pydantic.BaseModel):
    id: int
    ats_question_id: int | None
    ats_application_id: int
    original_question_label: str
    value: str | None
    original_question_type: AnswerOriginalQuestionType
    created_at: datetime.datetime
    updated_at: datetime.datetime


class _AnswerRootModel(pydantic.RootModel):
    root: list[Answer]


class AnswerEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/answers'

    async def all(self, **kwargs) -> list[Answer]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-answers."""
        return _AnswerRootModel.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, answer_id: int, **kwargs) -> Answer: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[Answer], _common.Meta]: ...

    async def get(self, *, answer_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-answers-id."""
        result = await self.api.get(self.endpoint, answer_id, **kwargs)
        return (
            Answer.model_validate(result)
            if answer_id is not None
            else (
                _AnswerRootModel.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class Application(pydantic.BaseModel):
    id: int
    company_id: int
    ats_job_posting_id: int
    ats_candidate_id: int
    employee_id: int | None
    phone: str | None
    qualified: bool | None
    ats_application_phase_id: int | None
    created_at: datetime.datetime
    cover_letter: str | None
    ats_conversation_id: int | None
    medium: str | None
    rating_average: int | None
    ats_rejection_reason_id: int | None
    source_id: int | None


class _ApplicationRoot(pydantic.RootModel):
    root: list[Application]


class ApplicationEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/applications'

    async def all(self, **kwargs) -> list[Application]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-applications."""
        return _ApplicationRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, application_id: int, **kwargs) -> Application: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[Application], _common.Meta]: ...

    async def get(self, *, application_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-applications-id."""
        result = await self.api.get(self.endpoint, application_id, **kwargs)
        return (
            Application.model_validate(result)
            if application_id is not None
            else (
                _ApplicationRoot.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class ApplicationPhasePhaseType(enum.StrEnum):
    initial = 'initial'
    normal = 'normal'
    hired = 'hired'
    screening = 'screening'
    interview = 'interview'
    assessment = 'assessment'
    offer = 'offer'


class ApplicationPhase(pydantic.BaseModel):
    id: int
    ats_job_posting_id: int
    name: str
    position: int
    editable: bool
    phase_type: ApplicationPhasePhaseType
    applications_count: int | None
    active_applications_count: int | None
    ats_hiring_stage_id: int | None


class _ApplicationPhaseRoot(pydantic.RootModel):
    root: list[ApplicationPhase]


class ApplicationPhaseEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/application_phases'

    async def all(self, **kwargs) -> list[ApplicationPhase]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-application-phases."""
        return _ApplicationPhaseRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, application_phase: int, **kwargs) -> ApplicationPhase: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[ApplicationPhase], _common.Meta]: ...

    async def get(self, *, application_phase_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-application-phases-id."""
        result = await self.api.get(self.endpoint, application_phase_id, **kwargs)
        return (
            ApplicationPhase.model_validate(result)
            if application_phase_id is not None
            else (
                _ApplicationPhaseRoot.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class CandidateGender(enum.StrEnum):
    female = 'female'
    male = 'male'
    unanswered = 'unanswered'
    other = 'other'


class Candidate(pydantic.BaseModel):
    id: int
    company_id: int | None
    first_name: str
    last_name: str
    full_name: str
    email: str | None
    talent_pool: bool
    phone_number: int | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    consent_given_at: datetime.datetime | None
    inactive_since: datetime.datetime | None
    ats_job_posting_ids: list[int] | None
    personal_url: str | None
    consent_expiration_date: datetime.datetime | None
    consent_to_talent_pool: bool | None
    medium: str | None
    source_id: int | None
    gender: CandidateGender | None
    score: int | None


class _CandidateRoot(pydantic.RootModel):
    root: list[Candidate]


class CandidateEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/candidates'

    async def all(self, **kwargs) -> list[Candidate]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-candidates."""
        return _CandidateRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, candidate_id: int, **kwargs) -> Candidate: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[Candidate], _common.Meta]: ...

    async def get(self, *, candidate_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-candidates-id."""
        result = await self.api.get(self.endpoint, candidate_id, **kwargs)
        return (
            Candidate.model_validate(result)
            if candidate_id is not None
            else (
                _CandidateRoot.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class CandidateSourceCategory(enum.StrEnum):
    job_board = 'job_board'
    referral = 'referral'
    social_media = 'social_media '
    agency_or_external_recruiter = 'agency_or_external_recruiter '
    event = 'event'
    internal = 'internal'
    manually_added = 'manually_added'
    organic = 'organic'


class CandidateSource(pydantic.BaseModel):
    id: int
    company_id: int
    category: CandidateSourceCategory
    name: str
    label: str


class _CandidateSourceRoot(pydantic.RootModel):
    root: list[CandidateSource]


class CandidateSourceEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/candidate_sources'

    async def all(self, **kwargs) -> list[CandidateSource]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-candidate-sources."""
        return _CandidateSourceRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, candidate_source_id: int, **kwargs) -> CandidateSource: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[CandidateSource], _common.Meta]: ...

    async def get(self, *, candidate_source_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-candidate-sources-id."""
        result = await self.api.get(self.endpoint, candidate_source_id, **kwargs)
        return (
            CandidateSource.model_validate(result)
            if candidate_source_id is not None
            else (
                _CandidateSourceRoot.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class EvaluationFormQuestion(pydantic.BaseModel):
    id: str  # should be int but the API returns a string (could be an uuid)
    text: str
    description: str


class EvaluationForm(pydantic.BaseModel):
    id: int
    company_id: int
    ats_job_posting_id: int | None
    name: str
    based_on_id: int | None
    questions: list[EvaluationFormQuestion]
    created_at: datetime.datetime
    updated_at: datetime.datetime


class _EvaluationFormRoot(pydantic.RootModel):
    root: list[EvaluationForm]


class EvaluationFormEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/evaluation_forms'

    async def all(self, **kwargs) -> list[EvaluationForm]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-evaluation-forms."""
        return _EvaluationFormRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, evaluation_form_id: int, **kwargs) -> EvaluationForm: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[EvaluationForm], _common.Meta]: ...

    async def get(self, *, evaluation_form_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-evaluation-forms-id."""
        result = await self.api.get(self.endpoint, evaluation_form_id, **kwargs)
        return (
            EvaluationForm.model_validate(result)
            if evaluation_form_id is not None
            else (
                _EvaluationFormRoot.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class FeedbackEvaluationFormAnswer(pydantic.BaseModel):
    id: int
    score: int
    note: str


class Feedback(pydantic.BaseModel):
    id: int
    rating: int | None
    description: str | None
    ats_application_id: int | None
    ats_application_phase_id: int | None
    created_at: datetime.datetime
    ats_candidate_id: int
    ats_evaluation_forms_id: int | None
    evaluation_form_answers: list[FeedbackEvaluationFormAnswer] | None


class _FeedbackRoot(pydantic.RootModel):
    root: list[Feedback]


class FeedbackEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/feedbacks'

    async def all(self, **kwargs) -> list[Feedback]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-feedbacks."""
        return _FeedbackRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, feedback_id: int, **kwargs) -> Feedback: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[Feedback], _common.Meta]: ...

    async def get(self, *, feedback_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-feedbacks-id."""
        result = await self.api.get(self.endpoint, feedback_id, **kwargs)
        return (
            Feedback.model_validate(result)
            if feedback_id is not None
            else (_FeedbackRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta']))
        )


class HiringStateName(enum.StrEnum):
    new = 'new'
    screening = 'screening'
    interview = 'interview'
    assessment = 'assessment'
    offer = 'offer'
    hired = 'hired'


class HiringStage(pydantic.BaseModel):
    id: int
    name: HiringStateName
    company_id: int
    position: int


class _HiringStageRoot(pydantic.RootModel):
    root: list[HiringStage]


class HiringStageEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/hiring_stages'

    async def all(self, **kwargs) -> list[HiringStage]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-hiring-stages."""
        return _HiringStageRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, hiring_stage_id: int, **kwargs) -> HiringStage: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[HiringStage], _common.Meta]: ...

    async def get(self, *, hiring_stage_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-hiring-stages-id."""
        result = await self.api.get(self.endpoint, hiring_stage_id, **kwargs)
        return (
            HiringStage.model_validate(result)
            if hiring_stage_id is not None
            else (
                _HiringStageRoot.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class JobPostingStatus(enum.StrEnum):
    draft = 'draft'
    published = 'published'
    unlisted = 'unlisted'
    archived = 'archived'
    cancelled = 'cancelled'


class JobPostingSalaryPeriod(enum.StrEnum):
    annual = 'annual'
    monthly = 'monthly'
    daily = 'daily'


class JobPosting(pydantic.BaseModel):
    id: int
    company_id: int
    ats_company_id: str
    title: str
    description: str | None
    contract_type: str | None
    workplace_type: str | None
    remote: bool
    status: JobPostingStatus
    schedule_type: str | None
    team_id: str | None
    location_id: str | None
    legal_entity_id: str | None
    salary_format: str | None
    salary_from_amount_in_cents: str | None
    salary_to_amount_in_cents: str | None
    hide_salary: str | None
    cv_requirement: str
    cover_letter_requirement: str
    phone_requirement: str
    photo_requirement: str
    preview_token: str | None
    url: str | None
    salary_period: JobPostingSalaryPeriod
    published_at: datetime.datetime | None
    created_at: datetime.datetime


class _JobPostingRootModel(pydantic.RootModel):
    root: list[JobPosting]


class JobPostingEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/job_postings'

    async def all(self, **kwargs) -> list[JobPosting]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-job-postings."""
        return _JobPostingRootModel.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, job_posting_id: int, **kwargs) -> JobPosting: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[JobPosting], _common.Meta]: ...

    async def get(self, *, job_posting_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-job-postings-id."""
        result = await self.api.get(self.endpoint, job_posting_id, **kwargs)
        return (
            JobPosting.model_validate(result)
            if job_posting_id is not None
            else (
                _JobPostingRootModel.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )


class Message(pydantic.BaseModel):
    id: int
    content: str
    ats_conversation_id: int
    sent_by_id: int
    sent_by_type: str
    created_at: datetime.datetime
    attachments: list[typing.Any]  # TODO: what is the attachment model?
    topic: str
    delayed_until: datetime.datetime | None
    sent_at: datetime.datetime | None
    delivered_at: datetime.datetime | None
    opened_at: datetime.datetime | None
    last_error_at: datetime.datetime | None


class _MessageRoot(pydantic.RootModel):
    root: list[Message]


class MessageEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/messages'

    async def all(self, **kwargs) -> list[Message]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-messages."""
        return _MessageRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, evaluation_form_id: int, **kwargs) -> Message: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[Message], _common.Meta]: ...

    async def get(self, *, evaluation_form_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-messages-id."""
        result = await self.api.get(self.endpoint, evaluation_form_id, **kwargs)
        return (
            Message.model_validate(result)
            if evaluation_form_id is not None
            else (_MessageRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta']))
        )


class RejectReasonDecisionMaker(enum.StrEnum):
    company = 'company'
    candidate = 'candidate'


class RejectReason(pydantic.BaseModel):
    id: int
    company_id: int
    decision_maker: RejectReasonDecisionMaker
    reason: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class _RejectReasonRoot(pydantic.RootModel):
    root: list[RejectReason]


class RejectReasonEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/ats/rejection_reasons'

    async def all(self, **kwargs) -> list[RejectReason]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-rejection-reasons."""
        return _RejectReasonRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, reject_reason_id: int, **kwargs) -> RejectReason: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[RejectReason], _common.Meta]: ...

    async def get(self, *, reject_reason_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-ats-rejection-reasons-id."""
        result = await self.api.get(self.endpoint, reject_reason_id, **kwargs)
        return (
            RejectReason.model_validate(result)
            if reject_reason_id is not None
            else (
                _RejectReasonRoot.model_validate(result).root,
                _common.Meta.model_validate(result['meta']),
            )
        )
