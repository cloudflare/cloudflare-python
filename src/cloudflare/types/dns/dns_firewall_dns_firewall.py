# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DNSFirewallDNSFirewall", "AttackMitigation"]


class AttackMitigation(BaseModel):
    enabled: Optional[bool] = None
    """
    When enabled, random-prefix attacks are automatically mitigated and the upstream
    DNS servers protected.
    """

    only_when_origin_unhealthy: Optional[object] = None
    """Deprecated alias for "only_when_upstream_unhealthy"."""

    only_when_upstream_unhealthy: Optional[bool] = None
    """Only mitigate attacks when upstream servers seem unhealthy."""


class DNSFirewallDNSFirewall(BaseModel):
    id: str
    """Identifier"""

    deprecate_any_requests: bool
    """Deprecate the response to ANY requests."""

    dns_firewall_ips: List[Union[str, str]]

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

    upstream_ips: List[Union[str, str]]

    attack_mitigation: Optional[AttackMitigation] = None
    """Attack mitigation settings."""

    negative_cache_ttl: Optional[float] = None
    """Negative DNS Cache TTL."""

    origin_ips: Optional[object] = None
    """Deprecated alias for "upstream_ips"."""

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
