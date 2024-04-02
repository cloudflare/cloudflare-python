# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .account import Account
from .._models import BaseModel
from .accounts import RolePermissionGrant

__all__ = ["Membership", "Permissions"]


class Permissions(BaseModel):
    analytics: Optional[RolePermissionGrant] = None

    billing: Optional[RolePermissionGrant] = None

    cache_purge: Optional[RolePermissionGrant] = None

    dns: Optional[RolePermissionGrant] = None

    dns_records: Optional[RolePermissionGrant] = None

    lb: Optional[RolePermissionGrant] = None

    logs: Optional[RolePermissionGrant] = None

    organization: Optional[RolePermissionGrant] = None

    ssl: Optional[RolePermissionGrant] = None

    waf: Optional[RolePermissionGrant] = None

    zone_settings: Optional[RolePermissionGrant] = None

    zones: Optional[RolePermissionGrant] = None


class Membership(BaseModel):
    id: Optional[str] = None
    """Membership identifier tag."""

    account: Optional[Account] = None

    api_access_enabled: Optional[bool] = None
    """Enterprise only.

    Indicates whether or not API access is enabled specifically for this user on a
    given account.
    """

    code: Optional[str] = None
    """The unique activation code for the account membership."""

    permissions: Optional[Permissions] = None
    """All access permissions for the user at the account."""

    roles: Optional[List[str]] = None
    """List of role names for the user at the account."""

    status: Optional[Literal["accepted", "pending", "rejected"]] = None
    """Status of this membership."""
