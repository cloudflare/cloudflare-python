# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ServerUpdateParams", "UpdatedPrompt", "UpdatedTool"]


class ServerUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    auth_credentials: str

    description: Optional[str]

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
