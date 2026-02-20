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

    model_config = pydantic.ConfigDict(frozen=True)

    #: Action plan ID
    id: str = pydantic.Field(description='Action plan ID')
    #: Review process ID
    process_id: int = pydantic.Field(description='Review process ID')
    #: Review process target ID
    target_id: str = pydantic.Field(description='Review process target ID')
    #: Manager access ID who signed the action plan
    signer_id: int | None = pydantic.Field(default=None, description='Manager access ID who signed the action plan')
    #: Manager employee ID
    reviewer_id: int | None = pydantic.Field(default=None, description='Manager employee ID')
    #: Date when the manager signed the action plan
    manager_signed_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the manager signed the action plan',
    )
    #: Date when the employee signed the action plan
    target_signed_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the employee signed the action plan',
    )
    #: Date when the action plan was last signed
    agreement_signed_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the action plan was last signed',
    )
    #: Date when the action plan was last modified
    last_modified_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the action plan was last modified',
    )
    #: Action plan status
    status: AgreementStatus = pydantic.Field(description='Action plan status')
    #: When the action plan cannot be edited anymore. Locked when both manager and employee signed it
    locked: bool = pydantic.Field(
        description='When the action plan cannot be edited anymore. Locked when both manager and employee signed it',
    )
    #: Conclusions of the action plan
    conclusions: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Conclusions of the action plan',
    )
    #: Self review evaluation ID
    self_evaluation_id: int | None = pydantic.Field(default=None, description='Self review evaluation ID')
    #: Manager review evaluation ID
    manager_evaluation_id: int | None = pydantic.Field(default=None, description='Manager review evaluation ID')
    #: Self comments by question
    self_comments: Sequence[Mapping[str, typing.Any]] = pydantic.Field(description='Self comments by question')
    #: Manager comments by question
    manager_comments: Sequence[Mapping[str, typing.Any]] = pydantic.Field(description='Manager comments by question')


class CompanyEmployeeScoreScale(pydantic.BaseModel):
    """Model for performance_company_employee_score_scale."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Company ID
    id: int = pydantic.Field(description='Company ID')
    #: Employee score scale ID
    scale_id: int = pydantic.Field(description='Employee score scale ID')
    #: Default employee score scale
    is_default: bool = pydantic.Field(description='Default employee score scale')


class EmployeeScoreScale(pydantic.BaseModel):
    """Model for performance_employee_score_scale."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Employee score scale ID
    id: int = pydantic.Field(description='Employee score scale ID')
    #: Scale to be used when scoring the employee performance
    scale: Sequence[typing.Any] = pydantic.Field(description='Scale to be used when scoring the employee performance')
    #: Whether this is the default score scale
    is_default: bool = pydantic.Field(description='Whether this is the default score scale')


class ReviewEvaluationScore(pydantic.BaseModel):
    """Model for performance_review_evaluation_score."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Review evaluation score identifier
    id: int = pydantic.Field(description='Review evaluation score identifier')
    #: Review evaluation identifier
    review_evaluation_id: int = pydantic.Field(description='Review evaluation identifier')
    #: Evaluation score
    score: float = pydantic.Field(description='Evaluation score')
    #: Creation date
    created_at: datetime.datetime = pydantic.Field(description='Creation date')
    #: Last update date
    updated_at: datetime.datetime = pydantic.Field(description='Last update date')


class ReviewEvaluation(pydantic.BaseModel):
    """Model for performance_review_evaluation."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Evaluation ID
    id: int = pydantic.Field(description='Evaluation ID')
    #: Review process ID
    performance_review_process_id: int | None = pydantic.Field(default=None, description='Review process ID')
    #: Participant access ID
    target_access_id: int | None = pydantic.Field(default=None, description='Participant access ID')
    #: Reviewer access ID
    reviewer_access_id: int | None = pydantic.Field(default=None, description='Reviewer access ID')
    #: Evaluation type
    evaluation_type: EvaluationType = pydantic.Field(description='Evaluation type')
    #: Whether the evaluation is published
    published: bool = pydantic.Field(description='Whether the evaluation is published')
    #: Evaluation status
    status: EvaluationStatus = pydantic.Field(description='Evaluation status')
    #: Review process target identifier
    review_process_target_id: str = pydantic.Field(description='Review process target identifier')
    #: Date when the evaluation was published
    published_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the evaluation was published',
    )


