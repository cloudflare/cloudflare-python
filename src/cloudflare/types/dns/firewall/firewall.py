# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from ..upstream_ips import UpstreamIPs
from ..attack_mitigation import AttackMitigation
from ..firewall_ips_item import FirewallIPsItem

__all__ = ["Firewall"]


class Firewall(BaseModel):
    id: str
    """Identifier"""

    deprecate_any_requests: bool
    """Deprecate the response to ANY requests."""

    dns_firewall_ips: List[FirewallIPsItem]

    ecs_fallback: bool
    """Forward client IP (resolver) subnet if no EDNS Client Subnet is sent."""

    maximum_cache_ttl: float
    """Maximum DNS Cache TTL."""

    minimum_cache_ttl: float
    """Minimum DNS Cache TTL."""

    modified_on: datetime
    """Last modification of DNS Firewall cluster."""

    name: str
    """DNS Firewall Cluster Name."""

    upstream_ips: List[UpstreamIPs]

    attack_mitigation: Optional[AttackMitigation] = None
    """Attack mitigation settings."""

    negative_cache_ttl: Optional[float] = None
    """Negative DNS Cache TTL."""

    ratelimit: Optional[float] = None
    """
    Ratelimit in queries per second per datacenter (applies to DNS queries sent to
    the upstream nameservers configured on the cluster).
    """

    retries: Optional[float] = None
    """
    Number of retries for fetching DNS responses from upstream nameservers (not
    counting the initial attempt).
    """
