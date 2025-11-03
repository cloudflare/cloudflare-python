# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PortalUpdateParams", "Server", "ServerUpdatedPrompt", "ServerUpdatedTool"]


class PortalUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    description: str

    hostname: str

    name: str

    servers: Iterable[Server]


class ServerUpdatedPrompt(TypedDict, total=False):
    name: Required[str]

    description: str

    enabled: bool


class ServerUpdatedTool(TypedDict, total=False):
    name: Required[str]

    description: str

    enabled: bool


class Server(TypedDict, total=False):
    server_id: Required[str]
    """server id"""

    default_disabled: bool

    on_behalf: bool

    updated_prompts: Iterable[ServerUpdatedPrompt]

    updated_tools: Iterable[ServerUpdatedTool]
