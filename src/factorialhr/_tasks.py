import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class TaskStatus(StrEnum):
    """Enum for task status."""

    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'
    DISCARDED = 'discarded'


class Task(pydantic.BaseModel):
    """Model for tasks_task."""

    id: int = pydantic.Field(description='Identifier of the task')
    name: str = pydantic.Field(description='Name of the task')
    company_id: int = pydantic.Field(description='Company identifier of the author of the task')
    content: str | None = pydantic.Field(default=None, description='Content of the task')
    due_on: datetime.date | None = pydantic.Field(default=None, description='Due on date of the task')
    assignee_ids: Sequence[int] = pydantic.Field(
        description='Employees assigned to the task, assignee_id references to access_id',
    )
    author_employee_id: int | None = pydantic.Field(default=None, description='Employee id of the author of the task')
    completed_at: str | None = pydantic.Field(default=None, description='Completed at date of the task')
    completed_by_id: int | None = pydantic.Field(default=None, description='Completed by identifier')
    created_at: datetime.datetime = pydantic.Field(description='Created at date of the task')
    updated_at: datetime.datetime = pydantic.Field(description='Updated at date of the task')
    status: TaskStatus | None = pydantic.Field(default=None, description='Status of the task')


class TaskFile(pydantic.BaseModel):
    """Model for tasks_task_file."""

    id: int = pydantic.Field(description='Identifier of the file')
    task_id: int = pydantic.Field(description='Identifier of the task')
    filename: str = pydantic.Field(description='Name of the file')
    content_type: str | None = pydantic.Field(default=None, description='Content type of the file')
    path: str = pydantic.Field(description='Path of the file, for downloading the file you need to concat api_url/path')
    created_at: datetime.datetime = pydantic.Field(description='Creation date of the file')


class TasksEndpoint(Endpoint):
    """Endpoint for tasks/tasks operations."""

    endpoint = 'tasks/tasks'

    async def all(self, **kwargs) -> ListApiResponse[Task]:
        """Get all tasks records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Task, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Task]:
        """Get tasks with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Task, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, task_id: int | str, **kwargs) -> Task:
        """Get a specific task by ID."""
        data = await self.api.get(self.endpoint, task_id, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Task:
        """Create a new task."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(response)

    async def update(self, task_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Task:
        """Update a task."""
        response = await self.api.put(self.endpoint, task_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(response)

    async def delete(self, task_id: int | str, **kwargs) -> Task:
        """Delete a task."""
        response = await self.api.delete(self.endpoint, task_id, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> list[Task]:
        """Bulk create tasks."""
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Task]).validate_python(response)

    async def bulk_delete(self, data: Mapping[str, typing.Any], **kwargs) -> list[Task]:
        """Bulk delete tasks."""
        response = await self.api.post(self.endpoint, 'bulk_delete', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Task]).validate_python(response)

    async def bulk_update(self, data: Mapping[str, typing.Any], **kwargs) -> list[Task]:
        """Bulk update tasks."""
        response = await self.api.post(self.endpoint, 'bulk_update', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Task]).validate_python(response)

    async def copy(self, data: Mapping[str, typing.Any], **kwargs) -> Task:
        """Copy a task."""
        response = await self.api.post(self.endpoint, 'copy', json=data, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(response)

    async def create_comment(self, data: Mapping[str, typing.Any], **kwargs) -> Task:
        """Create a comment on a task."""
        response = await self.api.post(self.endpoint, 'create_comment', json=data, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(response)


class TaskFilesEndpoint(Endpoint):
    """Endpoint for tasks/task_files operations."""

    endpoint = 'tasks/task_files'

    async def all(self, **kwargs) -> ListApiResponse[TaskFile]:
        """Get all task files records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=TaskFile, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[TaskFile]:
        """Get task files with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=TaskFile, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, file_id: int | str, **kwargs) -> TaskFile:
        """Get a specific task file by ID."""
        data = await self.api.get(self.endpoint, file_id, **kwargs)
        return pydantic.TypeAdapter(TaskFile).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> TaskFile:
        """Create a new task file."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(TaskFile).validate_python(response)

    async def delete(self, file_id: int | str, **kwargs) -> TaskFile:
        """Delete a task file."""
        response = await self.api.delete(self.endpoint, file_id, **kwargs)
        return pydantic.TypeAdapter(TaskFile).validate_python(response)
