import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class OriginalQuestionType(StrEnum):
    """Enum for ATS question types."""

    TEXT = 'text'
    LONG_TEXT = 'long_text'
    SINGLE_CHOICE = 'single_choice'
    MULTIPLE_CHOICE = 'multiple_choice'
    FILE = 'file'


class PhaseType(StrEnum):
    """Enum for ATS application phase types."""

    INITIAL = 'initial'
    NORMAL = 'normal'
    HIRED = 'hired'
    SCREENING = 'screening'
    INTERVIEW = 'interview'
    ASSESSMENT = 'assessment'
    OFFER = 'offer'


class Gender(StrEnum):
    """Enum for candidate gender."""

    FEMALE = 'female'
    MALE = 'male'
    UNANSWERED = 'unanswered'
    OTHER = 'other'


class CandidateSourceCategory(StrEnum):
    """Enum for candidate source categories."""

    JOB_BOARD = 'job_board'
    AGENCY_OR_EXTERNAL_RECRUITER = 'agency_or_external_recruiter'
    EVENT = 'event'
    SOCIAL_MEDIA = 'social_media'
    REFERRAL = 'referral'
    INTERNAL = 'internal'
    MANUALLY_ADDED = 'manually_added'
    ORGANIC = 'organic'
    SYSTEM = 'system'


class HiringStageName(StrEnum):
    """Enum for hiring stage names."""

    NEW = 'new'
    SCREENING = 'screening'
    INTERVIEW = 'interview'
    ASSESSMENT = 'assessment'
    OFFER = 'offer'
    HIRED = 'hired'


class ContractType(StrEnum):
    """Enum for job posting contract types."""

    INDEFINITE = 'indefinite'
    TEMPORARY = 'temporary'
    INTERN = 'intern'
    TRAINING = 'training'
    FREELANCE = 'freelance'
    VENDOR_CONTRACTOR = 'vendor_contractor'
    VOLUNTEER = 'volunteer'
    PER_HOUR = 'per_hour'
    OTHER = 'other'
    ALTERNANT = 'alternant'
    INTERIM = 'interim'
    MINIJOB = 'minijob'
    WERKSTUDENT = 'werkstudent'
    APPRENTICESHIP = 'apprenticeship'
    PJ = 'pj'
    CLT = 'clt'
    JOVEM_APRENDIZ = 'jovem_aprendiz'
    A_TERMO_INCERTO = 'a_termo_incerto'
    A_TERMO_CERTO = 'a_termo_certo'
    DE_CURTA_DURACAO = 'de_curta_duracao'
    DE_MUITA_CURTA_DURACAO = 'de_muita_curta_duracao'
    PROMESSA_DE_TRABALHO = 'promessa_de_trabalho'
    A_TEMPO_PARCIAL = 'a_tempo_parcial'
    COM_PLURALIDADE_DE_EMPREGADORES = 'com_pluralidade_de_empregadores'
    TELETRABALHO = 'teletrabalho'
    PRE_REFORMA = 'pre_reforma'
    RECIBOS_VERDES = 'recibos_verdes'
    ESTAGIO = 'estagio'
    SEM_TERMO = 'sem_termo'
    APPRENTISSAGE = 'apprentissage'
    FIXED_DISCONTINUED = 'fixed_discontinued'
    APPRENDISTATO = 'apprendistato'


class WorkplaceType(StrEnum):
    """Enum for job posting workplace types."""

    ONSITE = 'onsite'
    REMOTE = 'remote'
    HYBRID = 'hybrid'


class JobPostingStatus(StrEnum):
    """Enum for job posting status."""

    DRAFT = 'draft'
    PUBLISHED = 'published'
    UNLISTED = 'unlisted'
    ARCHIVED = 'archived'
    CANCELLED = 'cancelled'


class ScheduleType(StrEnum):
    """Enum for job posting schedule types."""

    FULL_TIME = 'full_time'
    PART_TIME = 'part_time'


class SalaryFormat(StrEnum):
    """Enum for salary format."""

    FIXED_AMOUNT = 'fixed_amount'
    RANGE = 'range'


class RequirementLevel(StrEnum):
    """Enum for requirement levels."""

    MANDATORY = 'mandatory'
    OPTIONAL = 'optional'
    DO_NOT_ASK = 'do_not_ask'


