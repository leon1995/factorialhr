import datetime
import enum
import typing

import pydantic

from factorialhr import _common
from factorialhr._client import Endpoint


class EmployeeBankNumberFormat(enum.StrEnum):
    iban = 'iban'
    sort_code_and_account_number = 'sort_code_and_account_number'
    routing_number_and_account_number = 'routing_number_and_account_number'
    clabe = 'clabe'
    other = 'other'
    bank_name_and_account_number = 'bank_name_and_account_number'


class Employee(pydantic.BaseModel):
    id: int
    access_id: int
    first_name: str
    last_name: str
    full_name: str
    preferred_name: str | None
    birth_name: str | None
    gender: str | None
    identifier: str | None
    identifier_type: str | None
    email: str | None
    login_email: str | None
    birthday_on: datetime.date | None
    nationality: str | None
    address_line_1: str | None
    address_line_2: str | None
    postal_code: str | None  #  should be int but api returns string
    city: str | None
    state: str | None
    country: str | None
    bank_number: str | None
    swift_bic: str | None
    bank_number_format: str | None
    company_id: int
    legal_entity_id: int | None
    location_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    social_security_number: int | None
    is_terminating: bool
    terminated_on: datetime.date | None
    termination_reason: str | None
    termination_observations: str | None
    manager_id: int | None
    timeoff_manager_id: int | None
    phone_number: str | None  # should be int but api returns string
    company_identifier: str | None
    age_number: int | None
    contact_name: str | None
    contact_number: str | None  # should be int but api returns string
    personal_email: str | None
    pronouns: str | None
    active: bool | None
    disability_percentage_cents: int | None
    identifier_expiration_date: str | None


class _EmployeeRoot(pydantic.RootModel):
    root: list[Employee]


class EmployeeEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/employees/employees'

    async def all(  # noqa: PLR0913
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        access_ids: typing.Sequence[int] | None = None,
        emails: typing.Sequence[str] | None = None,
        full_text_name: str | None = None,
        legal_entity_ids: typing.Sequence[int] | None = None,
        only_active: bool | None = None,
        team_ids: typing.Sequence[int] | None = None,
        location_ids: typing.Sequence[int] | None = None,
        only_managers: bool | None = None,
        name_starts_with: str | None = None,
        **kwargs,
    ) -> list[Employee]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-employees-employees."""
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'access_ids[]': access_ids,
                'emails[]': emails,
                'full_text_name': full_text_name,
                'legal_entity_ids[]': legal_entity_ids,
                'only_active': only_active,
                'team_ids[]': team_ids,
                'location_ids[]': location_ids,
                'only_managers': only_managers,
                'name_starts_with': name_starts_with,
            },
        )
        return _EmployeeRoot.model_validate(
            await self.api.get_all(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    @typing.overload
    async def get(self, *, employee_id: int, **kwargs) -> Employee: ...
    @typing.overload
    async def get(
        self,
        *,
        ids: typing.Sequence[int] | None = None,
        access_ids: typing.Sequence[int] | None = None,
        emails: typing.Sequence[str] | None = None,
        full_text_name: str | None = None,
        legal_entity_ids: typing.Sequence[int] | None = None,
        only_active: bool | None = None,
        team_ids: typing.Sequence[int] | None = None,
        location_ids: typing.Sequence[int] | None = None,
        only_managers: bool | None = None,
        name_starts_with: str | None = None,
        **kwargs,
    ) -> tuple[list[Employee], _common.Meta]: ...

    async def get(  # noqa: PLR0913
        self,
        *,
        employee_id: int | None = None,
        ids: typing.Sequence[int] | None = None,
        access_ids: typing.Sequence[int] | None = None,
        emails: typing.Sequence[str] | None = None,
        full_text_name: str | None = None,
        legal_entity_ids: typing.Sequence[int] | None = None,
        only_active: bool | None = None,
        team_ids: typing.Sequence[int] | None = None,
        location_ids: typing.Sequence[int] | None = None,
        only_managers: bool | None = None,
        name_starts_with: str | None = None,
        **kwargs,
    ):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-employees-employees-id."""
        if employee_id is not None:
            return Employee.model_validate(await self.api.get(self.endpoint, employee_id, **kwargs))
        params = kwargs.get('params', {})
        params.update(
            {
                'ids[]': ids,
                'access_ids[]': access_ids,
                'emails[]': emails,
                'full_text_name': full_text_name,
                'legal_entity_ids[]': legal_entity_ids,
                'only_active': only_active,
                'team_ids[]': team_ids,
                'location_ids[]': location_ids,
                'only_managers': only_managers,
                'name_starts_with': name_starts_with,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _EmployeeRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])
