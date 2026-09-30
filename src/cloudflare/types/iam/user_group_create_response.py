# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "UserGroupCreateResponse",
    "Policy",
    "PolicyPermissionGroup",
    "PolicyPermissionGroupMeta",
    "PolicyResourceGroup",
    "PolicyResourceGroupScope",
    "PolicyResourceGroupScopeObject",
    "PolicyResourceGroupMeta",
]


class PolicyPermissionGroupMeta(BaseModel):
    """Attributes associated to the permission group."""

    category: Optional[str] = None
    """A category used to group permission groups."""

    deprecated: Optional[str] = None
    """Indicates whether the permission group is deprecated."""

    description: Optional[str] = None
    """Additional information about the permission group."""

    editable: Optional[str] = None
    """Indicates whether the permission group can be edited."""

    eol_at: Optional[datetime] = None
    """The planned end-of-life date and time, when provided."""

    label: Optional[str] = None
    """A label identifying the permission group."""

    scopes: Optional[str] = None
    """The scope associated with the permission group."""

    visibility: Optional[str] = None
    """Indicates the permission group's availability or visibility."""


class PolicyPermissionGroup(BaseModel):
    """
    A named group of permissions that map to a group of operations against resources.
    """

    id: str
    """Identifier of the permission group."""

    meta: Optional[PolicyPermissionGroupMeta] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the permission group."""


class PolicyResourceGroupScopeObject(BaseModel):
    """
    A scope object represents any resource that can have actions applied against invite.
    """

    key: str
    """
    This is a combination of pre-defined resource name and identifier (like Zone ID
    etc.)
    """


class PolicyResourceGroupScope(BaseModel):
    """A scope is a combination of scope objects which provides additional context."""

    key: str
    """
    This is a combination of pre-defined resource name and identifier (like Account
    ID etc.)
    """

    objects: List[PolicyResourceGroupScopeObject]
    """A list of scope objects for additional context."""


class PolicyResourceGroupMeta(BaseModel):
    """Attributes associated to the resource group."""

    key: Optional[str] = None

    value: Optional[str] = None


class PolicyResourceGroup(BaseModel):
    """A group of scoped resources."""

    id: str
    """Identifier of the resource group."""

    scope: PolicyResourceGroupScope
    """A scope is a combination of scope objects which provides additional context."""

    meta: Optional[PolicyResourceGroupMeta] = None
    """Attributes associated to the resource group."""

    name: Optional[str] = None
    """Name of the resource group."""


class Policy(BaseModel):
    """Policy"""

    id: Optional[str] = None
    """Policy identifier."""

    access: Optional[Literal["allow", "deny"]] = None
    """Allow or deny operations against the resources."""

    permission_groups: Optional[List[PolicyPermissionGroup]] = None
    """A set of permission groups that are specified to the policy."""

    resource_groups: Optional[List[PolicyResourceGroup]] = None
    """A list of resource groups that the policy applies to."""


class UserGroupCreateResponse(BaseModel):
    """A group of policies resources."""

    id: str
    """User Group identifier tag."""

    created_on: datetime
    """Timestamp for the creation of the user group"""

    modified_on: datetime
    """Last time the user group was modified."""

    name: str
    """Name of the user group."""

    policies: Optional[List[Policy]] = None
    """Policies attached to the User group"""
