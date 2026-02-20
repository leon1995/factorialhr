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

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the task
    id: int = pydantic.Field(description='Identifier of the task')
    #: Name of the task
    name: str = pydantic.Field(description='Name of the task')
    #: Company identifier of the author of the task
    company_id: int = pydantic.Field(description='Company identifier of the author of the task')
    #: Content of the task
    content: str | None = pydantic.Field(default=None, description='Content of the task')
    #: Due on date of the task
    due_on: datetime.date | None = pydantic.Field(default=None, description='Due on date of the task')
    #: Employees assigned to the task, assignee_id references to access_id
    assignee_ids: Sequence[int] = pydantic.Field(
        description='Employees assigned to the task, assignee_id references to access_id',
    )
    #: Employee id of the author of the task
    author_employee_id: int | None = pydantic.Field(default=None, description='Employee id of the author of the task')
    #: Completed at date of the task
    completed_at: str | None = pydantic.Field(default=None, description='Completed at date of the task')
    #: Completed by identifier
    completed_by_id: int | None = pydantic.Field(default=None, description='Completed by identifier')
    #: Created at date of the task
    created_at: datetime.datetime = pydantic.Field(description='Created at date of the task')
    #: Updated at date of the task
    updated_at: datetime.datetime = pydantic.Field(description='Updated at date of the task')
    #: Status of the task
    status: TaskStatus | None = pydantic.Field(default=None, description='Status of the task')


class TaskFile(pydantic.BaseModel):
    """Model for tasks_task_file."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the file
    id: int = pydantic.Field(description='Identifier of the file')
    #: Identifier of the task
    task_id: int = pydantic.Field(description='Identifier of the task')
    #: Name of the file
    filename: str = pydantic.Field(description='Name of the file')
    #: Content type of the file
    content_type: str | None = pydantic.Field(default=None, description='Content type of the file')
    #: Path of the file, for downloading the file you need to concat api_url/path
    path: str = pydantic.Field(description='Path of the file, for downloading the file you need to concat api_url/path')
    #: Creation date of the file
    created_at: datetime.datetime = pydantic.Field(description='Creation date of the file')


class TasksEndpoint(Endpoint):
    """Endpoint for tasks/tasks operations."""

    endpoint = 'tasks/tasks'

    async def all(self, **kwargs) -> ListApiResponse[Task]:
        """Get all tasks records.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Task]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Task, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Task]:
        """Get tasks with pagination metadata.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Task]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Task, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, task_id: int | str, **kwargs) -> Task:
        """Get a specific task by ID.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param task_id: The unique identifier.
        :type task_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Task
        """
        data = await self.api.get(self.endpoint, task_id, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Task:
        """Create a new task.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Task
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(response)

    async def update(self, task_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Task:
        """Update a task.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param task_id: The unique identifier of the record to update.
        :type task_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Task
        """
        response = await self.api.put(self.endpoint, task_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(response)

    async def delete(self, task_id: int | str, **kwargs) -> Task:
        """Delete a task.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param task_id: The unique identifier of the record to delete.
        :type task_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: Task
        """
        response = await self.api.delete(self.endpoint, task_id, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[Task]:
        """Bulk create tasks.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[Task]
        """
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Task]).validate_python(response)

    async def bulk_delete(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[Task]:
        """Bulk delete tasks.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[Task]
        """
        response = await self.api.post(self.endpoint, 'bulk_delete', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Task]).validate_python(response)

    async def bulk_update(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[Task]:
        """Bulk update tasks.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[Task]
        """
        response = await self.api.post(self.endpoint, 'bulk_update', json=data, **kwargs)
        return pydantic.TypeAdapter(list[Task]).validate_python(response)

    async def copy(self, data: Mapping[str, typing.Any], **kwargs) -> Task:
        """Copy a task.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Task
        """
        response = await self.api.post(self.endpoint, 'copy', json=data, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(response)

    async def create_comment(self, data: Mapping[str, typing.Any], **kwargs) -> Task:
        """Create a comment on a task.

        Official documentation: `tasks/tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-tasks>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Task
        """
        response = await self.api.post(self.endpoint, 'create_comment', json=data, **kwargs)
        return pydantic.TypeAdapter(Task).validate_python(response)


class TaskFilesEndpoint(Endpoint):
    """Endpoint for tasks/task_files operations."""

    endpoint = 'tasks/task_files'

    async def all(self, **kwargs) -> ListApiResponse[TaskFile]:
        """Get all task files records.

        Official documentation: `tasks/task_files <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-task-files>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[TaskFile]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=TaskFile, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[TaskFile]:
        """Get task files with pagination metadata.

        Official documentation: `tasks/task_files <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-task-files>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[TaskFile]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=TaskFile, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, file_id: int | str, **kwargs) -> TaskFile:
        """Get a specific task file by ID.

        Official documentation: `tasks/task_files <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-task-files>`_

        :param file_id: The unique identifier.
        :type file_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: TaskFile
        """
        data = await self.api.get(self.endpoint, file_id, **kwargs)
        return pydantic.TypeAdapter(TaskFile).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> TaskFile:
        """Create a new task file.

        Official documentation: `tasks/task_files <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-task-files>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: TaskFile
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(TaskFile).validate_python(response)

    async def delete(self, file_id: int | str, **kwargs) -> TaskFile:
        """Delete a task file.

        Official documentation: `tasks/task_files <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-tasks-task-files>`_

        :param file_id: The unique identifier of the record to delete.
        :type file_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: TaskFile
        """
        response = await self.api.delete(self.endpoint, file_id, **kwargs)
        return pydantic.TypeAdapter(TaskFile).validate_python(response)
