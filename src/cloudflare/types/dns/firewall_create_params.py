# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FirewallCreateParams", "AttackMitigation"]


class FirewallCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: Required[str]
    """DNS Firewall Cluster Name."""

    upstream_ips: Required[List[Union[str, str]]]

    attack_mitigation: Optional[AttackMitigation]
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
