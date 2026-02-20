import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class CountryCode(StrEnum):
    """Enum for payroll employee country codes."""

    PORTUGAL = 'pt'
    GERMANY = 'de'
    ITALY = 'it'


class Payrollemployeesidentifier(pydantic.BaseModel):
    """Model for payroll_employees_identifier."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Payroll employee identifier
    id: int = pydantic.Field(description='Payroll employee identifier')
    #: Identifier of the employee
    employee_id: int = pydantic.Field(description='Identifier of the employee')
    #: Social security number of the employee
    social_security_number: str | None = pydantic.Field(
        default=None,
        description='Social security number of the employee',
    )
    #: Tax id of the employee
    tax_id: str | None = pydantic.Field(default=None, description='Tax id of the employee')
    #: Country code of the employee (pt | it | de)
    country: CountryCode = pydantic.Field(description='Country code of the employee (pt | it | de)')


class IdentifiersEndpoint(Endpoint):
    """Endpoint for payroll_employees/identifiers operations."""

    endpoint = 'payroll_employees/identifiers'

    async def all(self, **kwargs) -> ListApiResponse[Payrollemployeesidentifier]:
        """Get all payroll employee identifiers records.

        Official documentation: `payroll_employees/identifiers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-payroll-employees-identifiers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Payrollemployeesidentifier]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Payrollemployeesidentifier, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Payrollemployeesidentifier]:
        """Get payroll employee identifiers with pagination metadata.

        Official documentation: `payroll_employees/identifiers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-payroll-employees-identifiers>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Payrollemployeesidentifier]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=Payrollemployeesidentifier,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def get_by_id(self, identifier_id: int | str, **kwargs) -> Payrollemployeesidentifier:
        """Get a specific payroll employee identifier by ID.

        Official documentation: `payroll_employees/identifiers <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-payroll-employees-identifiers-id>`_

        :param identifier_id: The unique identifier.
        :type identifier_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Payrollemployeesidentifier
        """
        data = await self.api.get(self.endpoint, identifier_id, **kwargs)
        return pydantic.TypeAdapter(Payrollemployeesidentifier).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Payrollemployeesidentifier:
        """Create a new payroll employee identifier.

        Official documentation: `payroll_employees/identifiers <https://apidoc.factorialhr.com/reference/post_api-2026-01-01-resources-payroll-employees-identifiers>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Payrollemployeesidentifier
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Payrollemployeesidentifier).validate_python(response)

    async def update(
        self,
        identifier_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> Payrollemployeesidentifier:
        """Update a payroll employee identifier.

        Official documentation: `payroll_employees/identifiers <https://apidoc.factorialhr.com/reference/put_api-2026-01-01-resources-payroll-employees-identifiers-id>`_

        :param identifier_id: The unique identifier of the record to update.
        :type identifier_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Payrollemployeesidentifier
        """
        response = await self.api.put(self.endpoint, identifier_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Payrollemployeesidentifier).validate_python(response)

    async def delete(self, identifier_id: int | str, **kwargs) -> Payrollemployeesidentifier:
        """Delete a payroll employee identifier.

        Official documentation: `payroll_employees/identifiers <https://apidoc.factorialhr.com/reference/delete_api-2026-01-01-resources-payroll-employees-identifiers-id>`_

        :param identifier_id: The unique identifier of the record to delete.
        :type identifier_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: Payrollemployeesidentifier
        """
        response = await self.api.delete(self.endpoint, identifier_id, **kwargs)
        return pydantic.TypeAdapter(Payrollemployeesidentifier).validate_python(response)
