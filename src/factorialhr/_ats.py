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

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the answer
    id: int = pydantic.Field(description='Identifier of the answer')
    #: Identifier of the question
    ats_question_id: int | None = pydantic.Field(default=None, description='Identifier of the question')
    #: Identifier of the application
    ats_application_id: int = pydantic.Field(description='Identifier of the application')
    #: Question label of the answer
    original_question_label: str = pydantic.Field(description='Question label of the answer')
    #: Value of the answer
    value: str | None = pydantic.Field(default=None, description='Value of the answer')
    #: Original type of the question
    original_question_type: OriginalQuestionType = pydantic.Field(description='Original type of the question')
    #: Created date of the answer
    created_at: datetime.datetime = pydantic.Field(description='Created date of the answer')
    #: Last updated date of the answer
    updated_at: datetime.datetime = pydantic.Field(description='Last updated date of the answer')


class AnswersEndpoint(Endpoint):
    endpoint = 'ats/answers'

    async def all(self, **kwargs) -> ListApiResponse[Answer]:
        """Get all answers.

        Official documentation: `ats/answers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-answers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of answers.
        :rtype: ListApiResponse[Answer]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Answer, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Answer]:
        """Get answers with pagination metadata.

        Official documentation: `ats/answers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-answers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing answers and pagination metadata.
        :rtype: MetaApiResponse[Answer]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Answer)

    async def get_by_id(self, answer_id: int | str, **kwargs) -> Answer:
        """Get a specific answer by ID.

        Official documentation: `ats/answers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-answers>`_

        :param answer_id: The unique identifier of the answer.
        :type answer_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The answer record.
        :rtype: Answer
        """
        data = await self.api.get(self.endpoint, answer_id, **kwargs)
        return pydantic.TypeAdapter(Answer).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Answer:
        """Create an answer.

        Official documentation: `ats/answers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-answers>`_

        :param data: Payload for the new answer (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created answer record.
        :rtype: Answer
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Answer).validate_python(response)


class Application(pydantic.BaseModel):
    """Model for ats_application."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Id of the application
    id: int = pydantic.Field(description='Id of the application')
    #: Company id of the application
    company_id: int = pydantic.Field(description='Company id of the application')
    #: Job posting id of the application
    ats_job_posting_id: int = pydantic.Field(description='Job posting id of the application')
    #: Candidate id of the application
    ats_candidate_id: int = pydantic.Field(description='Candidate id of the application')
    #: Employee id of the application
    employee_id: int | None = pydantic.Field(default=None, description='Employee id of the application')
    #: Candidate phone of the application
    phone: str | None = pydantic.Field(default=None, description='Candidate phone of the application')
    #: Qualified of the application
    qualified: bool | None = pydantic.Field(default=None, description='Qualified of the application')
    #: Application phase id
    ats_application_phase_id: int | None = pydantic.Field(default=None, description='Application phase id')
    #: Application created at date
    created_at: datetime.datetime = pydantic.Field(description='Application created at date')
    #: Application cover letter
    cover_letter: str | None = pydantic.Field(default=None, description='Application cover letter')
    #: Application conversation id
    ats_conversation_id: int | None = pydantic.Field(default=None, description='Application conversation id')
    #: Application medium
    medium: str | None = pydantic.Field(default=None, description='Application medium')
    #: Application average rating
    rating_average: int | None = pydantic.Field(default=None, description='Application average rating')
    #: Application rejection reason id
    ats_rejection_reason_id: int | None = pydantic.Field(default=None, description='Application rejection reason id')
    #: Application source id
    source_id: int | None = pydantic.Field(default=None, description='Application source id')


class ApplicationsEndpoint(Endpoint):
    endpoint = 'ats/applications'

    async def all(self, **kwargs) -> ListApiResponse[Application]:
        """Get all applications.

        Official documentation: `ats/applications <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-applications>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of applications.
        :rtype: ListApiResponse[Application]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Application)

    async def get(self, **kwargs) -> MetaApiResponse[Application]:
        """Get applications with pagination metadata.

        Official documentation: `ats/applications <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-applications>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing applications and pagination metadata.
        :rtype: MetaApiResponse[Application]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Application)

    async def get_by_id(self, application_id: int | str, **kwargs) -> Application:
        """Get a specific application by ID.

        Official documentation: `ats/applications <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-applications>`_

        :param application_id: The unique identifier of the application.
        :type application_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The application record.
        :rtype: Application
        """
        data = await self.api.get(self.endpoint, application_id, **kwargs)
        return pydantic.TypeAdapter(Application).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Application:
        """Create an application.

        Official documentation: `ats/applications <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-applications>`_

        :param data: Payload for the new application (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created application record.
        :rtype: Application
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Application).validate_python(response)

    async def update(self, application_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Application:
        """Update an application.

        Official documentation: `ats/applications <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-applications>`_

        :param application_id: The unique identifier of the application to update.
        :type application_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated application record.
        :rtype: Application
        """
        response = await self.api.put(self.endpoint, application_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Application).validate_python(response)

    async def delete(self, application_id: int | str, **kwargs) -> Application:
        """Delete an application.

        Official documentation: `ats/applications <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-applications>`_

        :param application_id: The unique identifier of the application to delete.
        :type application_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted application record.
        :rtype: Application
        """
        response = await self.api.delete(self.endpoint, application_id, **kwargs)
        return pydantic.TypeAdapter(Application).validate_python(response)

    async def apply(self, data: Mapping[str, typing.Any], **kwargs) -> Application:
        """Apply to an application.

        Official documentation: `ats/applications <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-applications>`_

        :param data: Payload for the apply action (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The application record resulting from the apply action.
        :rtype: Application
        """
        response = await self.api.post(self.endpoint, 'apply', json=data, **kwargs)
        return pydantic.TypeAdapter(Application).validate_python(response)


class ApplicationPhase(pydantic.BaseModel):
    """Model for ats_application_phase."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the application Phase
    id: int = pydantic.Field(description='Identifier of the application Phase')
    #: Job posting of the application phase
    ats_job_posting_id: int = pydantic.Field(description='Job posting of the application phase')
    #: Name of the application phase
    name: str = pydantic.Field(description='Name of the application phase')
    #: Position of the application phase
    position: int = pydantic.Field(description='Position of the application phase')
    #: If the application phase is editable
    editable: bool = pydantic.Field(description='If the application phase is editable')
    #: Application phase type
    phase_type: PhaseType = pydantic.Field(description='Application phase type')
    #: Active application count
    applications_count: int | None = pydantic.Field(default=None, description='Active application count')
    #: Active applications count
    active_applications_count: int | None = pydantic.Field(default=None, description='Active applications count')
    #: Hiring stage identifier
    ats_hiring_stage_id: int | None = pydantic.Field(default=None, description='Hiring stage identifier')


class ApplicationPhasesEndpoint(Endpoint):
    endpoint = 'ats/application_phases'

    async def all(self, **kwargs) -> ListApiResponse[ApplicationPhase]:
        """Get all application phases.

        Official documentation: `ats/application_phases <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-application-phases>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of application phases.
        :rtype: ListApiResponse[ApplicationPhase]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=ApplicationPhase)

    async def get(self, **kwargs) -> MetaApiResponse[ApplicationPhase]:
        """Get application phases with pagination metadata.

        Official documentation: `ats/application_phases <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-application-phases>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing application phases and pagination metadata.
        :rtype: MetaApiResponse[ApplicationPhase]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=ApplicationPhase)

    async def get_by_id(self, application_phase_id: int | str, **kwargs) -> ApplicationPhase:
        """Get a single application phase by ID.

        Official documentation: `ats/application_phases <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-application-phases>`_

        :param application_phase_id: The unique identifier of the application phase.
        :type application_phase_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The application phase record.
        :rtype: ApplicationPhase
        """
        data = await self.api.get(self.endpoint, application_phase_id, **kwargs)
        return pydantic.TypeAdapter(ApplicationPhase).validate_python(data)


