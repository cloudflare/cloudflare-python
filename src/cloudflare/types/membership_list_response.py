# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "MembershipListResponse",
    "Account",
    "AccountSettings",
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


class AccountSettings(BaseModel):
    default_nameservers: Optional[Literal["cloudflare.standard", "custom.account", "custom.tenant"]] = None
    """
    Specifies the default nameservers to be used for new zones added to this
    account.

    - `cloudflare.standard` for Cloudflare-branded nameservers
    - `custom.account` for account custom nameservers
    - `custom.tenant` for tenant custom nameservers

    See
    [Custom Nameservers](https://developers.cloudflare.com/dns/additional-options/custom-nameservers/)
    for more information.
    """

    enforce_twofactor: Optional[bool] = None
    """
    Indicates whether membership in this account requires that Two-Factor
    Authentication is enabled
    """

    use_account_custom_ns_by_default: Optional[bool] = None
    """
    Indicates whether new zones should use the account-level custom nameservers by
    default.

    Deprecated in favor of `default_nameservers`.
    """


class Account(BaseModel):
    id: str
    """Identifier"""

    name: str
    """Account name"""

    created_on: Optional[datetime] = None
    """Timestamp for the creation of the account"""

    settings: Optional[AccountSettings] = None
    """Account settings"""


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


class MembershipListResponse(BaseModel):
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
