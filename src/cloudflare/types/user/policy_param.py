# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

from typing import Iterable

__all__ = ["PolicyParam", "PermissionGroup", "PermissionGroupMeta", "Resources"]


class PermissionGroupMeta(TypedDict, total=False):
    key: str

    value: str


class PermissionGroup(TypedDict, total=False):
    meta: PermissionGroupMeta
    """Attributes associated to the permission group."""


class Resources(TypedDict, total=False):
    resource: str

    scope: str


class PolicyParam(TypedDict, total=False):
    effect: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[PermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resources: Required[Resources]
    """A list of resource names that the policy applies to."""
