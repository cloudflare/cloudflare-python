# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenPolicy", "PermissionGroup", "PermissionGroupMeta"]


class PermissionGroupMeta(TypedDict, total=False):
    key: str

    value: str


class PermissionGroup(TypedDict, total=False):
    id: Required[str]
    """Identifier of the group."""

    meta: PermissionGroupMeta
    """Attributes associated to the permission group."""


class TokenPolicy(TypedDict, total=False):
    effect: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[PermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resources: Required[Dict[str, str]]
    """A list of resource names that the policy applies to."""
