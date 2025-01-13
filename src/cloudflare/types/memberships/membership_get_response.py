# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..accounts.account import Account
from ..shared.permission_grant import PermissionGrant

__all__ = [
    "MembershipGetResponse",
    "Permissions",
    "Policy",
    "PolicyPermissionGroup",
    "PolicyPermissionGroupMeta",
    "PolicyResourceGroup",
    "PolicyResourceGroupScope",
    "PolicyResourceGroupScopeObject",
    "PolicyResourceGroupMeta",
]


class Permissions(BaseModel):
    analytics: Optional[PermissionGrant] = None

    billing: Optional[PermissionGrant] = None

    cache_purge: Optional[PermissionGrant] = None

    dns: Optional[PermissionGrant] = None

    dns_records: Optional[PermissionGrant] = None

    lb: Optional[PermissionGrant] = None

    logs: Optional[PermissionGrant] = None

    organization: Optional[PermissionGrant] = None

    ssl: Optional[PermissionGrant] = None

    waf: Optional[PermissionGrant] = None

    zone_settings: Optional[PermissionGrant] = None

    zones: Optional[PermissionGrant] = None


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


class MembershipGetResponse(BaseModel):
    id: Optional[str] = None
    """Membership identifier tag."""

    account: Optional[Account] = None

    api_access_enabled: Optional[bool] = None
    """Enterprise only.

    Indicates whether or not API access is enabled specifically for this user on a
    given account.
    """

    permissions: Optional[Permissions] = None
    """All access permissions for the user at the account."""

    policies: Optional[List[Policy]] = None
    """Access policy for the membership"""

    roles: Optional[List[str]] = None
    """List of role names the membership has for this account."""

    status: Optional[Literal["accepted", "pending", "rejected"]] = None
    """Status of this membership."""
