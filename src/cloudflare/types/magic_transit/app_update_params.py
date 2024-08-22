# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["AppUpdateParams", "UpdateAppName", "UpdateAppType", "UpdateAppHostnames", "UpdateAppSubnets"]


class UpdateAppName(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[object]


class UpdateAppType(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[object]


class UpdateAppHostnames(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[object]


class UpdateAppSubnets(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[object]


AppUpdateParams: TypeAlias = Union[UpdateAppName, UpdateAppType, UpdateAppHostnames, UpdateAppSubnets]
