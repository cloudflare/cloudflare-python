# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from .firewall_ips import FirewallIPs

from datetime import datetime

from .upstream_ips import UpstreamIPs

from .attack_mitigation import AttackMitigation

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["FirewallGetResponse"]


class FirewallGetResponse(BaseModel):
    id: str
    """Identifier"""

    deprecate_any_requests: bool
    """Deprecate the response to ANY requests."""

    dns_firewall_ips: List[FirewallIPs]

    ecs_fallback: bool
    """Forward client IP (resolver) subnet if no EDNS Client Subnet is sent."""

    maximum_cache_ttl: float
    """Maximum DNS cache TTL.

    This setting sets an upper bound on DNS TTLs for purposes of caching between DNS
    Firewall and the upstream servers. Higher TTLs will be decreased to the maximum
    defined here for caching purposes.
    """

    minimum_cache_ttl: float
    """Minimum DNS cache TTL.

    This setting sets a lower bound on DNS TTLs for purposes of caching between DNS
    Firewall and the upstream servers. Lower TTLs will be increased to the minimum
    defined here for caching purposes.
    """

    modified_on: datetime
    """Last modification of DNS Firewall cluster."""

    name: str
    """DNS Firewall Cluster Name."""

    negative_cache_ttl: Optional[float] = None
    """Negative DNS cache TTL.

    This setting controls how long DNS Firewall should cache negative responses
    (e.g., NXDOMAIN) from the upstream servers.
    """

    ratelimit: Optional[float] = None
    """
    Ratelimit in queries per second per datacenter (applies to DNS queries sent to
    the upstream nameservers configured on the cluster).
    """

    retries: float
    """
    Number of retries for fetching DNS responses from upstream nameservers (not
    counting the initial attempt).
    """

    upstream_ips: List[UpstreamIPs]

    attack_mitigation: Optional[AttackMitigation] = None
    """Attack mitigation settings."""
