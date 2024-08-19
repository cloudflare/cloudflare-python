# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PolicyParam", "PermissionGroup"]


class PermissionGroup(TypedDict, total=False):
    meta: object
    """Attributes associated to the permission group."""


class PolicyParam(TypedDict, total=False):
    effect: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[PermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resources: Required[object]
    """A list of resource names that the policy applies to."""
