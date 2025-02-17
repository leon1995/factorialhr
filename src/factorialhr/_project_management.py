import datetime
import enum
import typing

import pydantic

from factorialhr import _common
from factorialhr._client import Endpoint


class ExpenseRecord(pydantic.BaseModel):
    id: int
    project_worker_id: int
    expense_id: int
    subproject_id: int | None
    original_amount_currency: str | None
    original_amount_cents: int | None
    legal_entity_amount_currency: str | None
    legal_entity_amount_cents: str | None
    effective_on: datetime.date | None
    exchange_rate: int | None
    status: str | None


class _ExpenseRecordRoot(pydantic.RootModel):
    root: list[ExpenseRecord]


class ExpenseRecordEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/project_management/expense_records'

    async def all(  # noqa: PLR0913
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        start_date: datetime.date | None = None,
        end_date: datetime.date | None = None,
        expenses_ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        updated_after: datetime.date | None = None,
        employee_user_name_like: str | None = None,
        project_worker_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> list[ExpenseRecord]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-expense-records."""
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'start_date': start_date,
                'end_date': end_date,
                'expenses_ids[]': expenses_ids,
                'project_ids[]': project_ids,
                'subproject_ids[]': subproject_ids,
                'updated_after': updated_after,
                'employee_user_name_like': employee_user_name_like,
                'project_worker_ids[]': project_worker_ids,
            },
        )
        return _ExpenseRecordRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, expense_record_id: int, **kwargs) -> ExpenseRecord: ...

    @typing.overload
    async def get(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        start_date: datetime.date | None = None,
        end_date: datetime.date | None = None,
        expenses_ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        updated_after: datetime.date | None = None,
        employee_user_name_like: str | None = None,
        project_worker_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> tuple[list[ExpenseRecord], _common.Meta]: ...

    async def get(  # noqa: PLR0913
        self,
        *,
        expense_record_id: int | None = None,
        ids: typing.Sequence[int] | None = None,
        start_date: datetime.date | None = None,
        end_date: datetime.date | None = None,
        expenses_ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        updated_after: datetime.date | None = None,
        employee_user_name_like: str | None = None,
        project_worker_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-expense-records-id."""
        if expense_record_id is not None:
            return ExpenseRecord.model_validate(await self.api.get(self.endpoint, expense_record_id, **kwargs))
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'start_date': start_date,
                'end_date': end_date,
                'expenses_ids[]': expenses_ids,
                'project_ids[]': project_ids,
                'subproject_ids[]': subproject_ids,
                'updated_after': updated_after,
                'employee_user_name_like': employee_user_name_like,
                'project_worker_ids[]': project_worker_ids,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _ExpenseRecordRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class ExportableExpense(pydantic.BaseModel):
    date: datetime.date | None
    project_name: str | None
    subproject_name: str | None
    employee_name: str
    preferred_name: str | None
    amount: str | None
    currency: str | None
    expense_category: str | None
    expense_subcategory: str | None
    expense_status: str | None
    expense_link: str | None


class _ExportableExpenseRoot(pydantic.RootModel):
    root: list[ExportableExpense]


class ExportableExpenseEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/project_management/exportable_expenses'

    async def all(
        self,
        *,
        start_date: datetime.date | None = None,
        end_date: datetime.date | None = None,
        project_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> list[ExportableExpense]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-exportable-expenses."""
        params = kwargs.get('params', {})
        params.update(
            {
                'start_date': start_date,
                'end_date': end_date,
                'project_ids[]': project_ids,
            },
        )
        return _ExportableExpenseRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    async def get(
        self,
        *,
        start_date: datetime.date | None = None,
        end_date: datetime.date | None = None,
        project_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> tuple[list[ExportableExpense], _common.Meta]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-exportable-expenses."""
        params = kwargs.get('params', {})
        params.update(
            {
                'start_date': start_date,
                'end_date': end_date,
                'project_ids[]': project_ids,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _ExportableExpenseRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class ExportableProject(pydantic.BaseModel):
    id: str
    date: datetime.date | None
    project_name: str
    project_code: str | None
    project_start_date: datetime.date | None
    project_due_date: datetime.date | None
    project_status: str
    subproject_name: str | None
    employee_name: str | None
    employee_id: int | None
    inputed_time: float  # api returns string but can actually be a float


class _ExportableProjectRoot(pydantic.RootModel):
    root: list[ExportableProject]


class ExportableProjectEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/project_management/exportable_projects'

    async def all(
        self,
        *,
        start_date: datetime.date | None = None,
        end_date: datetime.date | None = None,
        project_ids: typing.Sequence[int] | None = None,
        time_format: str | None = None,
        include_date: bool | None = None,
        **kwargs,
    ) -> list[ExportableProject]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-exportable-projects."""
        params = kwargs.get('params', {})
        params.update(
            {
                'start_date': start_date,
                'end_date': end_date,
                'project_ids[]': project_ids,
                'time_format': time_format,
                'include_date': include_date,
            },
        )
        return _ExportableProjectRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    async def get(
        self,
        *,
        start_date: datetime.date | None = None,
        end_date: datetime.date | None = None,
        project_ids: typing.Sequence[int] | None = None,
        time_format: str | None = None,
        include_date: bool | None = None,
        **kwargs,
    ) -> tuple[list[ExportableProject], _common.Meta]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-exportable-projects."""
        params = kwargs.get('params', {})
        params.update(
            {
                'start_date': start_date,
                'end_date': end_date,
                'project_ids[]': project_ids,
                'time_format': time_format,
                'include_date': include_date,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _ExportableProjectRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class FlexibleTimeRecord(pydantic.BaseModel):
    id: int
    date: datetime.date
    imputed_minutes: int
    project_worker_id: int
    subproject_id: int | None


class _FlexibleTimeRecordRoot(pydantic.RootModel):
    root: list[FlexibleTimeRecord]


class FlexibleTimeRecordEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/project_management/flexible_time_records'

    async def all(
        self,
        *,
        ids: typing.Sequence[int] | None = None,  # documentation says it's required but it's not
        project_worker_ids: typing.Sequence[int] | None = None,  # documentation says it's required but it's not
        starts_on: datetime.date | None = None,
        ends_on: datetime.date | None = None,
        updated_after: str | None = None,  # last time I checked it seems to have no effect
        **kwargs,
    ) -> list[FlexibleTimeRecord]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-flexible-time-records."""
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'project_worker_ids[]': project_worker_ids,
                'starts_on': starts_on,
                'ends_on': ends_on,
                'updated_after': updated_after,
            },
        )
        return _FlexibleTimeRecordRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, flexible_time_record_id: int, **kwargs) -> FlexibleTimeRecord: ...

    @typing.overload
    async def get(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        project_worker_ids: typing.Sequence[int] | None = None,
        starts_on: datetime.date | None = None,
        ends_on: datetime.date | None = None,
        updated_after: str | None = None,
        **kwargs,
    ) -> tuple[list[FlexibleTimeRecord], _common.Meta]: ...

    async def get(  # noqa: PLR0913
        self,
        *,
        flexible_time_record_id: int | None = None,
        ids: typing.Sequence[int] | None = None,
        project_worker_ids: typing.Sequence[int] | None = None,
        starts_on: datetime.date | None = None,
        ends_on: datetime.date | None = None,
        updated_after: str | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-flexible-time-records-id."""
        if flexible_time_record_id is not None:
            return FlexibleTimeRecord.model_validate(
                await self.api.get(self.endpoint, flexible_time_record_id, **kwargs),
            )

        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'project_worker_ids[]': project_worker_ids,
                'starts_on': starts_on,
                'ends_on': ends_on,
                'updated_after': updated_after,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return (
            _FlexibleTimeRecordRoot.model_validate(result['data']).root,
            _common.Meta.model_validate(result['meta']),
        )


class FlexibleTimeRecordComment(pydantic.BaseModel):
    id: int
    content: str
    flexible_time_record_id: int


class _FlexibleTimeRecordCommentRoot(pydantic.RootModel):
    root: list[FlexibleTimeRecordComment]


class FlexibleTimeRecordCommentEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/project_management/flexible_time_record_comments'

    async def all(self, **kwargs) -> list[FlexibleTimeRecordComment]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-flexible-time-record-comments."""
        return _FlexibleTimeRecordCommentRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, flexible_time_record_comment_id: int, **kwargs) -> FlexibleTimeRecordComment: ...

    @typing.overload
    async def get(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        flexible_time_record_id: int | None = None,
        **kwargs,
    ) -> tuple[list[FlexibleTimeRecordComment], _common.Meta]: ...

    async def get(
        self,
        *,
        flexible_time_record_comment_id: int | None = None,
        ids: typing.Sequence[int] | None = None,
        flexible_time_record_id: int | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-flexible-time-record-comments-id."""
        if flexible_time_record_comment_id is not None:
            return FlexibleTimeRecordComment.model_validate(
                await self.api.get(self.endpoint, flexible_time_record_comment_id, **kwargs),
            )

        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'flexible_time_record_id': flexible_time_record_id,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _FlexibleTimeRecordCommentRoot.model_validate(result['data']).root, _common.Meta.model_validate(
            result['meta'],
        )


class ProjectStatus(enum.StrEnum):
    active = 'active'
    closed = 'closed'
    processing = 'processing'


class ProjectEmployeeAssignment(enum.StrEnum):
    manual = 'manual'
    company = 'company'


class Project(pydantic.BaseModel):
    id: int
    name: str
    code: str | None
    start_date: datetime.date | None
    due_date: datetime.date | None
    status: ProjectStatus
    employees_assignment: ProjectEmployeeAssignment
    inputed_minutes: int | None
    is_billable: bool
    fixed_cost_cents: int | None
    labor_cost_cents: int | None
    legal_entity_id: int
    spending_cost_cents: int | None
    client_id: int | None
    total_cost_cents: int | None


class _ProjectRoot(pydantic.RootModel):
    root: list[Project]


class ProjectEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/project_management/projects'

    async def all(  # noqa: PLR0913
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        name: str | None = None,
        name_or_code: str | None = None,
        include_inputed_minutes: bool | None = None,
        updated_after: datetime.date | None = None,
        legal_entity_id: int | None = None,
        no_clients: bool | None = None,
        total_currency: str | None = None,
        **kwargs,
    ) -> list[Project]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-projects."""
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'name': name,
                'name_or_code': name_or_code,
                'include_inputed_minutes': include_inputed_minutes,
                'updated_after': updated_after,
                'legal_entity_id': legal_entity_id,
                'no_clients': no_clients,
                'total_currency': total_currency,
            },
        )
        return _ProjectRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, project_id: int, **kwargs) -> Project: ...

    @typing.overload
    async def get(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        name: str | None = None,
        name_or_code: str | None = None,
        include_inputed_minutes: bool | None = None,
        updated_after: datetime.date | None = None,
        legal_entity_id: int | None = None,
        no_clients: bool | None = None,
        total_currency: str | None = None,
        **kwargs,
    ) -> tuple[list[Project], _common.Meta]: ...

    async def get(  # noqa: PLR0913
        self,
        *,
        project_id: int | None = None,
        ids: typing.Sequence[int] | None = None,
        name: str | None = None,
        name_or_code: str | None = None,
        include_inputed_minutes: bool | None = None,
        updated_after: datetime.date | None = None,
        legal_entity_id: int | None = None,
        no_clients: bool | None = None,
        total_currency: str | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-projects-id."""
        if project_id is not None:
            return Project.model_validate(await self.api.get(self.endpoint, project_id, **kwargs))

        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'name': name,
                'name_or_code': name_or_code,
                'include_inputed_minutes': include_inputed_minutes,
                'updated_after': updated_after,
                'legal_entity_id': legal_entity_id,
                'no_clients': no_clients,
                'total_currency': total_currency,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _ProjectRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class ProjectTask(pydantic.BaseModel):
    id: int
    project_id: int
    subproject_id: int
    task_id: int
    follow_up: bool


class _ProjectTaskRoot(pydantic.RootModel):
    root: list[ProjectTask]


class ProjectTaskEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/project_management/project_tasks'

    async def all(  # noqa: PLR0913
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        task_ids: typing.Sequence[int] | None = None,
        completed: bool | None = None,
        overdue: bool | None = None,
        search: str | None = None,
        due_status: str | None = None,
        client_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> list[ProjectTask]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-project-tasks."""
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'project_ids[]': project_ids,
                'subproject_ids[]': subproject_ids,
                'task_ids[]': task_ids,
                'completed': completed,
                'overdue': overdue,
                'search': search,
                'due_status': due_status,
                'client_ids[]': client_ids,
            },
        )
        return _ProjectTaskRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, project_task_id: int, **kwargs) -> ProjectTask: ...

    @typing.overload
    async def get(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        task_ids: typing.Sequence[int] | None = None,
        completed: bool | None = None,
        overdue: bool | None = None,
        search: str | None = None,
        due_status: str | None = None,
        client_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> tuple[list[ProjectTask], _common.Meta]: ...

    async def get(  # noqa: PLR0913
        self,
        *,
        project_task_id: int | None = None,
        ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        task_ids: typing.Sequence[int] | None = None,
        completed: bool | None = None,
        overdue: bool | None = None,
        search: str | None = None,
        due_status: str | None = None,
        client_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-project-tasks-id."""
        if project_task_id is not None:
            return ProjectTask.model_validate(await self.api.get(self.endpoint, project_task_id, **kwargs))
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'project_ids[]': project_ids,
                'subproject_ids[]': subproject_ids,
                'task_ids[]': task_ids,
                'completed': completed,
                'overdue': overdue,
                'search': search,
                'due_status': due_status,
                'client_ids[]': client_ids,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _ProjectTaskRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class ProjectWorker(pydantic.BaseModel):
    id: int
    project_id: int
    employee_id: int
    assigned: bool
    inputed_minutes: int | None
    labor_cost_cents: int | None
    spending_cost_cents: int | None


class _ProjectWorkerRoot(pydantic.RootModel):
    root: list[ProjectWorker]


class ProjectWorkerEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/project_management/project_workers'

    async def all(  # noqa: PLR0913
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        no_subproject: bool | None = None,
        employee_ids: typing.Sequence[int] | None = None,
        assigned: bool | None = None,
        project_active: bool | None = None,
        employee_name: str | None = None,
        include_inputed_minuted: bool | None = None,
        include_cost: bool | None = None,
        updated_after: datetime.date | None = None,
        include_labor_cost: bool | None = None,
        **kwargs,
    ) -> list[ProjectWorker]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-project-workers."""
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'project_ids[]': project_ids,
                'subproject_ids[]': subproject_ids,
                'no_subproject': no_subproject,
                'employee_ids[]': employee_ids,
                'assigned': assigned,
                'project_active': project_active,
                'employee_name': employee_name,
                'include_inputed_minutes': include_inputed_minuted,
                'include_cost': include_cost,
                'updated_after': updated_after,
                'include_labor_cost': include_labor_cost,
            },
        )
        return _ProjectWorkerRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, project_worker_id: int, **kwargs) -> ProjectWorker: ...

    @typing.overload
    async def get(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        no_subproject: bool | None = None,
        employee_ids: typing.Sequence[int] | None = None,
        assigned: bool | None = None,
        project_active: bool | None = None,
        employee_name: str | None = None,
        include_inputed_minuted: bool | None = None,
        include_cost: bool | None = None,
        updated_after: datetime.date | None = None,
        include_labor_cost: bool | None = None,
        **kwargs,
    ) -> tuple[list[ProjectWorker], _common.Meta]: ...

    async def get(  # noqa: PLR0913
        self,
        *,
        project_worker_id: int | None = None,
        ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        no_subproject: bool | None = None,
        employee_ids: typing.Sequence[int] | None = None,
        assigned: bool | None = None,
        project_active: bool | None = None,
        employee_name: str | None = None,
        include_inputed_minuted: bool | None = None,
        include_cost: bool | None = None,
        updated_after: datetime.date | None = None,
        include_labor_cost: bool | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-project-workers-id."""
        if project_worker_id is not None:
            return ProjectWorker.model_validate(await self.api.get(self.endpoint, project_worker_id, **kwargs))
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'project_ids[]': project_ids,
                'subproject_ids[]': subproject_ids,
                'no_subproject': no_subproject,
                'employee_ids[]': employee_ids,
                'assigned': assigned,
                'project_active': project_active,
                'employee_name': employee_name,
                'include_inputed_minutes': include_inputed_minuted,
                'include_cost': include_cost,
                'updated_after': updated_after,
                'include_labor_cost': include_labor_cost,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _ProjectWorkerRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class Subproject(pydantic.BaseModel):
    id: int | None
    name: str
    project_id: int
    inputed_minutes: int | None
    labor_cost_cents: int | None


class _SubprojectRoot(pydantic.RootModel):
    root: list[Subproject]


class SubprojectEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/project_management/subprojects'

    async def all(  # noqa: PLR0913
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        name: str | None = None,
        include_no_subproject: bool | None = None,
        include_inputed_minuted: bool | None = None,
        include_cost: bool | None = None,
        updated_after: datetime.date | None = None,
        **kwargs,
    ) -> list[Subproject]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-subprojects."""
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'project_ids[]': project_ids,
                'name': name,
                'include_no_subproject': include_no_subproject,
                'include_inputed_minutes': include_inputed_minuted,
                'include_cost': include_cost,
                'updated_after': updated_after,
            },
        )
        return _SubprojectRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, subproject_id: int, **kwargs) -> Subproject: ...

    @typing.overload
    async def get(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        name: str | None = None,
        include_no_subproject: bool | None = None,
        include_inputed_minuted: bool | None = None,
        include_cost: bool | None = None,
        updated_after: datetime.date | None = None,
        **kwargs,
    ) -> tuple[list[Subproject], _common.Meta]: ...

    async def get(  # noqa: PLR0913
        self,
        *,
        subproject_id: int | None = None,
        ids: typing.Sequence[int] | None = None,
        project_ids: typing.Sequence[int] | None = None,
        name: str | None = None,
        include_no_subproject: bool | None = None,
        include_inputed_minuted: bool | None = None,
        include_cost: bool | None = None,
        updated_after: datetime.date | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-subprojects-id."""
        if subproject_id is not None:
            return Subproject.model_validate(await self.api.get(self.endpoint, subproject_id, **kwargs))
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'project_ids[]': project_ids,
                'name': name,
                'include_no_subproject': include_no_subproject,
                'include_inputed_minutes': include_inputed_minuted,
                'include_cost': include_cost,
                'updated_after': updated_after,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _SubprojectRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class TimeRecord(pydantic.BaseModel):
    id: int
    project_worker_id: int
    attendance_shift_id: int
    subproject_id: int | None
    date: datetime.date | None
    imputed_minutes: int | None
    clock_in: datetime.datetime | None  # date will always be 2000-01-01, only use for .time()
    clock_out: datetime.datetime | None  # date will always be 2000-01-01, only use for .time()


class _TimeRecordRoot(pydantic.RootModel):
    root: list[TimeRecord]


class TimeRecordEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/project_management/time_records'

    async def all(  # noqa: PLR0913
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        project_worker_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        attendance_shift_ids: typing.Sequence[int] | None = None,
        month: int | None = None,
        year: int | None = None,
        updated_after: datetime.date | None = None,
        **kwargs,
    ) -> list[TimeRecord]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-time-records."""
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'project_worker_ids[]': project_worker_ids,
                'subproject_ids[]': subproject_ids,
                'attendance_shift_ids[]': attendance_shift_ids,
                'month': month,
                'year': year,
                'updated_after': updated_after,
            },
        )
        return _TimeRecordRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, time_record_id: int, **kwargs) -> TimeRecord: ...

    @typing.overload
    async def get(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        project_worker_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        attendance_shift_ids: typing.Sequence[int] | None = None,
        month: int | None = None,
        year: int | None = None,
        updated_after: datetime.date | None = None,
        **kwargs,
    ) -> tuple[list[TimeRecord], _common.Meta]: ...

    async def get(  # noqa: PLR0913
        self,
        *,
        time_record_id: int | None = None,
        ids: typing.Sequence[int] | None = None,
        project_worker_ids: typing.Sequence[int] | None = None,
        subproject_ids: typing.Sequence[int] | None = None,
        attendance_shift_ids: typing.Sequence[int] | None = None,
        month: int | None = None,
        year: int | None = None,
        updated_after: datetime.date | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-time-records-id."""
        if time_record_id is not None:
            return TimeRecord.model_validate(await self.api.get(self.endpoint, time_record_id, **kwargs))
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'project_worker_ids[]': project_worker_ids,
                'subproject_ids[]': subproject_ids,
                'attendance_shift_ids[]': attendance_shift_ids,
                'month': month,
                'year': year,
                'updated_after': updated_after,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _TimeRecordRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])
