# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ZoneEditParams",
    "InternalDNS",
    "Nameservers",
    "NameserversDNSSettingsZoneNameserversCloudflare",
    "NameserversDNSSettingsZoneNameserversCustomExisting",
    "NameserversDNSSettingsZoneNameserversCustomSet",
    "SOA",
]


class ZoneEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    flatten_all_cnames: bool
    """Whether to flatten all CNAME records in the zone.

    Note that, due to DNS limitations, a CNAME record at the zone apex will always
    be flattened.
    """

    foundation_dns: bool
    """Deprecated. Use nameservers.type to configure Advanced Nameservers."""

    internal_dns: InternalDNS
    """Settings for this internal zone."""

    multi_provider: bool
    """
    Whether to enable multi-provider DNS, which causes Cloudflare to activate the
    zone even when non-Cloudflare NS records exist, and to respect NS records at the
    zone apex during outbound zone transfers.
    """

    nameservers: Nameservers
    """Controls the nameservers through which the zone is available."""

    ns_ttl: float
    """The time to live (TTL) of the zone's nameserver (NS) records."""

    secondary_overrides: bool
    """
    Allows a Secondary DNS zone to use (proxied) override records and CNAME
    flattening at the zone apex.
    """

    soa: SOA
    """Components of the zone's SOA record."""

    zone_mode: Literal["standard", "cdn_only", "dns_only"]
    """Whether the zone mode is a regular or CDN/DNS only zone."""


class InternalDNS(TypedDict, total=False):
    """Settings for this internal zone."""

    reference_zone_id: str
    """The ID of the zone to fallback to."""


class NameserversDNSSettingsZoneNameserversCloudflare(TypedDict, total=False):
    type: Required[Literal["cloudflare.standard", "cloudflare.advanced"]]
    """Nameserver type."""


class NameserversDNSSettingsZoneNameserversCustomExisting(TypedDict, total=False):
    type: Required[Literal["custom.account", "custom.tenant", "custom.zone"]]
    """Nameserver type."""

    ns_set: int
    """Configured nameserver set number to use for this zone."""


class NameserversDNSSettingsZoneNameserversCustomSet(TypedDict, total=False):
    nameserver_set_id: Required[str]
    """Identifier of the account-owned Custom Nameserver Set to use for this zone."""

    type: Required[Literal["custom"]]
    """Nameserver type."""


Nameservers: TypeAlias = Union[
    NameserversDNSSettingsZoneNameserversCloudflare,
    NameserversDNSSettingsZoneNameserversCustomExisting,
    NameserversDNSSettingsZoneNameserversCustomSet,
]


class SOA(TypedDict, total=False):
    """Components of the zone's SOA record."""

    expire: float
    """
    Time in seconds of being unable to query the primary server after which
    secondary servers should stop serving the zone.
    """

    min_ttl: float
    """The time to live (TTL) for negative caching of records within the zone."""

    mname: Optional[str]
    """The primary nameserver, which may be used for outbound zone transfers.

    If null, a Cloudflare-assigned value will be used.
    """

    refresh: float
    """
    Time in seconds after which secondary servers should re-check the SOA record to
    see if the zone has been updated.
    """

    retry: float
    """
    Time in seconds after which secondary servers should retry queries after the
    primary server was unresponsive.
    """

    rname: str
    """
    The email address of the zone administrator, with the first label representing
    the local part of the email address.
    """

    ttl: float
    """The time to live (TTL) of the SOA record itself."""
