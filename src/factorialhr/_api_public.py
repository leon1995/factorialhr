import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Credentials(pydantic.BaseModel):
    """Model for api_public_credential."""

    company_id: int = pydantic.Field(description='Company id for all kind of accesses')
    id: str = pydantic.Field(description='Id of the credential prefixed by the type of credential')
    email: str | None = pydantic.Field(default=None, description='Only for Access Oauth token')
    login_email: str | None = pydantic.Field(default=None, description='Only for Access Oauth token')
    full_name: str | None = pydantic.Field(default=None, description='Full name of the user')
    first_name: str | None = pydantic.Field(default=None, description='Only for Access Oauth token')
    last_name: str | None = pydantic.Field(default=None, description='Only for Access Oauth token')
    employee_id: int | None = pydantic.Field(
        default=None,
        description='Id for the employee related. Only for Access Oauth token',
    )
    role: str | None = pydantic.Field(
        default=None,
        description='Employee role in the Company. Only for Access Oauth token',
    )
    gdpr_tos: bool | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    legal_name: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    locale: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    logo: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    name: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    onboarded_on: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    subscription_plan: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    tin: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    to_be_deleted: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    tos: bool | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')


class CredentialsEndpoint(Endpoint):
    endpoint = '/api_public/credentials'

    async def all(self, **kwargs) -> ListApiResponse[Credentials]:
        """Get all credentials."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Credentials, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Credentials]:
        """Get credentials with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Credentials, raw_meta=response['meta'], raw_data=response['data'])


class WebhookSubscription(pydantic.BaseModel):
    """Model for api_public_webhook_subscription."""

    id: int = pydantic.Field(description='Identifier of the webhook subscription')
    target_url: str = pydantic.Field(description='URL where the webhook payload will be sent')
    type: str = pydantic.Field(description='Type of the webhook subscription')
    company_id: int | None = pydantic.Field(default=None, description='Company identifier of the webhook subscription')
    name: str | None = pydantic.Field(default=None, description='Name of the webhook subscription')
    challenge: str | None = pydantic.Field(default=None, description='String to verify the subscription')
    enabled: bool = pydantic.Field(description='Boolean to enable/disable the subscription')
    api_version: str = pydantic.Field(
        description='API version of the webhook subscription that determines the schema of the payload',
    )


class WebhookSubscriptionEndpoint(Endpoint):
    endpoint = '/api_public/webhook_subscriptions'

    async def all(self, **kwargs) -> ListApiResponse[WebhookSubscription]:
        """Get all webhooks."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=WebhookSubscription, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[WebhookSubscription]:
        """Get webhooks with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=WebhookSubscription, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, webhook_subscription_id: int | str, **kwargs) -> WebhookSubscription:
        """Get a specific webhook by ID."""
        data = await self.api.get(self.endpoint, webhook_subscription_id, **kwargs)
        return pydantic.TypeAdapter(WebhookSubscription).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> WebhookSubscription:
        """Create a new webhook subscription."""
        data = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(WebhookSubscription).validate_python(data)

    async def update(
        self,
        webhook_subscription_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> WebhookSubscription:
        """Update an existing webhook subscription."""
        data = await self.api.put(
            self.endpoint,
            webhook_subscription_id,
            json=data,
            **kwargs,
        )
        return pydantic.TypeAdapter(WebhookSubscription).validate_python(data)

    async def delete(self, webhook_subscription_id: int | str, **kwargs) -> WebhookSubscription:
        """Delete a webhook subscription."""
        data = await self.api.delete(self.endpoint, webhook_subscription_id, **kwargs)
        return pydantic.TypeAdapter(WebhookSubscription).validate_python(data)
