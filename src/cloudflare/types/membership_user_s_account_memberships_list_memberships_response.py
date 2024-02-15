# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "MembershipUserSAccountMembershipsListMembershipsResponse",
    "MembershipUserSAccountMembershipsListMembershipsResponseItem",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemAccount",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemAccountSettings",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissions",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsAnalytics",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsBilling",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsCachePurge",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsDNS",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsDNSRecords",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsLb",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsLogs",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsOrganization",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsSSL",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsWAF",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsZoneSettings",
    "MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsZones",
]


class MembershipUserSAccountMembershipsListMembershipsResponseItemAccountSettings(BaseModel):
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


class MembershipUserSAccountMembershipsListMembershipsResponseItemAccount(BaseModel):
    id: str
    """Identifier"""

    name: str
    """Account name"""

    created_on: Optional[datetime] = None
    """Timestamp for the creation of the account"""

    settings: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemAccountSettings] = None
    """Account settings"""


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsAnalytics(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsBilling(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsCachePurge(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsDNS(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsDNSRecords(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsLb(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsLogs(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsOrganization(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsSSL(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsWAF(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsZoneSettings(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsZones(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItemPermissions(BaseModel):
    analytics: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsAnalytics] = None

    billing: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsBilling] = None

    cache_purge: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsCachePurge] = None

    dns: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsDNS] = None

    dns_records: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsDNSRecords] = None

    lb: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsLb] = None

    logs: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsLogs] = None

    organization: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsOrganization] = None

    ssl: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsSSL] = None

    waf: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsWAF] = None

    zone_settings: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsZoneSettings] = None

    zones: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissionsZones] = None


class MembershipUserSAccountMembershipsListMembershipsResponseItem(BaseModel):
    id: Optional[str] = None
    """Membership identifier tag."""

    account: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemAccount] = None

    api_access_enabled: Optional[bool] = None
    """Enterprise only.

    Indicates whether or not API access is enabled specifically for this user on a
    given account.
    """

    code: Optional[str] = None
    """The unique activation code for the account membership."""

    permissions: Optional[MembershipUserSAccountMembershipsListMembershipsResponseItemPermissions] = None
    """All access permissions for the user at the account."""

    roles: Optional[List[str]] = None
    """List of role names for the user at the account."""

    status: Optional[Literal["accepted", "pending", "rejected"]] = None
    """Status of this membership."""


MembershipUserSAccountMembershipsListMembershipsResponse = List[
    MembershipUserSAccountMembershipsListMembershipsResponseItem
]