class Candidate(pydantic.BaseModel):
    """Model for ats_candidate."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the candidate
    id: int = pydantic.Field(description='Identifier of the candidate')
    #: Company identifier
    company_id: int | None = pydantic.Field(default=None, description='Company identifier')
    #: Name of the candidate
    first_name: str = pydantic.Field(description='Name of the candidate')
    #: Last name of the candidate
    last_name: str = pydantic.Field(description='Last name of the candidate')
    #: Full name of the candidate
    full_name: str = pydantic.Field(description='Full name of the candidate')
    #: Email of the candidate
    email: str | None = pydantic.Field(default=None, description='Email of the candidate')
    #: Is the candidate part of talent pool?
    talent_pool: bool = pydantic.Field(description='Is the candidate part of talent pool?')
    #: Phone number of the candidate
    phone_number: str | None = pydantic.Field(default=None, description='Phone number of the candidate')
    #: Creation date of the candidate
    created_at: datetime.datetime = pydantic.Field(description='Creation date of the candidate')
    #: Last update of the candidate
    updated_at: datetime.datetime = pydantic.Field(description='Last update of the candidate')
    #: Date when the consent was given
    consent_given_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the consent was given',
    )
    #: Date when the candidate became inactive
    inactive_since: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the candidate became inactive',
    )
    #: List of job posting identifiers
    ats_job_posting_ids: Sequence[int] | None = pydantic.Field(
        default=None,
        description='List of job posting identifiers',
    )
    #: Personal web resource from the candidate
    personal_url: str | None = pydantic.Field(default=None, description='Personal web resource from the candidate')
    #: Date when the consent expires
    consent_expiration_date: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the consent expires',
    )
    #: Consent to talent pool
    consent_to_talent_pool: bool | None = pydantic.Field(default=None, description='Consent to talent pool')
    #: Specifies additional details related to the source of the candidate, such as the referrer name for example if the
    #: source is referred
    medium: str | None = pydantic.Field(
        default=None,
        description=(
            'Specifies additional details related to the source of the candidate, '
            'such as the referrer name for example if the source is referred'
        ),
    )
    #: Candidate source identifier, refers to ats/candidate_sources endpoint
    source_id: int | None = pydantic.Field(
        default=None,
        description='Candidate source identifier, refers to ats/candidate_sources endpoint',
    )
    #: Gender of the candidate
    gender: Gender | None = pydantic.Field(default=None, description='Gender of the candidate')
    #: Score of the candidate
    score: float | None = pydantic.Field(default=None, description='Score of the candidate')


class CandidatesEndpoint(Endpoint):
    endpoint = 'ats/candidates'

    async def all(self, **kwargs) -> ListApiResponse[Candidate]:
        """Get all candidates.

        Official documentation: `ats/candidates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-candidates>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of candidates.
        :rtype: ListApiResponse[Candidate]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Candidate)

    async def get(self, **kwargs) -> MetaApiResponse[Candidate]:
        """Get candidates with pagination metadata.

        Official documentation: `ats/candidates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-candidates>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing candidates and pagination metadata.
        :rtype: MetaApiResponse[Candidate]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Candidate)

    async def get_by_id(self, candidate_id: int | str, **kwargs) -> Candidate:
        """Get a single candidate by ID.

        Official documentation: `ats/candidates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-candidates>`_

        :param candidate_id: The unique identifier of the candidate.
        :type candidate_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The candidate record.
        :rtype: Candidate
        """
        data = await self.api.get(self.endpoint, candidate_id, **kwargs)
        return pydantic.TypeAdapter(Candidate).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Candidate:
        """Create a candidate.

        Official documentation: `ats/candidates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-candidates>`_

        :param data: Payload for the new candidate (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created candidate record.
        :rtype: Candidate
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Candidate).validate_python(response)

    async def update(self, candidate_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Candidate:
        """Update a candidate.

        Official documentation: `ats/candidates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-candidates>`_

        :param candidate_id: The unique identifier of the candidate to update.
        :type candidate_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated candidate record.
        :rtype: Candidate
        """
        response = await self.api.put(self.endpoint, candidate_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Candidate).validate_python(response)

    async def delete(self, candidate_id: int | str, **kwargs) -> Candidate:
        """Delete a candidate.

        Official documentation: `ats/candidates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-candidates>`_

        :param candidate_id: The unique identifier of the candidate to delete.
        :type candidate_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted candidate record.
        :rtype: Candidate
        """
        response = await self.api.delete(self.endpoint, candidate_id, **kwargs)
        return pydantic.TypeAdapter(Candidate).validate_python(response)


class CandidateSource(pydantic.BaseModel):
    """Model for ats_candidate_source."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the source
    id: int = pydantic.Field(description='Identifier of the source')
    #: Identifier of the company
    company_id: int = pydantic.Field(description='Identifier of the company')
    #: Category of the source
    category: CandidateSourceCategory = pydantic.Field(description='Category of the source')
    #: Name of the source
    name: str = pydantic.Field(description='Name of the source')
    #: Translated label of the source if it is a default one, or name otherwise
    label: str = pydantic.Field(
        description='Translated label of the source if it is a default one, or name otherwise',
    )


