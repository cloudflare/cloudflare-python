# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .attack_mitigation_param import AttackMitigationParam
from .firewall_ips_item_param import FirewallIPsItemParam
from .upstream_ips_items_param import UpstreamIPsItemsParam

__all__ = ["FirewallEditParams"]


class FirewallEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    deprecate_any_requests: Required[bool]
    """Deprecate the response to ANY requests."""

    dns_firewall_ips: Required[List[FirewallIPsItemParam]]

    ecs_fallback: Required[bool]
    """Forward client IP (resolver) subnet if no EDNS Client Subnet is sent."""

    maximum_cache_ttl: Required[float]
    """Maximum DNS Cache TTL."""

    minimum_cache_ttl: Required[float]
    """Minimum DNS Cache TTL."""

    name: Required[str]
    """DNS Firewall Cluster Name."""

    upstream_ips: Required[List[UpstreamIPsItemsParam]]

    attack_mitigation: Optional[AttackMitigationParam]
    """Attack mitigation settings."""

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
