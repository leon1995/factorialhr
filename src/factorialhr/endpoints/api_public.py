from factorialhr.endpoints import _base


class Credentials(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/api_public/credentials'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-api-public-credentials."""
        return await self.api.get(self._endpoint, **kwargs)


class WebhookSubscription(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/api_public/webhook_subscriptions'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-api-public-webhook-subscriptions."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-api-public-webhook-subscriptions."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete(self, *, webhook_subscription_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-api-public-webhook-subscriptions-id."""
        return await self.api.delete(f'{self._endpoint}/{webhook_subscription_id}', **kwargs)

    async def update(self, *, webhook_subscription_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-api-public-webhook-subscriptions-id."""
        return await self.api.put(f'{self._endpoint}/{webhook_subscription_id}', **kwargs)

    async def single(self, *, webhook_subscription_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-api-public-webhook-subscriptions-id."""
        return await self.api.get(f'{self._endpoint}/{webhook_subscription_id}', **kwargs)
