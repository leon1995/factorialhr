import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class SessionModality(StrEnum):
    """Enum for session modality types."""

    ONLINE = 'online'
    INPERSON = 'inperson'
    MIXED = 'mixed'


class SessionSchedule(StrEnum):
    """Enum for session schedule types."""

    SCHEDULED = 'scheduled'
    SELFPACED = 'selfpaced'


class TrainingStatus(StrEnum):
    """Enum for training status."""

    DRAFT = 'draft'
    ACTIVE = 'active'
    DELETED = 'deleted'


class TrainingAttendanceStatus(StrEnum):
    """Enum for training attendance status."""

    NOTASSIGNED = 'notassigned'
    NOTSTARTED = 'notstarted'
    MISSING = 'missing'
    STARTED = 'started'
    PARTIALLYCOMPLETED = 'partiallycompleted'
    COMPLETED = 'completed'


class Category(pydantic.BaseModel):
    """Model for trainings_category."""

    id: int = pydantic.Field(description='Category ID')
    name: str = pydantic.Field(description='Category name')
    company_id: int = pydantic.Field(description='Company ID')
    created_at: datetime.datetime | None = pydantic.Field(default=None, description='Creation date')
    updated_at: datetime.datetime | None = pydantic.Field(default=None, description='Last update date')


class Session(pydantic.BaseModel):
    """Model for trainings_session."""

    id: int = pydantic.Field(description='Session ID')
    name: str = pydantic.Field(description='Session name')
    training_id: int = pydantic.Field(description='Identifier of the course')
    description: str | None = pydantic.Field(default=None, description='Session description')
    training_class_id: str | None = pydantic.Field(default=None, description='Identifier of the group')
    starts_at: datetime.datetime | None = pydantic.Field(default=None, description='Date when the session should start')
    ends_at: datetime.datetime | None = pydantic.Field(default=None, description='Date when the session should end')
    due_date: datetime.date | None = pydantic.Field(default=None, description='Date when the session should end')
    duration: Mapping[str, typing.Any] | None = pydantic.Field(
        default=None,
        description='The duration in hours and minutes of the session',
    )
    modality: SessionModality | None = pydantic.Field(
        default=None,
        description='The mode the session will be handled, online, in person or hybrid',
    )
    schedule: SessionSchedule | None = pydantic.Field(
        default=None,
        description='Session schedule information (scheduled, self-paced)',
    )
    link: str | None = pydantic.Field(default=None, description='The link to see material from the session')
    location: str | None = pydantic.Field(default=None, description='The place where the session takes place')
    session_attendance_ids: Sequence[int] | None = pydantic.Field(default=None, description='Session attendance IDs')
    session_feedback_id: int | None = pydantic.Field(default=None, description='Session feedback ID')
    subsidized: bool = pydantic.Field(description='If the session is subsidized')
    status: str | None = pydantic.Field(default=None, description='Status of the session')
    parent_id: int | None = pydantic.Field(
        default=None,
        description='ID of the recurrent session that is parent of the current one',
    )


class SessionAccessMembership(pydantic.BaseModel):
    """Model for trainings_session_access_membership."""

    id: int = pydantic.Field(description='ID of this membership')
    access_id: int = pydantic.Field(description='ID of the access associated with this membership')
    employee_id: int | None = pydantic.Field(
        default=None,
        description='ID of the employee associated with this membership',
    )
    session_id: int = pydantic.Field(description='ID of the session associated with this membership')
    first_name: str | None = pydantic.Field(
        default=None,
        description='First name of the user associated with this membership',
    )
    last_name: str | None = pydantic.Field(
        default=None,
        description='Last name of the user associated with this membership',
    )
    job_title: str | None = pydantic.Field(
        default=None,
        description='Job title of the user associated with this membership',
    )


