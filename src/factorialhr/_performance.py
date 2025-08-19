import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class AgreementStatus(StrEnum):
    """Enum for agreement status."""

    PENDING = 'pending'
    SIGNED = 'signed'


class ReviewerStrategy(StrEnum):
    """Enum for reviewer strategy types."""

    SELF = 'self'
    MANAGER = 'manager'
    DIRECT_REPORTS = 'direct_reports'
    PEERS = 'peers'


class EvaluationType(StrEnum):
    """Enum for evaluation types."""

    SELF = 'self'
    MANAGER = 'manager'
    DIRECT_REPORTS = 'direct_reports'
    PEERS = 'peers'


class EvaluationStatus(StrEnum):
    """Enum for evaluation status."""

    PENDING = 'pending'
    PUBLISHED = 'published'


class ProcessStatus(StrEnum):
    """Enum for review process status."""

    DRAFT = 'draft'
    SCHEDULED = 'scheduled'
    ACTIVE = 'active'
    FINISHED = 'finished'


class StartValidationError(StrEnum):
    """Enum for start validation errors."""

    MISSING_DEADLINE = 'missing_deadline'
    INVALID_DEADLINE = 'invalid_deadline'
    MISSING_TITLE = 'missing_title'
    MISSING_TARGET_STRATEGY = 'missing_target_strategy'
    MISSING_TARGET_STRATEGY_MEMBERS = 'missing_target_strategy_members'
    MISSING_REVIEWER_STRATEGY = 'missing_reviewer_strategy'
    MISSING_QUESTIONS = 'missing_questions'
    MISSING_POTENTIAL_REVIEWERS = 'missing_potential_reviewers'
    INVALID_SECTION_WEIGHTS_SUM = 'invalid_section_weights_sum'


class Agreement(pydantic.BaseModel):
    """Model for performance_agreement."""

    id: str = pydantic.Field(description='Action plan ID')
    process_id: int = pydantic.Field(description='Review process ID')
    target_id: str = pydantic.Field(description='Review process target ID')
    signer_id: int | None = pydantic.Field(default=None, description='Manager access ID who signed the action plan')
    reviewer_id: int | None = pydantic.Field(default=None, description='Manager employee ID')
    manager_signed_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the manager signed the action plan',
    )
    target_signed_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the employee signed the action plan',
    )
    agreement_signed_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the action plan was last signed',
    )
    last_modified_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the action plan was last modified',
    )
    status: AgreementStatus = pydantic.Field(description='Action plan status')
    locked: bool = pydantic.Field(
        description='When the action plan cannot be edited anymore. Locked when both manager and employee signed it',
    )
    conclusions: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Conclusions of the action plan',
    )
    self_evaluation_id: int | None = pydantic.Field(default=None, description='Self review evaluation ID')
    manager_evaluation_id: int | None = pydantic.Field(default=None, description='Manager review evaluation ID')
    self_comments: Sequence[Mapping[str, typing.Any]] = pydantic.Field(description='Self comments by question')
    manager_comments: Sequence[Mapping[str, typing.Any]] = pydantic.Field(description='Manager comments by question')


class CompanyEmployeeScoreScale(pydantic.BaseModel):
    """Model for performance_company_employee_score_scale."""

    id: int = pydantic.Field(description='Company ID')
    scale_id: int = pydantic.Field(description='Employee score scale ID')
    is_default: bool = pydantic.Field(description='Default employee score scale')


class EmployeeScoreScale(pydantic.BaseModel):
    """Model for performance_employee_score_scale."""

    id: int = pydantic.Field(description='Employee score scale ID')
    scale: Sequence[typing.Any] = pydantic.Field(description='Scale to be used when scoring the employee performance')
    is_default: bool = pydantic.Field(description='Whether this is the default score scale')


class ReviewEmployeeScore(pydantic.BaseModel):
    """Model for performance_review_employee_score."""

    id: int = pydantic.Field(description='Review employee score ID')
    review_process_id: int = pydantic.Field(description='Review process ID')
    review_evaluation_id: int = pydantic.Field(description='Review evaluation ID')
    target_access_id: int = pydantic.Field(description='Employee access ID')
    company_id: int = pydantic.Field(description='Company identifier of the review employee score')
    reviewer_strategy: ReviewerStrategy = pydantic.Field(description='Who scored the employee')
    review_process_target_id: str = pydantic.Field(
        description='Review process target ID (composed with review_process_id and target_access_id)',
    )
    potential_score: int | None = pydantic.Field(
        default=None,
        description='Employee potential score within the min and max scale',
    )
    normalized_potential_score: float | None = pydantic.Field(
        default=None,
        description='Employee potential score in percentage (0% to 100%)',
    )
    score: float = pydantic.Field(description='Employee score within the min and max scale')
    scale_min: int = pydantic.Field(description='Minimum score in the scale')
    scale_max: int = pydantic.Field(description='Maximum score in the scale')
    normalized_score: float = pydantic.Field(description='Employee score in percentage (0% to 100%)')
    comment: str | None = pydantic.Field(default=None, description='Comment about the employee score')
    published_at: datetime.datetime = pydantic.Field(description='Date and time when the employee score was published')


