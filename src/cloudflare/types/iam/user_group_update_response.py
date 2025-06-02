# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "UserGroupUpdateResponse",
    "Policy",
    "PolicyPermissionGroup",
    "PolicyPermissionGroupMeta",
    "PolicyResourceGroup",
    "PolicyResourceGroupScope",
    "PolicyResourceGroupScopeObject",
    "PolicyResourceGroupMeta",
]


class PolicyPermissionGroupMeta(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None


class PolicyPermissionGroup(BaseModel):
    id: str
    """Identifier of the permission group."""

    meta: Optional[PolicyPermissionGroupMeta] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the permission group."""


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
    """Identifier of the resource group."""

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


class UserGroupUpdateResponse(BaseModel):
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
