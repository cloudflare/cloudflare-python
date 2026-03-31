# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..rules.lists.list_cursor_param import ListCursorParam

__all__ = ["EnvironmentEditParams", "Environment"]


class EnvironmentEditParams(TypedDict, total=False):
    zone_id: Required[str]

    environments: Required[Iterable[Environment]]


class Environment(TypedDict, total=False):
    expression: Required[str]

    locked_on_deployment: Required[Optional[bool]]

    name: Required[str]

    position: Required[ListCursorParam]

    ref: Required[str]

    version: Required[Optional[int]]

    http_application_id: Optional[str]