class ReviewEvaluation(pydantic.BaseModel):
    """Model for performance_review_evaluation."""

    id: int = pydantic.Field(description='Evaluation ID')
    performance_review_process_id: int | None = pydantic.Field(default=None, description='Review process ID')
    target_access_id: int | None = pydantic.Field(default=None, description='Participant access ID')
    reviewer_access_id: int | None = pydantic.Field(default=None, description='Reviewer access ID')
    evaluation_type: EvaluationType = pydantic.Field(description='Evaluation type')
    published: bool = pydantic.Field(description='Whether the evaluation is published')
    status: EvaluationStatus = pydantic.Field(description='Evaluation status')
    review_process_target_id: str = pydantic.Field(description='Review process target identifier')
    published_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the evaluation was published',
    )


class ReviewEvaluationAnswer(pydantic.BaseModel):
    """Model for performance_review_evaluation_answer."""

    id: int = pydantic.Field(description='Review evaluation ID')
    performance_review_evaluation_id: int = pydantic.Field(description='Review evaluation ID')
    answered_questionnaire_with_sections: Mapping[str, typing.Any] = pydantic.Field(
        description='List of questions and their respective answers grouped by section',
    )
    answered_employee_score_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for getting employee score',
    )
    answered_employee_potential_score_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for getting the employee potential score',
    )


class ReviewOwner(pydantic.BaseModel):
    """Model for performance_review_owner."""

    id: int = pydantic.Field(description='Review owner ID')
    access_id: int = pydantic.Field(description='Review owner access ID')
    performance_review_process_id: int = pydantic.Field(description='Review process ID')


class ReviewProcess(pydantic.BaseModel):
    """Model for performance_review_process."""

    id: int = pydantic.Field(description='Review process ID')
    company_id: int = pydantic.Field(description='Company ID')
    name: str | None = pydantic.Field(default=None, description='Review process name')
    description: str | None = pydantic.Field(default=None, description='A brief description of the review process')
    status: ProcessStatus = pydantic.Field(description='Review process status')
    target_strategy: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description=(
            'Condition that defines the employees that will be evaluated (participants). '
            'Calculated when the review process starts'
        ),
    )
    reviewer_strategies: Sequence[str] | None = pydantic.Field(
        default=None,
        description=(
            'Review types that will be assigned to the review process. '
            "It'll be used to create the evaluations when the process starts"
        ),
    )
    starts_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the review process should start',
    )
    ends_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the review process should end',
    )
    start_validation_errors: Sequence[StartValidationError] = pydantic.Field(
        description='Missing or invalid information to be able to start the review process',
    )
    archived: bool = pydantic.Field(description='Whether the review process is archived or not')
    agreements_configuration: Mapping[str, typing.Any] = pydantic.Field(
        description='Action plans help track goal progress, and facilitate performance review discussions',
    )
    competencies_assessments_configuration: Mapping[str, typing.Any] = pydantic.Field(
        description=(
            'Assess employees based on their assigned competencies through both manager and self-reviews. '
            'Ensure roles with designated competencies are properly set up'
        ),
    )
    last_bulk_reminder: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the last bulk reminder was sent',
    )
    cycle_id: str | None = pydantic.Field(default=None, description='Performance cycle ID')


