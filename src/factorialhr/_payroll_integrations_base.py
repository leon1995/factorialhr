import typing
from collections.abc import Mapping
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Integration(StrEnum):
    """Enum for payroll integration types."""

    A3INNUVA = 'a3innuva'
    A3NOM = 'a3nom'
    PAIERH = 'paierh'
    YEAP_PAIERH = 'yeap_paierh'
    SILAE = 'silae'
    SILAE_API = 'silae_api'
    DATEV = 'datev'
    DATEV_API = 'datev_api'
    DATEV_LUG_API = 'datev_lug_api'
    DATEV_LAUDS = 'datev_lauds'
    ZUCCHETTI = 'zucchetti'
    GISPAGHE = 'gispaghe'


class Payrollintegrationsbasecode(pydantic.BaseModel):
    """Model for payroll_integrations_base_code."""

    id: int = pydantic.Field(description='Code identifier')
    company_id: int = pydantic.Field(description='Company ID where the code belongs to')
    code: str = pydantic.Field(description='Code value')
    codeable_id: int = pydantic.Field(description='Related object ID. Used together with codeable_type')
    codeable_type: str = pydantic.Field(
        description=(
            'Related object type. Used together with codeable_id '
            '(Employee | Company | LegalEntity | Location | TimeoffLeaveType)'
        ),
    )
    integration: Integration = pydantic.Field(description='Integration name')


class CodesEndpoint(Endpoint):
    """Endpoint for payroll_integrations_base/codes operations."""

    endpoint = 'payroll_integrations_base/codes'

    async def all(self, **kwargs) -> ListApiResponse[Payrollintegrationsbasecode]:
        """Get all payroll integration codes records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Payrollintegrationsbasecode, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Payrollintegrationsbasecode]:
        """Get payroll integration codes with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(
            model_type=Payrollintegrationsbasecode,
            raw_meta=response['meta'],
            raw_data=response['data'],
        )

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Payrollintegrationsbasecode:
        """Create a new payroll integration code."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Payrollintegrationsbasecode).validate_python(response)

    async def update(self, code_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Payrollintegrationsbasecode:
        """Update a payroll integration code."""
        response = await self.api.put(self.endpoint, code_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Payrollintegrationsbasecode).validate_python(response)

    async def delete(self, code_id: int | str, **kwargs) -> Payrollintegrationsbasecode:
        """Delete a payroll integration code."""
        response = await self.api.delete(self.endpoint, code_id, **kwargs)
        return pydantic.TypeAdapter(Payrollintegrationsbasecode).validate_python(response)
