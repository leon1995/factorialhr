import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class ExpenseRecord(pydantic.BaseModel):
    """Model for project_management_expense_record."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Expense record ID
    id: int = pydantic.Field(description='Expense record ID')
    #: Project worker ID
    project_worker_id: int = pydantic.Field(description='Project worker ID')
    #: Expense ID
    expense_id: int = pydantic.Field(description='Expense ID')
    #: Subproject ID
    subproject_id: int | None = pydantic.Field(default=None, description='Subproject ID')
    #: Original amount currency
    original_amount_currency: str | None = pydantic.Field(default=None, description='Original amount currency')
    #: Original amount in cents
    original_amount_cents: int | None = pydantic.Field(default=None, description='Original amount in cents')
    #: Legal entity amount currency
    legal_entity_amount_currency: str | None = pydantic.Field(default=None, description='Legal entity amount currency')
    #: Legal entity amount in cents
    legal_entity_amount_cents: str | None = pydantic.Field(default=None, description='Legal entity amount in cents')
    #: Effective date
    effective_on: datetime.date | None = pydantic.Field(default=None, description='Effective date')
    #: Exchange rate
    exchange_rate: int | None = pydantic.Field(default=None, description='Exchange rate')
    #: Expense record status
    status: str | None = pydantic.Field(default=None, description='Expense record status')


class ExpenseRecordEndpoint(Endpoint):
    endpoint = 'project_management/expense_records'

    async def all(self, **kwargs) -> ListApiResponse[ExpenseRecord]:
        """Get all expense records.

        Official documentation: `project_management/expense_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-expense-records>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ExpenseRecord]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ExpenseRecord, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ExpenseRecord]:
        """Get expense records with pagination metadata.

        Official documentation: `project_management/expense_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-expense-records>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ExpenseRecord]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ExpenseRecord, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, expense_id: int | str, **kwargs) -> ExpenseRecord:
        """Get a specific expense record by ID.

        Official documentation: `project_management/expense_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-expense-records-id>`_

        :param expense_id: The unique identifier.
        :type expense_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ExpenseRecord
        """
        data = await self.api.get(self.endpoint, expense_id, **kwargs)
        return pydantic.TypeAdapter(ExpenseRecord).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ExpenseRecord:
        """Create a new expense record.

        Official documentation: `project_management/expense_records <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-expense-records>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ExpenseRecord
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ExpenseRecord).validate_python(response['data'])

    async def update(self, expense_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ExpenseRecord:
        """Update an expense record.

        Official documentation: `project_management/expense_records <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-expense-records-id>`_

        :param expense_id: The unique identifier of the record to update.
        :type expense_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: ExpenseRecord
        """
        response = await self.api.put(self.endpoint, expense_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ExpenseRecord).validate_python(response['data'])

    async def delete(self, expense_id: int | str, **kwargs) -> None:
        """Delete an expense record.

        Official documentation: `project_management/expense_records <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-expense-records-id>`_

        :param expense_id: The unique identifier of the record to delete.
        :type expense_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: None.
        :rtype: None
        """
        await self.api.delete(self.endpoint, expense_id, **kwargs)


class ExportableExpense(pydantic.BaseModel):
    """Model for project_management_exportable_expense."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Expense date
    date: datetime.date | None = pydantic.Field(default=None, description='Expense date')
    #: Project name
    project_name: str | None = pydantic.Field(default=None, description='Project name')
    #: Subproject name
    subproject_name: str | None = pydantic.Field(default=None, description='Subproject name')
    #: Employee name
    employee_name: str = pydantic.Field(description='Employee name')
    #: Employee preferred name
    preferred_name: str | None = pydantic.Field(default=None, description='Employee preferred name')
    #: Expense amount
    amount: str | None = pydantic.Field(default=None, description='Expense amount')
    #: Currency
    currency: str | None = pydantic.Field(default=None, description='Currency')
    #: Expense category
    expense_category: str | None = pydantic.Field(default=None, description='Expense category')
    #: Expense subcategory
    expense_subcategory: str | None = pydantic.Field(default=None, description='Expense subcategory')
    #: Expense status
    expense_status: str | None = pydantic.Field(default=None, description='Expense status')
    #: Link to expense details
    expense_link: str | None = pydantic.Field(default=None, description='Link to expense details')


