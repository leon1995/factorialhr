import typing

import pydantic

from factorialhr import _common
from factorialhr._client import Endpoint


class Credentials(pydantic.BaseModel):
    company_id: int
    id: str
    email: str | None
    login_email: str | None
    full_name: str | None
    first_name: str | None
    last_name: str | None
    employee_id: int | None  # can be None if request is made using an api key
    role: str | None
    gdpr_tos: bool | None
    legal_name: str | None
    locale: str | None
    logo: str | None
    name: str | None
    onboarded_on: str | None
    subscription_plan: str | None
    tin: str | None
    to_be_deleted: str | None
    tos: bool | None


class _CredentialsRoot(pydantic.RootModel):
    root: list[Credentials]


class CredentialsEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/api_public/credentials'

    async def all(self, **kwargs) -> list[Credentials]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-api-public-credentials."""
        return _CredentialsRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    async def get(self, **kwargs) -> tuple[list[Credentials], _common.Meta]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-api-public-credentials."""
        result = await self.api.get(self.endpoint, **kwargs)
        return _CredentialsRoot.model_validate(result['data']).root, _common.Meta.model_validate(result['meta'])


class WebhookSubscription(pydantic.BaseModel):
    id: int
    target_url: str
    type: str
    company_id: int | None
    name: str | None
    challenge: str | None
    enabled: bool
    api_version: str


class _WebhookSubscriptionRoot(pydantic.RootModel):
    root: list[WebhookSubscription]


class WebhookSubscriptionEndpoint(Endpoint):
    endpoint = '/2025-01-01/resources/api_public/webhook_subscriptions'

    async def all(self, **kwargs) -> list[WebhookSubscription]:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-api-public-webhook-subscriptions."""
        return _WebhookSubscriptionRoot.model_validate(await self.api.get_all(self.endpoint, **kwargs)).root

    @typing.overload
    async def get(self, *, webhook_subscription_id: int, **kwargs) -> WebhookSubscription: ...

    @typing.overload
    async def get(self, **kwargs) -> tuple[list[WebhookSubscription], _common.Meta]: ...

    async def get(self, *, webhook_subscription_id: int | None = None, **kwargs):
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-api-public-webhook-subscriptions-id."""
        result = await self.api.get(self.endpoint, webhook_subscription_id, **kwargs)
        return (
            WebhookSubscription.model_validate(result)
            if webhook_subscription_id is not None
            else (
                _WebhookSubscriptionRoot.model_validate(result['data']).root,
                _common.Meta.model_validate(result['meta']),
            )
        )
