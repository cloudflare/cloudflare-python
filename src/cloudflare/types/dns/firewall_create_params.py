# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .upstream_ips_param import UpstreamIPsParam
from .attack_mitigation_param import AttackMitigationParam

__all__ = ["FirewallCreateParams"]


class FirewallCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: Required[str]
    """DNS Firewall Cluster Name."""

    upstream_ips: Required[List[UpstreamIPsParam]]

    attack_mitigation: Optional[AttackMitigationParam]
    """Attack mitigation settings."""

    deprecate_any_requests: bool
    """Deprecate the response to ANY requests."""

    ecs_fallback: bool
    """Forward client IP (resolver) subnet if no EDNS Client Subnet is sent."""

    maximum_cache_ttl: float
    """Maximum DNS Cache TTL."""

    minimum_cache_ttl: float
    """Minimum DNS Cache TTL."""

    negative_cache_ttl: Optional[float]
    """Negative DNS Cache TTL."""

    ratelimit: Optional[float]
    """
    Ratelimit in queries per second per datacenter (applies to DNS queries sent to
    the upstream nameservers configured on the cluster).
    """

    retries: float
    """
    Number of retries for fetching DNS responses from upstream nameservers (not
    counting the initial attempt).
    """
