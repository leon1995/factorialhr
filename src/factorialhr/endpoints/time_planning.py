from factorialhr.endpoints import _base


class PlanningVersion(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/time_planning/planning_versions'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-time-planning-planning-versions."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-time-planning-planning-versions."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete(self, *, planning_version_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-time-planning-planning-versions-id."""
        return await self.api.delete(f'{self._endpoint}/{planning_version_id}', **kwargs)

    async def update(self, *, planning_version_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-time-planning-planning-versions-id."""
        return await self.api.put(f'{self._endpoint}/{planning_version_id}', **kwargs)

    async def bulk_create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-time-planning-planning-versions-bulk-create."""
        return await self.api.post(f'{self._endpoint}/bulk_create', **kwargs)
