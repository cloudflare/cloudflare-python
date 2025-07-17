# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenPolicy", "PermissionGroup", "PermissionGroupMeta", "Resources"]


class PermissionGroupMeta(TypedDict, total=False):
    key: str

    value: str


class PermissionGroup(TypedDict, total=False):
    id: Required[str]
    """Identifier of the permission group."""

    meta: PermissionGroupMeta
    """Attributes associated to the permission group."""


class Resources(TypedDict, total=False):
    nested: Dict[str, Dict[str, str]]
    """Nested resource permissions for hierarchical scoping."""

    simple: Dict[str, str]
    """Simple resource permissions where each resource maps to a permission string."""


class TokenPolicy(TypedDict, total=False):
    effect: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[PermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resources: Required[Resources]
    """Resource permissions for the policy. Use either simple or nested permissions."""
