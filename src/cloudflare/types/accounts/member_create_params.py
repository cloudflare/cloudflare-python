# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "MemberCreateParams",
    "IamCreateMemberWithRoles",
    "IamCreateMemberWithPolicies",
    "IamCreateMemberWithPoliciesPolicy",
    "IamCreateMemberWithPoliciesPolicyPermissionGroup",
    "IamCreateMemberWithPoliciesPolicyResourceGroup",
]


class IamCreateMemberWithRoles(TypedDict, total=False):
    account_id: Required[str]

    email: Required[str]
    """The contact email address of the user."""

    roles: Required[List[str]]
    """Array of roles associated with this member."""

    status: Literal["accepted", "pending"]


class IamCreateMemberWithPolicies(TypedDict, total=False):
    account_id: Required[str]

    email: Required[str]
    """The contact email address of the user."""

    policies: Required[Iterable[IamCreateMemberWithPoliciesPolicy]]
    """Array of policies associated with this member."""

    status: Literal["accepted", "pending"]


class IamCreateMemberWithPoliciesPolicyPermissionGroup(TypedDict, total=False):
    id: Required[str]
    """Identifier of the group."""


class IamCreateMemberWithPoliciesPolicyResourceGroup(TypedDict, total=False):
    id: Required[str]
    """Identifier of the group."""


class IamCreateMemberWithPoliciesPolicy(TypedDict, total=False):
    access: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[IamCreateMemberWithPoliciesPolicyPermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resource_groups: Required[Iterable[IamCreateMemberWithPoliciesPolicyResourceGroup]]
    """A list of resource groups that the policy applies to."""


MemberCreateParams = Union[IamCreateMemberWithRoles, IamCreateMemberWithPolicies]
