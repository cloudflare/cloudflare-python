# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = [
    "MembershipListResponse",
    "MembershipListResponseItem",
    "MembershipListResponseItemAccount",
    "MembershipListResponseItemAccountSettings",
    "MembershipListResponseItemPermissions",
    "MembershipListResponseItemPermissionsAnalytics",
    "MembershipListResponseItemPermissionsBilling",
    "MembershipListResponseItemPermissionsCachePurge",
    "MembershipListResponseItemPermissionsDNS",
    "MembershipListResponseItemPermissionsDNSRecords",
    "MembershipListResponseItemPermissionsLb",
    "MembershipListResponseItemPermissionsLogs",
    "MembershipListResponseItemPermissionsOrganization",
    "MembershipListResponseItemPermissionsSSL",
    "MembershipListResponseItemPermissionsWAF",
    "MembershipListResponseItemPermissionsZoneSettings",
    "MembershipListResponseItemPermissionsZones",
]


class MembershipListResponseItemAccountSettings(BaseModel):
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


class MembershipListResponseItemAccount(BaseModel):
    id: str
    """Identifier"""

    name: str
    """Account name"""

    created_on: Optional[datetime] = None
    """Timestamp for the creation of the account"""

    settings: Optional[MembershipListResponseItemAccountSettings] = None
    """Account settings"""


class MembershipListResponseItemPermissionsAnalytics(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsBilling(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsCachePurge(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsDNS(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsDNSRecords(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsLb(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsLogs(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsOrganization(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsSSL(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsWAF(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsZoneSettings(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissionsZones(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None


class MembershipListResponseItemPermissions(BaseModel):
    analytics: Optional[MembershipListResponseItemPermissionsAnalytics] = None

    billing: Optional[MembershipListResponseItemPermissionsBilling] = None

    cache_purge: Optional[MembershipListResponseItemPermissionsCachePurge] = None

    dns: Optional[MembershipListResponseItemPermissionsDNS] = None

    dns_records: Optional[MembershipListResponseItemPermissionsDNSRecords] = None

    lb: Optional[MembershipListResponseItemPermissionsLb] = None

    logs: Optional[MembershipListResponseItemPermissionsLogs] = None

    organization: Optional[MembershipListResponseItemPermissionsOrganization] = None

    ssl: Optional[MembershipListResponseItemPermissionsSSL] = None

    waf: Optional[MembershipListResponseItemPermissionsWAF] = None

    zone_settings: Optional[MembershipListResponseItemPermissionsZoneSettings] = None

    zones: Optional[MembershipListResponseItemPermissionsZones] = None


class MembershipListResponseItem(BaseModel):
    id: Optional[str] = None
    """Membership identifier tag."""

    account: Optional[MembershipListResponseItemAccount] = None

    api_access_enabled: Optional[bool] = None
    """Enterprise only.

    Indicates whether or not API access is enabled specifically for this user on a
    given account.
    """

    code: Optional[str] = None
    """The unique activation code for the account membership."""

    permissions: Optional[MembershipListResponseItemPermissions] = None
    """All access permissions for the user at the account."""

    roles: Optional[List[str]] = None
    """List of role names for the user at the account."""

    status: Optional[Literal["accepted", "pending", "rejected"]] = None
    """Status of this membership."""


MembershipListResponse = List[MembershipListResponseItem]
