# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .upstream_ips import UpstreamIPs
from .attack_mitigation_param import AttackMitigationParam

__all__ = ["DNSFirewallEditParams"]


class DNSFirewallEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    attack_mitigation: Optional[AttackMitigationParam]
    """Attack mitigation settings"""

    deprecate_any_requests: bool
    """Whether to refuse to answer queries for the ANY type"""

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

    name: str
    """DNS Firewall cluster name"""

    negative_cache_ttl: Optional[float]
    """
    This setting controls how long DNS Firewall should cache negative responses
    (e.g., NXDOMAIN) from the upstream servers.

    This setting does not affect the TTL value in the DNS response Cloudflare
    returns to clients. Cloudflare will always forward the TTL value received from
    upstream nameservers.
    """

    ratelimit: Optional[float]
    """
    Ratelimit in queries per second per datacenter (applies to DNS queries sent to
    the upstream nameservers configured on the cluster)
    """

    retries: float
    """
    Number of retries for fetching DNS responses from upstream nameservers (not
    counting the initial attempt)
    """

    upstream_ips: SequenceNotStr[UpstreamIPs]