class ExportableExpenseEndpoint(Endpoint):
    endpoint = 'project_management/exportable_expenses'

    async def all(self, **kwargs) -> ListApiResponse[ExportableExpense]:
        """Get all exportable expenses.

        Official documentation: `project_management/exportable_expenses <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-exportable-expenses>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ExportableExpense]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ExportableExpense, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ExportableExpense]:
        """Get exportable expenses with pagination metadata.

        Official documentation: `project_management/exportable_expenses <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-exportable-expenses>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ExportableExpense]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ExportableExpense, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, expense_id: int | str, **kwargs) -> ExportableExpense:
        """Get a specific exportable expense by ID.

        Official documentation: `project_management/exportable_expenses <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-exportable-expenses-id>`_

        :param expense_id: The unique identifier.
        :type expense_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ExportableExpense
        """
        data = await self.api.get(self.endpoint, expense_id, **kwargs)
        return pydantic.TypeAdapter(ExportableExpense).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ExportableExpense:
        """Create a new exportable expense.

        Official documentation: `project_management/exportable_expenses <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-exportable-expenses>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ExportableExpense
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ExportableExpense).validate_python(response['data'])

    async def update(self, expense_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ExportableExpense:
        """Update an exportable expense.

        Official documentation: `project_management/exportable_expenses <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-exportable-expenses-id>`_

        :param expense_id: The unique identifier of the record to update.
        :type expense_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: ExportableExpense
        """
        response = await self.api.put(self.endpoint, expense_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ExportableExpense).validate_python(response['data'])

    async def delete(self, expense_id: int | str, **kwargs) -> None:
        """Delete an exportable expense.

        Official documentation: `project_management/exportable_expenses <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-exportable-expenses-id>`_

        :param expense_id: The unique identifier of the record to delete.
        :type expense_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: None.
        :rtype: None
        """
        await self.api.delete(self.endpoint, expense_id, **kwargs)


class ExportableProject(pydantic.BaseModel):
    """Model for project_management_exportable_project."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Project ID
    id: str = pydantic.Field(description='Project ID')
    #: Project date
    date: datetime.date | None = pydantic.Field(default=None, description='Project date')
    #: Project name
    project_name: str = pydantic.Field(description='Project name')
    #: Project code
    project_code: str | None = pydantic.Field(default=None, description='Project code')
    #: Project start date
    project_start_date: datetime.date | None = pydantic.Field(default=None, description='Project start date')
    #: Project due date
    project_due_date: datetime.date | None = pydantic.Field(default=None, description='Project due date')
    #: Project status
    project_status: str = pydantic.Field(description='Project status')
    #: Subproject name
    subproject_name: str | None = pydantic.Field(default=None, description='Subproject name')
    #: Employee name
    employee_name: str | None = pydantic.Field(default=None, description='Employee name')
    #: Employee ID
    employee_id: int | None = pydantic.Field(default=None, description='Employee ID')
    #: Inputted time (API returns string but can be float)
    inputed_time: float = pydantic.Field(description='Inputted time (API returns string but can be float)')


class ExportableProjectEndpoint(Endpoint):
    endpoint = 'project_management/exportable_projects'

    async def all(self, **kwargs) -> ListApiResponse[ExportableProject]:
        """Get all exportable projects.

        Official documentation: `project_management/exportable_projects <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-exportable-projects>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ExportableProject]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ExportableProject, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ExportableProject]:
        """Get exportable projects with pagination metadata.

        Official documentation: `project_management/exportable_projects <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-exportable-projects>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ExportableProject]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ExportableProject, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, project_id: int | str, **kwargs) -> ExportableProject:
        """Get a specific exportable project by ID.

        Official documentation: `project_management/exportable_projects <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-exportable-projects-id>`_

        :param project_id: The unique identifier.
        :type project_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ExportableProject
        """
        data = await self.api.get(self.endpoint, project_id, **kwargs)
        return pydantic.TypeAdapter(ExportableProject).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ExportableProject:
        """Create a new exportable project.

        Official documentation: `project_management/exportable_projects <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-exportable-projects>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ExportableProject
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ExportableProject).validate_python(response['data'])

    async def update(self, project_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ExportableProject:
        """Update an exportable project.

        Official documentation: `project_management/exportable_projects <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-exportable-projects-id>`_

        :param project_id: The unique identifier of the record to update.
        :type project_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: ExportableProject
        """
        response = await self.api.put(self.endpoint, project_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ExportableProject).validate_python(response['data'])

    async def delete(self, project_id: int | str, **kwargs) -> None:
        """Delete an exportable project.

        Official documentation: `project_management/exportable_projects <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-exportable-projects-id>`_

        :param project_id: The unique identifier of the record to delete.
        :type project_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: None.
        :rtype: None
        """
        await self.api.delete(self.endpoint, project_id, **kwargs)


class FlexibleTimeRecord(pydantic.BaseModel):
    """Model for project_management_flexible_time_record."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Flexible time record ID
    id: int = pydantic.Field(description='Flexible time record ID')
    #: Record date
    date: datetime.date = pydantic.Field(description='Record date')
    #: Imputed minutes
    imputed_minutes: int = pydantic.Field(description='Imputed minutes')
    #: Project worker ID
    project_worker_id: int = pydantic.Field(description='Project worker ID')
    #: Subproject ID
    subproject_id: int | None = pydantic.Field(default=None, description='Subproject ID')