class SalaryPeriod(StrEnum):
    """Enum for salary periods."""

    ANNUAL = 'annual'
    MONTHLY = 'monthly'
    DAILY = 'daily'


class DecisionMaker(StrEnum):
    """Enum for rejection reason decision maker."""

    COMPANY = 'company'
    CANDIDATE = 'candidate'


class Answer(pydantic.BaseModel):
    """Model for ats_answer."""

    id: int = pydantic.Field(description='Identifier of the answer')
    ats_question_id: int | None = pydantic.Field(default=None, description='Identifier of the question')
    ats_application_id: int = pydantic.Field(description='Identifier of the application')
    original_question_label: str = pydantic.Field(description='Question label of the answer')
    value: str | None = pydantic.Field(default=None, description='Value of the answer')
    original_question_type: OriginalQuestionType = pydantic.Field(description='Original type of the question')
    created_at: datetime.datetime = pydantic.Field(description='Created date of the answer')
    updated_at: datetime.datetime = pydantic.Field(description='Last updated date of the answer')


class AnswersEndpoint(Endpoint):
    endpoint = '/ats/answers'

    async def all(self, **kwargs) -> ListApiResponse[Answer]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Answer, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Answer]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Answer)

    async def get_by_id(self, answer_id: int | str, **kwargs) -> Answer:
        data = await self.api.get(self.endpoint, answer_id, **kwargs)
        return pydantic.TypeAdapter(Answer).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Answer:
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Answer).validate_python(response)


class Application(pydantic.BaseModel):
    """Model for ats_application."""

    id: int = pydantic.Field(description='Id of the application')
    company_id: int = pydantic.Field(description='Company id of the application')
    ats_job_posting_id: int = pydantic.Field(description='Job posting id of the application')
    ats_candidate_id: int = pydantic.Field(description='Candidate id of the application')
    employee_id: int | None = pydantic.Field(default=None, description='Employee id of the application')
    phone: str | None = pydantic.Field(default=None, description='Candidate phone of the application')
    qualified: bool | None = pydantic.Field(default=None, description='Qualified of the application')
    ats_application_phase_id: int | None = pydantic.Field(default=None, description='Application phase id')
    created_at: datetime.datetime = pydantic.Field(description='Application created at date')
    cover_letter: str | None = pydantic.Field(default=None, description='Application cover letter')
    ats_conversation_id: int | None = pydantic.Field(default=None, description='Application conversation id')
    medium: str | None = pydantic.Field(default=None, description='Application medium')
    rating_average: int | None = pydantic.Field(default=None, description='Application average rating')
    ats_rejection_reason_id: int | None = pydantic.Field(default=None, description='Application rejection reason id')
    source_id: int | None = pydantic.Field(default=None, description='Application source id')


class ApplicationsEndpoint(Endpoint):
    endpoint = '/ats/applications'

    async def all(self, **kwargs) -> ListApiResponse[Application]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Application)

    async def get(self, **kwargs) -> MetaApiResponse[Application]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Application)

    async def get_by_id(self, application_id: int | str, **kwargs) -> Application:
        data = await self.api.get(self.endpoint, application_id, **kwargs)
        return pydantic.TypeAdapter(Application).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Application:
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Application).validate_python(response)

    async def update(self, application_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Application:
        response = await self.api.put(self.endpoint, application_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Application).validate_python(response)

    async def delete(self, application_id: int | str, **kwargs) -> Application:
        response = await self.api.delete(self.endpoint, application_id, **kwargs)
        return pydantic.TypeAdapter(Application).validate_python(response)

    async def apply(self, data: Mapping[str, typing.Any], **kwargs) -> Application:
        response = await self.api.post(self.endpoint, 'apply', json=data, **kwargs)
        return pydantic.TypeAdapter(Application).validate_python(response)


class ApplicationPhase(pydantic.BaseModel):
    """Model for ats_application_phase."""

    id: int = pydantic.Field(description='Identifier of the application Phase')
    ats_job_posting_id: int = pydantic.Field(description='Job posting of the application phase')
    name: str = pydantic.Field(description='Name of the application phase')
    position: int = pydantic.Field(description='Position of the application phase')
    editable: bool = pydantic.Field(description='If the application phase is editable')
    phase_type: PhaseType = pydantic.Field(description='Application phase type')
    applications_count: int | None = pydantic.Field(default=None, description='Active application count')
    active_applications_count: int | None = pydantic.Field(default=None, description='Active applications count')
    ats_hiring_stage_id: int | None = pydantic.Field(default=None, description='Hiring stage identifier')


class ApplicationPhasesEndpoint(Endpoint):
    endpoint = '/ats/application_phases'

    async def all(self, **kwargs) -> ListApiResponse[ApplicationPhase]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=ApplicationPhase)

    async def get(self, **kwargs) -> MetaApiResponse[ApplicationPhase]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=ApplicationPhase)

    async def get_by_id(self, application_phase_id: int | str, **kwargs) -> ApplicationPhase:
        data = await self.api.get(self.endpoint, application_phase_id, **kwargs)
        return pydantic.TypeAdapter(ApplicationPhase).validate_python(data)


