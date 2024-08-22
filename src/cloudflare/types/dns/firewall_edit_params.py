# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Optional

from .firewall_ips import FirewallIPs

from .upstream_ips import UpstreamIPs

from .attack_mitigation_param import AttackMitigationParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["FirewallEditParams"]

class FirewallEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    id: Required[str]
    """Identifier"""

    deprecate_any_requests: Required[bool]
    """Deprecate the response to ANY requests."""

    dns_firewall_ips: Required[List[FirewallIPs]]

    ecs_fallback: Required[bool]
    """Forward client IP (resolver) subnet if no EDNS Client Subnet is sent."""

    maximum_cache_ttl: Required[float]
    """Maximum DNS cache TTL.

    This setting sets an upper bound on DNS TTLs for purposes of caching between DNS
    Firewall and the upstream servers. Higher TTLs will be decreased to the maximum
    defined here for caching purposes.
    """

    minimum_cache_ttl: Required[float]
    """Minimum DNS cache TTL.

    This setting sets a lower bound on DNS TTLs for purposes of caching between DNS
    Firewall and the upstream servers. Lower TTLs will be increased to the minimum
    defined here for caching purposes.
    """

    name: Required[str]
    """DNS Firewall Cluster Name."""

    upstream_ips: Required[List[UpstreamIPs]]

    attack_mitigation: Optional[AttackMitigationParam]
    """Attack mitigation settings."""

    negative_cache_ttl: Optional[float]
    """Negative DNS cache TTL.

    This setting controls how long DNS Firewall should cache negative responses
    (e.g., NXDOMAIN) from the upstream servers.
    """

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