# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "MemberCreateParams",
    "IAMCreateMemberWithRoles",
    "IAMCreateMemberWithPolicies",
    "IAMCreateMemberWithPoliciesPolicy",
    "IAMCreateMemberWithPoliciesPolicyPermissionGroup",
    "IAMCreateMemberWithPoliciesPolicyResourceGroup",
]


class IAMCreateMemberWithRoles(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    email: Required[str]
    """The contact email address of the user."""

    roles: Required[List[str]]
    """Array of roles associated with this member."""

    status: Literal["accepted", "pending"]


class IAMCreateMemberWithPolicies(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    email: Required[str]
    """The contact email address of the user."""

    policies: Required[Iterable[IAMCreateMemberWithPoliciesPolicy]]
    """Array of policies associated with this member."""

    status: Literal["accepted", "pending"]


class IAMCreateMemberWithPoliciesPolicyPermissionGroup(TypedDict, total=False):
    id: Required[str]
    """Identifier of the group."""


class IAMCreateMemberWithPoliciesPolicyResourceGroup(TypedDict, total=False):
    id: Required[str]
    """Identifier of the group."""


class IAMCreateMemberWithPoliciesPolicy(TypedDict, total=False):
    access: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[IAMCreateMemberWithPoliciesPolicyPermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resource_groups: Required[Iterable[IAMCreateMemberWithPoliciesPolicyResourceGroup]]
    """A list of resource groups that the policy applies to."""


MemberCreateParams: TypeAlias = Union[IAMCreateMemberWithRoles, IAMCreateMemberWithPolicies]
