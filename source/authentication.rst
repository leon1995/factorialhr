Authentication
==============

Read the official documentation for more information about authentication: https://apidoc.factorialhr.com/docs/authentication

The Factorial API client supports four authentication methods, each suited for different use cases:

:class:`factorialhr.ApiKeyAuth`
   Simple API key authentication using the ``x-api-key`` header. Best for server-to-server integrations and automated scripts.

   **Advantages:**

   * Simple to use - just provide your API key

   * No token expiration to manage

   * Suitable for long-running processes and background jobs

   **Disadvantages:**

   * Less secure than OAuth tokens (keys don't expire automatically)

   * Requires manual key rotation for security

   * Not suitable for user-facing applications

   **When to use:** Server-side integrations, CI/CD pipelines, scheduled scripts, or when you need a persistent authentication method without token management.

:class:`factorialhr.AccessTokenAuth`
   OAuth access token authentication. The token is used as-is without automatic refresh.

   **Advantages:**

   * Simple OAuth integration

   * Full control over token lifecycle

   * Suitable for short-lived scripts or when you handle token refresh externally

   **Disadvantages:**

   * Access tokens expire after 1 hour - you must manually refresh them

   * Requires implementing your own token refresh logic

   * Not ideal for long-running applications

   **When to use:** Short-lived scripts, one-off operations, or when you're managing token refresh through another system (e.g., a token management service).

:class:`factorialhr.RefreshTokenAuth`
   OAuth authentication with automatic access token refresh. Automatically refreshes expired access tokens using the refresh token.

   **Advantages:**

   * Access tokens are refreshed seamlessly when expired (after 1 hour)

   * Automatic token refresh - no manual intervention needed

   * Refresh tokens last 1 week, providing longer-term access

   * Ideal for applications that run continuously

   **Disadvantages:**

   * Requires storing refresh token, client ID, and client secret securely

   * More complex initialization (needs multiple parameters)

   * Refresh tokens expire after 1 week - you'll need to re-authenticate

   **When to use:** Long-running applications, services, or daemons that need continuous API access without manual token management.

:class:`factorialhr.RefreshTokenAuthFile`
   Extends :class:`factorialhr.RefreshTokenAuth` with automatic persistence to a JSON file. Automatically saves refreshed tokens to disk and can load session data from a file.

   **Advantages:**

   * All advantages of :class:`factorialhr.RefreshTokenAuth`

   * Automatic session persistence - tokens are saved to disk after refresh

   * Can resume sessions after application restart using ``from_file()``

   * Convenient for applications that need to survive restarts

   **Disadvantages:**

   * Requires file system access and proper file permissions

   * Security consideration: tokens stored in plain JSON file (ensure proper file permissions)

   * File-based approach may not scale for multi-instance deployments

   **When to use:** Desktop applications, local scripts, or single-instance services that benefit from session persistence across restarts.

**Choosing the right authentication method:**

* **API Key** → Server integrations, automation, CI/CD
* **Access Token** → Short scripts, external token management
* **Refresh Token** → Long-running services, automated token refresh needed
* **Refresh Token File** → Applications needing session persistence, single-instance deployments

.. autoclass:: factorialhr.AccessTokenAuth
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.ApiKeyAuth
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.RefreshTokenAuth
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.RefreshTokenAuthFile
   :members:
   :exclude-members: model_config

Response models
~~~~~~~~~~~~~~~

.. autoclass:: factorialhr.ListApiResponse
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.MetaApiResponse
   :members:
   :exclude-members: model_config

.. autoclass:: factorialhr.PaginationMeta
   :members:
   :exclude-members: model_config

Api client
~~~~~~~~~~

.. autoclass:: factorialhr.ApiClient
   :members: