from factorialhr.endpoints import _base


class ExpenseRecord(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/project_management/expense_records'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-expense-records."""
        return await self.api.get(self._endpoint, **kwargs)

    async def single(self, *, expense_record_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-expense-records-id."""
        return await self.api.get(f'{self._endpoint}/{expense_record_id}', **kwargs)


class ExportableExpense(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/project_management/exportable_expenses'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-exportable-expenses."""
        return await self.api.get(self._endpoint, **kwargs)


class ExportableProject(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/project_management/exportable_projects'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-exportable-projects."""
        return await self.api.get(self._endpoint, **kwargs)


class FlexibleTimeRecord(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/project_management/flexible_time_records'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-flexible-time-records."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-flexible-time-records."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete(self, *, flexible_time_record_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-project-management-flexible-time-records-id."""
        return await self.api.delete(f'{self._endpoint}/{flexible_time_record_id}', **kwargs)

    async def update(self, *, flexible_time_record_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-project-management-flexible-time-records-id."""
        return await self.api.put(f'{self._endpoint}/{flexible_time_record_id}', **kwargs)

    async def single(self, *, flexible_time_record_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-flexible-time-records-id."""
        return await self.api.get(f'{self._endpoint}/{flexible_time_record_id}', **kwargs)


class FlexibleTimeRecordComment(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/project_management/flexible_time_record_comments'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-flexible-time-record-comments."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-flexible-time-record-comments."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete_by_flexible_time_record(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-flexible-time-record-comments-delete-by-flexible-time-record."""
        return await self.api.post(f'{self._endpoint}/delete_by_flexible_time_record', **kwargs)

    async def update_by_flexible_time_record(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-flexible-time-record-comments-update-by-flexible-time-record."""
        return await self.api.post(f'{self._endpoint}/update_by_flexible_time_record', **kwargs)

    async def single(self, *, flexible_time_record_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-flexible-time-record-comments-id."""
        return await self.api.get(f'{self._endpoint}/{flexible_time_record_id}', **kwargs)


class Project(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/project_management/projects'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-projects."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-projects."""
        return await self.api.post(self._endpoint, **kwargs)

    async def update(self, *, project_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-project-management-projects-id."""
        return await self.api.post(f'{self._endpoint}/{project_id}', **kwargs)

    async def single(self, *, project_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-projects-id."""
        return await self.api.get(f'{self._endpoint}/{project_id}', **kwargs)

    async def activate(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-projects-activate."""
        return await self.api.post(f'{self._endpoint}/activate', **kwargs)

    async def change_assignment(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-projects-change-assignment."""
        return await self.api.post(f'{self._endpoint}/change_assignment', **kwargs)

    async def close(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-projects-close."""
        return await self.api.post(f'{self._endpoint}/close', **kwargs)

    async def soft_delete(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-projects-soft-delete."""
        return await self.api.post(f'{self._endpoint}/soft_delete', **kwargs)


class ProjectTask(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/project_management/project_tasks'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-project-tasks."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-project-tasks."""
        return await self.api.post(self._endpoint, **kwargs)

    async def update(self, *, project_task_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-project-management-project-tasks-id."""
        return await self.api.post(f'{self._endpoint}/{project_task_id}', **kwargs)

    async def single(self, *, project_task_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-project-tasks-id."""
        return await self.api.get(f'{self._endpoint}/{project_task_id}', **kwargs)

    async def bulk_destroy(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-project-tasks-bulk-destroy."""
        return await self.api.post(f'{self._endpoint}/bulk_destroy', **kwargs)

    async def bulk_duplicate(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-project-tasks-bulk-duplicate."""
        return await self.api.post(f'{self._endpoint}/bulk_duplicate', **kwargs)


class ProjectWorker(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/project_management/project_workers'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-project-workers."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-project-workers."""
        return await self.api.post(self._endpoint, **kwargs)

    async def single(self, *, project_worker_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-project-workers-id."""
        return await self.api.get(f'{self._endpoint}/{project_worker_id}', **kwargs)

    async def bulk_assign(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-project-workers-bulk-assign."""
        return await self.api.post(f'{self._endpoint}/bulk_assign', **kwargs)

    async def bulk_create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-project-workers-bulk-create."""
        return await self.api.post(f'{self._endpoint}/bulk_create', **kwargs)

    async def unassign(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-project-workers-unassign."""
        return await self.api.post(f'{self._endpoint}/unassign', **kwargs)


class Subproject(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/project_management/subprojects'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-subprojects."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-subprojects."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete(self, *, subproject_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-project-management-subprojects-id."""
        return await self.api.delete(f'{self._endpoint}/{subproject_id}', **kwargs)

    async def rename(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-subprojects-rename."""
        return await self.api.post(f'{self._endpoint}/rename', **kwargs)

    async def single(self, *, subproject_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-subprojects-id."""
        return await self.api.get(f'{self._endpoint}/{subproject_id}', **kwargs)


class TimeRecord(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/project_management/time_records'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-time-records."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-time-records."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete(self, *, flexible_time_record_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-project-management-time-records-id."""
        return await self.api.delete(f'{self._endpoint}/{flexible_time_record_id}', **kwargs)

    async def single(self, *, flexible_time_record_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-project-management-time-records-id."""
        return await self.api.get(f'{self._endpoint}/{flexible_time_record_id}', **kwargs)

    async def bulk_delete(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-time-records-bulk-delete."""
        return await self.api.post(f'{self._endpoint}/bulk_delete', **kwargs)

    async def bulk_process(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-time-records-bulk-process."""
        return await self.api.post(f'{self._endpoint}/bulk_process', **kwargs)

    async def update_project_worker(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-project-management-time-records-update-project-worker."""
        return await self.api.post(f'{self._endpoint}/update_project_worker', **kwargs)
