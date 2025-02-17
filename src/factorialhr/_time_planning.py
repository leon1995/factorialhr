import datetime
import typing

import pydantic

from factorialhr import _common
from factorialhr._client import Endpoint


class PlanningVersion(pydantic.BaseModel):
    id: int | None
    effective_at: datetime.date
    planning_tool: str
    number_of_rest_days_in_cents: int | None
    employee_id: int
    work_schedule_schedule_id: int | None


class _PlanningVersionRoot(pydantic.RootModel):
    root: list[PlanningVersion]


class PlanningVersionEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/time_planning/planning_versions'

    async def all(
        self,
        *,
        employee_ids: typing.Sequence[int] | None = None,
        for_shifts: bool | None = None,
        only_active: bool | None = None,
        planning_tool: str | None = None,
        schedule_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> list[PlanningVersion]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-time-planning-planning-versions."""
        params = kwargs.get('params', {})
        params.update(
            {
                'employee_ids[]': employee_ids,
                'for_shifts': for_shifts,
                'only_active': only_active,
                'planning_tool': planning_tool,
                'schedule_ids[]': schedule_ids,
            },
        )
        return _PlanningVersionRoot.model_validate(
            await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs),
        ).root

    async def get(
        self,
        *,
        employee_ids: typing.Sequence[int] | None = None,
        for_shifts: bool | None = None,
        only_active: bool | None = None,
        planning_tool: str | None = None,
        schedule_ids: typing.Sequence[int] | None = None,
        **kwargs,
    ) -> tuple[list[PlanningVersion], _common.Meta]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-time-planning-planning-versions."""
        params = kwargs.get('params', {})
        params.update(
            {
                'employee_ids[]': employee_ids,
                'for_shifts': for_shifts,
                'only_active': only_active,
                'planning_tool': planning_tool,
                'schedule_ids[]': schedule_ids,
            },
        )
        result = await self.api.get(self.endpoint, params=_common.build_params(**params), **kwargs)
        return _PlanningVersionRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])