class CandidateSourcesEndpoint(Endpoint):
    endpoint = 'ats/candidate_sources'

    async def all(self, **kwargs) -> ListApiResponse[CandidateSource]:
        """Get all candidate sources.

        Official documentation: `ats/candidate_sources <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-candidate-sources>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of candidate sources.
        :rtype: ListApiResponse[CandidateSource]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=CandidateSource)

    async def get(self, **kwargs) -> MetaApiResponse[CandidateSource]:
        """Get candidate sources with pagination metadata.

        Official documentation: `ats/candidate_sources <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-candidate-sources>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing candidate sources and pagination metadata.
        :rtype: MetaApiResponse[CandidateSource]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=CandidateSource)

    async def get_by_id(self, candidate_source_id: int | str, **kwargs) -> CandidateSource:
        """Get a single candidate source by ID.

        Official documentation: `ats/candidate_sources <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-candidate-sources>`_

        :param candidate_source_id: The unique identifier of the candidate source.
        :type candidate_source_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The candidate source record.
        :rtype: CandidateSource
        """
        data = await self.api.get(self.endpoint, candidate_source_id, **kwargs)
        return pydantic.TypeAdapter(CandidateSource).validate_python(data)


class EvaluationForm(pydantic.BaseModel):
    """Model for ats_evaluation_form."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Id of the evaluation form
    id: int = pydantic.Field(description='Id of the evaluation form')
    #: Id of the company that the evaluation form belongs to
    company_id: int = pydantic.Field(description='Id of the company that the evaluation form belongs to')
    #: Id of the job posting that the evaluation form is associated with
    ats_job_posting_id: int | None = pydantic.Field(
        default=None,
        description='Id of the job posting that the evaluation form is associated with',
    )
    #: Name of the evaluation form
    name: str = pydantic.Field(description='Name of the evaluation form')
    #: Id of the evaluation form that this evaluation form is related
    based_on_id: int | None = pydantic.Field(
        default=None,
        description='Id of the evaluation form that this evaluation form is related',
    )
    #: List of questions in the evaluation form
    questions: Sequence[typing.Any] = pydantic.Field(description='List of questions in the evaluation form')
    #: Date and time when the evaluation form was created
    created_at: datetime.datetime = pydantic.Field(description='Date and time when the evaluation form was created')
    #: Date and time when the evaluation form was last updated
    updated_at: datetime.datetime = pydantic.Field(
        description='Date and time when the evaluation form was last updated',
    )


class EvaluationFormsEndpoint(Endpoint):
    endpoint = 'ats/evaluation_forms'

    async def all(self, **kwargs) -> ListApiResponse[EvaluationForm]:
        """Get all evaluation forms.

        Official documentation: `ats/evaluation_forms <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-evaluation-forms>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of evaluation forms.
        :rtype: ListApiResponse[EvaluationForm]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=EvaluationForm)

    async def get(self, **kwargs) -> MetaApiResponse[EvaluationForm]:
        """Get evaluation forms with pagination metadata.

        Official documentation: `ats/evaluation_forms <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-evaluation-forms>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing evaluation forms and pagination metadata.
        :rtype: MetaApiResponse[EvaluationForm]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=EvaluationForm)

    async def get_by_id(self, evaluation_form_id: int | str, **kwargs) -> EvaluationForm:
        """Get a single evaluation form by ID.

        Official documentation: `ats/evaluation_forms <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-evaluation-forms>`_

        :param evaluation_form_id: The unique identifier of the evaluation form.
        :type evaluation_form_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The evaluation form record.
        :rtype: EvaluationForm
        """
        data = await self.api.get(self.endpoint, evaluation_form_id, **kwargs)
        return pydantic.TypeAdapter(EvaluationForm).validate_python(data)

    async def save_as_template(self, data: Mapping[str, typing.Any], **kwargs) -> EvaluationForm:
        """Save the evaluation form as a template.

        Official documentation: `ats/evaluation_forms <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-evaluation-forms>`_

        :param data: Payload for saving as template (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The evaluation form record saved as template.
        :rtype: EvaluationForm
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(EvaluationForm).validate_python(response)


class Feedback(pydantic.BaseModel):
    """Model for ats_feedback."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: The ID of the feedback entry
    id: int = pydantic.Field(description='The ID of the feedback entry')
    #: The overall rating from 1 to 5 for the candidate's application
    rating: int | None = pydantic.Field(
        default=None,
        description="The overall rating from 1 to 5 for the candidate's application",
    )
    #: The description of the feedback provided
    description: str | None = pydantic.Field(default=None, description='The description of the feedback provided')
    #: The ID of the application related to the feedback
    ats_application_id: int | None = pydantic.Field(
        default=None,
        description='The ID of the application related to the feedback',
    )
    #: The ID of the phase within the application related to the feedback
    ats_application_phase_id: int | None = pydantic.Field(
        default=None,
        description='The ID of the phase within the application related to the feedback',
    )
    #: The date and time when the feedback entry was created
    created_at: datetime.datetime = pydantic.Field(description='The date and time when the feedback entry was created')
    #: The ID of the candidate to whom the feedback is associated
    ats_candidate_id: int = pydantic.Field(description='The ID of the candidate to whom the feedback is associated')
    #: The ID of the evaluation form to which the feedback belongs if the evaluation forms feature is active
    ats_evaluation_forms_id: int | None = pydantic.Field(
        default=None,
        description=(
            'The ID of the evaluation form to which the feedback belongs if the evaluation forms feature is active'
        ),
    )
    #: The answers from the evaluation form, if this feedback is related to an evaluation form
    evaluation_form_answers: Sequence[typing.Any] | None = pydantic.Field(
        default=None,
        description='The answers from the evaluation form, if this feedback is related to an evaluation form',
    )


class FeedbacksEndpoint(Endpoint):
    endpoint = 'ats/feedbacks'

    async def all(self, **kwargs) -> ListApiResponse[Feedback]:
        """Get all feedbacks.

        Official documentation: `ats/feedbacks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-feedbacks>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of feedbacks.
        :rtype: ListApiResponse[Feedback]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Feedback)

    async def get(self, **kwargs) -> MetaApiResponse[Feedback]:
        """Get feedbacks with pagination metadata.

        Official documentation: `ats/feedbacks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-feedbacks>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing feedbacks and pagination metadata.
        :rtype: MetaApiResponse[Feedback]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Feedback)

    async def get_by_id(self, feedback_id: int | str, **kwargs) -> Feedback:
        """Get a single feedback by ID.

        Official documentation: `ats/feedbacks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-feedbacks>`_

        :param feedback_id: The unique identifier of the feedback.
        :type feedback_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The feedback record.
        :rtype: Feedback
        """
        data = await self.api.get(self.endpoint, feedback_id, **kwargs)
        return pydantic.TypeAdapter(Feedback).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Feedback:
        """Create a feedback.

        Official documentation: `ats/feedbacks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-feedbacks>`_

        :param data: Payload for the new feedback (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created feedback record.
        :rtype: Feedback
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Feedback).validate_python(response)

    async def update(self, feedback_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Feedback:
        """Update a feedback.

        Official documentation: `ats/feedbacks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-feedbacks>`_

        :param feedback_id: The unique identifier of the feedback to update.
        :type feedback_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated feedback record.
        :rtype: Feedback
        """
        response = await self.api.put(self.endpoint, feedback_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Feedback).validate_python(response)

    async def delete(self, feedback_id: int | str, **kwargs) -> Feedback:
        """Delete a feedback.

        Official documentation: `ats/feedbacks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-feedbacks>`_

        :param feedback_id: The unique identifier of the feedback to delete.
        :type feedback_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted feedback record.
        :rtype: Feedback
        """
        response = await self.api.delete(self.endpoint, feedback_id, **kwargs)
        return pydantic.TypeAdapter(Feedback).validate_python(response)


class HiringStage(pydantic.BaseModel):
    """Model for ats_hiring_stage."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the hiring stage
    id: int = pydantic.Field(description='Identifier of the hiring stage')
    #: Name of the hiring stage
    name: HiringStageName = pydantic.Field(description='Name of the hiring stage')
    #: Label of the hiring stage
    label: str = pydantic.Field(description='Label of the hiring stage')
    #: Company identifier of the hiring stage
    company_id: int = pydantic.Field(description='Company identifier of the hiring stage')
    #: Position of the hiring stage
    position: int = pydantic.Field(description='Position of the hiring stage')


