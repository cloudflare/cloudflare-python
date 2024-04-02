# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RolePermissionGrantParam"]


class RolePermissionGrantParam(TypedDict, total=False):
    read: bool

    write: bool
