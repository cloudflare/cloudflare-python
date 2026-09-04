# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ServerUpdateParams", "UpdatedPrompt", "UpdatedTool"]


class ServerUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    auth_credentials: str
    """Static credential for the upstream MCP server.

    For auth_type "bearer", either a raw token string (e.g. "sk-abc123"), which is
    wrapped server-side as `Authorization: Bearer <token>`, or a JSON-encoded object
    of the form `{"headers":{"Header-Name":"value",...}}` for custom or multiple
    static headers (e.g. Cloudflare Access service tokens:
    `{"headers":{"cf-access-client-id":"...","cf-access-client-secret":"..."}}`).
    """

    client_secret: str
    """Pre-registered OAuth client_secret.

    Write-only - accepted on create/update when auth_credentials.auth_mode is
    'manual'. Stored AES-GCM-encrypted in server_oauth_secrets; never returned by
    read endpoints.
    """

    client_secret: str
    """Pre-registered OAuth client_secret.

    Write-only - accepted on create/update when auth_credentials.auth_mode is
    'manual'. Stored AES-GCM-encrypted in server_oauth_secrets; never returned by
    read endpoints.
    """

    description: Optional[str]
    """Optional description of the MCP server."""

    is_shared_oauth_callback_enabled: bool
    """
    When true, the gateway worker uses the shared Cloudflare-owned OAuth callback
    endpoint as the redirect_uri for upstream on-behalf OAuth, instead of the
    customer portal hostname. Defaults to false (off); opt in per server by setting
    true.
    """

    name: str
    """Display name for the MCP server."""

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
