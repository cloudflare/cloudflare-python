# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .account import Account
from .._models import BaseModel

__all__ = [
    "Membership",
    "Permissions",
    "PermissionsAnalytics",
    "PermissionsBilling",
    "PermissionsCachePurge",
    "PermissionsDNS",
    "PermissionsDNSRecords",
    "PermissionsLb",
    "PermissionsLogs",
    "PermissionsOrganization",
    "PermissionsSSL",
    "PermissionsWAF",
    "PermissionsZoneSettings",
    "PermissionsZones",
]


class PermissionsAnalytics(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsBilling(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsCachePurge(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsDNS(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsDNSRecords(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsLb(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsLogs(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsOrganization(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsSSL(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsWAF(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsZoneSettings(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class PermissionsZones(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class Permissions(BaseModel):
    analytics: Optional[PermissionsAnalytics] = None

    billing: Optional[PermissionsBilling] = None

    cache_purge: Optional[PermissionsCachePurge] = None

    dns: Optional[PermissionsDNS] = None

    dns_records: Optional[PermissionsDNSRecords] = None

    lb: Optional[PermissionsLb] = None

    logs: Optional[PermissionsLogs] = None

    organization: Optional[PermissionsOrganization] = None

    ssl: Optional[PermissionsSSL] = None

    waf: Optional[PermissionsWAF] = None

    zone_settings: Optional[PermissionsZoneSettings] = None

    zones: Optional[PermissionsZones] = None


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
