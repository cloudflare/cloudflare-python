# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountEditParams", "ZoneDefaults", "ZoneDefaultsInternalDNS", "ZoneDefaultsNameservers", "ZoneDefaultsSOA"]


class AccountEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    zone_defaults: ZoneDefaults


class ZoneDefaultsInternalDNS(TypedDict, total=False):
    reference_zone_id: str
    """The ID of the zone to fallback to."""


class ZoneDefaultsNameservers(TypedDict, total=False):
    type: Required[Literal["cloudflare.standard", "cloudflare.standard.random", "custom.account", "custom.tenant"]]
    """Nameserver type"""


class ZoneDefaultsSOA(TypedDict, total=False):
    expire: Required[float]
    """
    Time in seconds of being unable to query the primary server after which
    secondary servers should stop serving the zone.
    """

    min_ttl: Required[float]
    """The time to live (TTL) for negative caching of records within the zone."""

    mname: Required[str]
    """The primary nameserver, which may be used for outbound zone transfers."""

    refresh: Required[float]
    """
    Time in seconds after which secondary servers should re-check the SOA record to
    see if the zone has been updated.
    """

    retry: Required[float]
    """
    Time in seconds after which secondary servers should retry queries after the
    primary server was unresponsive.
    """

    rname: Required[str]
    """
    The email address of the zone administrator, with the first label representing
    the local part of the email address.
    """

    ttl: Required[float]
    """The time to live (TTL) of the SOA record itself."""


class ZoneDefaults(TypedDict, total=False):
    flatten_all_cnames: bool
    """Whether to flatten all CNAME records in the zone.

    Note that, due to DNS limitations, a CNAME record at the zone apex will always
    be flattened.
    """

    foundation_dns: bool
    """Whether to enable Foundation DNS Advanced Nameservers on the zone."""

    internal_dns: ZoneDefaultsInternalDNS
    """Settings for this internal zone."""

    multi_provider: bool
    """
    Whether to enable multi-provider DNS, which causes Cloudflare to activate the
    zone even when non-Cloudflare NS records exist, and to respect NS records at the
    zone apex during outbound zone transfers.
    """

    nameservers: ZoneDefaultsNameservers
    """
    Settings determining the nameservers through which the zone should be available.
    """

    ns_ttl: float
    """The time to live (TTL) of the zone's nameserver (NS) records."""

    secondary_overrides: bool
    """
    Allows a Secondary DNS zone to use (proxied) override records and CNAME
    flattening at the zone apex.
    """

    soa: ZoneDefaultsSOA
    """Components of the zone's SOA record."""

    zone_mode: Literal["standard", "cdn_only", "dns_only"]
    """Whether the zone mode is a regular or CDN/DNS only zone."""
