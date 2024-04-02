# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .account import Account
from .._models import BaseModel
from .accounts import RolePermissionGrants

__all__ = ["Membership", "Permissions"]


class Permissions(BaseModel):
    analytics: Optional[RolePermissionGrants] = None

    billing: Optional[RolePermissionGrants] = None

    cache_purge: Optional[RolePermissionGrants] = None

    dns: Optional[RolePermissionGrants] = None

    dns_records: Optional[RolePermissionGrants] = None

    lb: Optional[RolePermissionGrants] = None

    logs: Optional[RolePermissionGrants] = None

    organization: Optional[RolePermissionGrants] = None

    ssl: Optional[RolePermissionGrants] = None

    waf: Optional[RolePermissionGrants] = None

    zone_settings: Optional[RolePermissionGrants] = None

    zones: Optional[RolePermissionGrants] = None


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