class ReviewEvaluationAnswer(pydantic.BaseModel):
    """Model for performance_review_evaluation_answer."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Review evaluation ID
    id: int = pydantic.Field(description='Review evaluation ID')
    #: Review evaluation ID
    performance_review_evaluation_id: int = pydantic.Field(description='Review evaluation ID')
    #: List of questions and their respective answers grouped by section
    answered_questionnaire_with_sections: Mapping[str, typing.Any] = pydantic.Field(
        description='List of questions and their respective answers grouped by section',
    )
    #: Questionnaire for getting employee score
    answered_employee_score_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for getting employee score',
    )
    #: Questionnaire for getting the employee potential score
    answered_employee_potential_score_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for getting the employee potential score',
    )


class ReviewOwner(pydantic.BaseModel):
    """Model for performance_review_owner."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Review owner ID
    id: int = pydantic.Field(description='Review owner ID')
    #: Review owner access ID
    access_id: int = pydantic.Field(description='Review owner access ID')
    #: Review process ID
    performance_review_process_id: int = pydantic.Field(description='Review process ID')


class ReviewProcess(pydantic.BaseModel):
    """Model for performance_review_process."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Review process ID
    id: int = pydantic.Field(description='Review process ID')
    #: Company ID
    company_id: int = pydantic.Field(description='Company ID')
    #: Review process name
    name: str | None = pydantic.Field(default=None, description='Review process name')
    #: A brief description of the review process
    description: str | None = pydantic.Field(default=None, description='A brief description of the review process')
    #: Review process status
    status: ProcessStatus = pydantic.Field(description='Review process status')
    #: Condition that defines the employees that will be evaluated (participants). Calculated when the review process
    #: starts
    target_strategy: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description=(
            'Condition that defines the employees that will be evaluated (participants). '
            'Calculated when the review process starts'
        ),
    )
    #: Review types that will be assigned to the review process. It'll be used to create the evaluations when the
    #: process starts
    reviewer_strategies: Sequence[str] | None = pydantic.Field(
        default=None,
        description=(
            'Review types that will be assigned to the review process. '
            "It'll be used to create the evaluations when the process starts"
        ),
    )
    #: Date when the review process should start
    starts_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the review process should start',
    )
    #: Date when the review process should end
    ends_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the review process should end',
    )
    #: Missing or invalid information to be able to start the review process
    start_validation_errors: Sequence[StartValidationError] = pydantic.Field(
        description='Missing or invalid information to be able to start the review process',
    )
    #: Whether the review process is archived or not
    archived: bool = pydantic.Field(description='Whether the review process is archived or not')
    #: Action plans help track goal progress, and facilitate performance review discussions
    agreements_configuration: Mapping[str, typing.Any] = pydantic.Field(
        description='Action plans help track goal progress, and facilitate performance review discussions',
    )
    #: Assess employees based on their assigned competencies through both manager and self-reviews. Ensure roles with
    #: designated competencies are properly set up
    competencies_assessments_configuration: Mapping[str, typing.Any] = pydantic.Field(
        description=(
            'Assess employees based on their assigned competencies through both manager and self-reviews. '
            'Ensure roles with designated competencies are properly set up'
        ),
    )
    #: Date when the last bulk reminder was sent
    last_bulk_reminder: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the last bulk reminder was sent',
    )
    #: Performance cycle ID
    cycle_id: str | None = pydantic.Field(default=None, description='Performance cycle ID')


class ReviewProcessCustomTemplate(pydantic.BaseModel):
    """Model for performance_review_process_custom_template."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Review process template ID
    id: int = pydantic.Field(description='Review process template ID')
    #: Author of the custom template
    author_id: int | None = pydantic.Field(default=None, description='Author of the custom template')
    #: Company ID
    company_id: int = pydantic.Field(description='Company ID')
    #: Review process name
    name: str = pydantic.Field(description='Review process name')
    #: A brief description of the review process
    description: str | None = pydantic.Field(default=None, description='A brief description of the review process')
    #: A brief description of the review process template
    template_description: str | None = pydantic.Field(
        default=None,
        description='A brief description of the review process template',
    )
    #: Condition that defines the employees that will be evaluated (participants). Calculated when the review process
    #: starts
    target_strategy: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description=(
            'Condition that defines the employees that will be evaluated (participants). '
            'Calculated when the review process starts'
        ),
    )
    #: Review types that will be assigned to the review process. It'll be used to create the evaluations when the
    #: process starts
    reviewer_strategies: Sequence[str] | None = pydantic.Field(
        default=None,
        description=(
            'Review types that will be assigned to the review process. '
            "It'll be used to create the evaluations when the process starts"
        ),
    )
    #: Action plans help track goal progress, and facilitate performance review discussions
    agreements_enabled: bool | None = pydantic.Field(
        default=None,
        description='Action plans help track goal progress, and facilitate performance review discussions',
    )
    #: Include one question at the end of the review to rate participants' potential. This rating will be reflected in
    #: the 9 box grid
    employee_potential_score_enabled: bool | None = pydantic.Field(
        default=None,
        description=(
            "Include one question at the end of the review to rate participants' potential. "
            'This rating will be reflected in the 9 box grid'
        ),
    )
    #: Assess employees based on their assigned competencies through both manager and self-reviews. Ensure roles with
    #: designated competencies are properly set up
    competencies_assessments_enabled: bool | None = pydantic.Field(
        default=None,
        description=(
            'Assess employees based on their assigned competencies through both manager and self-reviews. '
            'Ensure roles with designated competencies are properly set up'
        ),
    )
    #: Visibility settings for the custom template
    visibility_settings: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Visibility settings for the custom template',
    )
    #: Creation date of the template
    created_at: datetime.datetime = pydantic.Field(description='Creation date of the template')


