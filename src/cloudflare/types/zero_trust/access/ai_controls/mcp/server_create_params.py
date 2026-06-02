# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ServerCreateParams", "UpdatedPrompt", "UpdatedTool"]


class ServerCreateParams(TypedDict, total=False):
    account_id: Required[str]

    id: Required[str]
    """server id"""

    auth_type: Required[Literal["oauth", "bearer", "unauthenticated"]]

    hostname: Required[str]

    name: Required[str]

    auth_credentials: str

    description: Optional[str]

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
