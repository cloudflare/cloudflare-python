# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .role import Role
from ..._models import BaseModel

__all__ = [
    "Member",
    "Policy",
    "PolicyPermissionGroup",
    "PolicyPermissionGroupMeta",
    "PolicyResourceGroup",
    "PolicyResourceGroupScope",
    "PolicyResourceGroupScopeObject",
    "PolicyResourceGroupMeta",
    "User",
]


class PolicyPermissionGroupMeta(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None


class PolicyPermissionGroup(BaseModel):
    id: str
    """Identifier of the group."""

    meta: Optional[PolicyPermissionGroupMeta] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the group."""


class PolicyResourceGroupScopeObject(BaseModel):
    key: str
    """
    This is a combination of pre-defined resource name and identifier (like Zone ID
    etc.)
    """


class PolicyResourceGroupScope(BaseModel):
    key: str
    """
    This is a combination of pre-defined resource name and identifier (like Account
    ID etc.)
    """

    objects: List[PolicyResourceGroupScopeObject]
    """A list of scope objects for additional context."""


class PolicyResourceGroupMeta(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None


class PolicyResourceGroup(BaseModel):
    id: str
    """Identifier of the group."""

    scope: List[PolicyResourceGroupScope]
    """The scope associated to the resource group"""

    meta: Optional[PolicyResourceGroupMeta] = None
    """Attributes associated to the resource group."""

    name: Optional[str] = None
    """Name of the resource group."""


class Policy(BaseModel):
    id: Optional[str] = None
    """Policy identifier."""

    access: Optional[Literal["allow", "deny"]] = None
    """Allow or deny operations against the resources."""

    permission_groups: Optional[List[PolicyPermissionGroup]] = None
    """A set of permission groups that are specified to the policy."""

    resource_groups: Optional[List[PolicyResourceGroup]] = None
    """A list of resource groups that the policy applies to."""


class User(BaseModel):
    email: str
    """The contact email address of the user."""

    id: Optional[str] = None
    """Identifier"""

    first_name: Optional[str] = None
    """User's first name"""

    last_name: Optional[str] = None
    """User's last name"""

    two_factor_authentication_enabled: Optional[bool] = None
    """Indicates whether two-factor authentication is enabled for the user account.

    Does not apply to API authentication.
    """


class Member(BaseModel):
    id: Optional[str] = None
    """Membership identifier tag."""

    policies: Optional[List[Policy]] = None
    """Access policy for the membership"""

    roles: Optional[List[Role]] = None
    """Roles assigned to this Member."""

    status: Optional[Literal["accepted", "pending"]] = None
    """A member's status in the account."""

    user: Optional[User] = None
    """Details of the user associated to the membership."""