class ReviewProcessEstimatedTarget(pydantic.BaseModel):
    """Model for performance_review_process_estimated_target."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Process target ID
    id: str = pydantic.Field(description='Process target ID')
    #: Review process ID
    performance_review_process_id: int = pydantic.Field(description='Review process ID')
    #: Access ID
    access_id: int = pydantic.Field(description='Access ID')
    #: Employee ID
    employee_id: int = pydantic.Field(description='Employee ID')


class ReviewProcessTarget(pydantic.BaseModel):
    """Model for performance_review_process_target."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Review process target ID
    id: str = pydantic.Field(description='Review process target ID')
    #: Participant access ID
    access_id: int = pydantic.Field(description='Participant access ID')
    #: Review process ID
    performance_review_process_id: int = pydantic.Field(description='Review process ID')
    #: Materialized process target ID
    materialized_process_target_id: int = pydantic.Field(description='Materialized process target ID')


class ReviewQuestionnairesByStrategy(pydantic.BaseModel):
    """Model for performance_review_questionnaires_by_strategy."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Review process ID
    id: int = pydantic.Field(description='Review process ID')
    #: Review process ID
    performance_review_process_id: int = pydantic.Field(description='Review process ID')
    #: Scoring range used in rating questions
    default_rating_scale: Sequence[typing.Any] = pydantic.Field(description='Scoring range used in rating questions')
    #: Questionnaire for self evaluation
    self_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for self evaluation',
    )
    #: Questionnaire for manager evaluation
    manager_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for manager evaluation',
    )
    #: Questionnaire for direct report evaluation
    direct_report_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for direct report evaluation',
    )
    #: Questionnaire for peers evaluation
    peers_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire for peers evaluation',
    )
    #: Questionnaire included in the end of self evaluation to evaluate the employee performance
    employee_score_self_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire included in the end of self evaluation to evaluate the employee performance',
    )
    #: Questionnaire included in the end of manager evaluation to evaluate the employee performance
    employee_score_manager_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire included in the end of manager evaluation to evaluate the employee performance',
    )
    #: Questionnaire included in the end of manager evaluation to evaluate the employee potential
    employee_potential_score_manager_questionnaire: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='Questionnaire included in the end of manager evaluation to evaluate the employee potential',
    )


class ReviewVisibilitySetting(pydantic.BaseModel):
    """Model for performance_review_visibility_setting."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Review process ID
    id: int = pydantic.Field(description='Review process ID')
    #: Review process ID
    performance_review_process_id: int = pydantic.Field(description='Review process ID')
    #: Employees don't have access to their results when enabled
    restrict_answers_visibility_to_reportees: bool = pydantic.Field(
        description="Employees don't have access to their results when enabled",
    )
    #: Managers can access the results of their reports before deadline when enabled
    early_access_to_answers_for_managers: bool = pydantic.Field(
        description='Managers can access the results of their reports before deadline when enabled',
    )
    #: Peer evaluations are anonymous when enabled, so employees don't know who reviewed them
    anonymous_peer_evaluation_for_target: bool = pydantic.Field(
        description="Peer evaluations are anonymous when enabled, so employees don't know who reviewed them",
    )


