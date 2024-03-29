"""Implements the endpoints."""

import datetime
import typing

import httpx

from factorialhr import models


class NetworkHandler:
    """Factorial api class."""

    def __init__(self, authorizer: httpx.Auth, base_url: str = "https://api.factorialhr.com"):
        headers = {"accept": "application/json"}
        self._client = httpx.AsyncClient(base_url=base_url, headers=headers, auth=authorizer)

    async def close(self):
        """Close the client session."""
        await self._client.aclose()

    async def __aexit__(self, *_, **__):  # noqa: ANN002
        await self.close()

    async def __aenter__(self) -> "NetworkHandler":
        return self

    async def get(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a get request."""
        resp = await self._client.get("/api/" + endpoint, **kwargs)
        resp.raise_for_status()
        return resp.json()

    async def post(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a post request."""
        resp = await self._client.post("/api/" + endpoint, **kwargs)
        resp.raise_for_status()
        return resp.json()

    async def put(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a put request."""
        resp = await self._client.put("/api/" + endpoint, **kwargs)
        resp.raise_for_status()
        return resp.json()

    async def delete(self, endpoint: str, **kwargs) -> typing.Any:
        """Perform a delete request."""
        resp = await self._client.delete("/api/" + endpoint, **kwargs)
        resp.raise_for_status()
        return resp.json()


class EmployeesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/core/employees"

    async def all(self, *, full_text_name: str | None = None, **kwargs) -> list[models.Employee]:
        """Implement https://apidoc.factorialhr.com/reference/get_v2-core-employees."""
        params = {"full_text_name": full_text_name} if full_text_name is not None else {}
        return [models.Employee(**e) for e in await self.api.get(self._endpoint, params=params, **kwargs)]

    async def create(self, **kwargs) -> models.Employee:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-core-employees."""
        return models.Employee(**await self.api.post(self._endpoint, **kwargs))

    async def get(self, *, employee_id: int, **kwargs) -> models.Employee:
        """Implement https://apidoc.factorialhr.com/reference/get_v2-core-employees-id."""
        return models.Employee(**await self.api.get(f"{self._endpoint}/{employee_id}", **kwargs))

    async def update(self, *, employee_id: int, **kwargs) -> models.Employee:
        """Implement https://apidoc.factorialhr.com/reference/put_v2-core-employees-id."""
        return models.Employee(**await self.api.put(f"{self._endpoint}/{employee_id}", **kwargs))

    async def invite(self, *, employee_id: int, **kwargs) -> models.Employee:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-core-employees-id-invite."""
        return models.Employee(**await self.api.post(f"{self._endpoint}/{employee_id}/invite", **kwargs))

    async def change_email(self, *, employee_id: int, **kwargs) -> models.Employee:
        """Implement https://apidoc.factorialhr.com/reference/put_v2-core-employees-id-email."""
        return models.Employee(**await self.api.put(f"{self._endpoint}/{employee_id}/email", **kwargs))

    async def terminate(self, *, employee_id: int, **kwargs) -> models.Employee:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-core-employees-id-terminate."""
        return models.Employee(**await self.api.post(f"{self._endpoint}/{employee_id}/terminate", **kwargs))


class Webhook:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/core/webhooks"

    async def all(self, **kwargs) -> list[models.Webhook]:
        """Implement https://apidoc.factorialhr.com/reference/get_v2-core-webhooks."""
        return [models.Webhook(**w) for w in await self.api.get(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> list[models.Webhook]:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-core-webhooks."""
        return [models.Webhook(**w) for w in await self.api.post(self._endpoint, **kwargs)]

    async def update(self, *, webhook_id: int, **kwargs) -> models.Webhook:
        """Implement https://apidoc.factorialhr.com/reference/put_v2-core-webhooks-id."""
        return models.Webhook(**await self.api.put(f"{self._endpoint}/{webhook_id}", **kwargs))

    async def delete(self, *, webhook_id: int, **kwargs) -> models.Webhook:
        """Implement https://apidoc.factorialhr.com/reference/delete_v2-core-webhooks-id."""
        return models.Webhook(**await self.api.delete(f"{self._endpoint}/{webhook_id}", **kwargs))


class MeEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/me"

    async def get(self, **kwargs) -> models.Me:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-me."""
        return models.Me(**await self.api.get(self._endpoint, **kwargs))


class LocationsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/locations"

    async def all(self, **kwargs) -> list[models.Location]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-locations."""
        return [models.Location(**loc) for loc in await self.api.get(self._endpoint, **kwargs)]

    async def get(self, *, location_id: int, **kwargs) -> models.Location:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-locations-id."""
        return models.Location(**await self.api.get(f"{self._endpoint}/{location_id}", **kwargs))


class HolidaysEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/company_holidays"

    async def all(self, **kwargs) -> list[models.CompanyHoliday]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-company-holidays."""
        return [models.CompanyHoliday(**h) for h in await self.api.get(self._endpoint, **kwargs)]

    async def get(self, *, holiday_id: int, **kwargs) -> models.CompanyHoliday:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-company-holidays-id."""
        return models.CompanyHoliday(**await self.api.get(f"{self._endpoint}/{holiday_id}", **kwargs))


class TeamsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/teams"

    async def all(self, **kwargs) -> list[models.Team]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-teams."""
        return [models.Team(**t) for t in await self.api.get(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> models.Team:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-teams."""
        return models.Team(**await self.api.post(self._endpoint, **kwargs))

    async def get(self, *, team_id: int, **kwargs) -> models.Team:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-teams-id."""
        return models.Team(**await self.api.get(f"{self._endpoint}/{team_id}", **kwargs))

    async def update(self, *, team_id: int, **kwargs) -> models.Team:
        """Implement https://apidoc.factorialhr.com/reference/put_v1-core-teams-id."""
        return models.Team(**await self.api.put(f"{self._endpoint}/{team_id}", **kwargs))

    async def delete(self, *, team_id: int, **kwargs) -> models.Team:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-teams-id."""
        return models.Team(**await self.api.delete(f"{self._endpoint}/{team_id}", **kwargs))

    async def assign_employee(self, *, team_id: int, employee_id: int, **kwargs) -> models.Team:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-teams-id-employees-employee-id."""
        return models.Team(**await self.api.post(f"{self._endpoint}/{team_id}/employees/{employee_id}", **kwargs))

    async def update_employee(self, *, team_id: int, employee_id: int, **kwargs) -> models.Team:
        """Implement https://apidoc.factorialhr.com/reference/put_v1-core-teams-id-employees-employee-id."""
        return models.Team(**await self.api.put(f"{self._endpoint}/{team_id}/employees/{employee_id}", **kwargs))

    async def unassign_employee(self, *, team_id: int, employee_id: int, **kwargs) -> models.Team:
        """Implement https://apidoc.factorialhr.com/reference/delete_v1-core-teams-id-employees-employee-id."""
        return models.Team(**await self.api.delete(f"{self._endpoint}/{team_id}/employees/{employee_id}", **kwargs))


class FoldersEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/folders"

    async def all(self, *, name: str | None = None, active: bool | None = None, **kwargs) -> list[models.Folder]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-folders."""
        params: dict[str, str | bool] = {}
        if name is not None:
            params["name"] = name
        if active is not None:
            params["active"] = active
        return [models.Folder(**f) for f in await self.api.get(self._endpoint, params=params, **kwargs)]

    async def create(self, **kwargs) -> models.Folder:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-folders."""
        return models.Folder(**await self.api.post(self._endpoint, **kwargs))

    async def get(self, *, folder_id: int, **kwargs) -> models.Folder:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-folders-id."""
        return models.Folder(**await self.api.post(f"{self._endpoint}/{folder_id}", **kwargs))

    async def update(self, *, folder_id: int, **kwargs) -> models.Folder:
        """Implement https://apidoc.factorialhr.com/reference/put_v1-core-folders-id."""
        return models.Folder(**await self.api.put(f"{self._endpoint}/{folder_id}", **kwargs))


class DocumentsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/documents"

    async def all(self, **kwargs) -> list[models.Document]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-documents."""
        return [models.Document(**d) for d in await self.api.put(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> models.Document:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-documents."""
        return models.Document(**await self.api.post(self._endpoint, **kwargs))

    async def get(self, *, document_id: int, **kwargs) -> models.Document:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-documents-id."""
        return models.Document(**await self.api.get(f"{self._endpoint}/{document_id}", **kwargs))

    async def update(self, *, document_id: int, **kwargs) -> models.Document:
        """Implement https://apidoc.factorialhr.com/reference/put_v1-core-documents-id."""
        return models.Document(**await self.api.put(f"v1/core/documents/{document_id}", **kwargs))

    async def delete(self, *, document_id: int, **kwargs) -> models.Document:
        """Implement https://apidoc.factorialhr.com/reference/delete_v1-core-documents-id."""
        return models.Document(**await self.api.delete(f"{self._endpoint}/{document_id}", **kwargs))


class LegalEntitiesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/legal_entities"

    async def all(self, **kwargs) -> list[models.LegalEntity]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-legal-entities."""
        return [models.LegalEntity(**le) for le in await self.api.get(self._endpoint, **kwargs)]

    async def get(self, *, entity_id: int, **kwargs) -> models.LegalEntity:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-legal-entities-id."""
        return models.LegalEntity(**await self.api.get(f"{self._endpoint}/{entity_id}", **kwargs))


class KeysEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/keys"

    async def all(self, **kwargs) -> list[models.Key]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-keys."""
        return [models.Key(**k) for k in await self.api.put(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> models.Key:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-keys."""
        return models.Key(**await self.api.post(self._endpoint, **kwargs))

    async def delete(self, *, key_id: int, **kwargs) -> models.Key:
        """Implement https://apidoc.factorialhr.com/reference/delete_v1-core-keys-id."""
        return models.Key(**await self.api.delete(f"{self._endpoint}/{key_id}", **kwargs))


class TasksEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/tasks"

    async def all(self, **kwargs) -> list[models.Task]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-tasks."""
        return [models.Task(**t) for t in await self.api.get(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> models.Task:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-tasks."""
        return models.Task(**await self.api.post(self._endpoint, **kwargs))

    async def get(self, *, task_id: int, **kwargs) -> models.Task:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-tasks-id."""
        return models.Task(**await self.api.get(f"{self._endpoint}/{task_id}", **kwargs))

    async def update(self, *, task_id: int, **kwargs) -> models.Task:
        """Implement https://apidoc.factorialhr.com/reference/put_v1-core-tasks-id."""
        return models.Task(**await self.api.put(f"{self._endpoint}/{task_id}", **kwargs))

    async def delete(self, *, task_id: int, **kwargs) -> models.Task:
        """Implement https://apidoc.factorialhr.com/reference/delete_v1-core-tasks-id."""
        return models.Task(**await self.api.get(f"{self._endpoint}/{task_id}", **kwargs))

    async def resolve(self, *, task_id: int, **kwargs) -> models.Task:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-tasks-id-resolve."""
        return models.Task(**await self.api.post(f"{self._endpoint}/{task_id}/resolve", **kwargs))

    async def copy(self, *, task_id: int, **kwargs) -> models.Task:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-tasks-id-copy."""
        return models.Task(**await self.api.post(f"{self._endpoint}/{task_id}/copy", **kwargs))

    async def get_files(self, *, task_id: int, **kwargs) -> list[models.File]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-tasks-id-files."""
        return [models.File(**f) for f in await self.api.get(f"{self._endpoint}/{task_id}/files", **kwargs)]

    async def create_file(self, *, task_id: int, **kwargs) -> models.File:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-tasks-id-files."""
        return models.File(**await self.api.post(f"{self._endpoint}/{task_id}/files", **kwargs))

    async def get_file(self, *, task_id: int, file_id: int, **kwargs) -> models.File:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-tasks-task-id-files-id."""
        return models.File(**await self.api.get(f"{self._endpoint}/{task_id}/files/{file_id}", **kwargs))

    async def delete_file(self, *, task_id: int, file_id: int, **kwargs) -> models.File:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-tasks-task-id-files-id."""
        return models.File(**await self.api.post(f"{self._endpoint}/{task_id}/files/{file_id}", **kwargs))


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
            **kwargs,
    ) -> list[models.CustomField]:
        """Implement https://apidoc.factorialhr.com/reference/get_v2-custom-fields-fields."""
        params: dict[str, str | int] = {}
        if field_id is not None:
            params["field_id"] = field_id
        if label is not None:
            params["label"] = label
        if slug_id is not None:
            params["slug_id"] = slug_id
        if slug_name is not None:
            params["slug_name"] = slug_name
        return [
            models.CustomField(**cf) for cf in await self.api.get(f"{self._endpoint}/fields", params=params, **kwargs)
        ]

    async def create(self, **kwargs) -> models.CustomField:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-custom-fields-fields."""
        return models.CustomField(**await self.api.post(f"{self._endpoint}/fields", **kwargs))

    async def delete(self, *, field_id: int, **kwargs) -> models.CustomField:
        """Implement https://apidoc.factorialhr.com/reference/delete_v2-custom-fields-fields-id."""
        return models.CustomField(**await self.api.delete(f"{self._endpoint}/fields/{field_id}", **kwargs))

    async def get_values(
            self,
            *,
            field_id: int,
            label: str | None = None,
            slug_id: int | None = None,
            slug_name: str | None = None,
            **kwargs,
    ) -> list[models.CustomFieldValue]:
        """Implement https://apidoc.factorialhr.com/reference/get_v2-custom-fields-values."""
        params: dict[str, str | int] = {}
        if field_id is not None:
            params["field_id"] = field_id
        if label is not None:
            params["label"] = label
        if slug_id is not None:
            params["slug_id"] = slug_id
        if slug_name is not None:
            params["slug_name"] = slug_name
        return [
            models.CustomFieldValue(**cfv)
            for cfv in await self.api.get(f"{self._endpoint}/values", params=params, **kwargs)
        ]

    async def update_value(self, **kwargs) -> models.CustomField:
        """Implement https://apidoc.factorialhr.com/reference/put_v2-custom-fields-values."""
        return models.CustomField(**await self.api.put(self._endpoint, **kwargs))


class PostsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/posts"

    async def all(self, **kwargs) -> list[models.Post]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-posts."""
        return [models.Post(**p) for p in await self.api.get(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> models.Post:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-posts."""
        return models.Post(**await self.api.post(self._endpoint, **kwargs))

    async def get(self, *, post_id: int, **kwargs) -> models.Post:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-posts-id."""
        return models.Post(**await self.api.post(f"{self._endpoint}/{post_id}", **kwargs))

    async def update(self, *, post_id: int, **kwargs) -> models.Post:
        """Implement https://apidoc.factorialhr.com/reference/put_v1-posts-id."""
        return models.Post(**await self.api.put(f"{self._endpoint}/{post_id}", **kwargs))

    async def delete(self, *, post_id: int, **kwargs) -> models.Post:
        """Implement https://apidoc.factorialhr.com/reference/delete_v1-posts-id."""
        return models.Post(**await self.api.delete(f"{self._endpoint}/{post_id}", **kwargs))


class BulkEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/core/bulk"

    async def employees(self, **kwargs) -> list[models.Employee]:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-core-bulk-employee."""
        return [models.Employee(**e) for e in await self.api.post(f"{self._endpoint}/employees", **kwargs)]

    async def attendance(self, **kwargs) -> list[models.Attendance]:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-core-bulk-attendance."""
        return [models.Attendance(**a) for a in await self.api.post(f"{self._endpoint}/attendance", **kwargs)]

    async def contract_versions(self, **kwargs) -> list[models.ContractVersion]:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-core-bulk-contract-version."""
        return [
            models.ContractVersion(**a) for a in await self.api.post(f"{self._endpoint}/contract_version", **kwargs)
        ]


class CustomTablesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/custom/tables"

    async def all(self, *, topic_name: str | None = None, **kwargs) -> list[models.CustomTable]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-custom-tables."""
        params = {"topic_name": topic_name} if topic_name else {}
        return [models.CustomTable(**ct) for ct in await self.api.get(self._endpoint, params=params, **kwargs)]

    async def create(self, **kwargs) -> models.CustomTable:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-custom-tables."""
        return models.CustomTable(**await self.api.post(self._endpoint, **kwargs))

    async def get(self, *, table_id: int, **kwargs) -> models.CustomTable:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-custom-tables-id."""
        return models.CustomTable(**await self.api.get(f"{self._endpoint}/{table_id}", **kwargs))

    async def get_fields(self, *, table_id: int, **kwargs) -> list[models.CustomTableField]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-custom-tables-id-fields."""
        return [
            models.CustomTableField(**ctf)
            for ctf in await self.api.get(f"{self._endpoint}/{table_id}/fields", **kwargs)
        ]

    async def create_field(self, *, table_id: int, **kwargs) -> models.CustomField:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-custom-tables-id-fields."""
        return models.CustomField(**await self.api.post(f"{self._endpoint}/{table_id}/fields", **kwargs))

    async def get_employee_fields(self, *, table_id: int, employee_id: int, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-custom-tables-id-values-employee-id."""
        raise NotImplementedError("Not implemented because of lacking documentation")

    async def create_employee_fields(self, *, table_id: int, employee_id: int, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/post_v1-core-custom-tables-id-values-employee-id."""
        raise NotImplementedError("Not implemented because of lacking documentation")


class EventsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/core/events"

    async def get_triggered(self, **kwargs) -> list[models.Event]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-core-events."""
        return [models.Event(**e) for e in await self.api.get(self._endpoint, **kwargs)]


class WorkplacesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/core/workplaces"

    async def all(self, **kwargs) -> list[models.Workplace]:
        """Implement https://apidoc.factorialhr.com/reference/get_v2-core-workplaces."""
        return [models.Workplace(**w) for w in await self.api.get(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> models.Workplace:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-core-workplaces."""
        return models.Workplace(**await self.api.post(self._endpoint, **kwargs))

    async def get(self, *, workplace_id: int, **kwargs) -> models.Workplace:
        """Implement https://apidoc.factorialhr.com/reference/get_v2-core-workplaces-id."""
        return models.Workplace(**await self.api.get(f"{self._endpoint}/{workplace_id}", **kwargs))

    async def update(self, *, workplace_id: int, **kwargs) -> models.Workplace:
        """Implement https://apidoc.factorialhr.com/reference/put_v2-core-workplaces-id."""
        return models.Workplace(**await self.api.put(f"{self._endpoint}/{workplace_id}", **kwargs))

    async def delete(self, *, workplace_id: int, **kwargs) -> models.Workplace:
        """Implement https://apidoc.factorialhr.com/reference/delete_v2-core-workplaces-id."""
        return models.Workplace(**await self.api.delete(f"{self._endpoint}/{workplace_id}", **kwargs))


class AttendanceEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/time/attendance"

    async def all(
            self,
            employee_ids: list[int] | None = None,
            date_from: datetime.date | None = None,
            date_to: datetime.date | None = None,
            **kwargs,
    ) -> list[models.Attendance]:
        """Implement https://apidoc.factorialhr.com/reference/get_v2-time-attendance."""
        params: list[tuple[str, str]] = []
        if employee_ids is not None:
            params = [("employee_ids[]", str(e_id)) for e_id in employee_ids]
        if date_from is not None:
            params.append(("date_from", str(date_from)))
        if date_to is not None:
            params.append(("date_to", str(date_to)))
        return [models.Attendance(**a) for a in await self.api.get(self._endpoint, params=params, **kwargs)]

    async def create(self, **kwargs) -> models.Attendance:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-time-attendance."""
        return models.Attendance(**await self.api.post(self._endpoint, **kwargs))


class LeaveTypesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/time/leave_types"

    async def all(self, **kwargs) -> list[models.LeaveType]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-time-leave-types."""
        return [models.LeaveType(**lt) for lt in await self.api.get(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> models.LeaveType:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-time-leave-types."""
        return models.LeaveType(**await self.api.post(self._endpoint, **kwargs))

    async def update(self, *, leave_type_id: int, **kwargs) -> models.LeaveType:
        """Implement https://apidoc.factorialhr.com/reference/put_v1-time-leave-types-id."""
        return models.LeaveType(**await self.api.put(f"{self._endpoint}/{leave_type_id}", **kwargs))


class LeavesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v2/time/leaves"

    async def all(self, **kwargs) -> list[models.Leave]:
        """Implement https://apidoc.factorialhr.com/reference/get_v2-time-leaves."""
        return [models.Leave(**leave) for leave in await self.api.get(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> models.Leave:
        """Implement https://apidoc.factorialhr.com/reference/post_v2-time-leaves."""
        return models.Leave(**await self.api.post(self._endpoint, **kwargs))

    async def get(self, *, leave_id: int, **kwargs) -> models.Leave:
        """Implement https://apidoc.factorialhr.com/reference/get_v2-time-leaves-id."""
        return models.Leave(**await self.api.get(f"{self._endpoint}/{leave_id}", **kwargs))

    async def update(self, *, leave_id: int, **kwargs) -> models.Leave:
        """Implement https://apidoc.factorialhr.com/reference/put_v2-time-leaves-id."""
        return models.Leave(**await self.api.put(f"{self._endpoint}/{leave_id}", **kwargs))

    async def delete(self, *, leave_id: int, **kwargs) -> models.Leave:
        """Implement https://apidoc.factorialhr.com/reference/delete_v2-time-leaves-id."""
        return models.Leave(**await self.api.delete(f"{self._endpoint}/{leave_id}", **kwargs))


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
            **kwargs,
    ) -> list[models.JobPosting]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-ats-job-postings."""
        params: dict[str, int | models.JobPostingStatus] = {}
        if status is not None:
            params["status"] = status
        if team_id is not None:
            params["team_id"] = team_id
        if location_id is not None:
            params["location_id"] = location_id
        return [models.JobPosting(**p) for p in await self.api.get(self._endpoint, params=params, **kwargs)]

    async def create(self, **kwargs) -> models.JobPosting:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-ats-job-postings."""
        return models.JobPosting(**await self.api.post(self._endpoint, **kwargs))

    async def update(self, *, job_id: int, **kwargs) -> models.JobPosting:
        """Implement https://apidoc.factorialhr.com/reference/put_v1-ats-job-postings-id."""
        return models.JobPosting(**await self.api.put(f"{self._endpoint}/{job_id}", **kwargs))

    async def delete(self, *, job_id: int, **kwargs) -> models.JobPosting:
        """Implement https://apidoc.factorialhr.com/reference/delete_v1-ats-job-postings-id."""
        return models.JobPosting(**await self.api.delete(f"{self._endpoint}/{job_id}", **kwargs))

    async def duplicate(self, *, job_id: int, **kwargs) -> models.JobPosting:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-ats-job-postings-id-duplicate."""
        return models.JobPosting(**await self.api.post(f"{self._endpoint}/{job_id}", **kwargs))


class CandidatesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/ats/job_postings"

    async def all(self, **kwargs) -> list[models.Candidate]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-ats-candidates."""
        return [models.Candidate(**p) for p in await self.api.get(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> models.Candidate:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-ats-candidates."""
        return models.Candidate(**await self.api.post(self._endpoint, **kwargs))

    async def update(self, *, candidate_id: int, **kwargs) -> models.Candidate:
        """Implement https://apidoc.factorialhr.com/reference/put_v1-ats-candidates-id."""
        return models.Candidate(**await self.api.put(f"{self._endpoint}/{candidate_id}", **kwargs))


class ContractVersionsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError

    @property
    def _endpoint(self) -> str:
        return "v1/payroll/contract_versions"


class SupplementsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError

    @property
    def _endpoint(self) -> str:
        return "v1/payroll/supplements"


class ShiftManagementEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError

    @property
    def _endpoint(self) -> str:
        return "v1/time/shifts_management"


class BreaksEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        # TODO: oauth2 only
        raise NotImplementedError

    @property
    def _endpoint(self) -> str:
        return "v1/time/breaks"


class ApplicationEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError

    @property
    def _endpoint(self) -> str:
        return "v1/ats/applications"


class ATSMessagesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        raise NotImplementedError

    @property
    def _endpoint(self) -> str:
        return "v1/ats/messages"


class TimeOffPoliciesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/time/policies"

    async def all(self, **kwargs) -> list[models.TimeOffPolicy]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-time-policies."""
        return [models.TimeOffPolicy(**top) for top in await self.api.get(self._endpoint, **kwargs)]

    async def get(self, *, policy_id: int, **kwargs) -> models.TimeOffPolicy:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-time-policies-id."""
        return models.TimeOffPolicy(**await self.api.get(f"{self._endpoint}/{policy_id}", **kwargs))


class ExpensesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api
        # TODO: oauth2 only
        raise NotImplementedError

    @property
    def _endpoint(self) -> str:
        return "v1/finance/expenses"


class CompensationsEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/payroll/compensations"

    async def all(self, **kwargs) -> list[models.Compensation]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-payroll-compensations."""
        return [models.Compensation(**top) for top in await self.api.get(self._endpoint, **kwargs)]

    async def create(self, **kwargs) -> models.Compensation:
        """Implement https://apidoc.factorialhr.com/reference/post_v1-payroll-compensations."""
        return models.Compensation(**await self.api.post(self._endpoint, **kwargs))

    async def get(self, *, compensation_id: int, **kwargs) -> models.Compensation:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-payroll-compensations-id."""
        return models.Compensation(**await self.api.get(f"{self._endpoint}/{compensation_id}", **kwargs))

    async def update(self, *, compensation_id: int, **kwargs) -> models.Compensation:
        """Implement https://apidoc.factorialhr.com/reference/put_v1-payroll-compensations-id."""
        return models.Compensation(**await self.api.put(f"{self._endpoint}/{compensation_id}", **kwargs))

    async def delete(self, *, compensation_id: int, **kwargs) -> models.Compensation:
        """Implement https://apidoc.factorialhr.com/reference/delete_v1-payroll-compensations-id."""
        return models.Compensation(**await self.api.delete(f"{self._endpoint}/{compensation_id}", **kwargs))


class TaxonomiesEndpoint:
    def __init__(self, api: NetworkHandler):
        self.api = api

    @property
    def _endpoint(self) -> str:
        return "v1/payroll/taxonomies"

    async def all(self, **kwargs) -> list[models.Taxonomy]:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-payroll-taxonomies."""
        return [models.Taxonomy(**top) for top in await self.api.get(self._endpoint, **kwargs)]

    async def get(self, *, taxonomy_id: int, **kwargs) -> models.Taxonomy:
        """Implement https://apidoc.factorialhr.com/reference/get_v1-payroll-taxonomies-id."""
        return models.Taxonomy(**await self.api.get(f"{self._endpoint}/{taxonomy_id}", **kwargs))
