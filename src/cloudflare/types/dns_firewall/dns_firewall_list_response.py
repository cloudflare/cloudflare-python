# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .firewall_ips import FirewallIPs
from .upstream_ips import UpstreamIPs
from .attack_mitigation import AttackMitigation

__all__ = ["DNSFirewallListResponse"]


class DNSFirewallListResponse(BaseModel):
    id: str
    """Identifier."""

    deprecate_any_requests: bool
    """Whether to refuse to answer queries for the ANY type"""

    dns_firewall_ips: List[FirewallIPs]

    ecs_fallback: bool
    """Whether to forward client IP (resolver) subnet if no EDNS Client Subnet is sent"""

    maximum_cache_ttl: float
    """
    By default, Cloudflare attempts to cache responses for as long as indicated by
    the TTL received from upstream nameservers. This setting sets an upper bound on
    this duration. For caching purposes, higher TTLs will be decreased to the
    maximum value defined by this setting.

    This setting does not affect the TTL value in the DNS response Cloudflare
    returns to clients. Cloudflare will always forward the TTL value received from
    upstream nameservers.
    """

    minimum_cache_ttl: float
    """
    By default, Cloudflare attempts to cache responses for as long as indicated by
    the TTL received from upstream nameservers. This setting sets a lower bound on
    this duration. For caching purposes, lower TTLs will be increased to the minimum
    value defined by this setting.

    This setting does not affect the TTL value in the DNS response Cloudflare
    returns to clients. Cloudflare will always forward the TTL value received from
    upstream nameservers.

    Note that, even with this setting, there is no guarantee that a response will be
    cached for at least the specified duration. Cached responses may be removed
    earlier for capacity or other operational reasons.
    """

    modified_on: datetime
    """Last modification of DNS Firewall cluster"""

    name: str
    """DNS Firewall cluster name"""

    negative_cache_ttl: Optional[float] = None
    """
    This setting controls how long DNS Firewall should cache negative responses
    (e.g., NXDOMAIN) from the upstream servers.

    This setting does not affect the TTL value in the DNS response Cloudflare
    returns to clients. Cloudflare will always forward the TTL value received from
    upstream nameservers.
    """

    ratelimit: Optional[float] = None
    """
    Ratelimit in queries per second per datacenter (applies to DNS queries sent to
    the upstream nameservers configured on the cluster)
    """

    retries: float
    """
    Number of retries for fetching DNS responses from upstream nameservers (not
    counting the initial attempt)
    """

    upstream_ips: List[UpstreamIPs]

    attack_mitigation: Optional[AttackMitigation] = None
    """Attack mitigation settings"""
