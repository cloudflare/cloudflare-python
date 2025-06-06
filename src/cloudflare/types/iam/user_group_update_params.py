# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserGroupUpdateParams", "Policy", "PolicyPermissionGroup", "PolicyResourceGroup"]


class UserGroupUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    name: str
    """Name of the User group."""

    policies: Iterable[Policy]
    """Policies attached to the User group"""


class PolicyPermissionGroup(TypedDict, total=False):
    id: Required[str]
    """Permission Group identifier tag."""


class PolicyResourceGroup(TypedDict, total=False):
    id: Required[str]
    """Resource Group identifier tag."""


class Policy(TypedDict, total=False):
    id: Required[str]
    """Policy identifier."""

    access: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[PolicyPermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resource_groups: Required[Iterable[PolicyResourceGroup]]
    """A set of resource groups that are specified to the policy."""