class SessionAttendance(pydantic.BaseModel):
    """Model for trainings_session_attendance."""

    id: int = pydantic.Field(description='Session attendance ID')
    status: str = pydantic.Field(description='Attendance status')
    session_access_membership_id: int = pydantic.Field(description='Session access membership ID')
    access_id: int = pydantic.Field(description='Access ID')
    employee_id: int | None = pydantic.Field(default=None, description='Employee ID')


class Training(pydantic.BaseModel):
    """Model for trainings_training."""

    id: int  # Identifier of the course
    company_id: int  # Company identifier
    author_id: int  # The person that creates the training
    name: str  # Name of the training
    code: str | None = None  # Code of the training
    description: str  # Description of the training
    created_at: datetime.datetime | None = None  # Creation date of the course
    updated_at: datetime.datetime | None = None  # Last modification date of the course
    external_provider: str | None = None  # The name of the provider if any
    external: bool  # External training
    total_cost: int | None = None
    fundae_subsidized: bool  # Subsidized by Fundae
    subsidized: bool  # Marked as subsidized
    cost: int
    subsidized_cost: int
    total_cost_decimal: Mapping[str, typing.Any] | None = None
    cost_decimal: Mapping[str, typing.Any]
    subsidized_cost_decimal: Mapping[str, typing.Any]
    category_ids: Sequence[int] | None = None  # List of ids of training categories
    status: TrainingStatus | None = pydantic.Field(
        default=None,
        description='Training status. Can be one of the following values',
    )
    year: int  # Year of the training
    catalog: bool  # Visible in catalog
    competency_ids: Sequence[int]  # List of ids of training competencies
    total_training_cost: Mapping[str, typing.Any]  # The total direct cost of all course's groups
    total_training_indirect_cost: Mapping[str, typing.Any]  # The total indirect cost of all course's groups
    total_training_salary_cost: Mapping[str, typing.Any]  # The total salary cost of all course's groups
    total_training_subsidized_cost: Mapping[str, typing.Any]  # The total subsidized cost of all course's groups
    total_participants: int  # Number of participants of all course's groups
    training_attendance_status: TrainingAttendanceStatus = pydantic.Field(description='Training attendance status')
    valid_for: int | None = None  # Number of years this course is valid for
    objectives: str | None = None  # Objectives of the course
    number_of_expired_participants: int | None = None  # Number of participants with expired/expiring courses


class TrainingClass(pydantic.BaseModel):
    """Model for trainings_training_class."""

    id: str  # Identifier of the training to which the class belongs to
    training_id: int  # Identifier of the course
    name: str  # Class name
    description: str | None = None  # Class description
    start_date: datetime.date | None = None  # Traning class start date
    end_date: datetime.date | None = None  # Traning class end date
    cost: str  # Training-related expenses, such as instructor fees, materials, venue, and logistics.
    indirect_cost: str  # General business expenses related to training, such as utilities and administrative fees.
    salary_cost: str  # Cost of all employees' time spent on the course.
    subsidized_cost: str  # Amount of training expenses covered by financial aid or grants for this group.


class TrainingMembership(pydantic.BaseModel):
    """Model for trainings_training_membership."""

    id: int  # Unique identifier for the training membership.
    access_id: int  # Access_id associated to the employee, refers to employees/employees endpoint.
    training_id: int  # This field is used to filter those trainings memberships that belongs to this training.
    status: str  # This field is used to filter those trainings memberships whose attendance status is the given.
    training_due_date: datetime.date | None = None  # This field is used for those trainings with an expiry date.
    training_completed_at: datetime.date | None = (
        None  # This field is used to record the date a training was completed for trainings that have an expiry date.
    )