class ReviewProcessCustomTemplate(pydantic.BaseModel):
    """Model for performance_review_process_custom_template."""

    id: int = pydantic.Field(description='Review process template ID')
    author_id: int | None = pydantic.Field(default=None, description='Author of the custom template')
    company_id: int = pydantic.Field(description='Company ID')
    name: str = pydantic.Field(description='Review process name')
    description: str | None = pydantic.Field(default=None, description='A brief description of the review process')
    template_description: str | None = pydantic.Field(
        default=None,
        description='A brief description of the review process template',
    )
    target_strategy: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description=(
            'Condition that defines the employees that will be evaluated (participants). '
            'Calculated when the review process starts'
        ),
    )
    reviewer_strategies: Sequence[str] | None = pydantic.Field(
        default=None,
        description=(
            'Review types that will be assigned to the review process. '
            "It'll be used to create the evaluations when the process starts"
        ),
    )
    agreements_enabled: bool | None = pydantic.Field(
        default=None,
        description='Action plans help track goal progress, and facilitate performance review discussions',
    )
    employee_potential_score_enabled: bool | None = pydantic.Field(
        default=None,
        description=(
            "Include one question at the end of the review to rate participants' potential. "
            'This rating will be reflected in the 9 box grid'
        ),
    )
    competencies_assessments_enabled: bool | None = pydantic.Field(
        default=None,
        description=(
            'Assess employees based on their assigned competencies through both manager and self-reviews. '
            'Ensure roles with designated competencies are properly set up'
        ),
    )
    visibility_settings: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Visibility settings for the custom template',
    )
    created_at: datetime.datetime = pydantic.Field(description='Creation date of the template')


class ReviewProcessEstimatedTarget(pydantic.BaseModel):
    """Model for performance_review_process_estimated_target."""

    id: str = pydantic.Field(description='Process target ID')
    performance_review_process_id: int = pydantic.Field(description='Review process ID')
    access_id: int = pydantic.Field(description='Access ID')
    employee_id: int = pydantic.Field(description='Employee ID')


class ReviewProcessTarget(pydantic.BaseModel):
    """Model for performance_review_process_target."""

    id: str = pydantic.Field(description='Review process target ID')
    access_id: int = pydantic.Field(description='Participant access ID')
    performance_review_process_id: int = pydantic.Field(description='Review process ID')
    materialized_process_target_id: int = pydantic.Field(description='Materialized process target ID')


class ReviewQuestionnairesByStrategy(pydantic.BaseModel):
    """Model for performance_review_questionnaires_by_strategy."""

    id: int = pydantic.Field(description='Review process ID')
    performance_review_process_id: int = pydantic.Field(description='Review process ID')
    default_rating_scale: Sequence[typing.Any] = pydantic.Field(description='Scoring range used in rating questions')
    self_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for self evaluation',
    )
    manager_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for manager evaluation',
    )
    direct_report_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for direct report evaluation',
    )
    peers_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for peers evaluation',
    )
    employee_score_self_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire included in the end of self evaluation to evaluate the employee performance',
    )
    employee_score_manager_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire included in the end of manager evaluation to evaluate the employee performance',
    )
    employee_potential_score_manager_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire included in the end of manager evaluation to evaluate the employee potential',
    )


class ReviewVisibilitySetting(pydantic.BaseModel):
    """Model for performance_review_visibility_setting."""

    id: int = pydantic.Field(description='Review process ID')
    performance_review_process_id: int = pydantic.Field(description='Review process ID')
    restrict_answers_visibility_to_reportees: bool = pydantic.Field(
        description="Employees don't have access to their results when enabled",
    )
    early_access_to_answers_for_managers: bool = pydantic.Field(
        description='Managers can access the results of their reports before deadline when enabled',
    )
    anonymous_peer_evaluation_for_target: bool = pydantic.Field(
        description="Peer evaluations are anonymous when enabled, so employees don't know who reviewed them",
    )


class TargetManager(pydantic.BaseModel):
    """Model for performance_target_manager."""

    id: str = pydantic.Field(description='Manager employee ID')
    performance_review_process_id: int = pydantic.Field(description='Review process ID')
    manager_access_id: int = pydantic.Field(description='Manager access ID')
    manager_full_name: str = pydantic.Field(description='Manager full name')


class AgreementsEndpoint(Endpoint):
    """Endpoint for performance/agreements operations."""

    endpoint = 'performance/agreements'

    async def all(self, **kwargs) -> ListApiResponse[Agreement]:
        """Get all agreements."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Agreement, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Agreement]:
        """Get agreements with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Agreement, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, agreement_id: int | str, **kwargs) -> Agreement:
        """Get a specific agreement by ID."""
        data = await self.api.get(self.endpoint, agreement_id, **kwargs)
        return pydantic.TypeAdapter(Agreement).validate_python(data)

    async def bulk_initiate(self, data: Mapping[str, typing.Any], **kwargs) -> list[Agreement]:
        """Initiate action plans for all direct reports in a review process."""
        response = await self.api.post(self.endpoint, 'bulk_initiate', json=data, **kwargs)
        return [pydantic.TypeAdapter(Agreement).validate_python(item) for item in response]

    async def initiate(self, data: Mapping[str, typing.Any], **kwargs) -> Agreement:
        """Initiate an action plan for a specific review process target."""
        response = await self.api.post(self.endpoint, 'initiate', json=data, **kwargs)
        return pydantic.TypeAdapter(Agreement).validate_python(response)


class CompanyEmployeeScoreScalesEndpoint(Endpoint):
    """Endpoint for performance/company_employee_score_scales operations."""

    endpoint = 'performance/company_employee_score_scales'

    async def all(self, **kwargs) -> ListApiResponse[CompanyEmployeeScoreScale]:
        """Get all company employee score scales."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=CompanyEmployeeScoreScale, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[CompanyEmployeeScoreScale]:
        """Get company employee score scales with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=CompanyEmployeeScoreScale,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, scale_id: int | str, **kwargs) -> CompanyEmployeeScoreScale:
        """Get a specific company employee score scale by ID."""
        data = await self.api.get(self.endpoint, scale_id, **kwargs)
        return pydantic.TypeAdapter(CompanyEmployeeScoreScale).validate_python(data)

    async def set_scale(self, data: Mapping[str, typing.Any], **kwargs) -> CompanyEmployeeScoreScale:
        """Set the predefined employee score scale for the company."""
        response = await self.api.post(self.endpoint, 'set', json=data, **kwargs)
        return pydantic.TypeAdapter(CompanyEmployeeScoreScale).validate_python(response)


class EmployeeScoreScalesEndpoint(Endpoint):
    """Endpoint for performance/employee_score_scales operations."""

    endpoint = 'performance/employee_score_scales'

    async def all(self, **kwargs) -> ListApiResponse[EmployeeScoreScale]:
        """Get all employee score scales."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=EmployeeScoreScale, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[EmployeeScoreScale]:
        """Get employee score scales with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=EmployeeScoreScale, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, scale_id: int | str, **kwargs) -> EmployeeScoreScale:
        """Get a specific employee score scale by ID."""
        data = await self.api.get(self.endpoint, scale_id, **kwargs)
        return pydantic.TypeAdapter(EmployeeScoreScale).validate_python(data)


class ReviewEmployeeScoresEndpoint(Endpoint):
    """Endpoint for performance/review_employee_scores operations."""

    endpoint = 'performance/review_employee_scores'

    async def all(self, **kwargs) -> ListApiResponse[ReviewEmployeeScore]:
        """Get all review employee scores."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewEmployeeScore, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewEmployeeScore]:
        """Get review employee scores with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewEmployeeScore, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, score_id: int | str, **kwargs) -> ReviewEmployeeScore:
        """Get a specific review employee score by ID."""
        data = await self.api.get(self.endpoint, score_id, **kwargs)
        return pydantic.TypeAdapter(ReviewEmployeeScore).validate_python(data)


class ReviewEvaluationsEndpoint(Endpoint):
    """Endpoint for performance/review_evaluations operations."""

    endpoint = 'performance/review_evaluations'

    async def all(self, **kwargs) -> ListApiResponse[ReviewEvaluation]:
        """Get all review evaluations."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewEvaluation, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewEvaluation]:
        """Get review evaluations with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewEvaluation, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, evaluation_id: int | str, **kwargs) -> ReviewEvaluation:
        """Get a specific review evaluation by ID."""
        data = await self.api.get(self.endpoint, evaluation_id, **kwargs)
        return pydantic.TypeAdapter(ReviewEvaluation).validate_python(data)

    async def replace_reviewer(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewEvaluation:
        """Replace a reviewer for an evaluation."""
        response = await self.api.post(self.endpoint, 'replace_reviewer', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewEvaluation).validate_python(response)


class ReviewEvaluationAnswersEndpoint(Endpoint):
    """Endpoint for performance/review_evaluation_answers operations."""

    endpoint = 'performance/review_evaluation_answers'

    async def all(self, **kwargs) -> ListApiResponse[ReviewEvaluationAnswer]:
        """Get all review evaluation answers."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewEvaluationAnswer, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewEvaluationAnswer]:
        """Get review evaluation answers with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewEvaluationAnswer, raw_meta=response['meta'], raw_data=response['data'])


