# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ServerUpdateParams", "UpdatedPrompt", "UpdatedTool"]


class ServerUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    auth_credentials: str

    client_secret: str
    """Pre-registered OAuth client_secret.

    Write-only - accepted on create/update when auth_credentials.auth_mode is
    'manual'. Stored AES-GCM-encrypted in server_oauth_secrets; never returned by
    read endpoints.
    """

    description: Optional[str]

    is_shared_oauth_callback_enabled: bool
    """
    When true, the gateway worker uses the shared Cloudflare-owned OAuth callback
    endpoint as the redirect_uri for upstream on-behalf OAuth, instead of the
    customer portal hostname. Defaults to false (off); opt in per server by setting
    true. Effective behavior is gated by the gateway worker's per-env rollout mode
    KV key.
    """

    name: str

    secure_web_gateway: bool
    """Route outbound traffic to this MCP server through Zero Trust Secure Web Gateway"""

    updated_prompts: Iterable[UpdatedPrompt]

    updated_tools: Iterable[UpdatedTool]


class UpdatedPrompt(TypedDict, total=False):
    name: Required[str]

    alias: str

    description: str

    enabled: bool


class UpdatedTool(TypedDict, total=False):
    name: Required[str]

    alias: str

    description: str

    enabled: bool
