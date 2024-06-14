# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "MemberUpdateParams",
    "Member",
    "MemberRole",
    "IamUpdateMemberWithPolicies",
    "IamUpdateMemberWithPoliciesPolicy",
    "IamUpdateMemberWithPoliciesPolicyPermissionGroup",
    "IamUpdateMemberWithPoliciesPolicyResourceGroup",
]


class Member(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    roles: Iterable[MemberRole]
    """Roles assigned to this member."""


class MemberRole(TypedDict, total=False):
    id: Required[str]
    """Role identifier tag."""


class IamUpdateMemberWithPolicies(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    policies: Required[Iterable[IamUpdateMemberWithPoliciesPolicy]]
    """Array of policies associated with this member."""


class IamUpdateMemberWithPoliciesPolicyPermissionGroup(TypedDict, total=False):
    id: Required[str]
    """Identifier of the group."""


class IamUpdateMemberWithPoliciesPolicyResourceGroup(TypedDict, total=False):
    id: Required[str]
    """Identifier of the group."""


class IamUpdateMemberWithPoliciesPolicy(TypedDict, total=False):
    access: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[IamUpdateMemberWithPoliciesPolicyPermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resource_groups: Required[Iterable[IamUpdateMemberWithPoliciesPolicyResourceGroup]]
    """A list of resource groups that the policy applies to."""


MemberUpdateParams = Union[Member, IamUpdateMemberWithPolicies]