class FlexibleTimeRecordEndpoint(Endpoint):
    endpoint = 'project_management/flexible_time_records'

    async def all(self, **kwargs) -> ListApiResponse[FlexibleTimeRecord]:
        """Get all flexible time records.

        Official documentation: `project_management/flexible_time_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-flexible-time-records>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[FlexibleTimeRecord]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=FlexibleTimeRecord, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[FlexibleTimeRecord]:
        """Get flexible time records with pagination metadata.

        Official documentation: `project_management/flexible_time_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-flexible-time-records>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[FlexibleTimeRecord]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=FlexibleTimeRecord, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, record_id: int | str, **kwargs) -> FlexibleTimeRecord:
        """Get a specific flexible time record by ID.

        Official documentation: `project_management/flexible_time_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-flexible-time-records-id>`_

        :param record_id: The unique identifier.
        :type record_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: FlexibleTimeRecord
        """
        data = await self.api.get(self.endpoint, record_id, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecord).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> FlexibleTimeRecord:
        """Create a new flexible time record.

        Official documentation: `project_management/flexible_time_records <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-flexible-time-records>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: FlexibleTimeRecord
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecord).validate_python(response['data'])

    async def update(self, record_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> FlexibleTimeRecord:
        """Update a flexible time record.

        Official documentation: `project_management/flexible_time_records <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-flexible-time-records-id>`_

        :param record_id: The unique identifier of the record to update.
        :type record_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: FlexibleTimeRecord
        """
        response = await self.api.put(self.endpoint, record_id, json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecord).validate_python(response['data'])

    async def delete(self, record_id: int | str, **kwargs) -> FlexibleTimeRecord:
        """Delete a flexible time record.

        Official documentation: `project_management/flexible_time_records <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-flexible-time-records-id>`_

        :param record_id: The unique identifier of the record to delete.
        :type record_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: FlexibleTimeRecord
        """
        response = await self.api.delete(self.endpoint, record_id, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecord).validate_python(response)


class FlexibleTimeRecordComment(pydantic.BaseModel):
    """Model for project_management_flexible_time_record_comment."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Comment ID
    id: int = pydantic.Field(description='Comment ID')
    #: Comment content
    content: str = pydantic.Field(description='Comment content')
    #: Flexible time record ID
    flexible_time_record_id: int = pydantic.Field(description='Flexible time record ID')


class FlexibleTimeRecordCommentEndpoint(Endpoint):
    endpoint = 'project_management/flexible_time_record_comments'

    async def all(self, **kwargs) -> ListApiResponse[FlexibleTimeRecordComment]:
        """Get all flexible time record comments.

        Official documentation: `project_management/flexible_time_record_comments <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-flexible-time-record-comments>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[FlexibleTimeRecordComment]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=FlexibleTimeRecordComment, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[FlexibleTimeRecordComment]:
        """Get flexible time record comments with pagination metadata.

        Official documentation: `project_management/flexible_time_record_comments <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-flexible-time-record-comments>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[FlexibleTimeRecordComment]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=FlexibleTimeRecordComment,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, comment_id: int | str, **kwargs) -> FlexibleTimeRecordComment:
        """Get a specific flexible time record comment by ID.

        Official documentation: `project_management/flexible_time_record_comments <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-flexible-time-record-comments-id>`_

        :param comment_id: The unique identifier.
        :type comment_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: FlexibleTimeRecordComment
        """
        data = await self.api.get(self.endpoint, comment_id, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> FlexibleTimeRecordComment:
        """Create a new flexible time record comment.

        Official documentation: `project_management/flexible_time_record_comments <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-flexible-time-record-comments>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: FlexibleTimeRecordComment
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(response['data'])

    async def update(
        self,
        comment_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> FlexibleTimeRecordComment:
        """Update a flexible time record comment.

        Official documentation: `project_management/flexible_time_record_comments <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-flexible-time-record-comments-id>`_

        :param comment_id: The unique identifier of the record to update.
        :type comment_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: FlexibleTimeRecordComment
        """
        response = await self.api.put(self.endpoint, comment_id, json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(response['data'])

    async def delete(self, comment_id: int | str, **kwargs) -> FlexibleTimeRecordComment:
        """Delete a flexible time record comment.

        Official documentation: `project_management/flexible_time_record_comments <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-flexible-time-record-comments-id>`_

        :param comment_id: The unique identifier of the record to delete.
        :type comment_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: FlexibleTimeRecordComment
        """
        response = await self.api.delete(self.endpoint, comment_id, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(response)

    async def delete_by_flexible_time_record(
        self,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> FlexibleTimeRecordComment:
        """Delete a flexible time record comment by flexible time record ID.

        Official documentation: `project_management/flexible_time_record_comments <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-flexible-time-record-comments-delete-by-flexible-time-record>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: FlexibleTimeRecordComment
        """
        response = await self.api.post(self.endpoint, 'delete_by_flexible_time_record', json=data, **kwargs)
        return pydantic.TypeAdapter(FlexibleTimeRecordComment).validate_python(response)

    async def update_by_flexible_time_record(
        self,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> FlexibleTimeRecordComment:
        """Update a flexible time record comment by flexible time record ID.

        Official documentation: `project_management/flexible_time_record_comments <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-flexible-time-record-comments-update-by-flexible-time-record>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: FlexibleTimeRecordComment
        """
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

    model_config = pydantic.ConfigDict(frozen=True)

    #: Project ID
    id: int = pydantic.Field(description='Project ID')
    #: Project name
    name: str = pydantic.Field(description='Project name')
    #: Project code
    code: str | None = pydantic.Field(default=None, description='Project code')
    #: Project start date
    start_date: datetime.date | None = pydantic.Field(default=None, description='Project start date')
    #: Project due date
    due_date: datetime.date | None = pydantic.Field(default=None, description='Project due date')
    #: Project status
    status: ProjectStatus = pydantic.Field(description='Project status')
    #: Employee assignment type
    employees_assignment: ProjectEmployeeAssignment = pydantic.Field(description='Employee assignment type')
    #: Total inputted minutes
    inputed_minutes: int | None = pydantic.Field(default=None, description='Total inputted minutes')
    #: Whether the project is billable
    is_billable: bool = pydantic.Field(description='Whether the project is billable')
    #: Fixed cost in cents
    fixed_cost_cents: int | None = pydantic.Field(default=None, description='Fixed cost in cents')
    #: Labor cost in cents
    labor_cost_cents: int | None = pydantic.Field(default=None, description='Labor cost in cents')
    #: Legal entity ID
    legal_entity_id: int = pydantic.Field(description='Legal entity ID')
    #: Spending cost in cents
    spending_cost_cents: int | None = pydantic.Field(default=None, description='Spending cost in cents')
    #: Client ID
    client_id: int | None = pydantic.Field(default=None, description='Client ID')
    #: Billable rate type
    billable_rate_type: str | None = pydantic.Field(default=None, description='Billable rate type')
    #: Total cost in cents
    total_cost_cents: int | None = pydantic.Field(default=None, description='Total cost in cents')


class ProjectEndpoint(Endpoint):
    endpoint = 'project_management/projects'

    async def all(self, **kwargs) -> ListApiResponse[Project]:
        """Get all projects.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-projects>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Project]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Project, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Project]:
        """Get projects with pagination metadata.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-projects>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Project]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Project, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, project_id: int | str, **kwargs) -> Project:
        """Get a specific project by ID.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-projects-id>`_

        :param project_id: The unique identifier.
        :type project_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Project
        """
        data = await self.api.get(self.endpoint, project_id, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Create a new project.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-projects>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Project
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response['data'])

    async def update(self, project_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Update a project.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-projects-id>`_

        :param project_id: The unique identifier of the record to update.
        :type project_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Project
        """
        response = await self.api.put(self.endpoint, project_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response['data'])

    async def delete(self, project_id: int | str, **kwargs) -> Project:
        """Delete a project.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-projects-id>`_

        :param project_id: The unique identifier of the record to delete.
        :type project_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: Project
        """
        response = await self.api.delete(self.endpoint, project_id, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)

    async def activate(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Activate a project.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-projects-activate>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Project
        """
        response = await self.api.post(self.endpoint, 'activate', json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)

    async def change_assignment(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Change assignment of a project.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-projects-change-assignment>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Project
        """
        response = await self.api.post(self.endpoint, 'change_assignment', json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)

    async def change_status(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Change status of a project.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-projects-change-status>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Project
        """
        response = await self.api.post(self.endpoint, 'change_status', json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)

    async def close(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Close a project.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-projects-close>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Project
        """
        response = await self.api.post(self.endpoint, 'close', json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)

    async def soft_delete(self, data: Mapping[str, typing.Any], **kwargs) -> Project:
        """Soft delete a project.

        Official documentation: `project_management/projects <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-projects-soft-delete>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Project
        """
        response = await self.api.post(self.endpoint, 'soft_delete', json=data, **kwargs)
        return pydantic.TypeAdapter(Project).validate_python(response)


class ProjectTask(pydantic.BaseModel):
    """Model for project_management_project_task."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Project task ID
    id: int = pydantic.Field(description='Project task ID')
    #: Project ID
    project_id: int = pydantic.Field(description='Project ID')
    #: Subproject ID
    subproject_id: int = pydantic.Field(description='Subproject ID')
    #: Task ID
    task_id: int = pydantic.Field(description='Task ID')
    #: Whether this is a follow-up task
    follow_up: bool = pydantic.Field(description='Whether this is a follow-up task')


