# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ServerUpdateParams", "UpdatedPrompt", "UpdatedTool"]


class ServerUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    auth_credentials: str

    description: Optional[str]

    is_shared_oauth_callback_enabled: bool
    """
    When true, the gateway worker uses the shared Cloudflare-owned OAuth callback
    endpoint as the redirect_uri for upstream on-behalf OAuth, instead of the
    customer portal hostname. New public server creates default to true; existing
    servers default to false from migration until explicitly updated. Effective
    behavior is gated by the gateway worker's per-env rollout mode KV key.
    """

    name: str

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