class CategoriesEndpoint(Endpoint):
    """Endpoint for trainings/categories operations."""

    endpoint = 'trainings/categories'

    async def all(self, **kwargs) -> ListApiResponse[Category]:
        """Get all training categories."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Category, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Category]:
        """Get training categories with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Category, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, category_id: int | str, **kwargs) -> Category:
        """Get a specific training category by ID."""
        data = await self.api.get(self.endpoint, category_id, **kwargs)
        return pydantic.TypeAdapter(Category).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Category:
        """Create a new training category."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Category).validate_python(response)

    async def delete(self, category_id: int | str, **kwargs) -> Category:
        """Delete a training category."""
        response = await self.api.delete(self.endpoint, category_id, **kwargs)
        return pydantic.TypeAdapter(Category).validate_python(response)


class SessionsEndpoint(Endpoint):
    """Endpoint for trainings/sessions operations."""

    endpoint = 'trainings/sessions'

    async def all(self, **kwargs) -> ListApiResponse[Session]:
        """Get all training sessions."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Session, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Session]:
        """Get training sessions with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Session, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, session_id: int | str, **kwargs) -> Session:
        """Get a specific training session by ID."""
        data = await self.api.get(self.endpoint, session_id, **kwargs)
        return pydantic.TypeAdapter(Session).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Session:
        """Create a new training session."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Session).validate_python(response)

    async def update(self, session_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Session:
        """Update a training session."""
        response = await self.api.put(self.endpoint, session_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Session).validate_python(response)

    async def delete(self, session_id: int | str, **kwargs) -> Session:
        """Delete a training session."""
        response = await self.api.delete(self.endpoint, session_id, **kwargs)
        return pydantic.TypeAdapter(Session).validate_python(response)


class SessionAccessMembershipsEndpoint(Endpoint):
    """Endpoint for trainings/session_access_memberships operations."""

    endpoint = 'trainings/session_access_memberships'

    async def all(self, **kwargs) -> ListApiResponse[SessionAccessMembership]:
        """Get all session access memberships."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SessionAccessMembership, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SessionAccessMembership]:
        """Get session access memberships with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=SessionAccessMembership, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, membership_id: int | str, **kwargs) -> SessionAccessMembership:
        """Get a specific session access membership by ID."""
        data = await self.api.get(self.endpoint, membership_id, **kwargs)
        return pydantic.TypeAdapter(SessionAccessMembership).validate_python(data)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> list[SessionAccessMembership]:
        """Bulk create session access memberships."""
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[SessionAccessMembership]).validate_python(response)

    async def bulk_destroy(self, data: Mapping[str, typing.Any], **kwargs) -> list[SessionAccessMembership]:
        """Bulk destroy session access memberships."""
        response = await self.api.post(self.endpoint, 'bulk_destroy', json=data, **kwargs)
        return pydantic.TypeAdapter(list[SessionAccessMembership]).validate_python(response)


class SessionAttendancesEndpoint(Endpoint):
    """Endpoint for trainings/session_attendances operations."""

    endpoint = 'trainings/session_attendances'

    async def all(self, **kwargs) -> ListApiResponse[SessionAttendance]:
        """Get all session attendances."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=SessionAttendance, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[SessionAttendance]:
        """Get session attendances with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=SessionAttendance, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, attendance_id: int | str, **kwargs) -> SessionAttendance:
        """Get a specific session attendance by ID."""
        data = await self.api.get(self.endpoint, attendance_id, **kwargs)
        return pydantic.TypeAdapter(SessionAttendance).validate_python(data)

    async def bulk_update(self, data: Mapping[str, typing.Any], **kwargs) -> list[SessionAttendance]:
        """Bulk update session attendances."""
        response = await self.api.post(self.endpoint, 'bulk_update', json=data, **kwargs)
        return pydantic.TypeAdapter(list[SessionAttendance]).validate_python(response)


