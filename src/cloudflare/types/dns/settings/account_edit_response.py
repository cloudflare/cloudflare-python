# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "AccountEditResponse",
    "ZoneDefaults",
    "ZoneDefaultsInternalDNS",
    "ZoneDefaultsNameservers",
    "ZoneDefaultsSOA",
]


class ZoneDefaultsInternalDNS(BaseModel):
    reference_zone_id: Optional[str] = None
    """The ID of the zone to fallback to."""


class ZoneDefaultsNameservers(BaseModel):
    type: Literal["cloudflare.standard", "cloudflare.standard.random", "custom.account", "custom.tenant"]
    """Nameserver type"""


class ZoneDefaultsSOA(BaseModel):
    expire: float
    """
    Time in seconds of being unable to query the primary server after which
    secondary servers should stop serving the zone.
    """

    min_ttl: float
    """The time to live (TTL) for negative caching of records within the zone."""

    mname: str
    """The primary nameserver, which may be used for outbound zone transfers."""

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


class ZoneDefaults(BaseModel):
    flatten_all_cnames: Optional[bool] = None
    """Whether to flatten all CNAME records in the zone.

    Note that, due to DNS limitations, a CNAME record at the zone apex will always
    be flattened.
    """

    foundation_dns: Optional[bool] = None
    """Whether to enable Foundation DNS Advanced Nameservers on the zone."""

    internal_dns: Optional[ZoneDefaultsInternalDNS] = None
    """Settings for this internal zone."""

    multi_provider: Optional[bool] = None
    """
    Whether to enable multi-provider DNS, which causes Cloudflare to activate the
    zone even when non-Cloudflare NS records exist, and to respect NS records at the
    zone apex during outbound zone transfers.
    """

    nameservers: Optional[ZoneDefaultsNameservers] = None
    """
    Settings determining the nameservers through which the zone should be available.
    """

    ns_ttl: Optional[float] = None
    """The time to live (TTL) of the zone's nameserver (NS) records."""

    secondary_overrides: Optional[bool] = None
    """
    Allows a Secondary DNS zone to use (proxied) override records and CNAME
    flattening at the zone apex.
    """

    soa: Optional[ZoneDefaultsSOA] = None
    """Components of the zone's SOA record."""

    zone_mode: Optional[Literal["standard", "cdn_only", "dns_only"]] = None
    """Whether the zone mode is a regular or CDN/DNS only zone."""


class AccountEditResponse(BaseModel):
    zone_defaults: Optional[ZoneDefaults] = None
