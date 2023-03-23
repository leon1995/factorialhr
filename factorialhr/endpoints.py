import typing

import aiohttp

from factorialhr import models


class NetworkHandler:
    """
    Factorial api class.
    """

    def __init__(self, api_key: str, base_url="https://api.factorialhr.com"):
        self.headers = {"accept": "application/json", "x-api-key": api_key}
        self.session = aiohttp.ClientSession(base_url, headers=self.headers)

    async def close(self):
        await self.session.close()

    async def __aexit__(self, *_, **__):
        await self.close()

    async def __aenter__(self) -> "NetworkHandler":
        return self

    async def get(self, endpoint: str, **params: typing.Any | None) -> typing.Any:
        params = {k: str(v) for k, v in params.items() if v is not None}
        async with self.session.get("/api/" + endpoint, params=params, raise_for_status=True) as resp:
            return await resp.json()

    async def post(self, endpoint: str, data: typing.Any = None, **params: str | None) -> typing.Any:
        return await self.session.post("/api/" + endpoint, data=data, params=params, raise_for_status=True)

    async def put(self, endpoint: str, data: typing.Any = None, **params: str | None) -> typing.Any:
        return await self.session.put("/api/" + endpoint, data=data, params=params, raise_for_status=True)

    async def delete(self, endpoint: str, **params: str | None) -> typing.Any:
        return await self.session.delete("/api/" + endpoint, params=params, raise_for_status=True)


class EmployeesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/core/employees"

    async def all(self, *, full_text_name: str | None = None) -> list[models.Employee]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v2-core-employees
        """
        return [models.Employee(**e) for e in await self.api.get(self._endpoint, full_text_name=full_text_name)]

    async def create(self, **kwargs) -> models.Employee:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-core-employees
        """
        return models.Employee(**await self.api.post(self._endpoint, data=kwargs))

    async def get(self, *, employee_id: int) -> models.Employee:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v2-core-employees-id
        """
        return models.Employee(**await self.api.get(f"{self._endpoint}/{employee_id}"))

    async def update(self, *, employee_id: int, **kwargs) -> models.Employee:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v2-core-employees-id
        """
        return models.Employee(**await self.api.put(f"{self._endpoint}/{employee_id}", data=kwargs))

    async def invite(self, *, employee_id: int, **kwargs) -> models.Employee:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-core-employees-id-invite
        """
        return models.Employee(**await self.api.post(f"{self._endpoint}/{employee_id}/invite", data=kwargs))

    async def change_email(self, *, employee_id: int, **kwargs) -> models.Employee:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v2-core-employees-id-email
        """
        return models.Employee(**await self.api.put(f"{self._endpoint}/{employee_id}/email", data=kwargs))

    async def terminate(self, *, employee_id: int, **kwargs) -> models.Employee:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-core-employees-id-terminate
        """
        return models.Employee(**await self.api.post(f"{self._endpoint}/{employee_id}/terminate", data=kwargs))


class Webhook:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/core/webhooks"

    async def all(self) -> list[models.Webhook]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v2-core-webhooks
        """
        return [models.Webhook(**w) for w in await self.api.get(self._endpoint)]

    async def create(self, **kwargs) -> list[models.Webhook]:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-core-webhooks
        """
        return [models.Webhook(**w) for w in await self.api.post(self._endpoint, data=kwargs)]

    async def update(self, *, webhook_id: int, **kwargs) -> models.Webhook:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v2-core-webhooks-id
        """
        return models.Webhook(**await self.api.put(f"{self._endpoint}/{webhook_id}", data=kwargs))

    async def delete(self, *, webhook_id: int) -> models.Webhook:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v2-core-webhooks-id
        """
        return models.Webhook(**await self.api.delete(f"{self._endpoint}/{webhook_id}"))


class LocationsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/locations"

    async def all(self) -> list[models.Location]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-locations
        """
        return [models.Location(**loc) for loc in await self.api.get(self._endpoint)]

    async def get(self, *, location_id: int) -> models.Location:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-locations-id
        """
        return models.Location(**await self.api.get(f"{self._endpoint}/{location_id}"))


class HolidaysEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/company_holidays"

    async def all(self) -> list[models.CompanyHoliday]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-company-holidays
        """
        return [models.CompanyHoliday(**h) for h in await self.api.get(self._endpoint)]

    async def get(self, *, holiday_id: int) -> models.CompanyHoliday:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-company-holidays-id
        """
        return models.CompanyHoliday(**await self.api.get(f"{self._endpoint}/{holiday_id}"))


class TeamsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/teams"

    async def all(self) -> list[models.Team]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-teams
        """
        return [models.Team(**t) for t in await self.api.get(self._endpoint)]

    async def create(self, **kwargs) -> models.Team:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-teams
        """
        return models.Team(**await self.api.post(self._endpoint, data=kwargs))

    async def get(self, *, team_id: int) -> models.Team:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-teams-id
        """
        return models.Team(**await self.api.get(f"{self._endpoint}/{team_id}"))

    async def update(self, *, team_id: int, **kwargs) -> models.Team:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v1-core-teams-id
        """
        return models.Team(**await self.api.put(f"{self._endpoint}/{team_id}", data=kwargs))

    async def delete(self, *, team_id: int) -> models.Team:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-teams-id
        """
        return models.Team(**await self.api.delete(f"{self._endpoint}/{team_id}"))

    async def assign_employee(self, *, team_id: int, employee_id: int) -> models.Team:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-teams-id-employees-employee-id
        """
        return models.Team(**await self.api.post(f"{self._endpoint}/{team_id}/employees/{employee_id}"))

    async def update_employee(self, *, team_id: int, employee_id: int, **kwargs) -> models.Team:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v1-core-teams-id-employees-employee-id
        """
        return models.Team(**await self.api.put(f"{self._endpoint}/{team_id}/employees/{employee_id}", data=kwargs))

    async def unassign_employee(self, *, team_id: int, employee_id: int) -> models.Team:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v1-core-teams-id-employees-employee-id
        """
        return models.Team(**await self.api.delete(f"{self._endpoint}/{team_id}/employees/{employee_id}"))


class FoldersEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/folders"

    async def all(self, *, name: str | None = None, active: bool | None = None) -> list[models.Folder]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-folders
        """
        return [models.Folder(**f) for f in await self.api.get(self._endpoint, name=name, active=active)]

    async def create(self, **kwargs) -> models.Folder:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-folders
        """
        return models.Folder(**await self.api.post(self._endpoint, data=kwargs))

    async def get(self, *, folder_id: int) -> models.Folder:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-folders-id
        """
        return models.Folder(**await self.api.post(f"{self._endpoint}/{folder_id}"))

    async def update(self, *, folder_id: int, **kwargs) -> models.Folder:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v1-core-folders-id
        """
        return models.Folder(**await self.api.put(f"{self._endpoint}/{folder_id}", data=kwargs))


class DocumentsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/documents"

    async def all(self) -> list[models.Document]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-documents
        """
        return [models.Document(**d) for d in await self.api.put(self._endpoint)]

    async def create(self, **kwargs) -> models.Document:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-documents
        """
        return models.Document(**await self.api.post(self._endpoint, data=kwargs))

    async def get(self, *, document_id: int) -> models.Document:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-documents-id
        """
        return models.Document(**await self.api.get(f"{self._endpoint}/{document_id}"))

    async def update(self, *, document_id: int, **kwargs) -> models.Document:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v1-core-documents-id
        """
        return models.Document(**await self.api.put(f"v1/core/documents/{document_id}", data=kwargs))

    async def delete(self, *, document_id: int) -> models.Document:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v1-core-documents-id
        """
        return models.Document(**await self.api.delete(f"{self._endpoint}/{document_id}"))


class LegalEntitiesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/legal_entities"

    async def all(self) -> list[models.LegalEntity]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-legal-entities
        """
        return [models.LegalEntity(**le) for le in await self.api.put(self._endpoint)]

    async def get(self, *, entity_id: int) -> models.LegalEntity:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-legal-entities-id
        """
        return models.LegalEntity(**await self.api.put(f"{self._endpoint}/{entity_id}"))


class KeysEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/keys"

    async def all(self) -> list[models.Key]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-keys
        """
        return [models.Key(**k) for k in await self.api.put(self._endpoint)]

    async def create(self, **kwargs) -> models.Key:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-keys
        """
        return models.Key(**await self.api.post(self._endpoint, data=kwargs))

    async def delete(self, *, key_id: int) -> models.Key:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v1-core-keys-id
        """
        return models.Key(**await self.api.delete(f"{self._endpoint}/{key_id}"))


class TasksEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/tasks"

    async def all(self) -> list[models.Task]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-tasks
        """
        return [models.Task(**t) for t in await self.api.get(self._endpoint)]

    async def create(self, **kwargs) -> models.Task:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-tasks
        """
        return models.Task(**await self.api.post(self._endpoint, data=kwargs))

    async def get(self, *, task_id: int) -> models.Task:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-tasks-id
        """
        return models.Task(**await self.api.get(f"{self._endpoint}/{task_id}"))

    async def update(self, *, task_id: int, **kwargs) -> models.Task:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v1-core-tasks-id
        """
        return models.Task(**await self.api.put(f"{self._endpoint}/{task_id}", data=kwargs))

    async def delete(self, *, task_id: int) -> models.Task:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v1-core-tasks-id
        """
        return models.Task(**await self.api.get(f"{self._endpoint}/{task_id}"))

    async def resolve(self, *, task_id: int, **kwargs) -> models.Task:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-tasks-id-resolve
        """
        return models.Task(**await self.api.post(f"{self._endpoint}/{task_id}/resolve", data=kwargs))

    async def copy(self, *, task_id: int, **kwargs) -> models.Task:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-tasks-id-copy
        """
        return models.Task(**await self.api.post(f"{self._endpoint}/{task_id}/copy", data=kwargs))

    async def get_files(self, *, task_id: int) -> list[models.File]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-tasks-id-files
        """
        return [models.File(**f) for f in await self.api.get(f"{self._endpoint}/{task_id}/files")]

    async def create_file(self, *, task_id: int, **kwargs) -> models.File:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-tasks-id-files
        """
        return models.File(**await self.api.post(f"{self._endpoint}/{task_id}/files", data=kwargs))

    async def get_file(self, *, task_id: int, file_id: int) -> models.File:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-tasks-task-id-files-id
        """
        return models.File(**await self.api.get(f"{self._endpoint}/{task_id}/files/{file_id}"))

    async def delete_file(self, *, task_id: int, file_id: int) -> models.File:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-tasks-task-id-files-id
        """
        return models.File(**await self.api.post(f"{self._endpoint}/{task_id}/files/{file_id}"))


class CustomFieldsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/custom_fields/"

    async def all(
        self,
        *,
        field_id: int | None = None,
        label: str | None = None,
        slug_id: int | None = None,
        slug_name: str | None = None,
    ) -> list[models.CustomField]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v2-custom-fields-fields
        """
        return [
            models.CustomField(**cf)
            for cf in await self.api.get(
                f"{self._endpoint}/fields", id=field_id, label=label, slug_id=slug_id, slug_name=slug_name
            )
        ]

    async def create(self, **kwargs) -> models.CustomField:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-custom-fields-fields
        """
        return models.CustomField(**await self.api.post(f"{self._endpoint}/fields", data=kwargs))

    async def delete(self, *, field_id: int) -> models.CustomField:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v2-custom-fields-fields-id
        """
        return models.CustomField(**await self.api.delete(f"{self._endpoint}/fields/{field_id}"))

    async def get_values(
        self, *, field_id: int, label: str | None = None, slug_id: int | None = None, slug_name: str | None = None
    ) -> list[models.CustomFieldValue]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v2-custom-fields-values
        """
        return [
            models.CustomFieldValue(**cfv)
            for cfv in await self.api.get(
                f"{self._endpoint}/values", id=field_id, label=label, slug_id=slug_id, slug_name=slug_name
            )
        ]

    async def update_value(self, **kwargs) -> models.CustomField:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v2-custom-fields-values
        """
        return models.CustomField(**await self.api.put(self._endpoint, data=kwargs))


class PostsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/posts"

    async def all(self) -> list[models.Post]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-posts
        """
        return [models.Post(**p) for p in await self.api.get(self._endpoint)]

    async def create(self, **kwargs) -> models.Post:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-posts
        """
        return models.Post(**await self.api.post(self._endpoint, data=kwargs))

    async def get(self, *, post_id: int) -> models.Post:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-posts-id
        """
        return models.Post(**await self.api.post(f"{self._endpoint}/{post_id}"))

    async def update(self, *, post_id: int, **kwargs) -> models.Post:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v1-posts-id
        """
        return models.Post(**await self.api.put(f"{self._endpoint}/{post_id}", data=kwargs))

    async def delete(self, *, post_id: int) -> models.Post:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v1-posts-id
        """
        return models.Post(**await self.api.delete(f"{self._endpoint}/{post_id}"))


class BulkEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/core/bulk"

    async def employees(self) -> list[models.Employee]:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-core-bulk-employee
        """
        return [models.Employee(**e) for e in await self.api.post(f"{self._endpoint}/employees")]

    async def attendance(self) -> list[models.Attendance]:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-core-bulk-attendance
        """
        return [models.Attendance(**a) for a in await self.api.post(f"{self._endpoint}/attendance")]

    async def contract_versions(self) -> list[models.ContractVersion]:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-core-bulk-contract-version
        """
        return [models.ContractVersion(**a) for a in await self.api.post(f"{self._endpoint}/contract_version")]


class CustomTablesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/custom/tables"

    async def all(self, *, topic_name: str | None = None) -> list[models.CustomTable]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-custom-tables
        """
        return [models.CustomTable(**ct) for ct in await self.api.get(self._endpoint, topic_name=topic_name)]

    async def create(self, **kwargs) -> models.CustomTable:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-custom-tables
        """
        return models.CustomTable(**await self.api.post(self._endpoint, data=kwargs))

    async def get(self, *, table_id: int) -> models.CustomTable:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-custom-tables-id
        """
        return models.CustomTable(**await self.api.get(f"{self._endpoint}/{table_id}"))

    async def get_fields(self, *, table_id: int) -> list[models.CustomTableField]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-custom-tables-id-fields
        """
        return [models.CustomTableField(**ctf) for ctf in await self.api.get(f"{self._endpoint}/{table_id}/fields")]

    async def create_field(self, *, table_id: int, **kwargs) -> models.CustomField:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-custom-tables-id-fields
        """
        return models.CustomField(**await self.api.post(f"{self._endpoint}/{table_id}/fields", data=kwargs))

    async def get_employee_fields(self, *, table_id: int, employee_id: int):
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-custom-tables-id-values-employee-id
        """
        raise NotImplementedError("Not implemented because of lacking documentation")

    async def create_employee_fields(self, *, table_id: int, employee_id: int, **kwargs):
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-core-custom-tables-id-values-employee-id
        """
        raise NotImplementedError("Not implemented because of lacking documentation")


class EventsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/events"

    async def get_triggered(self) -> list[models.Event]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-core-events
        """
        return [models.Event(**e) for e in await self.api.get(self._endpoint)]


class WorkplacesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/core/workplaces"

    async def all(self) -> list[models.Workplace]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v2-core-workplaces
        """
        return [models.Workplace(**w) for w in await self.api.get(self._endpoint)]

    async def create(self, **kwargs) -> models.Workplace:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-core-workplaces
        """
        return models.Workplace(**await self.api.post(self._endpoint, data=kwargs))

    async def get(self, *, workplace_id: int) -> models.Workplace:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v2-core-workplaces-id
        """
        return models.Workplace(**await self.api.get(f"{self._endpoint}/{workplace_id}"))

    async def update(self, *, workplace_id: int, **kwargs) -> models.Workplace:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v2-core-workplaces-id
        """
        return models.Workplace(**await self.api.put(f"{self._endpoint}/{workplace_id}", data=kwargs))

    async def delete(self, *, workplace_id: int) -> models.Workplace:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v2-core-workplaces-id
        """
        return models.Workplace(**await self.api.delete(f"{self._endpoint}/{workplace_id}"))


class AttendanceEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/time/attendance"

    async def all(self) -> list[models.Attendance]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v2-time-attendance
        """
        return [models.Attendance(**a) for a in await self.api.get(self._endpoint)]

    async def create(self, **kwargs) -> models.Attendance:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-time-attendance
        """
        return models.Attendance(**await self.api.post(self._endpoint, data=kwargs))


class LeaveTypesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/time/leave_types"

    async def all(self) -> list[models.LeaveType]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-time-leave-types
        """
        return [models.LeaveType(**lt) for lt in await self.api.get(self._endpoint)]

    async def create(self, **kwargs) -> models.LeaveType:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-time-leave-types
        """
        return models.LeaveType(**await self.api.post(self._endpoint, data=kwargs))

    async def update(self, *, leave_type_id: int, **kwargs) -> models.LeaveType:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v1-time-leave-types-id
        """
        return models.LeaveType(**await self.api.put(f"{self._endpoint}/{leave_type_id}", data=kwargs))


class LeavesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/time/leaves"

    async def all(self) -> list[models.Leave]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v2-time-leaves
        """
        return [models.Leave(**leave) for leave in await self.api.get(self._endpoint)]

    async def create(self, **kwargs) -> models.Leave:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v2-time-leaves
        """
        return models.Leave(**await self.api.post(self._endpoint, data=kwargs))

    async def get(self, *, leave_id: int) -> models.Leave:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v2-time-leaves-id
        """
        return models.Leave(**await self.api.get(f"{self._endpoint}/{leave_id}"))

    async def update(self, *, leave_id: int, **kwargs) -> models.Leave:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v2-time-leaves-id
        """
        return models.Leave(**await self.api.put(f"{self._endpoint}/{leave_id}", data=kwargs))

    async def delete(self, *, leave_id: int) -> models.Leave:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v2-time-leaves-id
        """
        return models.Leave(**await self.api.delete(f"{self._endpoint}/{leave_id}"))


class FamilySituationEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError("This is france only and will be added in a future release")

    @property
    def _endpoint(self) -> str:
        return "v1/payroll/family_situation"


class JobPostingsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/ats/job_postings"

    async def all(
        self,
        *,
        status: models.JobPostingStatus | None = None,
        team_id: int | None = None,
        location_id: int | None = None,
    ) -> list[models.JobPosting]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-ats-job-postings
        """
        return [
            models.JobPosting(**p)
            for p in await self.api.get(self._endpoint, status=status, team_id=team_id, location_id=location_id)
        ]

    async def create(self, **kwargs) -> models.JobPosting:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-ats-job-postings
        """
        return models.JobPosting(**await self.api.post(self._endpoint, data=kwargs))

    async def update(self, *, job_id: int, **kwargs) -> models.JobPosting:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v1-ats-job-postings-id
        """
        return models.JobPosting(**await self.api.put(f"{self._endpoint}/{job_id}", data=kwargs))

    async def delete(self, *, job_id: int) -> models.JobPosting:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v1-ats-job-postings-id
        """
        return models.JobPosting(**await self.api.delete(f"{self._endpoint}/{job_id}"))

    async def duplicate(self, *, job_id: int) -> models.JobPosting:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-ats-job-postings-id-duplicate
        """
        return models.JobPosting(**await self.api.post(f"{self._endpoint}/{job_id}"))


class CandidatesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/ats/job_postings"

    async def all(self) -> list[models.Candidate]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-ats-candidates
        """
        return [models.Candidate(**p) for p in await self.api.get(self._endpoint)]

    async def create(self, **kwargs) -> models.Candidate:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-ats-candidates
        """
        return models.Candidate(**await self.api.post(self._endpoint, data=kwargs))

    async def update(self, *, candidate_id: int, **kwargs) -> models.Candidate:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v1-ats-candidates-id
        """
        return models.Candidate(**await self.api.put(f"{self._endpoint}/{candidate_id}", data=kwargs))


class ContractVersionsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError()

    @property
    def _endpoint(self) -> str:
        return "v1/payroll/contract_versions"


class SupplementsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError()

    @property
    def _endpoint(self) -> str:
        return "v1/payroll/supplements"


class ShiftManagementEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError()

    @property
    def _endpoint(self) -> str:
        return "v1/time/shifts_management"


class BreaksEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        # TODO: oauth2 only
        raise NotImplementedError()

    @property
    def _endpoint(self) -> str:
        return "v1/time/breaks"


class ApplicationEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError()

    @property
    def _endpoint(self) -> str:
        return "v1/ats/applications"


class ATSMessagesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError()

    @property
    def _endpoint(self) -> str:
        return "v1/ats/messages"


class TimeOffPoliciesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/time/policies"

    async def all(self) -> list[models.TimeOffPolicy]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-time-policies
        """
        return [models.TimeOffPolicy(**top) for top in await self.api.get(self._endpoint)]

    async def get(self, *, policy_id: int) -> models.TimeOffPolicy:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-time-policies-id
        """
        return models.TimeOffPolicy(**await self.api.get(f"{self._endpoint}/{policy_id}"))


class ExpensesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        # TODO: oauth2 only
        raise NotImplementedError()

    @property
    def _endpoint(self) -> str:
        return "v1/finance/expenses"


class CompensationsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/payroll/compensations"

    async def all(self) -> list[models.Compensation]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-payroll-compensations
        """
        return [models.Compensation(**top) for top in await self.api.get(self._endpoint)]

    async def create(self, **kwargs) -> models.Compensation:
        """
        Implements https://apidoc.factorialhr.com/reference/post_v1-payroll-compensations
        """
        return models.Compensation(**await self.api.post(self._endpoint, data=kwargs))

    async def get(self, *, compensation_id: int) -> models.Compensation:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-payroll-compensations-id
        """
        return models.Compensation(**await self.api.get(f"{self._endpoint}/{compensation_id}"))

    async def update(self, *, compensation_id: int, **kwargs) -> models.Compensation:
        """
        Implements https://apidoc.factorialhr.com/reference/put_v1-payroll-compensations-id
        """
        return models.Compensation(**await self.api.put(f"{self._endpoint}/{compensation_id}", data=kwargs))

    async def delete(self, *, compensation_id: int) -> models.Compensation:
        """
        Implements https://apidoc.factorialhr.com/reference/delete_v1-payroll-compensations-id
        """
        return models.Compensation(**await self.api.delete(f"{self._endpoint}/{compensation_id}"))


class TaxonomiesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/payroll/taxonomies"

    async def all(self) -> list[models.Taxonomy]:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-payroll-taxonomies
        """
        return [models.Taxonomy(**top) for top in await self.api.get(self._endpoint)]

    async def get(self, *, taxonomy_id: int) -> models.Taxonomy:
        """
        Implements https://apidoc.factorialhr.com/reference/get_v1-payroll-taxonomies-id
        """
        return models.Taxonomy(**await self.api.get(f"{self._endpoint}/{taxonomy_id}"))