class TargetManager(pydantic.BaseModel):
    """Model for performance_target_manager."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Manager employee ID
    id: str = pydantic.Field(description='Manager employee ID')
    #: Review process ID
    performance_review_process_id: int = pydantic.Field(description='Review process ID')
    #: Manager access ID
    manager_access_id: int = pydantic.Field(description='Manager access ID')
    #: Manager full name
    manager_full_name: str = pydantic.Field(description='Manager full name')


class AgreementsEndpoint(Endpoint):
    """Endpoint for performance/agreements operations."""

    endpoint = 'performance/agreements'

    async def all(self, **kwargs) -> ListApiResponse[Agreement]:
        """Get all agreements.

        Official documentation: `performance/agreements <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-agreements>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Agreement]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Agreement, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Agreement]:
        """Get agreements with pagination metadata.

        Official documentation: `performance/agreements <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-agreements>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Agreement]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Agreement, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, agreement_id: int | str, **kwargs) -> Agreement:
        """Get a specific agreement by ID.

        Official documentation: `performance/agreements <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-agreements-id>`_

        :param agreement_id: The unique identifier.
        :type agreement_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Agreement
        """
        data = await self.api.get(self.endpoint, agreement_id, **kwargs)
        return pydantic.TypeAdapter(Agreement).validate_python(data)

    async def bulk_initiate(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[Agreement]:
        """Initiate action plans for all direct reports in a review process.

        Official documentation: `performance/agreements <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-agreements-bulk-initiate>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[Agreement]
        """
        response = await self.api.post(self.endpoint, 'bulk_initiate', json=data, **kwargs)
        return [pydantic.TypeAdapter(Agreement).validate_python(item) for item in response]

    async def initiate(self, data: Mapping[str, typing.Any], **kwargs) -> Agreement:
        """Initiate an action plan for a specific review process target.

        Official documentation: `performance/agreements <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-agreements-initiate>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Agreement
        """
        response = await self.api.post(self.endpoint, 'initiate', json=data, **kwargs)
        return pydantic.TypeAdapter(Agreement).validate_python(response)


class CompanyEmployeeScoreScalesEndpoint(Endpoint):
    """Endpoint for performance/company_employee_score_scales operations."""

    endpoint = 'performance/company_employee_score_scales'

    async def all(self, **kwargs) -> ListApiResponse[CompanyEmployeeScoreScale]:
        """Get all company employee score scales.

        Official documentation: `performance/company_employee_score_scales <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-company-employee-score-scales>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[CompanyEmployeeScoreScale]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=CompanyEmployeeScoreScale, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[CompanyEmployeeScoreScale]:
        """Get company employee score scales with pagination metadata.

        Official documentation: `performance/company_employee_score_scales <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-company-employee-score-scales>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[CompanyEmployeeScoreScale]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=CompanyEmployeeScoreScale,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, scale_id: int | str, **kwargs) -> CompanyEmployeeScoreScale:
        """Get a specific company employee score scale by ID.

        Official documentation: `performance/company_employee_score_scales <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-company-employee-score-scales-id>`_

        :param scale_id: The unique identifier.
        :type scale_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: CompanyEmployeeScoreScale
        """
        data = await self.api.get(self.endpoint, scale_id, **kwargs)
        return pydantic.TypeAdapter(CompanyEmployeeScoreScale).validate_python(data)

    async def set_scale(self, data: Mapping[str, typing.Any], **kwargs) -> CompanyEmployeeScoreScale:
        """Set the predefined employee score scale for the company.

        Official documentation: `performance/company_employee_score_scales <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-company-employee-score-scales-set>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: CompanyEmployeeScoreScale
        """
        response = await self.api.post(self.endpoint, 'set', json=data, **kwargs)
        return pydantic.TypeAdapter(CompanyEmployeeScoreScale).validate_python(response)


class EmployeeScoreScalesEndpoint(Endpoint):
    """Endpoint for performance/employee_score_scales operations."""

    endpoint = 'performance/employee_score_scales'

    async def all(self, **kwargs) -> ListApiResponse[EmployeeScoreScale]:
        """Get all employee score scales.

        Official documentation: `performance/employee_score_scales <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-employee-score-scales>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[EmployeeScoreScale]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=EmployeeScoreScale, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[EmployeeScoreScale]:
        """Get employee score scales with pagination metadata.

        Official documentation: `performance/employee_score_scales <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-employee-score-scales>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[EmployeeScoreScale]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=EmployeeScoreScale, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, scale_id: int | str, **kwargs) -> EmployeeScoreScale:
        """Get a specific employee score scale by ID.

        Official documentation: `performance/employee_score_scales <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-employee-score-scales-id>`_

        :param scale_id: The unique identifier.
        :type scale_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: EmployeeScoreScale
        """
        data = await self.api.get(self.endpoint, scale_id, **kwargs)
        return pydantic.TypeAdapter(EmployeeScoreScale).validate_python(data)


