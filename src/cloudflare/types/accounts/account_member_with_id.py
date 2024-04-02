# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .role_permission_grants import RolePermissionGrants

__all__ = ["AccountMemberWithID", "Role", "RolePermissions", "User"]


class RolePermissions(BaseModel):
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


class Role(BaseModel):
    id: str
    """Role identifier tag."""

    description: str
    """Description of role's permissions."""

    name: str
    """Role name."""

    permissions: RolePermissions


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


class AccountMemberWithID(BaseModel):
    id: str
    """Membership identifier tag."""

    roles: List[Role]
    """Roles assigned to this member."""

    status: object

    user: User

    code: Optional[str] = None
    """The unique activation code for the account membership."""
