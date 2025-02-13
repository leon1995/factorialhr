from factorialhr.endpoints import _base


class Employee(_base.Endpoint):
    endpoint = '/2025-01-01/resources/employees/employees'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-employees-employees."""
        return await self.api.get(self.endpoint, **kwargs)

    async def create_with_contracts(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-employees-employees-create-with-contract."""
        return await self.api.post(self.endpoint, **kwargs)

    async def update(self, *, employee_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-employees-employees-id."""
        return await self.api.put(f'{self.endpoint}/{employee_id}', **kwargs)

    async def single(self, *, employee_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-employees-employees-id."""
        return await self.api.get(f'{self.endpoint}/{employee_id}', **kwargs)

    async def invite(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-employees-employees-invite."""
        return await self.api.post(self.endpoint, **kwargs)

    async def terminate(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-employees-employees-terminate."""
        return await self.api.post(self.endpoint, **kwargs)

    async def unterminate(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-employees-employees-unterminate."""
        return await self.api.post(self.endpoint, **kwargs)