class ReviewEvaluationScoresEndpoint(Endpoint):
    """Endpoint for performance/review_evaluation_scores operations."""

    endpoint = 'performance/review_evaluation_scores'

    async def all(self, **kwargs) -> ListApiResponse[ReviewEvaluationScore]:
        """Get all review evaluation scores.

        Official documentation: `performance/review_evaluation_scores <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-evaluation-scores>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ReviewEvaluationScore]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewEvaluationScore, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewEvaluationScore]:
        """Get review evaluation scores with pagination metadata.

        Official documentation: `performance/review_evaluation_scores <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-evaluation-scores>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ReviewEvaluationScore]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewEvaluationScore, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, score_id: int | str, **kwargs) -> ReviewEvaluationScore:
        """Get a specific review evaluation score by ID.

        Official documentation: `performance/review_evaluation_scores <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-evaluation-scores-id>`_

        :param score_id: The unique identifier.
        :type score_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ReviewEvaluationScore
        """
        data = await self.api.get(self.endpoint, score_id, **kwargs)
        return pydantic.TypeAdapter(ReviewEvaluationScore).validate_python(data)


class ReviewEvaluationsEndpoint(Endpoint):
    """Endpoint for performance/review_evaluations operations."""

    endpoint = 'performance/review_evaluations'

    async def all(self, **kwargs) -> ListApiResponse[ReviewEvaluation]:
        """Get all review evaluations.

        Official documentation: `performance/review_evaluations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-evaluations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ReviewEvaluation]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewEvaluation, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewEvaluation]:
        """Get review evaluations with pagination metadata.

        Official documentation: `performance/review_evaluations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-evaluations>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ReviewEvaluation]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewEvaluation, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, evaluation_id: int | str, **kwargs) -> ReviewEvaluation:
        """Get a specific review evaluation by ID.

        Official documentation: `performance/review_evaluations <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-evaluations-id>`_

        :param evaluation_id: The unique identifier.
        :type evaluation_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ReviewEvaluation
        """
        data = await self.api.get(self.endpoint, evaluation_id, **kwargs)
        return pydantic.TypeAdapter(ReviewEvaluation).validate_python(data)

    async def replace_reviewer(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewEvaluation:
        """Replace a reviewer for an evaluation.

        Official documentation: `performance/review_evaluations <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-evaluations-replace-reviewer>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewEvaluation
        """
        response = await self.api.post(self.endpoint, 'replace_reviewer', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewEvaluation).validate_python(response)


class ReviewEvaluationAnswersEndpoint(Endpoint):
    """Endpoint for performance/review_evaluation_answers operations."""

    endpoint = 'performance/review_evaluation_answers'

    async def all(self, **kwargs) -> ListApiResponse[ReviewEvaluationAnswer]:
        """Get all review evaluation answers.

        Official documentation: `performance/review_evaluation_answers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-evaluation-answers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ReviewEvaluationAnswer]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewEvaluationAnswer, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewEvaluationAnswer]:
        """Get review evaluation answers with pagination metadata.

        Official documentation: `performance/review_evaluation_answers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-evaluation-answers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ReviewEvaluationAnswer]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewEvaluationAnswer, raw_meta=response['meta'], raw_data=response['data'])


class ReviewOwnersEndpoint(Endpoint):
    """Endpoint for performance/review_owners operations."""

    endpoint = 'performance/review_owners'

    async def all(self, **kwargs) -> ListApiResponse[ReviewOwner]:
        """Get all review owners.

        Official documentation: `performance/review_owners <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-owners>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ReviewOwner]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewOwner, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewOwner]:
        """Get review owners with pagination metadata.

        Official documentation: `performance/review_owners <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-owners>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ReviewOwner]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewOwner, raw_meta=response['meta'], raw_data=response['data'])

    async def delete(self, owner_id: int | str, **kwargs) -> ReviewOwner:
        """Delete a review owner.

        Official documentation: `performance/review_owners <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-performance-review-owners-id>`_

        :param owner_id: The unique identifier of the record to delete.
        :type owner_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: ReviewOwner
        """
        response = await self.api.delete(self.endpoint, owner_id, **kwargs)
        return pydantic.TypeAdapter(ReviewOwner).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[ReviewOwner]:
        """Add multiple owners to a review process.

        Official documentation: `performance/review_owners <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-owners-bulk-create>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[ReviewOwner]
        """
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return [pydantic.TypeAdapter(ReviewOwner).validate_python(item) for item in response]