class ProjectTaskEndpoint(Endpoint):
    endpoint = 'project_management/project_tasks'

    async def all(self, **kwargs) -> ListApiResponse[ProjectTask]:
        """Get all project tasks.

        Official documentation: `project_management/project_tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-project-tasks>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ProjectTask]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ProjectTask, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ProjectTask]:
        """Get project tasks with pagination metadata.

        Official documentation: `project_management/project_tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-project-tasks>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ProjectTask]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ProjectTask, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, task_id: int | str, **kwargs) -> ProjectTask:
        """Get a specific project task by ID.

        Official documentation: `project_management/project_tasks <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-project-tasks-id>`_

        :param task_id: The unique identifier.
        :type task_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ProjectTask
        """
        data = await self.api.get(self.endpoint, task_id, **kwargs)
        return pydantic.TypeAdapter(ProjectTask).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ProjectTask:
        """Create a new project task.

        Official documentation: `project_management/project_tasks <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-project-tasks>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ProjectTask
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ProjectTask).validate_python(response['data'])

    async def update(self, task_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ProjectTask:
        """Update a project task.

        Official documentation: `project_management/project_tasks <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-project-tasks-id>`_

        :param task_id: The unique identifier of the record to update.
        :type task_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: ProjectTask
        """
        response = await self.api.put(self.endpoint, task_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ProjectTask).validate_python(response['data'])

    async def delete(self, task_id: int | str, **kwargs) -> ProjectTask:
        """Delete a project task.

        Official documentation: `project_management/project_tasks <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-project-tasks-id>`_

        :param task_id: The unique identifier of the record to delete.
        :type task_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: ProjectTask
        """
        response = await self.api.delete(self.endpoint, task_id, **kwargs)
        return pydantic.TypeAdapter(ProjectTask).validate_python(response)

    async def bulk_destroy(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[ProjectTask]:
        """Bulk destroy project tasks.

        Official documentation: `project_management/project_tasks <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-project-tasks-bulk-destroy>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[ProjectTask]
        """
        response = await self.api.post(self.endpoint, 'bulk_destroy', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ProjectTask]).validate_python(response)

    async def bulk_duplicate(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[ProjectTask]:
        """Bulk duplicate project tasks.

        Official documentation: `project_management/project_tasks <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-project-tasks-bulk-duplicate>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[ProjectTask]
        """
        response = await self.api.post(self.endpoint, 'bulk_duplicate', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ProjectTask]).validate_python(response)


class ProjectWorker(pydantic.BaseModel):
    """Model for project_management_project_worker."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Project worker ID
    id: int = pydantic.Field(description='Project worker ID')
    #: Project ID
    project_id: int = pydantic.Field(description='Project ID')
    #: Employee ID
    employee_id: int = pydantic.Field(description='Employee ID')
    #: Whether the worker is assigned to the project
    assigned: bool = pydantic.Field(description='Whether the worker is assigned to the project')
    #: Total inputted minutes
    inputed_minutes: int | None = pydantic.Field(default=None, description='Total inputted minutes')
    #: Labor cost in cents
    labor_cost_cents: int | None = pydantic.Field(default=None, description='Labor cost in cents')
    #: Spending cost in cents
    spending_cost_cents: int | None = pydantic.Field(default=None, description='Spending cost in cents')


class ProjectWorkerEndpoint(Endpoint):
    endpoint = 'project_management/project_workers'

    async def all(self, **kwargs) -> ListApiResponse[ProjectWorker]:
        """Get all project workers.

        Official documentation: `project_management/project_workers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-project-workers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[ProjectWorker]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=ProjectWorker, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[ProjectWorker]:
        """Get project workers with pagination metadata.

        Official documentation: `project_management/project_workers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-project-workers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[ProjectWorker]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=ProjectWorker, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, worker_id: int | str, **kwargs) -> ProjectWorker:
        """Get a specific project worker by ID.

        Official documentation: `project_management/project_workers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-project-workers-id>`_

        :param worker_id: The unique identifier.
        :type worker_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: ProjectWorker
        """
        data = await self.api.get(self.endpoint, worker_id, **kwargs)
        return pydantic.TypeAdapter(ProjectWorker).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> ProjectWorker:
        """Create a new project worker.

        Official documentation: `project_management/project_workers <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-project-workers>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: ProjectWorker
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(ProjectWorker).validate_python(response['data'])

    async def update(self, worker_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> ProjectWorker:
        """Update a project worker.

        Official documentation: `project_management/project_workers <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-project-workers-id>`_

        :param worker_id: The unique identifier of the record to update.
        :type worker_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: ProjectWorker
        """
        response = await self.api.put(self.endpoint, worker_id, json=data, **kwargs)
        return pydantic.TypeAdapter(ProjectWorker).validate_python(response['data'])

    async def delete(self, worker_id: int | str, **kwargs) -> ProjectWorker:
        """Delete a project worker.

        Official documentation: `project_management/project_workers <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-project-workers-id>`_

        :param worker_id: The unique identifier of the record to delete.
        :type worker_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: ProjectWorker
        """
        response = await self.api.delete(self.endpoint, worker_id, **kwargs)
        return pydantic.TypeAdapter(ProjectWorker).validate_python(response)

    async def bulk_assign(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[ProjectWorker]:
        """Bulk assign project workers.

        Official documentation: `project_management/project_workers <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-project-workers-bulk-assign>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[ProjectWorker]
        """
        response = await self.api.post(self.endpoint, 'bulk_assign', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ProjectWorker]).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[ProjectWorker]:
        """Bulk create project workers.

        Official documentation: `project_management/project_workers <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-project-workers-bulk-create>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[ProjectWorker]
        """
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[ProjectWorker]).validate_python(response)

    async def unassign(self, data: Mapping[str, typing.Any], **kwargs) -> ProjectWorker:
        """Unassign a project worker.

        Official documentation: `project_management/project_workers <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-project-workers-unassign>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: ProjectWorker
        """
        response = await self.api.post(self.endpoint, 'unassign', json=data, **kwargs)
        return pydantic.TypeAdapter(ProjectWorker).validate_python(response)


class Subproject(pydantic.BaseModel):
    """Model for project_management_subproject."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Subproject ID
    id: int | None = pydantic.Field(default=None, description='Subproject ID')
    #: Subproject name
    name: str = pydantic.Field(description='Subproject name')
    #: Project ID
    project_id: int = pydantic.Field(description='Project ID')
    #: Total inputted minutes
    inputed_minutes: int | None = pydantic.Field(default=None, description='Total inputted minutes')
    #: Labor cost in cents
    labor_cost_cents: int | None = pydantic.Field(default=None, description='Labor cost in cents')
    #: The description of the subproject
    description: str | None = pydantic.Field(default=None, description='The description of the subproject')
    #: The status of the subproject
    status: str | None = pydantic.Field(default=None, description='The status of the subproject')
    #: The code of the subproject
    code: str | None = pydantic.Field(default=None, description='The code of the subproject')
    #: The start date of the subproject
    start_date: datetime.date | None = pydantic.Field(default=None, description='The start date of the subproject')
    #: The due date of the subproject
    due_date: datetime.date | None = pydantic.Field(default=None, description='The due date of the subproject')
    #: Whether the subproject is billable
    is_billable: bool | None = pydantic.Field(default=None, description='Whether the subproject is billable')


class SubprojectEndpoint(Endpoint):
    endpoint = 'project_management/subprojects'

    async def all(self, **kwargs) -> ListApiResponse[Subproject]:
        """Get all subprojects.

        Official documentation: `project_management/subprojects <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-subprojects>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Subproject]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Subproject, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Subproject]:
        """Get subprojects with pagination metadata.

        Official documentation: `project_management/subprojects <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-subprojects>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Subproject]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Subproject, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, subproject_id: int | str, **kwargs) -> Subproject:
        """Get a specific subproject by ID.

        Official documentation: `project_management/subprojects <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-subprojects-id>`_

        :param subproject_id: The unique identifier.
        :type subproject_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Subproject
        """
        data = await self.api.get(self.endpoint, subproject_id, **kwargs)
        return pydantic.TypeAdapter(Subproject).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Subproject:
        """Create a new subproject.

        Official documentation: `project_management/subprojects <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-subprojects>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Subproject
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Subproject).validate_python(response['data'])

    async def update(self, subproject_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Subproject:
        """Update a subproject.

        Official documentation: `project_management/subprojects <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-subprojects-id>`_

        :param subproject_id: The unique identifier of the record to update.
        :type subproject_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Subproject
        """
        response = await self.api.put(self.endpoint, subproject_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Subproject).validate_python(response['data'])

    async def delete(self, subproject_id: int | str, **kwargs) -> Subproject:
        """Delete a subproject.

        Official documentation: `project_management/subprojects <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-subprojects-id>`_

        :param subproject_id: The unique identifier of the record to delete.
        :type subproject_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: Subproject
        """
        response = await self.api.delete(self.endpoint, subproject_id, **kwargs)
        return pydantic.TypeAdapter(Subproject).validate_python(response)

    async def rename(self, data: Mapping[str, typing.Any], **kwargs) -> Subproject:
        """Rename a subproject.

        Official documentation: `project_management/subprojects <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-subprojects-rename>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Subproject
        """
        response = await self.api.post(self.endpoint, 'rename', json=data, **kwargs)
        return pydantic.TypeAdapter(Subproject).validate_python(response)


class TimeRecord(pydantic.BaseModel):
    """Model for project_management_time_record."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Time record ID
    id: int = pydantic.Field(description='Time record ID')
    #: Project worker ID
    project_worker_id: int = pydantic.Field(description='Project worker ID')
    #: Attendance shift ID
    attendance_shift_id: int = pydantic.Field(description='Attendance shift ID')
    #: Subproject ID
    subproject_id: int | None = pydantic.Field(default=None, description='Subproject ID')
    #: Record date
    date: datetime.date | None = pydantic.Field(default=None, description='Record date')
    #: Imputed minutes
    imputed_minutes: int | None = pydantic.Field(default=None, description='Imputed minutes')
    #: Clock in time (date will always be 2000-01-01, only use for .time())
    clock_in: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Clock in time (date will always be 2000-01-01, only use for .time())',
    )
    #: Clock out time (date will always be 2000-01-01, only use for .time())
    clock_out: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Clock out time (date will always be 2000-01-01, only use for .time())',
    )


