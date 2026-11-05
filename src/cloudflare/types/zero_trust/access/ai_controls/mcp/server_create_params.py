# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ServerCreateParams", "UpdatedPrompt", "UpdatedTool"]


class ServerCreateParams(TypedDict, total=False):
    account_id: Required[str]

    id: Required[str]
    """Unique identifier for the MCP server."""

    auth_type: Required[Literal["oauth", "bearer", "unauthenticated"]]
    """Authentication method used to connect to the upstream MCP server."""

    hostname: Required[str]
    """URL of the upstream MCP endpoint."""

    name: Required[str]
    """Display name for the MCP server."""

    auth_credentials: str
    """Credential configuration for the upstream MCP server.

    For auth_type "bearer", either a raw token string (e.g. "sk-abc123"), which is
    wrapped server-side as `Authorization: Bearer <token>`, or a JSON-encoded object
    of the form `{"headers":{"Header-Name":"value",...}}` for custom or multiple
    static headers (e.g. Cloudflare Access service tokens:
    `{"headers":{"cf-access-client-id":"...","cf-access-client-secret":"..."}}`).
    For auth_type "oauth" with a pre-registered client, send a JSON-encoded object
    containing `auth_mode:"manual"`, `config.authorization_endpoint`,
    `config.token_endpoint`, and `registration_info.client_id`. Also provide
    `registration_info.redirect_uris` unless `is_shared_oauth_callback_enabled` is
    true. Optional fields include `config.issuer`, `config.revocation_endpoint`,
    `registration_info.scope`, and `registration_info.token_endpoint_auth_method`.
    Send the client secret in the separate `client_secret` field. Omit
    `auth_credentials` on update to preserve the existing configuration.
    """

    client_secret: str
    """Provides 'client_secret' for a pre-registered OAuth client.

    This field is accepted on create or update only when
    'auth_credentials.auth_mode' is 'manual'. It is required when creating an MCP
    server with manual OAuth credentials or changing an existing server to use
    manual OAuth credentials. Omit 'client_secret' on update to preserve the
    existing secret. Provide a new 'client_secret' to rotate the secret. The secret
    is never returned by read, create, or update requests.
    """

    description: Optional[str]
    """Optional description of the MCP server."""

    is_shared_oauth_callback_enabled: bool
    """
    When true, per-user authorization uses the shared Cloudflare callback URL as the
    'redirect_uri' instead of the portal callback URL. The default is false. Set
    'is_shared_oauth_callback_enabled' to true to enable the shared Cloudflare
    callback URL for this MCP server.
    """

    secure_web_gateway: bool
    """
    Route outbound traffic to this MCP server through Zero Trust Secure Web Gateway.
    """

    updated_prompts: Iterable[UpdatedPrompt]
    """Server-wide prompt capability overrides."""

    updated_tools: Iterable[UpdatedTool]
    """Server-wide tool capability overrides."""


class UpdatedPrompt(TypedDict, total=False):
    name: Required[str]
    """Name of the tool or prompt capability to override."""

    alias: str
    """Custom name exposed for the capability."""

    description: str
    """Custom description exposed for the capability."""

    enabled: bool
    """Whether the capability is available through the MCP server."""


class UpdatedTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool or prompt capability to override."""

    alias: str
    """Custom name exposed for the capability."""

    description: str
    """Custom description exposed for the capability."""

    enabled: bool
    """Whether the capability is available through the MCP server."""