class ReviewProcessesEndpoint(Endpoint):
    """Endpoint for performance/review_processes operations."""

    endpoint = 'performance/review_processes'

    async def all(self, **kwargs) -> ListApiResponse[ReviewProcess]:
        """Get all review processes.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-processes>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ReviewProcess]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewProcess, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewProcess]:
        """Get review processes with pagination metadata.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-processes>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ReviewProcess]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewProcess, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, process_id: int | str, **kwargs) -> ReviewProcess:
        """Get a specific review process by ID.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-processes-id>`_

        :param process_id: The unique identifier.
        :type process_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ReviewProcess
        """
        data = await self.api.get(self.endpoint, process_id, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Create a new review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def delete(self, process_id: int | str, **kwargs) -> ReviewProcess:
        """Delete a review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-performance-review-processes-id>`_

        :param process_id: The unique identifier of the record to delete.
        :type process_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: ReviewProcess
        """
        response = await self.api.delete(self.endpoint, process_id, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def create_from_template(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Create a new review process from a template.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-create-from-template>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'create_from_template', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def duplicate(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Duplicate an existing review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-duplicate>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'duplicate', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def remind_in_bulk(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Send bulk reminders to reviewers.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-remind-in-bulk>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'remind_in_bulk', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def remove_schedule(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Remove the schedule job for a review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-remove-schedule>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'remove_schedule', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def reopen(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Reopen a finished review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-reopen>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'reopen', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def schedule(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Schedule a review process to start at a given date.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-schedule>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'schedule', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def start(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Start a review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-start>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'start', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def stop(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Stop a review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-stop>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'stop', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def toggle_archive(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Archive or unarchive a review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-toggle-archive>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'toggle_archive', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_agreements_configuration(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Enable or disable action plans in a review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-update-agreements-configuration>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'update_agreements_configuration', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_basic_info(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update the basic information of a review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-update-basic-info>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'update_basic_info', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_competencies_assessments_configuration(
        self,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> ReviewProcess:
        """Update competencies assessments configuration.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-update-competencies-assessments-configuration>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(
            self.endpoint,
            'update_competencies_assessments_configuration',
            json=data,
            **kwargs,
        )
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_deadline(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update the deadline of a review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-update-deadline>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'update_deadline', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_employee_score_configuration(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update employee score configuration.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-update-employee-score-configuration>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'update_employee_score_configuration', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_reviewer_strategies(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update the review types of a review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-update-reviewer-strategies>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'update_reviewer_strategies', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_schedule(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update the starting date of a scheduled review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-update-schedule>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'update_schedule', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)

    async def update_target_strategy(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcess:
        """Update the criteria for calculating the participants of a review process.

        Official documentation: `performance/review_processes <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-processes-update-target-strategy>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcess
        """
        response = await self.api.post(self.endpoint, 'update_target_strategy', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcess).validate_python(response)


class ReviewProcessCustomTemplatesEndpoint(Endpoint):
    """Endpoint for performance/review_process_custom_templates operations."""

    endpoint = 'performance/review_process_custom_templates'

    async def all(self, **kwargs) -> ListApiResponse[ReviewProcessCustomTemplate]:
        """Get all review process custom templates.

        Official documentation: `performance/review_process_custom_templates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-process-custom-templates>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ReviewProcessCustomTemplate]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewProcessCustomTemplate, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewProcessCustomTemplate]:
        """Get review process custom templates with pagination metadata.

        Official documentation: `performance/review_process_custom_templates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-process-custom-templates>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ReviewProcessCustomTemplate]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=ReviewProcessCustomTemplate,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, template_id: int | str, **kwargs) -> ReviewProcessCustomTemplate:
        """Get a specific review process custom template by ID.

        Official documentation: `performance/review_process_custom_templates <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-process-custom-templates-id>`_

        :param template_id: The unique identifier.
        :type template_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ReviewProcessCustomTemplate
        """
        data = await self.api.get(self.endpoint, template_id, **kwargs)
        return pydantic.TypeAdapter(ReviewProcessCustomTemplate).validate_python(data)


class ReviewProcessEstimatedTargetsEndpoint(Endpoint):
    """Endpoint for performance/review_process_estimated_targets operations."""

    endpoint = 'performance/review_process_estimated_targets'

    async def all(self, **kwargs) -> ListApiResponse[ReviewProcessEstimatedTarget]:
        """Get all review process estimated targets.

        Official documentation: `performance/review_process_estimated_targets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-process-estimated-targets>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ReviewProcessEstimatedTarget]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewProcessEstimatedTarget, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewProcessEstimatedTarget]:
        """Get review process estimated targets with pagination metadata.

        Official documentation: `performance/review_process_estimated_targets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-process-estimated-targets>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ReviewProcessEstimatedTarget]
        """
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
        """Get all review process targets.

        Official documentation: `performance/review_process_targets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-process-targets>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ReviewProcessTarget]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewProcessTarget, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewProcessTarget]:
        """Get review process targets with pagination metadata.

        Official documentation: `performance/review_process_targets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-process-targets>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ReviewProcessTarget]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewProcessTarget, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, target_id: str, **kwargs) -> ReviewProcessTarget:
        """Get a specific review process target by ID.

        Official documentation: `performance/review_process_targets <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-process-targets-id>`_

        :param target_id: The unique identifier.
        :type target_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ReviewProcessTarget
        """
        data = await self.api.get(self.endpoint, target_id, **kwargs)
        return pydantic.TypeAdapter(ReviewProcessTarget).validate_python(data)

    async def delete(self, target_id: str, **kwargs) -> ReviewProcessTarget:
        """Delete a participant from the active review process.

        Official documentation: `performance/review_process_targets <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-performance-review-process-targets-id>`_

        :param target_id: The unique identifier of the record to delete.
        :type target_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: ReviewProcessTarget
        """
        response = await self.api.delete(self.endpoint, target_id, **kwargs)
        return pydantic.TypeAdapter(ReviewProcessTarget).validate_python(response)

    async def add_peers(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcessTarget:
        """Assign peers to evaluate a specific participant.

        Official documentation: `performance/review_process_targets <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-process-targets-add-peers>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcessTarget
        """
        response = await self.api.post(self.endpoint, 'add_peers', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcessTarget).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[ReviewProcessTarget]:
        """Add multiple participants to the active review process.

        Official documentation: `performance/review_process_targets <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-process-targets-bulk-create>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[ReviewProcessTarget]
        """
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return [pydantic.TypeAdapter(ReviewProcessTarget).validate_python(item) for item in response]

    async def remove_peer_evaluations(self, data: Mapping[str, typing.Any], **kwargs) -> ReviewProcessTarget:
        """Remove peers and their evaluations from a specific participant.

        Official documentation: `performance/review_process_targets <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-process-targets-remove-peer-evaluations>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewProcessTarget
        """
        response = await self.api.post(self.endpoint, 'remove_peer_evaluations', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewProcessTarget).validate_python(response)


class ReviewQuestionnaireByStrategiesEndpoint(Endpoint):
    """Endpoint for performance/review_questionnaire_by_strategies operations."""

    endpoint = 'performance/review_questionnaire_by_strategies'

    async def all(self, **kwargs) -> ListApiResponse[ReviewQuestionnairesByStrategy]:
        """Get all review questionnaires by strategies.

        Official documentation: `performance/review_questionnaire_by_strategies <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-questionnaire-by-strategies>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ReviewQuestionnairesByStrategy]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewQuestionnairesByStrategy, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewQuestionnairesByStrategy]:
        """Get review questionnaires by strategies with pagination metadata.

        Official documentation: `performance/review_questionnaire_by_strategies <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-questionnaire-by-strategies>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ReviewQuestionnairesByStrategy]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=ReviewQuestionnairesByStrategy,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, questionnaire_id: int | str, **kwargs) -> ReviewQuestionnairesByStrategy:
        """Get a specific review questionnaire by strategy by ID.

        Official documentation: `performance/review_questionnaire_by_strategies <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-questionnaire-by-strategies-id>`_

        :param questionnaire_id: The unique identifier.
        :type questionnaire_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ReviewQuestionnairesByStrategy
        """
        data = await self.api.get(self.endpoint, questionnaire_id, **kwargs)
        return pydantic.TypeAdapter(ReviewQuestionnairesByStrategy).validate_python(data)

    async def update_default_rating_scale(
        self,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> ReviewQuestionnairesByStrategy:
        """Update the scoring range used in rating questions for all reviewer strategies.

        Official documentation: `performance/review_questionnaire_by_strategies <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-questionnaire-by-strategies-update-default-rating-scale>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewQuestionnairesByStrategy
        """
        response = await self.api.post(self.endpoint, 'update_default_rating_scale', json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewQuestionnairesByStrategy).validate_python(response)

    async def update_questionnaire_for_strategy(
        self,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> ReviewQuestionnairesByStrategy:
        """Update the review process questionnaire for a specific reviewer strategy.

        Official documentation: `performance/review_questionnaire_by_strategies <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-performance-review-questionnaire-by-strategies-update-questionnaire-for-strategy>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ReviewQuestionnairesByStrategy
        """
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
        """Get all review visibility settings.

        Official documentation: `performance/review_visibility_settings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-visibility-settings>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ReviewVisibilitySetting]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ReviewVisibilitySetting, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ReviewVisibilitySetting]:
        """Get review visibility settings with pagination metadata.

        Official documentation: `performance/review_visibility_settings <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-review-visibility-settings>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ReviewVisibilitySetting]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ReviewVisibilitySetting, raw_meta=response['meta'], raw_data=response['data'])

    async def update(self, setting_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ReviewVisibilitySetting:
        """Update the visibility settings of a review process.

        Official documentation: `performance/review_visibility_settings <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-performance-review-visibility-settings-id>`_

        :param setting_id: The unique identifier of the record to update.
        :type setting_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: ReviewVisibilitySetting
        """
        response = await self.api.put(self.endpoint, setting_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ReviewVisibilitySetting).validate_python(response)


class TargetManagersEndpoint(Endpoint):
    """Endpoint for performance/target_managers operations."""

    endpoint = 'performance/target_managers'

    async def all(self, **kwargs) -> ListApiResponse[TargetManager]:
        """Get all target managers.

        Official documentation: `performance/target_managers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-target-managers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[TargetManager]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=TargetManager, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[TargetManager]:
        """Get target managers with pagination metadata.

        Official documentation: `performance/target_managers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-target-managers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[TargetManager]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=TargetManager, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, manager_id: int | str, **kwargs) -> TargetManager:
        """Get a specific target manager by ID.

        Official documentation: `performance/target_managers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-performance-target-managers-id>`_

        :param manager_id: The unique identifier.
        :type manager_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: TargetManager
        """
        data = await self.api.get(self.endpoint, manager_id, **kwargs)
        return pydantic.TypeAdapter(TargetManager).validate_python(data)