class Candidate(pydantic.BaseModel):
    """Model for ats_candidate."""

    id: int = pydantic.Field(description='Identifier of the candidate')
    company_id: int | None = pydantic.Field(default=None, description='Company identifier')
    first_name: str = pydantic.Field(description='Name of the candidate')
    last_name: str = pydantic.Field(description='Last name of the candidate')
    full_name: str = pydantic.Field(description='Full name of the candidate')
    email: str | None = pydantic.Field(default=None, description='Email of the candidate')
    talent_pool: bool = pydantic.Field(description='Is the candidate part of talent pool?')
    phone_number: str | None = pydantic.Field(default=None, description='Phone number of the candidate')
    created_at: datetime.datetime = pydantic.Field(description='Creation date of the candidate')
    updated_at: datetime.datetime = pydantic.Field(description='Last update of the candidate')
    consent_given_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the consent was given',
    )
    inactive_since: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the candidate became inactive',
    )
    ats_job_posting_ids: Sequence[int] | None = pydantic.Field(
        default=None,
        description='List of job posting identifiers',
    )
    personal_url: str | None = pydantic.Field(default=None, description='Personal web resource from the candidate')
    consent_expiration_date: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the consent expires',
    )
    consent_to_talent_pool: bool | None = pydantic.Field(default=None, description='Consent to talent pool')
    medium: str | None = pydantic.Field(
        default=None,
        description=(
            'Specifies additional details related to the source of the candidate, '
            'such as the referrer name for example if the source is referred'
        ),
    )
    source_id: int | None = pydantic.Field(
        default=None,
        description='Candidate source identifier, refers to ats/candidate_sources endpoint',
    )
    gender: Gender | None = pydantic.Field(default=None, description='Gender of the candidate')
    score: float | None = pydantic.Field(default=None, description='Score of the candidate')


class CandidatesEndpoint(Endpoint):
    endpoint = '/ats/candidates'

    async def all(self, **kwargs) -> ListApiResponse[Candidate]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Candidate)

    async def get(self, **kwargs) -> MetaApiResponse[Candidate]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Candidate)

    async def get_by_id(self, candidate_id: int | str, **kwargs) -> Candidate:
        data = await self.api.get(self.endpoint, candidate_id, **kwargs)
        return pydantic.TypeAdapter(Candidate).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Candidate:
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Candidate).validate_python(response)

    async def update(self, candidate_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Candidate:
        response = await self.api.put(self.endpoint, candidate_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Candidate).validate_python(response)

    async def delete(self, candidate_id: int | str, **kwargs) -> Candidate:
        response = await self.api.delete(self.endpoint, candidate_id, **kwargs)
        return pydantic.TypeAdapter(Candidate).validate_python(response)


class CandidateSource(pydantic.BaseModel):
    """Model for ats_candidate_source."""

    id: int = pydantic.Field(description='Identifier of the source')
    company_id: int = pydantic.Field(description='Identifier of the company')
    category: CandidateSourceCategory = pydantic.Field(description='Category of the source')
    name: str = pydantic.Field(description='Name of the source')
    label: str = pydantic.Field(
        description='Translated label of the source if it is a default one, or name otherwise',
    )


class CandidateSourcesEndpoint(Endpoint):
    endpoint = '/ats/candidate_sources'

    async def all(self, **kwargs) -> ListApiResponse[CandidateSource]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=CandidateSource)

    async def get(self, **kwargs) -> MetaApiResponse[CandidateSource]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=CandidateSource)

    async def get_by_id(self, candidate_source_id: int | str, **kwargs) -> CandidateSource:
        data = await self.api.get(self.endpoint, candidate_source_id, **kwargs)
        return pydantic.TypeAdapter(CandidateSource).validate_python(data)