class TimeRecordEndpoint(Endpoint):
    endpoint = 'project_management/time_records'

    async def all(self, **kwargs) -> ListApiResponse[TimeRecord]:
        """Get all time records.

        Official documentation: `project_management/time_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-time-records>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[TimeRecord]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=TimeRecord, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[TimeRecord]:
        """Get time records with pagination metadata.

        Official documentation: `project_management/time_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-time-records>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[TimeRecord]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=TimeRecord, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, record_id: int | str, **kwargs) -> TimeRecord:
        """Get a specific time record by ID.

        Official documentation: `project_management/time_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-time-records-id>`_

        :param record_id: The unique identifier.
        :type record_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: TimeRecord
        """
        data = await self.api.get(self.endpoint, record_id, **kwargs)
        return pydantic.TypeAdapter(TimeRecord).validate_python(data['data'])

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> TimeRecord:
        """Create a new time record.

        Official documentation: `project_management/time_records <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-time-records>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: TimeRecord
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(TimeRecord).validate_python(response['data'])

    async def update(self, record_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> TimeRecord:
        """Update a time record.

        Official documentation: `project_management/time_records <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-time-records-id>`_

        :param record_id: The unique identifier of the record to update.
        :type record_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: TimeRecord
        """
        response = await self.api.put(self.endpoint, record_id, json=data, **kwargs)
        return pydantic.TypeAdapter(TimeRecord).validate_python(response['data'])

    async def delete(self, record_id: int | str, **kwargs) -> TimeRecord:
        """Delete a time record.

        Official documentation: `project_management/time_records <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-time-records-id>`_

        :param record_id: The unique identifier of the record to delete.
        :type record_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: TimeRecord
        """
        response = await self.api.delete(self.endpoint, record_id, **kwargs)
        return pydantic.TypeAdapter(TimeRecord).validate_python(response)

    async def bulk_delete(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[TimeRecord]:
        """Bulk delete time records.

        Official documentation: `project_management/time_records <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-time-records-bulk-delete>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[TimeRecord]
        """
        response = await self.api.post(self.endpoint, 'bulk_delete', json=data, **kwargs)
        return pydantic.TypeAdapter(list[TimeRecord]).validate_python(response)

    async def bulk_process(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[TimeRecord]:
        """Bulk process time records.

        Official documentation: `project_management/time_records <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-time-records-bulk-process>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[TimeRecord]
        """
        response = await self.api.post(self.endpoint, 'bulk_process', json=data, **kwargs)
        return pydantic.TypeAdapter(list[TimeRecord]).validate_python(response)

    async def update_project_worker(self, data: Mapping[str, typing.Any], **kwargs) -> TimeRecord:
        """Update project worker for a time record.

        Official documentation: `project_management/time_records <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-time-records-update-project-worker>`_

        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: TimeRecord
        """
        response = await self.api.post(self.endpoint, 'update_project_worker', json=data, **kwargs)
        return pydantic.TypeAdapter(TimeRecord).validate_python(response)


class PlannedRecord(pydantic.BaseModel):
    """Model for project_management_planned_record."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: The id of the planned record
    id: int = pydantic.Field(description='The id of the planned record')
    #: The daily minutes of the planned record
    daily_minutes: int = pydantic.Field(description='The daily minutes of the planned record')
    #: The start date of the planned record
    start_date: datetime.date = pydantic.Field(description='The start date of the planned record')
    #: The end date of the planned record
    end_date: datetime.date = pydantic.Field(description='The end date of the planned record')
    #: The project worker id of the planned record
    project_worker_id: int = pydantic.Field(description='The project worker id of the planned record')
    #: The week days of the planned record, start in Sunday 0 and end in Saturday 6
    week_days: Sequence[int] = pydantic.Field(
        description='The week days of the planned record, start in Sunday 0 and end in Saturday 6',
    )
    #: The subproject id of the planned record
    subproject_id: int | None = pydantic.Field(default=None, description='The subproject id of the planned record')


class PlannedRecordsEndpoint(Endpoint):
    """Endpoint for project_management/planned_records operations."""

    endpoint = 'project_management/planned_records'

    async def all(self, **kwargs) -> ListApiResponse[PlannedRecord]:
        """Get all planned records.

        Official documentation: `project_management/planned_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-planned-records>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[PlannedRecord]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=PlannedRecord, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[PlannedRecord]:
        """Get planned records with pagination metadata.

        Official documentation: `project_management/planned_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-planned-records>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[PlannedRecord]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=PlannedRecord, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, planned_record_id: int | str, **kwargs) -> PlannedRecord:
        """Get a specific planned record by ID.

        Official documentation: `project_management/planned_records <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-project-management-planned-records-id>`_

        :param planned_record_id: The unique identifier.
        :type planned_record_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: PlannedRecord
        """
        data = await self.api.get(self.endpoint, planned_record_id, **kwargs)
        return pydantic.TypeAdapter(PlannedRecord).validate_python(data['data'])

    async def update(self, planned_record_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> PlannedRecord:
        """Update a planned record.

        Official documentation: `project_management/planned_records <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-project-management-planned-records-id>`_

        :param planned_record_id: The unique identifier of the record to update.
        :type planned_record_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: PlannedRecord
        """
        response = await self.api.put(self.endpoint, planned_record_id, json=data, **kwargs)
        return pydantic.TypeAdapter(PlannedRecord).validate_python(response['data'])

    async def delete(self, planned_record_id: int | str, **kwargs) -> PlannedRecord:
        """Delete a planned record.

        Official documentation: `project_management/planned_records <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-project-management-planned-records-id>`_

        :param planned_record_id: The unique identifier of the record to delete.
        :type planned_record_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: PlannedRecord
        """
        response = await self.api.delete(self.endpoint, planned_record_id, **kwargs)
        return pydantic.TypeAdapter(PlannedRecord).validate_python(response)

    async def bulk_create(self, data: Mapping[str, typing.Any], **kwargs) -> Sequence[PlannedRecord]:
        """Bulk create planned records.

        Official documentation: `project_management/planned_records <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-project-management-planned-records-bulk-create>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[PlannedRecord]
        """
        response = await self.api.post(self.endpoint, 'bulk_create', json=data, **kwargs)
        return pydantic.TypeAdapter(list[PlannedRecord]).validate_python(response)
