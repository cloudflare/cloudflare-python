# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict

__all__ = ["DHCPServerParam"]


class DHCPServerParam(TypedDict, total=False):
    dhcp_pool_end: str
    """A valid IPv4 address."""

    dhcp_pool_start: str
    """A valid IPv4 address."""

    dns_server: str
    """A valid IPv4 address."""

    dns_servers: List[str]

    reservations: Dict[str, str]
    """Mapping of MAC addresses to IP addresses"""