class EvaluationForm(pydantic.BaseModel):
    """Model for ats_evaluation_form."""

    id: int = pydantic.Field(description='Id of the evaluation form')
    company_id: int = pydantic.Field(description='Id of the company that the evaluation form belongs to')
    ats_job_posting_id: int | None = pydantic.Field(
        default=None,
        description='Id of the job posting that the evaluation form is associated with',
    )
    name: str = pydantic.Field(description='Name of the evaluation form')
    based_on_id: int | None = pydantic.Field(
        default=None,
        description='Id of the evaluation form that this evaluation form is related',
    )
    questions: Sequence[typing.Any] = pydantic.Field(description='List of questions in the evaluation form')
    created_at: datetime.datetime = pydantic.Field(description='Date and time when the evaluation form was created')
    updated_at: datetime.datetime = pydantic.Field(
        description='Date and time when the evaluation form was last updated',
    )


class EvaluationFormsEndpoint(Endpoint):
    endpoint = '/ats/evaluation_forms'

    async def all(self, **kwargs) -> ListApiResponse[EvaluationForm]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=EvaluationForm)

    async def get(self, **kwargs) -> MetaApiResponse[EvaluationForm]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=EvaluationForm)

    async def get_by_id(self, evaluation_form_id: int | str, **kwargs) -> EvaluationForm:
        data = await self.api.get(self.endpoint, evaluation_form_id, **kwargs)
        return pydantic.TypeAdapter(EvaluationForm).validate_python(data)

    async def save_as_template(self, data: Mapping[str, typing.Any], **kwargs) -> EvaluationForm:
        response = await self.api.post(self.endpoint, 'save_as_template', json=data, **kwargs)
        return pydantic.TypeAdapter(EvaluationForm).validate_python(response)


class Feedback(pydantic.BaseModel):
    """Model for ats_feedback."""

    id: int = pydantic.Field(description='The ID of the feedback entry')
    rating: int | None = pydantic.Field(
        default=None,
        description="The overall rating from 1 to 5 for the candidate's application",
    )
    description: str | None = pydantic.Field(default=None, description='The description of the feedback provided')
    ats_application_id: int | None = pydantic.Field(
        default=None,
        description='The ID of the application related to the feedback',
    )
    ats_application_phase_id: int | None = pydantic.Field(
        default=None,
        description='The ID of the phase within the application related to the feedback',
    )
    created_at: datetime.datetime = pydantic.Field(description='The date and time when the feedback entry was created')
    ats_candidate_id: int = pydantic.Field(description='The ID of the candidate to whom the feedback is associated')
    ats_evaluation_forms_id: int | None = pydantic.Field(
        default=None,
        description=(
            'The ID of the evaluation form to which the feedback belongs if the evaluation forms feature is active'
        ),
    )
    evaluation_form_answers: Sequence[typing.Any] | None = pydantic.Field(
        default=None,
        description='The answers from the evaluation form, if this feedback is related to an evaluation form',
    )


class FeedbacksEndpoint(Endpoint):
    endpoint = '/ats/feedbacks'

    async def all(self, **kwargs) -> ListApiResponse[Feedback]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Feedback)

    async def get(self, **kwargs) -> MetaApiResponse[Feedback]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Feedback)

    async def get_by_id(self, feedback_id: int | str, **kwargs) -> Feedback:
        data = await self.api.get(self.endpoint, feedback_id, **kwargs)
        return pydantic.TypeAdapter(Feedback).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Feedback:
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Feedback).validate_python(response)

    async def update(self, feedback_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Feedback:
        response = await self.api.put(self.endpoint, feedback_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Feedback).validate_python(response)

    async def delete(self, feedback_id: int | str, **kwargs) -> Feedback:
        response = await self.api.delete(self.endpoint, feedback_id, **kwargs)
        return pydantic.TypeAdapter(Feedback).validate_python(response)


class HiringStage(pydantic.BaseModel):
    """Model for ats_hiring_stage."""

    id: int = pydantic.Field(description='Identifier of the hiring stage')
    name: HiringStageName = pydantic.Field(description='Name of the hiring stage')
    label: str = pydantic.Field(description='Label of the hiring stage')
    company_id: int = pydantic.Field(description='Company identifier of the hiring stage')
    position: int = pydantic.Field(description='Position of the hiring stage')


class HiringStagesEndpoint(Endpoint):
    endpoint = '/ats/hiring_stages'

    async def all(self, **kwargs) -> ListApiResponse[HiringStage]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=HiringStage)

    async def get(self, **kwargs) -> MetaApiResponse[HiringStage]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=HiringStage)

    async def get_by_id(self, hiring_stage_id: int | str, **kwargs) -> HiringStage:
        data = await self.api.get(self.endpoint, hiring_stage_id, **kwargs)
        return pydantic.TypeAdapter(HiringStage).validate_python(data)


