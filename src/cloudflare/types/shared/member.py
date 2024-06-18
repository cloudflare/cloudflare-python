# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .permission_grant import PermissionGrant

__all__ = ["Member", "Role", "RolePermissions", "User"]


class RolePermissions(BaseModel):
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


class Member(BaseModel):
    id: Optional[str] = None
    """Membership identifier tag."""

    roles: Optional[List[Role]] = None
    """Roles assigned to this member."""

    status: Optional[Literal["accepted", "pending"]] = None
    """A member's status in the account."""

    user: Optional[User] = None
    """Details of the user associated to the membership."""
