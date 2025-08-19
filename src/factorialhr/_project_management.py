import datetime
import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class ExpenseRecord(pydantic.BaseModel):
    """Model for project_management_expense_record."""

    id: int = pydantic.Field(description='Expense record ID')
    project_worker_id: int = pydantic.Field(description='Project worker ID')
    expense_id: int = pydantic.Field(description='Expense ID')
    subproject_id: int | None = pydantic.Field(default=None, description='Subproject ID')
    original_amount_currency: str | None = pydantic.Field(default=None, description='Original amount currency')
    original_amount_cents: int | None = pydantic.Field(default=None, description='Original amount in cents')
    legal_entity_amount_currency: str | None = pydantic.Field(default=None, description='Legal entity amount currency')
    legal_entity_amount_cents: str | None = pydantic.Field(default=None, description='Legal entity amount in cents')
    effective_on: datetime.date | None = pydantic.Field(default=None, description='Effective date')
    exchange_rate: int | None = pydantic.Field(default=None, description='Exchange rate')
    status: str | None = pydantic.Field(default=None, description='Expense record status')


class ExpenseRecordEndpoint(Endpoint):
    endpoint = 'project_management/expense_records'

    async def all(self, **kwargs) -> ListApiResponse[ExpenseRecord]:
        """Get all expense records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ExpenseRecord, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ExpenseRecord]:
        """Get expense records with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ExpenseRecord, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, expense_id: int | str, **kwargs) -> ExpenseRecord:
        """Get a specific expense record by ID."""
        data = await self.api.get(self.endpoint, expense_id, **kwargs)
        return pydantic.TypeAdapter(ExpenseRecord).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ExpenseRecord:
        """Create a new expense record."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ExpenseRecord).validate_python(response['data'])

    async def update(self, expense_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ExpenseRecord:
        """Update an expense record."""
        response = await self.api.put(self.endpoint, expense_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ExpenseRecord).validate_python(response['data'])

    async def delete(self, expense_id: int | str, **kwargs) -> None:
        """Delete an expense record."""
        await self.api.delete(self.endpoint, expense_id, **kwargs)


class ExportableExpense(pydantic.BaseModel):
    """Model for project_management_exportable_expense."""

    date: datetime.date | None = pydantic.Field(default=None, description='Expense date')
    project_name: str | None = pydantic.Field(default=None, description='Project name')
    subproject_name: str | None = pydantic.Field(default=None, description='Subproject name')
    employee_name: str = pydantic.Field(description='Employee name')
    preferred_name: str | None = pydantic.Field(default=None, description='Employee preferred name')
    amount: str | None = pydantic.Field(default=None, description='Expense amount')
    currency: str | None = pydantic.Field(default=None, description='Currency')
    expense_category: str | None = pydantic.Field(default=None, description='Expense category')
    expense_subcategory: str | None = pydantic.Field(default=None, description='Expense subcategory')
    expense_status: str | None = pydantic.Field(default=None, description='Expense status')
    expense_link: str | None = pydantic.Field(default=None, description='Link to expense details')


class ExportableExpenseEndpoint(Endpoint):
    endpoint = 'project_management/exportable_expenses'

    async def all(self, **kwargs) -> ListApiResponse[ExportableExpense]:
        """Get all exportable expenses."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ExportableExpense, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ExportableExpense]:
        """Get exportable expenses with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ExportableExpense, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, expense_id: int | str, **kwargs) -> ExportableExpense:
        """Get a specific exportable expense by ID."""
        data = await self.api.get(self.endpoint, expense_id, **kwargs)
        return pydantic.TypeAdapter(ExportableExpense).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ExportableExpense:
        """Create a new exportable expense."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ExportableExpense).validate_python(response['data'])

    async def update(self, expense_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ExportableExpense:
        """Update an exportable expense."""
        response = await self.api.put(self.endpoint, expense_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ExportableExpense).validate_python(response['data'])

    async def delete(self, expense_id: int | str, **kwargs) -> None:
        """Delete an exportable expense."""
        await self.api.delete(self.endpoint, expense_id, **kwargs)


class ExportableProject(pydantic.BaseModel):
    """Model for project_management_exportable_project."""

    id: str = pydantic.Field(description='Project ID')
    date: datetime.date | None = pydantic.Field(default=None, description='Project date')
    project_name: str = pydantic.Field(description='Project name')
    project_code: str | None = pydantic.Field(default=None, description='Project code')
    project_start_date: datetime.date | None = pydantic.Field(default=None, description='Project start date')
    project_due_date: datetime.date | None = pydantic.Field(default=None, description='Project due date')
    project_status: str = pydantic.Field(description='Project status')
    subproject_name: str | None = pydantic.Field(default=None, description='Subproject name')
    employee_name: str | None = pydantic.Field(default=None, description='Employee name')
    employee_id: int | None = pydantic.Field(default=None, description='Employee ID')
    inputed_time: float = pydantic.Field(description='Inputted time (API returns string but can be float)')


class ExportableProjectEndpoint(Endpoint):
    endpoint = 'project_management/exportable_projects'

    async def all(self, **kwargs) -> ListApiResponse[ExportableProject]:
        """Get all exportable projects."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ExportableProject, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ExportableProject]:
        """Get exportable projects with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ExportableProject, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, project_id: int | str, **kwargs) -> ExportableProject:
        """Get a specific exportable project by ID."""
        data = await self.api.get(self.endpoint, project_id, **kwargs)
        return pydantic.TypeAdapter(ExportableProject).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ExportableProject:
        """Create a new exportable project."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ExportableProject).validate_python(response['data'])

    async def update(self, project_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ExportableProject:
        """Update an exportable project."""
        response = await self.api.put(self.endpoint, project_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ExportableProject).validate_python(response['data'])

    async def delete(self, project_id: int | str, **kwargs) -> None:
        """Delete an exportable project."""
        await self.api.delete(self.endpoint, project_id, **kwargs)


class FlexibleTimeRecord(pydantic.BaseModel):
    """Model for project_management_flexible_time_record."""

    id: int = pydantic.Field(description='Flexible time record ID')
    date: datetime.date = pydantic.Field(description='Record date')
    imputed_minutes: int = pydantic.Field(description='Imputed minutes')
    project_worker_id: int = pydantic.Field(description='Project worker ID')
    subproject_id: int | None = pydantic.Field(default=None, description='Subproject ID')


class FlexibleTimeRecordEndpoint(Endpoint):
    endpoint = 'project_management/flexible_time_records'

    async def all(self, **kwargs) -> ListApiResponse[FlexibleTimeRecord]:
        """Get all flexible time records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=FlexibleTimeRecord, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[FlexibleTimeRecord]:
        """Get flexible time records with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=FlexibleTimeRecord, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, record_id: int | str, **kwargs) -> FlexibleTimeRecord:
        """Get a specific flexible time record by ID."""
        data = await self.api.get(self.endpoint, record_id, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecord).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> FlexibleTimeRecord:
        """Create a new flexible time record."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecord).validate_python(response['data'])

    async def update(self, record_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> FlexibleTimeRecord:
        """Update a flexible time record."""
        response = await self.api.put(self.endpoint, record_id, json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecord).validate_python(response['data'])

    async def delete(self, record_id: int | str, **kwargs) -> FlexibleTimeRecord:
        """Delete a flexible time record."""
        response = await self.api.delete(self.endpoint, record_id, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecord).validate_python(response)


class FlexibleTimeRecordComment(pydantic.BaseModel):
    """Model for project_management_flexible_time_record_comment."""

    id: int = pydantic.Field(description='Comment ID')
    content: str = pydantic.Field(description='Comment content')
    flexible_time_record_id: int = pydantic.Field(description='Flexible time record ID')


class FlexibleTimeRecordCommentEndpoint(Endpoint):
    endpoint = 'project_management/flexible_time_record_comments'

    async def all(self, **kwargs) -> ListApiResponse[FlexibleTimeRecordComment]:
        """Get all flexible time record comments."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=FlexibleTimeRecordComment, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[FlexibleTimeRecordComment]:
        """Get flexible time record comments with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=FlexibleTimeRecordComment,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, comment_id: int | str, **kwargs) -> FlexibleTimeRecordComment:
        """Get a specific flexible time record comment by ID."""
        data = await self.api.get(self.endpoint, comment_id, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> FlexibleTimeRecordComment:
        """Create a new flexible time record comment."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(response['data'])

    async def update(
        self,
        comment_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> FlexibleTimeRecordComment:
        """Update a flexible time record comment."""
        response = await self.api.put(self.endpoint, comment_id, json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(response['data'])

    async def delete(self, comment_id: int | str, **kwargs) -> FlexibleTimeRecordComment:
        """Delete a flexible time record comment."""
        response = await self.api.delete(self.endpoint, comment_id, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(response)

    async def delete_by_flexible_time_record(
        self,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> FlexibleTimeRecordComment:
        """Delete a flexible time record comment by flexible time record ID."""
        response = await self.api.post(self.endpoint, 'delete_by_flexible_time_record', json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(response)

    async def update_by_flexible_time_record(
        self,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> FlexibleTimeRecordComment:
        """Update a flexible time record comment by flexible time record ID."""
        response = await self.api.post(self.endpoint, 'update_by_flexible_time_record', json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(response)


class ProjectStatus(StrEnum):
    """Enum for project status."""

    ACTIVE = 'active'
    CLOSED = 'closed'
    DRAFT = 'draft'
    PROCESSING = 'processing'


class ProjectEmployeeAssignment(StrEnum):
    """Enum for project employee assignment types."""

    MANUAL = 'manual'
    COMPANY = 'company'


class Project(pydantic.BaseModel):
    """Model for project_management_project."""

    id: int = pydantic.Field(description='Project ID')
    name: str = pydantic.Field(description='Project name')
    code: str | None = pydantic.Field(default=None, description='Project code')
    start_date: datetime.date | None = pydantic.Field(default=None, description='Project start date')
    due_date: datetime.date | None = pydantic.Field(default=None, description='Project due date')
    status: ProjectStatus = pydantic.Field(description='Project status')
    employees_assignment: ProjectEmployeeAssignment = pydantic.Field(description='Employee assignment type')
    inputed_minutes: int | None = pydantic.Field(default=None, description='Total inputted minutes')
    is_billable: bool = pydantic.Field(description='Whether the project is billable')
    fixed_cost_cents: int | None = pydantic.Field(default=None, description='Fixed cost in cents')
    labor_cost_cents: int | None = pydantic.Field(default=None, description='Labor cost in cents')
    legal_entity_id: int = pydantic.Field(description='Legal entity ID')
    spending_cost_cents: int | None = pydantic.Field(default=None, description='Spending cost in cents')
    client_id: int | None = pydantic.Field(default=None, description='Client ID')
    total_cost_cents: int | None = pydantic.Field(default=None, description='Total cost in cents')


class ProjectEndpoint(Endpoint):
    endpoint = 'project_management/projects'

    async def all(self, **kwargs) -> ListApiResponse[Project]:
        """Get all projects."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Project, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Project]:
        """Get projects with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Project, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, project_id: int | str, **kwargs) -> Project:
        """Get a specific project by ID."""
        data = await self.api.get(self.endpoint, project_id, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Create a new project."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response['data'])

    async def update(self, project_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Update a project."""
        response = await self.api.put(self.endpoint, project_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response['data'])

    async def delete(self, project_id: int | str, **kwargs) -> Project:
        """Delete a project."""
        response = await self.api.delete(self.endpoint, project_id, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)

    async def activate(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Activate a project."""
        response = await self.api.post(self.endpoint, 'activate', json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)

    async def change_assignment(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Change assignment of a project."""
        response = await self.api.post(self.endpoint, 'change_assignment', json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)

    async def change_status(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Change status of a project."""
        response = await self.api.post(self.endpoint, 'change_status', json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)

    async def close(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Close a project."""
        response = await self.api.post(self.endpoint, 'close', json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)

    async def soft_delete(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Soft delete a project."""
        response = await self.api.post(self.endpoint, 'soft_delete', json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)


class ProjectTask(pydantic.BaseModel):
    """Model for project_management_project_task."""

    id: int = pydantic.Field(description='Project task ID')
    project_id: int = pydantic.Field(description='Project ID')
    subproject_id: int = pydantic.Field(description='Subproject ID')
    task_id: int = pydantic.Field(description='Task ID')
    follow_up: bool = pydantic.Field(description='Whether this is a follow-up task')


class ProjectTaskEndpoint(Endpoint):
    endpoint = 'project_management/project_tasks'

    async def all(self, **kwargs) -> ListApiResponse[ProjectTask]:
        """Get all project tasks."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ProjectTask, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ProjectTask]:
        """Get project tasks with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ProjectTask, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, task_id: int | str, **kwargs) -> ProjectTask:
        """Get a specific project task by ID."""
        data = await self.api.get(self.endpoint, task_id, **kwargs)
        return pydantic.TypeAdapter(ProjectTask).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ProjectTask:
        """Create a new project task."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ProjectTask).validate_python(response['data'])

    async def update(self, task_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ProjectTask:
        """Update a project task."""
        response = await self.api.put(self.endpoint, task_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ProjectTask).validate_python(response['data'])

    async def delete(self, task_id: int | str, **kwargs) -> ProjectTask:
        """Delete a project task."""
        response = await self.api.delete(self.endpoint, task_id, **kwargs)
        return pydantic.TypeAdapter(ProjectTask).validate_python(response)

    async def bulk_destroy(self, data: Mapping[str, typing.Any], **kwargs) -> list[ProjectTask]:
        """Bulk destroy project tasks."""
        response = await self.api.post(self.endpoint, 'bulk_destroy', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ProjectTask]).validate_python(response)

    async def bulk_duplicate(self, data: Mapping[str, typing.Any], **kwargs) -> list[ProjectTask]:
        """Bulk duplicate project tasks."""
        response = await self.api.post(self.endpoint, 'bulk_duplicate', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ProjectTask]).validate_python(response)


class ProjectWorker(pydantic.BaseModel):
    """Model for project_management_project_worker."""

    id: int = pydantic.Field(description='Project worker ID')
    project_id: int = pydantic.Field(description='Project ID')
    employee_id: int = pydantic.Field(description='Employee ID')
    assigned: bool = pydantic.Field(description='Whether the worker is assigned to the project')
    inputed_minutes: int | None = pydantic.Field(default=None, description='Total inputted minutes')
    labor_cost_cents: int | None = pydantic.Field(default=None, description='Labor cost in cents')
    spending_cost_cents: int | None = pydantic.Field(default=None, description='Spending cost in cents')


class ProjectWorkerEndpoint(Endpoint):
    endpoint = 'project_management/project_workers'

    async def all(self, **kwargs) -> ListApiResponse[ProjectWorker]:
        """Get all project workers."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ProjectWorker, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ProjectWorker]:
        """Get project workers with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ProjectWorker, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, worker_id: int | str, **kwargs) -> ProjectWorker:
        """Get a specific project worker by ID."""
        data = await self.api.get(self.endpoint, worker_id, **kwargs)
        return pydantic.TypeAdapter(ProjectWorker).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ProjectWorker:
        """Create a new project worker."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ProjectWorker).validate_python(response['data'])

    async def update(self, worker_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ProjectWorker:
        """Update a project worker."""
        response = await self.api.put(self.endpoint, worker_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ProjectWorker).validate_python(response['data'])

    async def delete(self, worker_id: int | str, **kwargs) -> ProjectWorker:
        """Delete a project worker."""
        response = await self.api.delete(self.endpoint, worker_id, **kwargs)
        return pydantic.TypeAdapter(ProjectWorker).validate_python(response)

    async def bulk_assign(self, data: Mapping[str, typing.Any], **kwargs) -> list[ProjectWorker]:
        """Bulk assign project workers."""
        response = await self.api.post(self.endpoint, 'bulk_assign', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ProjectWorker]).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> list[ProjectWorker]:
        """Bulk create project workers."""
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ProjectWorker]).validate_python(response)

    async def unassign(self, data: Mapping[str, typing.Any], **kwargs) -> ProjectWorker:
        """Unassign a project worker."""
        response = await self.api.post(self.endpoint, 'unassign', json=data, **kwargs)
        return pydantic.TypeAdapter(ProjectWorker).validate_python(response)


class Subproject(pydantic.BaseModel):
    """Model for project_management_subproject."""

    id: int | None = pydantic.Field(default=None, description='Subproject ID')
    name: str = pydantic.Field(description='Subproject name')
    project_id: int = pydantic.Field(description='Project ID')
    inputed_minutes: int | None = pydantic.Field(default=None, description='Total inputted minutes')
    labor_cost_cents: int | None = pydantic.Field(default=None, description='Labor cost in cents')


class SubprojectEndpoint(Endpoint):
    endpoint = 'project_management/subprojects'

    async def all(self, **kwargs) -> ListApiResponse[Subproject]:
        """Get all subprojects."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Subproject, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Subproject]:
        """Get subprojects with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Subproject, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, subproject_id: int | str, **kwargs) -> Subproject:
        """Get a specific subproject by ID."""
        data = await self.api.get(self.endpoint, subproject_id, **kwargs)
        return pydantic.TypeAdapter(Subproject).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Subproject:
        """Create a new subproject."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Subproject).validate_python(response['data'])

    async def update(self, subproject_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Subproject:
        """Update a subproject."""
        response = await self.api.put(self.endpoint, subproject_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Subproject).validate_python(response['data'])

    async def delete(self, subproject_id: int | str, **kwargs) -> Subproject:
        """Delete a subproject."""
        response = await self.api.delete(self.endpoint, subproject_id, **kwargs)
        return pydantic.TypeAdapter(Subproject).validate_python(response)

    async def rename(self, data: Mapping[str, typing.Any], **kwargs) -> Subproject:
        """Rename a subproject."""
        response = await self.api.post(self.endpoint, 'rename', json=data, **kwargs)
        return pydantic.TypeAdapter(Subproject).validate_python(response)


class TimeRecord(pydantic.BaseModel):
    """Model for project_management_time_record."""

    id: int = pydantic.Field(description='Time record ID')
    project_worker_id: int = pydantic.Field(description='Project worker ID')
    attendance_shift_id: int = pydantic.Field(description='Attendance shift ID')
    subproject_id: int | None = pydantic.Field(default=None, description='Subproject ID')
    date: datetime.date | None = pydantic.Field(default=None, description='Record date')
    imputed_minutes: int | None = pydantic.Field(default=None, description='Imputed minutes')
    clock_in: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Clock in time (date will always be 2000-01-01, only use for .time())',
    )
    clock_out: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Clock out time (date will always be 2000-01-01, only use for .time())',
    )


class TimeRecordEndpoint(Endpoint):
    endpoint = 'project_management/time_records'

    async def all(self, **kwargs) -> ListApiResponse[TimeRecord]:
        """Get all time records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=TimeRecord, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[TimeRecord]:
        """Get time records with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=TimeRecord, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, record_id: int | str, **kwargs) -> TimeRecord:
        """Get a specific time record by ID."""
        data = await self.api.get(self.endpoint, record_id, **kwargs)
        return pydantic.TypeAdapter(TimeRecord).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> TimeRecord:
        """Create a new time record."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(TimeRecord).validate_python(response['data'])

    async def update(self, record_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> TimeRecord:
        """Update a time record."""
        response = await self.api.put(self.endpoint, record_id, json=data, **kwargs)
        return pydantic.TypeAdapter(TimeRecord).validate_python(response['data'])

    async def delete(self, record_id: int | str, **kwargs) -> TimeRecord:
        """Delete a time record."""
        response = await self.api.delete(self.endpoint, record_id, **kwargs)
        return pydantic.TypeAdapter(TimeRecord).validate_python(response)

    async def bulk_delete(self, data: Mapping[str, typing.Any], **kwargs) -> list[TimeRecord]:
        """Bulk delete time records."""
        response = await self.api.post(self.endpoint, 'bulk_delete', json=data, **kwargs)
        return pydantic.TypeAdapter(list[TimeRecord]).validate_python(response)

    async def bulk_process(self, data: Mapping[str, typing.Any], **kwargs) -> list[TimeRecord]:
        """Bulk process time records."""
        response = await self.api.post(self.endpoint, 'bulk_process', json=data, **kwargs)
        return pydantic.TypeAdapter(list[TimeRecord]).validate_python(response)

    async def update_project_worker(self, data: Mapping[str, typing.Any], **kwargs) -> TimeRecord:
        """Update project worker for a time record."""
        response = await self.api.post(self.endpoint, 'update_project_worker', json=data, **kwargs)
        return pydantic.TypeAdapter(TimeRecord).validate_python(response)
