# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "AccountMember",
    "Role",
    "RolePermissions",
    "RolePermissionsAnalytics",
    "RolePermissionsBilling",
    "RolePermissionsCachePurge",
    "RolePermissionsDNS",
    "RolePermissionsDNSRecords",
    "RolePermissionsLb",
    "RolePermissionsLogs",
    "RolePermissionsOrganization",
    "RolePermissionsSSL",
    "RolePermissionsWAF",
    "RolePermissionsZoneSettings",
    "RolePermissionsZones",
    "User",
]


class RolePermissionsAnalytics(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsBilling(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsCachePurge(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsDNS(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsDNSRecords(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsLb(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsLogs(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsOrganization(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsSSL(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsWAF(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsZoneSettings(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissionsZones(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class RolePermissions(BaseModel):
    analytics: Optional[RolePermissionsAnalytics] = None

    billing: Optional[RolePermissionsBilling] = None

    cache_purge: Optional[RolePermissionsCachePurge] = None

    dns: Optional[RolePermissionsDNS] = None

    dns_records: Optional[RolePermissionsDNSRecords] = None

    lb: Optional[RolePermissionsLb] = None

    logs: Optional[RolePermissionsLogs] = None

    organization: Optional[RolePermissionsOrganization] = None

    ssl: Optional[RolePermissionsSSL] = None

    waf: Optional[RolePermissionsWAF] = None

    zone_settings: Optional[RolePermissionsZoneSettings] = None

    zones: Optional[RolePermissionsZones] = None


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


class AccountMember(BaseModel):
    id: str
    """Membership identifier tag."""

    roles: List[Role]
    """Roles assigned to this member."""

    status: object

    user: User
