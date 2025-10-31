from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class ConceptCategory(StrEnum):
    """Enum for concept categories."""

    EARNINGS_FIXED_SALARY = 'earnings_fixed_salary'
    EARNINGS_VARIABLE = 'earnings_variable'
    EARNINGS_BENEFITS_IN_KIND = 'earnings_benefits_in_kind'
    EARNINGS_OTHERS = 'earnings_others'
    DEDUCTIONS = 'deductions'
    COMPANY_CONTRIBUTION = 'company_contribution'
    SUMMARIZED_VALUES = 'summarized_values'


class UnitType(StrEnum):
    """Enum for unit types."""

    DISTANCE = 'distance'
    MONEY = 'money'
    TIME = 'time'
    UNIT = 'unit'


class Concept(pydantic.BaseModel):
    """Model for compensations_concept."""

    model_config = pydantic.ConfigDict(frozen=True)

    id: int = pydantic.Field(description='The identifier of the concept')
    company_id: int = pydantic.Field(description='The company identifier of the concept')
    default: bool = pydantic.Field(description='Whether the concept is a default or a custom concept')
    description: str = pydantic.Field(description='The description of the concept')
    label: str = pydantic.Field(description='The label of the concept')
    name: str = pydantic.Field(description='The name of the concept')
    category: ConceptCategory | None = pydantic.Field(default=None, description='The category of the concept')
    translated_name: str | None = pydantic.Field(
        default=None,
        description='The translated name of the concept if it is a default concept',
    )
    unit_name: str | None = pydantic.Field(default=None, description='The name of the unit of the concept')
    unit_type: UnitType | None = pydantic.Field(default=None, description='The type of the unit of the concept')


class ConceptsEndpoint(Endpoint):
    """Endpoint for compensations/concepts operations."""

    endpoint = 'compensations/concepts'

    async def all(self, **kwargs) -> ListApiResponse[Concept]:
        """Get all concepts records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Concept, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Concept]:
        """Get concepts with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Concept, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, concept_id: int | str, **kwargs) -> Concept:
        """Get a specific concept by ID."""
        data = await self.api.get(self.endpoint, concept_id, **kwargs)
        return pydantic.TypeAdapter(Concept).validate_python(data)