class TrainingsEndpoint(Endpoint):
    """Endpoint for trainings/trainings operations."""

    endpoint = 'trainings/trainings'

    async def all(self, **kwargs) -> ListApiResponse[Training]:
        """Get all trainings."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Training, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Training]:
        """Get trainings with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Training, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, training_id: int | str, **kwargs) -> Training:
        """Get a specific training by ID."""
        data = await self.api.get(self.endpoint, training_id, **kwargs)
        return pydantic.TypeAdapter(Training).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Training:
        """Create a new training."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Training).validate_python(response)

    async def update(self, training_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Training:
        """Update a training."""
        response = await self.api.put(self.endpoint, training_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Training).validate_python(response)

    async def delete(self, training_id: int | str, **kwargs) -> Training:
        """Delete a training."""
        response = await self.api.delete(self.endpoint, training_id, **kwargs)
        return pydantic.TypeAdapter(Training).validate_python(response)

    async def bulk_delete(self, data: Mapping[str, typing.Any], **kwargs) -> list[Training]:
        """Bulk delete trainings."""
        response = await self.api.post(self.endpoint, 'bulk_delete', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Training]).validate_python(response)

    async def bulk_update_catalog(self, data: Mapping[str, typing.Any], **kwargs) -> list[Training]:
        """Bulk update catalog visibility for trainings."""
        response = await self.api.post(self.endpoint, 'bulk_update_catalog', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Training]).validate_python(response)

    async def update_status(self, data: Mapping[str, typing.Any], **kwargs) -> Training:
        """Update training status."""
        response = await self.api.post(self.endpoint, 'update_status', json=data, **kwargs)
        return pydantic.TypeAdapter(Training).validate_python(response)


class TrainingClassesEndpoint(Endpoint):
    """Endpoint for trainings/training_classes operations."""

    endpoint = 'trainings/training_classes'

    async def all(self, **kwargs) -> ListApiResponse[TrainingClass]:
        """Get all training classes."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=TrainingClass, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[TrainingClass]:
        """Get training classes with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=TrainingClass, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, class_id: int | str, **kwargs) -> TrainingClass:
        """Get a specific training class by ID."""
        data = await self.api.get(self.endpoint, class_id, **kwargs)
        return pydantic.TypeAdapter(TrainingClass).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> TrainingClass:
        """Create a new training class."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(TrainingClass).validate_python(response)

    async def update(self, class_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> TrainingClass:
        """Update a training class."""
        response = await self.api.put(self.endpoint, class_id, json=data, **kwargs)
        return pydantic.TypeAdapter(TrainingClass).validate_python(response)

    async def delete(self, class_id: int | str, **kwargs) -> TrainingClass:
        """Delete a training class."""
        response = await self.api.delete(self.endpoint, class_id, **kwargs)
        return pydantic.TypeAdapter(TrainingClass).validate_python(response)


class TrainingMembershipsEndpoint(Endpoint):
    """Endpoint for trainings/training_memberships operations."""

    endpoint = 'trainings/training_memberships'

    async def all(self, **kwargs) -> ListApiResponse[TrainingMembership]:
        """Get all training memberships."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=TrainingMembership, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[TrainingMembership]:
        """Get training memberships with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=TrainingMembership, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, membership_id: int | str, **kwargs) -> TrainingMembership:
        """Get a specific training membership by ID."""
        data = await self.api.get(self.endpoint, membership_id, **kwargs)
        return pydantic.TypeAdapter(TrainingMembership).validate_python(data)

    async def update(self, membership_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> TrainingMembership:
        """Update a training membership."""
        response = await self.api.put(self.endpoint, membership_id, json=data, **kwargs)
        return pydantic.TypeAdapter(TrainingMembership).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> list[TrainingMembership]:
        """Bulk create training memberships."""
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[TrainingMembership]).validate_python(response)

    async def bulk_destroy(self, data: Mapping[str, typing.Any], **kwargs) -> list[TrainingMembership]:
        """Bulk destroy training memberships."""
        response = await self.api.post(self.endpoint, 'bulk_destroy', json=data, **kwargs)
        return pydantic.TypeAdapter(list[TrainingMembership]).validate_python(response)
