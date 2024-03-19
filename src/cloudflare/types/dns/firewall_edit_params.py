# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FirewallEditParams", "AttackMitigation"]


class FirewallEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    deprecate_any_requests: Required[bool]
    """Deprecate the response to ANY requests."""

    dns_firewall_ips: Required[List[Union[str, str]]]

    ecs_fallback: Required[bool]
    """Forward client IP (resolver) subnet if no EDNS Client Subnet is sent."""

    maximum_cache_ttl: Required[float]
    """Maximum DNS Cache TTL."""

    minimum_cache_ttl: Required[float]
    """Minimum DNS Cache TTL."""

    name: Required[str]
    """DNS Firewall Cluster Name."""

    upstream_ips: Required[List[Union[str, str]]]

    attack_mitigation: Optional[AttackMitigation]
    """Attack mitigation settings."""

    negative_cache_ttl: Optional[float]
    """Negative DNS Cache TTL."""

    origin_ips: object
    """Deprecated alias for "upstream_ips"."""

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


class AttackMitigation(TypedDict, total=False):
    enabled: bool
    """
    When enabled, random-prefix attacks are automatically mitigated and the upstream
    DNS servers protected.
    """

    only_when_origin_unhealthy: object
    """Deprecated alias for "only_when_upstream_unhealthy"."""

    only_when_upstream_unhealthy: bool
    """Only mitigate attacks when upstream servers seem unhealthy."""