class HiringStagesEndpoint(Endpoint):
    endpoint = 'ats/hiring_stages'

    async def all(self, **kwargs) -> ListApiResponse[HiringStage]:
        """Get all hiring stages.

        Official documentation: `ats/hiring_stages <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-hiring-stages>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of hiring stages.
        :rtype: ListApiResponse[HiringStage]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=HiringStage)

    async def get(self, **kwargs) -> MetaApiResponse[HiringStage]:
        """Get hiring stages with pagination metadata.

        Official documentation: `ats/hiring_stages <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-hiring-stages>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing hiring stages and pagination metadata.
        :rtype: MetaApiResponse[HiringStage]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=HiringStage)

    async def get_by_id(self, hiring_stage_id: int | str, **kwargs) -> HiringStage:
        """Get a single hiring stage by ID.

        Official documentation: `ats/hiring_stages <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-hiring-stages>`_

        :param hiring_stage_id: The unique identifier of the hiring stage.
        :type hiring_stage_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The hiring stage record.
        :rtype: HiringStage
        """
        data = await self.api.get(self.endpoint, hiring_stage_id, **kwargs)
        return pydantic.TypeAdapter(HiringStage).validate_python(data)


class JobPosting(pydantic.BaseModel):
    """Model for ats_job_posting."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Unique identifier for the job posting
    id: int = pydantic.Field(description='Unique identifier for the job posting')
    #: Company identifier
    company_id: int = pydantic.Field(description='Company identifier')
    #: Identifier of the ATS company associated with the job posting
    ats_company_id: int = pydantic.Field(description='Identifier of the ATS company associated with the job posting')
    #: Title of the job posting
    title: str = pydantic.Field(description='Title of the job posting')
    #: Description of the job posting
    description: str | None = pydantic.Field(default=None, description='Description of the job posting')
    #: Contract type of the job posting
    contract_type: ContractType | None = pydantic.Field(default=None, description='Contract type of the job posting')
    #: Workplace type of the job posting
    workplace_type: WorkplaceType | None = pydantic.Field(default=None, description='Workplace type of the job posting')
    #: Indicates if the job posting is remote
    remote: bool = pydantic.Field(description='Indicates if the job posting is remote')
    #: The current status of the job posting
    status: JobPostingStatus = pydantic.Field(description='The current status of the job posting')
    #: The schedule type of the job posting
    schedule_type: ScheduleType | None = pydantic.Field(
        default=None,
        description='The schedule type of the job posting',
    )
    #: Identifier of the team associated with the job posting
    team_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the team associated with the job posting',
    )
    #: Identifier of the location associated with the job posting
    location_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the location associated with the job posting',
    )
    #: Identifier of the legal entity associated with the job posting
    legal_entity_id: int | None = pydantic.Field(
        default=None,
        description='Identifier of the legal entity associated with the job posting',
    )
    #: The format of the salary
    salary_format: SalaryFormat | None = pydantic.Field(default=None, description='The format of the salary')
    #: The minimum salary amount in cents
    salary_from_amount_in_cents: int | None = pydantic.Field(
        default=None,
        description='The minimum salary amount in cents',
    )
    #: The maximum salary amount in cents
    salary_to_amount_in_cents: int | None = pydantic.Field(
        default=None,
        description='The maximum salary amount in cents',
    )
    #: Indicates whether the salary information for the job posting should be hidden from applicants
    hide_salary: bool | None = pydantic.Field(
        default=None,
        description='Indicates whether the salary information for the job posting should be hidden from applicants',
    )
    #: Requirement for the CV
    cv_requirement: RequirementLevel = pydantic.Field(description='Requirement for the CV')
    #: Requirement for the cover letter
    cover_letter_requirement: RequirementLevel = pydantic.Field(description='Requirement for the cover letter')
    #: Requirement for the phone number
    phone_requirement: RequirementLevel = pydantic.Field(description='Requirement for the phone number')
    #: Requirement for the photo
    photo_requirement: RequirementLevel = pydantic.Field(description='Requirement for the photo')
    #: Preview token for the job posting
    preview_token: str | None = pydantic.Field(default=None, description='Preview token for the job posting')
    #: If published, the public URL of the job posting. Otherwise will be null
    url: str | None = pydantic.Field(
        default=None,
        description='If published, the public URL of the job posting. Otherwise will be null',
    )
    #: Salary period
    salary_period: SalaryPeriod = pydantic.Field(description='Salary period')
    #: Published date in ISO 8601 format of the job. If never been published the value will be null
    published_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Published date in ISO 8601 format of the job. If never been published the value will be null',
    )
    #: Date in ISO 8601 format when the job posting was created
    created_at: datetime.datetime = pydantic.Field(
        description='Date in ISO 8601 format when the job posting was created',
    )


class JobPostingsEndpoint(Endpoint):
    endpoint = 'ats/job_postings'

    async def all(self, **kwargs) -> ListApiResponse[JobPosting]:
        """Get all job postings.

        Official documentation: `ats/job_postings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-job-postings>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of job postings.
        :rtype: ListApiResponse[JobPosting]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=JobPosting)

    async def get(self, **kwargs) -> MetaApiResponse[JobPosting]:
        """Get job postings with pagination metadata.

        Official documentation: `ats/job_postings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-job-postings>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing job postings and pagination metadata.
        :rtype: MetaApiResponse[JobPosting]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=JobPosting)

    async def get_by_id(self, job_posting_id: int | str, **kwargs) -> JobPosting:
        """Get a single job posting by ID.

        Official documentation: `ats/job_postings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-job-postings>`_

        :param job_posting_id: The unique identifier of the job posting.
        :type job_posting_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The job posting record.
        :rtype: JobPosting
        """
        data = await self.api.get(self.endpoint, job_posting_id, **kwargs)
        return pydantic.TypeAdapter(JobPosting).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> JobPosting:
        """Create a job posting.

        Official documentation: `ats/job_postings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-job-postings>`_

        :param data: Payload for the new job posting (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created job posting record.
        :rtype: JobPosting
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(JobPosting).validate_python(response)

    async def update(self, job_posting_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> JobPosting:
        """Update a job posting.

        Official documentation: `ats/job_postings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-job-postings>`_

        :param job_posting_id: The unique identifier of the job posting to update.
        :type job_posting_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated job posting record.
        :rtype: JobPosting
        """
        response = await self.api.put(self.endpoint, job_posting_id, json=data, **kwargs)
        return pydantic.TypeAdapter(JobPosting).validate_python(response)

    async def delete(self, job_posting_id: int | str, **kwargs) -> JobPosting:
        """Delete a job posting.

        Official documentation: `ats/job_postings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-job-postings>`_

        :param job_posting_id: The unique identifier of the job posting to delete.
        :type job_posting_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted job posting record.
        :rtype: JobPosting
        """
        response = await self.api.delete(self.endpoint, job_posting_id, **kwargs)
        return pydantic.TypeAdapter(JobPosting).validate_python(response)

    async def duplicate(self, data: Mapping[str, typing.Any], **kwargs) -> JobPosting:
        """Duplicate a job posting.

        Official documentation: `ats/job_postings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-job-postings>`_

        :param data: Payload for the duplicate action (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The duplicated job posting record.
        :rtype: JobPosting
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(JobPosting).validate_python(response)


class Message(pydantic.BaseModel):
    """Model for ats_message."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Message identifier
    id: int = pydantic.Field(description='Message identifier')
    #: Message content
    content: str = pydantic.Field(description='Message content')
    #: Conversation identifier
    ats_conversation_id: int = pydantic.Field(description='Conversation identifier')
    #: Sender identifier
    sent_by_id: int = pydantic.Field(description='Sender identifier')
    #: Sender type
    sent_by_type: str = pydantic.Field(description='Sender type')
    #: Message creation date
    created_at: datetime.datetime = pydantic.Field(description='Message creation date')
    #: Message attachments
    attachments: Sequence[typing.Any] = pydantic.Field(description='Message attachments')
    #: Message topic
    topic: str = pydantic.Field(description='Message topic')
    #: Delayed until date
    delayed_until: datetime.datetime | None = pydantic.Field(default=None, description='Delayed until date')
    #: Sent at date
    sent_at: datetime.datetime | None = pydantic.Field(default=None, description='Sent at date')
    #: Delivered at date
    delivered_at: datetime.datetime | None = pydantic.Field(default=None, description='Delivered at date')
    #: Opened at date
    opened_at: datetime.datetime | None = pydantic.Field(default=None, description='Opened at date')
    #: Last error at date
    last_error_at: datetime.datetime | None = pydantic.Field(default=None, description='Last error at date')


class MessagesEndpoint(Endpoint):
    endpoint = 'ats/messages'

    async def all(self, **kwargs) -> ListApiResponse[Message]:
        """Get all messages.

        Official documentation: `ats/messages <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-messages>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of messages.
        :rtype: ListApiResponse[Message]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Message)

    async def get(self, **kwargs) -> MetaApiResponse[Message]:
        """Get messages with pagination metadata.

        Official documentation: `ats/messages <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-messages>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing messages and pagination metadata.
        :rtype: MetaApiResponse[Message]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Message)

    async def get_by_id(self, message_id: int | str, **kwargs) -> Message:
        """Get a single message by ID.

        Official documentation: `ats/messages <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-messages>`_

        :param message_id: The unique identifier of the message.
        :type message_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The message record.
        :rtype: Message
        """
        data = await self.api.get(self.endpoint, message_id, **kwargs)
        return pydantic.TypeAdapter(Message).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Message:
        """Create a message.

        Official documentation: `ats/messages <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-messages>`_

        :param data: Payload for the new message (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created message record.
        :rtype: Message
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Message).validate_python(response)


class Question(pydantic.BaseModel):
    """Model for ats_question."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Question identifier
    id: int = pydantic.Field(description='Question identifier')
    #: Job posting identifier
    ats_job_posting_id: int = pydantic.Field(description='Job posting identifier')
    #: Text of the question
    label: str = pydantic.Field(description='Text of the question')
    #: Position of the question in the list
    position: int = pydantic.Field(description='Position of the question in the list')
    #: Is the question mandatory or not
    mandatory: bool = pydantic.Field(description='Is the question mandatory or not')
    #: If the question autodisqualifies the candidate depending on its response
    auto_disqualify: bool = pydantic.Field(
        description='If the question autodisqualifies the candidate depending on its response',
    )
    #: Type of the question
    question_type: OriginalQuestionType = pydantic.Field(description='Type of the question')
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')
    #: Options for the question
    options: Sequence[typing.Any] | None = pydantic.Field(default=None, description='Options for the question')


class QuestionsEndpoint(Endpoint):
    endpoint = 'ats/questions'

    async def all(self, **kwargs) -> ListApiResponse[Question]:
        """Get all questions.

        Official documentation: `ats/questions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-questions>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of questions.
        :rtype: ListApiResponse[Question]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Question)

    async def get(self, **kwargs) -> MetaApiResponse[Question]:
        """Get questions with pagination metadata.

        Official documentation: `ats/questions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-questions>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing questions and pagination metadata.
        :rtype: MetaApiResponse[Question]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Question)

    async def get_by_id(self, question_id: int | str, **kwargs) -> Question:
        """Get a single question by ID.

        Official documentation: `ats/questions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-questions>`_

        :param question_id: The unique identifier of the question.
        :type question_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The question record.
        :rtype: Question
        """
        data = await self.api.get(self.endpoint, question_id, **kwargs)
        return pydantic.TypeAdapter(Question).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Question:
        """Create a question.

        Official documentation: `ats/questions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-questions>`_

        :param data: Payload for the new question (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created question record.
        :rtype: Question
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Question).validate_python(response)

    async def update(self, question_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Question:
        """Update a question.

        Official documentation: `ats/questions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-questions>`_

        :param question_id: The unique identifier of the question to update.
        :type question_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated question record.
        :rtype: Question
        """
        response = await self.api.put(self.endpoint, question_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Question).validate_python(response)

    async def delete(self, question_id: int | str, **kwargs) -> Question:
        """Delete a question.

        Official documentation: `ats/questions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-questions>`_

        :param question_id: The unique identifier of the question to delete.
        :type question_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted question record.
        :rtype: Question
        """
        response = await self.api.delete(self.endpoint, question_id, **kwargs)
        return pydantic.TypeAdapter(Question).validate_python(response)


class RejectionReason(pydantic.BaseModel):
    """Model for ats_rejection_reason."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Rejection reason identifier
    id: int = pydantic.Field(description='Rejection reason identifier')
    #: Company identifier of the rejection reason
    company_id: int = pydantic.Field(description='Company identifier of the rejection reason')
    #: Decision maker of the rejection reason
    decision_maker: DecisionMaker = pydantic.Field(description='Decision maker of the rejection reason')
    #: Reason of the rejection
    reason: str = pydantic.Field(description='Reason of the rejection')
    #: Rejection reason created date
    created_at: datetime.datetime = pydantic.Field(description='Rejection reason created date')
    #: Rejection reason updated date
    updated_at: datetime.datetime = pydantic.Field(description='Rejection reason updated date')


class RejectionReasonsEndpoint(Endpoint):
    endpoint = 'ats/rejection_reasons'

    async def all(self, **kwargs) -> ListApiResponse[RejectionReason]:
        """Get all rejection reasons.

        Official documentation: `ats/rejection_reasons <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-rejection-reasons>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of rejection reasons.
        :rtype: ListApiResponse[RejectionReason]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=RejectionReason)

    async def get(self, **kwargs) -> MetaApiResponse[RejectionReason]:
        """Get rejection reasons with pagination metadata.

        Official documentation: `ats/rejection_reasons <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-rejection-reasons>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing rejection reasons and pagination metadata.
        :rtype: MetaApiResponse[RejectionReason]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=RejectionReason)

    async def get_by_id(self, rejection_reason_id: int | str, **kwargs) -> RejectionReason:
        """Get a single rejection reason by ID.

        Official documentation: `ats/rejection_reasons <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-ats-rejection-reasons>`_

        :param rejection_reason_id: The unique identifier of the rejection reason.
        :type rejection_reason_id: int | str
        :param kwargs: Optional keyword arguments forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The rejection reason record.
        :rtype: RejectionReason
        """
        data = await self.api.get(self.endpoint, rejection_reason_id, **kwargs)
        return pydantic.TypeAdapter(RejectionReason).validate_python(data)