class JobPosting(pydantic.BaseModel):
    """Model for ats_job_posting."""

    id: int = pydantic.Field(description='Unique identifier for the job posting')
    company_id: int = pydantic.Field(description='Company identifier')
    ats_company_id: int = pydantic.Field(description='Identifier of the ATS company associated with the job posting')
    title: str = pydantic.Field(description='Title of the job posting')
    description: str | None = pydantic.Field(default=None, description='Description of the job posting')
    contract_type: ContractType | None = pydantic.Field(default=None, description='Contract type of the job posting')
    workplace_type: WorkplaceType | None = pydantic.Field(default=None, description='Workplace type of the job posting')
    remote: bool = pydantic.Field(description='Indicates if the job posting is remote')
    status: JobPostingStatus = pydantic.Field(description='The current status of the job posting')
    schedule_type: ScheduleType | None = pydantic.Field(
        default=None,
        description='The schedule type of the job posting',
    )
    team_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the team associated with the job posting',
    )
    location_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the location associated with the job posting',
    )
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the legal entity associated with the job posting',
    )
    salary_format: SalaryFormat | None = pydantic.Field(default=None, description='The format of the salary')
    salary_from_amount_in_cents: int | None = pydantic.Field(
        default=None,
        description='The minimum salary amount in cents',
    )
    salary_to_amount_in_cents: int | None = pydantic.Field(
        default=None,
        description='The maximum salary amount in cents',
    )
    hide_salary: bool | None = pydantic.Field(
        default=None,
        description='Indicates whether the salary information for the job posting should be hidden from applicants',
    )
    cv_requirement: RequirementLevel = pydantic.Field(description='Requirement for the CV')
    cover_letter_requirement: RequirementLevel = pydantic.Field(description='Requirement for the cover letter')
    phone_requirement: RequirementLevel = pydantic.Field(description='Requirement for the phone number')
    photo_requirement: RequirementLevel = pydantic.Field(description='Requirement for the photo')
    preview_token: str | None = pydantic.Field(default=None, description='Preview token for the job posting')
    url: str | None = pydantic.Field(
        default=None,
        description='If published, the public URL of the job posting. Otherwise will be null',
    )
    salary_period: SalaryPeriod = pydantic.Field(description='Salary period')
    published_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Published date in ISO 8601 format of the job. If never been published the value will be null',
    )
    created_at: datetime.datetime = pydantic.Field(
        description='Date in ISO 8601 format when the job posting was created',
    )


