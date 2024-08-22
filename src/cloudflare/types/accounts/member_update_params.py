# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, TypeAlias

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["MemberUpdateParams", "Member", "MemberRole", "IAMUpdateMemberWithPolicies", "IAMUpdateMemberWithPoliciesPolicy", "IAMUpdateMemberWithPoliciesPolicyPermissionGroup", "IAMUpdateMemberWithPoliciesPolicyResourceGroup"]

class Member(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    roles: Iterable[MemberRole]
    """Roles assigned to this member."""

class MemberRole(TypedDict, total=False):
    id: Required[str]
    """Role identifier tag."""

class IAMUpdateMemberWithPolicies(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    policies: Required[Iterable[IAMUpdateMemberWithPoliciesPolicy]]
    """Array of policies associated with this member."""

class IAMUpdateMemberWithPoliciesPolicyPermissionGroup(TypedDict, total=False):
    id: Required[str]
    """Identifier of the group."""

class IAMUpdateMemberWithPoliciesPolicyResourceGroup(TypedDict, total=False):
    id: Required[str]
    """Identifier of the group."""

class IAMUpdateMemberWithPoliciesPolicy(TypedDict, total=False):
    access: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[IAMUpdateMemberWithPoliciesPolicyPermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resource_groups: Required[Iterable[IAMUpdateMemberWithPoliciesPolicyResourceGroup]]
    """A list of resource groups that the policy applies to."""

MemberUpdateParams: TypeAlias = Union[Member, IAMUpdateMemberWithPolicies]