class ReviewOwnersEndpoint(Endpoint):
    """Endpoint for performance/review_owners operations."""

    endpoint = 'performance/review_owners'

    async def all(self, **kwargs) -> ListApiResponse[ReviewOwner]:
        """Get all review owners."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewOwner, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewOwner]:
        """Get review owners with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewOwner, raw_meta=response['meta'], raw_data=response['data'])

    async def delete(self, owner_id: int | str, **kwargs) -> ReviewOwner:
        """Delete a review owner."""
        response = await self.api.delete(self.endpoint, owner_id, **kwargs)
        return pydantic.TypeAdapter(ReviewOwner).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> list[ReviewOwner]:
        """Add multiple owners to a review process."""
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return [pydantic.TypeAdapter(ReviewOwner).validate_python(item) for item in response]


class ReviewProcessesEndpoint(Endpoint):
    """Endpoint for performance/review_processes operations."""

    endpoint = 'performance/review_processes'

    async def all(self, **kwargs) -> ListApiResponse[ReviewProcess]:
        """Get all review processes."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewProcess, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewProcess]:
        """Get review processes with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewProcess, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, process_id: int | str, **kwargs) -> ReviewProcess:
        """Get a specific review process by ID."""
        data = await self.api.get(self.endpoint, process_id, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Create a new review process."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def delete(self, process_id: int | str, **kwargs) -> ReviewProcess:
        """Delete a review process."""
        response = await self.api.delete(self.endpoint, process_id, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def create_from_template(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Create a new review process from a template."""
        response = await self.api.post(self.endpoint, 'create_from_template', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def duplicate(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Duplicate an existing review process."""
        response = await self.api.post(self.endpoint, 'duplicate', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def remind_in_bulk(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Send bulk reminders to reviewers."""
        response = await self.api.post(self.endpoint, 'remind_in_bulk', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def remove_schedule(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Remove the schedule job for a review process."""
        response = await self.api.post(self.endpoint, 'remove_schedule', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def reopen(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Reopen a finished review process."""
        response = await self.api.post(self.endpoint, 'reopen', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def schedule(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Schedule a review process to start at a given date."""
        response = await self.api.post(self.endpoint, 'schedule', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def start(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Start a review process."""
        response = await self.api.post(self.endpoint, 'start', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def stop(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Stop a review process."""
        response = await self.api.post(self.endpoint, 'stop', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def toggle_archive(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Archive or unarchive a review process."""
        response = await self.api.post(self.endpoint, 'toggle_archive', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_agreements_configuration(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Enable or disable action plans in a review process."""
        response = await self.api.post(self.endpoint, 'update_agreements_configuration', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_basic_info(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update the basic information of a review process."""
        response = await self.api.post(self.endpoint, 'update_basic_info', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_competencies_assessments_configuration(
        self,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> ReviewProcess:
        """Update competencies assessments configuration."""
        response = await self.api.post(
            self.endpoint,
            'update_competencies_assessments_configuration',
            json=data,
            **kwargs,
        )
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_deadline(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update the deadline of a review process."""
        response = await self.api.post(self.endpoint, 'update_deadline', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_employee_score_configuration(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update employee score configuration."""
        response = await self.api.post(self.endpoint, 'update_employee_score_configuration', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_reviewer_strategies(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update the review types of a review process."""
        response = await self.api.post(self.endpoint, 'update_reviewer_strategies', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_schedule(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update the starting date of a scheduled review process."""
        response = await self.api.post(self.endpoint, 'update_schedule', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_target_strategy(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update the criteria for calculating the participants of a review process."""
        response = await self.api.post(self.endpoint, 'update_target_strategy', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)


class ReviewProcessCustomTemplatesEndpoint(Endpoint):
    """Endpoint for performance/review_process_custom_templates operations."""

    endpoint = 'performance/review_process_custom_templates'

    async def all(self, **kwargs) -> ListApiResponse[ReviewProcessCustomTemplate]:
        """Get all review process custom templates."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewProcessCustomTemplate, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewProcessCustomTemplate]:
        """Get review process custom templates with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=ReviewProcessCustomTemplate,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, template_id: int | str, **kwargs) -> ReviewProcessCustomTemplate:
        """Get a specific review process custom template by ID."""
        data = await self.api.get(self.endpoint, template_id, **kwargs)
        return pydantic.TypeAdapter(ReviewProcessCustomTemplate).validate_python(data)


class ReviewProcessEstimatedTargetsEndpoint(Endpoint):
    """Endpoint for performance/review_process_estimated_targets operations."""

    endpoint = 'performance/review_process_estimated_targets'

    async def all(self, **kwargs) -> ListApiResponse[ReviewProcessEstimatedTarget]:
        """Get all review process estimated targets."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewProcessEstimatedTarget, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewProcessEstimatedTarget]:
        """Get review process estimated targets with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=ReviewProcessEstimatedTarget,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )


class ReviewProcessTargetsEndpoint(Endpoint):
    """Endpoint for performance/review_process_targets operations."""

    endpoint = 'performance/review_process_targets'

    async def all(self, **kwargs) -> ListApiResponse[ReviewProcessTarget]:
        """Get all review process targets."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewProcessTarget, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewProcessTarget]:
        """Get review process targets with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewProcessTarget, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, target_id: str, **kwargs) -> ReviewProcessTarget:
        """Get a specific review process target by ID."""
        data = await self.api.get(self.endpoint, target_id, **kwargs)
        return pydantic.TypeAdapter(ReviewProcessTarget).validate_python(data)

    async def delete(self, target_id: str, **kwargs) -> ReviewProcessTarget:
        """Delete a participant from the active review process."""
        response = await self.api.delete(self.endpoint, target_id, **kwargs)
        return pydantic.TypeAdapter(ReviewProcessTarget).validate_python(response)

    async def add_peers(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcessTarget:
        """Assign peers to evaluate a specific participant."""
        response = await self.api.post(self.endpoint, 'add_peers', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcessTarget).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> list[ReviewProcessTarget]:
        """Add multiple participants to the active review process."""
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return [pydantic.TypeAdapter(ReviewProcessTarget).validate_python(item) for item in response]

    async def remove_peer_evaluations(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcessTarget:
        """Remove peers and their evaluations from a specific participant."""
        response = await self.api.post(self.endpoint, 'remove_peer_evaluations', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcessTarget).validate_python(response)


class ReviewQuestionnaireByStrategiesEndpoint(Endpoint):
    """Endpoint for performance/review_questionnaire_by_strategies operations."""

    endpoint = 'performance/review_questionnaire_by_strategies'

    async def all(self, **kwargs) -> ListApiResponse[ReviewQuestionnairesByStrategy]:
        """Get all review questionnaires by strategies."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewQuestionnairesByStrategy, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewQuestionnairesByStrategy]:
        """Get review questionnaires by strategies with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=ReviewQuestionnairesByStrategy,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, questionnaire_id: int | str, **kwargs) -> ReviewQuestionnairesByStrategy:
        """Get a specific review questionnaire by strategy by ID."""
        data = await self.api.get(self.endpoint, questionnaire_id, **kwargs)
        return pydantic.TypeAdapter(ReviewQuestionnairesByStrategy).validate_python(data)

    async def update_default_rating_scale(
        self,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> ReviewQuestionnairesByStrategy:
        """Update the scoring range used in rating questions for all reviewer strategies."""
        response = await self.api.post(self.endpoint, 'update_default_rating_scale', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewQuestionnairesByStrategy).validate_python(response)

    async def update_questionnaire_for_strategy(
        self,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> ReviewQuestionnairesByStrategy:
        """Update the review process questionnaire for a specific reviewer strategy."""
        response = await self.api.post(
            self.endpoint,
            'update_questionnaire_for_strategy',
            json=data,
            **kwargs,
        )
        return pydantic.TypeAdapter(ReviewQuestionnairesByStrategy).validate_python(response)


class ReviewVisibilitySettingsEndpoint(Endpoint):
    """Endpoint for performance/review_visibility_settings operations."""

    endpoint = 'performance/review_visibility_settings'

    async def all(self, **kwargs) -> ListApiResponse[ReviewVisibilitySetting]:
        """Get all review visibility settings."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewVisibilitySetting, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewVisibilitySetting]:
        """Get review visibility settings with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewVisibilitySetting, raw_meta=response['meta'], raw_data=response['data'])

    async def update(self, setting_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ReviewVisibilitySetting:
        """Update the visibility settings of a review process."""
        response = await self.api.put(self.endpoint, setting_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewVisibilitySetting).validate_python(response)


class TargetManagersEndpoint(Endpoint):
    """Endpoint for performance/target_managers operations."""

    endpoint = 'performance/target_managers'

    async def all(self, **kwargs) -> ListApiResponse[TargetManager]:
        """Get all target managers."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=TargetManager, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[TargetManager]:
        """Get target managers with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=TargetManager, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, manager_id: int | str, **kwargs) -> TargetManager:
        """Get a specific target manager by ID."""
        data = await self.api.get(self.endpoint, manager_id, **kwargs)
        return pydantic.TypeAdapter(TargetManager).validate_python(data)