class JobPostingsEndpoint(Endpoint):
    endpoint = '/ats/job_postings'

    async def all(self, **kwargs) -> ListApiResponse[JobPosting]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=JobPosting)

    async def get(self, **kwargs) -> MetaApiResponse[JobPosting]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=JobPosting)

    async def get_by_id(self, job_posting_id: int | str, **kwargs) -> JobPosting:
        data = await self.api.get(self.endpoint, job_posting_id, **kwargs)
        return pydantic.TypeAdapter(JobPosting).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> JobPosting:
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(JobPosting).validate_python(response)

    async def update(self, job_posting_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> JobPosting:
        response = await self.api.put(self.endpoint, job_posting_id, json=data, **kwargs)
        return pydantic.TypeAdapter(JobPosting).validate_python(response)

    async def delete(self, job_posting_id: int | str, **kwargs) -> JobPosting:
        response = await self.api.delete(self.endpoint, job_posting_id, **kwargs)
        return pydantic.TypeAdapter(JobPosting).validate_python(response)

    async def duplicate(self, data: Mapping[str, typing.Any], **kwargs) -> JobPosting:
        response = await self.api.post(self.endpoint, 'duplicate', json=data, **kwargs)
        return pydantic.TypeAdapter(JobPosting).validate_python(response)


class Message(pydantic.BaseModel):
    """Model for ats_message."""

    id: int = pydantic.Field(description='Message identifier')
    content: str = pydantic.Field(description='Message content')
    ats_conversation_id: int = pydantic.Field(description='Conversation identifier')
    sent_by_id: int = pydantic.Field(description='Sender identifier')
    sent_by_type: str = pydantic.Field(description='Sender type')
    created_at: datetime.datetime = pydantic.Field(description='Message creation date')
    attachments: Sequence[typing.Any] = pydantic.Field(description='Message attachments')
    topic: str = pydantic.Field(description='Message topic')
    delayed_until: datetime.datetime | None = pydantic.Field(default=None, description='Delayed until date')
    sent_at: datetime.datetime | None = pydantic.Field(default=None, description='Sent at date')
    delivered_at: datetime.datetime | None = pydantic.Field(default=None, description='Delivered at date')
    opened_at: datetime.datetime | None = pydantic.Field(default=None, description='Opened at date')
    last_error_at: datetime.datetime | None = pydantic.Field(default=None, description='Last error at date')


class MessagesEndpoint(Endpoint):
    endpoint = '/ats/messages'

    async def all(self, **kwargs) -> ListApiResponse[Message]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Message)

    async def get(self, **kwargs) -> MetaApiResponse[Message]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Message)

    async def get_by_id(self, message_id: int | str, **kwargs) -> Message:
        data = await self.api.get(self.endpoint, message_id, **kwargs)
        return pydantic.TypeAdapter(Message).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Message:
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Message).validate_python(response)


class Question(pydantic.BaseModel):
    """Model for ats_question."""

    id: int = pydantic.Field(description='Question identifier')
    ats_job_posting_id: int = pydantic.Field(description='Job posting identifier')
    label: str = pydantic.Field(description='Text of the question')
    position: int = pydantic.Field(description='Position of the question in the list')
    mandatory: bool = pydantic.Field(description='Is the question mandatory or not')
    auto_disqualify: bool = pydantic.Field(
        description='If the question autodisqualifies the candidate depending on its response',
    )
    question_type: OriginalQuestionType = pydantic.Field(description='Type of the question')
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')
    options: Sequence[typing.Any] | None = pydantic.Field(default=None, description='Options for the question')


class QuestionsEndpoint(Endpoint):
    endpoint = '/ats/questions'

    async def all(self, **kwargs) -> ListApiResponse[Question]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Question)

    async def get(self, **kwargs) -> MetaApiResponse[Question]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Question)

    async def get_by_id(self, question_id: int | str, **kwargs) -> Question:
        data = await self.api.get(self.endpoint, question_id, **kwargs)
        return pydantic.TypeAdapter(Question).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Question:
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Question).validate_python(response)

    async def update(self, question_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Question:
        response = await self.api.put(self.endpoint, question_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Question).validate_python(response)

    async def delete(self, question_id: int | str, **kwargs) -> Question:
        response = await self.api.delete(self.endpoint, question_id, **kwargs)
        return pydantic.TypeAdapter(Question).validate_python(response)


class RejectionReason(pydantic.BaseModel):
    """Model for ats_rejection_reason."""

    id: int = pydantic.Field(description='Rejection reason identifier')
    company_id: int = pydantic.Field(description='Company identifier of the rejection reason')
    decision_maker: DecisionMaker = pydantic.Field(description='Decision maker of the rejection reason')
    reason: str = pydantic.Field(description='Reason of the rejection')
    created_at: datetime.datetime = pydantic.Field(description='Rejection reason created date')
    updated_at: datetime.datetime = pydantic.Field(description='Rejection reason updated date')


class RejectionReasonsEndpoint(Endpoint):
    endpoint = '/ats/rejection_reasons'

    async def all(self, **kwargs) -> ListApiResponse[RejectionReason]:
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=RejectionReason)

    async def get(self, **kwargs) -> MetaApiResponse[RejectionReason]:
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=RejectionReason)

    async def get_by_id(self, rejection_reason_id: int | str, **kwargs) -> RejectionReason:
        data = await self.api.get(self.endpoint, rejection_reason_id, **kwargs)
        return pydantic.TypeAdapter(RejectionReason).validate_python(data)
