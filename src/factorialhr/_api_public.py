import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Credentials(pydantic.BaseModel):
    """Model for api_public_credential."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Company id for all kind of accesses.
    company_id: int = pydantic.Field(description='Company id for all kind of accesses')
    #: Id of the credential prefixed by the type of credential.
    id: str = pydantic.Field(description='Id of the credential prefixed by the type of credential')
    #: Only for Access Oauth token.
    email: str | None = pydantic.Field(default=None, description='Only for Access Oauth token')
    #: Only for Access Oauth token.
    login_email: str | None = pydantic.Field(default=None, description='Only for Access Oauth token')
    #: Full name of the user.
    full_name: str | None = pydantic.Field(default=None, description='Full name of the user')
    #: Only for Access Oauth token.
    first_name: str | None = pydantic.Field(default=None, description='Only for Access Oauth token')
    #: Only for Access Oauth token.
    last_name: str | None = pydantic.Field(default=None, description='Only for Access Oauth token')
    #: Id for the employee related. Only for Access Oauth token.
    employee_id: int | None = pydantic.Field(
        default=None,
        description='Id for the employee related. Only for Access Oauth token',
    )
    #: Employee role in the Company. Only for Access Oauth token.
    role: str | None = pydantic.Field(
        default=None,
        description='Employee role in the Company. Only for Access Oauth token',
    )
    #: Only for Company Oauth or API key.
    gdpr_tos: bool | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    #: Only for Company Oauth or API key.
    legal_name: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    #: Only for Company Oauth or API key.
    locale: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    #: Only for Company Oauth or API key.
    logo: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    #: Only for Company Oauth or API key.
    name: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    #: Only for Company Oauth or API key.
    onboarded_on: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    #: Only for Company Oauth or API key.
    subscription_plan: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    #: Only for Company Oauth or API key.
    tin: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    #: Only for Company Oauth or API key.
    to_be_deleted: str | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')
    #: Only for Company Oauth or API key.
    tos: bool | None = pydantic.Field(default=None, description='Only for Company Oauth or API key')


class CredentialsEndpoint(Endpoint):
    endpoint = 'api_public/credentials'

    async def all(self, **kwargs) -> ListApiResponse[Credentials]:
        """Get all credentials.

        Official documentation: `api_public/credentials <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-api-public-credentials>`_

        :return: List of credentials
        :rtype: ListApiResponse[Credentials]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Credentials]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Credentials, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Credentials]:
        """Get credentials with pagination metadata.

        Official documentation: `api_public/credentials <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-api-public-credentials>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Credentials]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Credentials, raw_meta=response['meta'], raw_data=response['data'])


class WebhookSubscription(pydantic.BaseModel):
    """Model for api_public_webhook_subscription."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the webhook subscription.
    id: int = pydantic.Field(description='Identifier of the webhook subscription')
    #: URL where the webhook payload will be sent.
    target_url: str = pydantic.Field(description='URL where the webhook payload will be sent')
    #: Type of the webhook subscription.
    type: str = pydantic.Field(description='Type of the webhook subscription')
    #: Company identifier of the webhook subscription.
    company_id: int | None = pydantic.Field(default=None, description='Company identifier of the webhook subscription')
    #: Name of the webhook subscription.
    name: str | None = pydantic.Field(default=None, description='Name of the webhook subscription')
    #: String to verify the subscription.
    challenge: str | None = pydantic.Field(default=None, description='String to verify the subscription')
    #: Boolean to enable/disable the subscription.
    enabled: bool = pydantic.Field(description='Boolean to enable/disable the subscription')
    #: API version of the webhook subscription that determines the schema of the payload.
    api_version: str = pydantic.Field(
        description='API version of the webhook subscription that determines the schema of the payload',
    )


class WebhookSubscriptionEndpoint(Endpoint):
    endpoint = 'api_public/webhook_subscriptions'

    async def all(self, **kwargs) -> ListApiResponse[WebhookSubscription]:
        """Get all webhooks.

        Official documentation: `api_public/webhook_subscriptions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-api-public-webhook-subscriptions>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[WebhookSubscription]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=WebhookSubscription, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[WebhookSubscription]:
        """Get webhooks with pagination metadata.

        Official documentation: `api_public/webhook_subscriptions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-api-public-webhook-subscriptions>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[WebhookSubscription]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=WebhookSubscription, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, webhook_subscription_id: int | str, **kwargs) -> WebhookSubscription:
        """Get a specific webhook by ID.

        Official documentation: `api_public/webhook_subscriptions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-api-public-webhook-subscriptions>`_

        :param webhook_subscription_id: The unique identifier.
        :type webhook_subscription_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: WebhookSubscription
        """
        data = await self.api.get(self.endpoint, webhook_subscription_id, **kwargs)
        return pydantic.TypeAdapter(WebhookSubscription).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> WebhookSubscription:
        """Create a new webhook subscription.

        Official documentation: `api_public/webhook_subscriptions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-api-public-webhook-subscriptions>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: WebhookSubscription
        """
        data = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(WebhookSubscription).validate_python(data)

    async def update(
        self,
        webhook_subscription_id: int | str,
        data: Mapping[str, typing.Any],
        **kwargs,
    ) -> WebhookSubscription:
        """Update an existing webhook subscription.

        Official documentation: `api_public/webhook_subscriptions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-api-public-webhook-subscriptions>`_

        :param webhook_subscription_id: The unique identifier of the record to update.
        :type webhook_subscription_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: WebhookSubscription
        """
        data = await self.api.put(
            self.endpoint,
            webhook_subscription_id,
            json=data,
            **kwargs,
        )
        return pydantic.TypeAdapter(WebhookSubscription).validate_python(data)

    async def delete(self, webhook_subscription_id: int | str, **kwargs) -> WebhookSubscription:
        """Delete a webhook subscription.

        Official documentation: `api_public/webhook_subscriptions <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-api-public-webhook-subscriptions>`_

        :param webhook_subscription_id: The unique identifier of the record to delete.
        :type webhook_subscription_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: WebhookSubscription
        """
        data = await self.api.delete(self.endpoint, webhook_subscription_id, **kwargs)
        return pydantic.TypeAdapter(WebhookSubscription).validate_python(data)
