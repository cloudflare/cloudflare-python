# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .upstream_ips import UpstreamIPs
from .attack_mitigation_param import AttackMitigationParam

__all__ = ["DNSFirewallEditParams"]


class DNSFirewallEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    attack_mitigation: Optional[AttackMitigationParam]
    """Attack mitigation settings"""

    deprecate_any_requests: bool
    """Whether to refuse to answer queries for the ANY type"""

    ecs_fallback: bool
    """Whether to forward client IP (resolver) subnet if no EDNS Client Subnet is sent"""

    maximum_cache_ttl: float
    """
    Maximum DNS cache TTL This setting sets an upper bound on DNS TTLs for purposes
    of caching between DNS Firewall and the upstream servers. Higher TTLs will be
    decreased to the maximum defined here for caching purposes.
    """

    minimum_cache_ttl: float
    """
    Minimum DNS cache TTL This setting sets a lower bound on DNS TTLs for purposes
    of caching between DNS Firewall and the upstream servers. Lower TTLs will be
    increased to the minimum defined here for caching purposes.
    """

    name: str
    """DNS Firewall cluster name"""

    negative_cache_ttl: Optional[float]
    """
    Negative DNS cache TTL This setting controls how long DNS Firewall should cache
    negative responses (e.g., NXDOMAIN) from the upstream servers.
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

    upstream_ips: List[UpstreamIPs]
