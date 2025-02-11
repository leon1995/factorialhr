from factorialhr.endpoints import _base


class Membership(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/teams/memberships'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-teams-memberships."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-teams-memberships."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete(self, *, membership_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-teams-memberships-id."""
        return await self.api.delete(f'{self._endpoint}/{membership_id}', **kwargs)

    async def update(self, *, membership_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-teams-memberships-id."""
        return await self.api.put(f'{self._endpoint}/{membership_id}', **kwargs)

    async def single(self, *, membership_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-teams-memberships-id."""
        return await self.api.get(f'{self._endpoint}/{membership_id}', **kwargs)


class Team(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/teams/teams'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-teams-teams."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-teams-teams."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete(self, *, team_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-teams-teams-id."""
        return await self.api.delete(f'{self._endpoint}/{team_id}', **kwargs)

    async def update(self, *, team_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-teams-teams-id."""
        return await self.api.put(f'{self._endpoint}/{team_id}', **kwargs)

    async def single(self, *, team_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-teams-teams-id."""
        return await self.api.get(f'{self._endpoint}/{team_id}', **kwargs)
