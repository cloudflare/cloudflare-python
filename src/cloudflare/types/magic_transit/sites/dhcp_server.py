# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["DHCPServer"]


class DHCPServer(BaseModel):
    dhcp_pool_end: Optional[str] = None
    """A valid IPv4 address."""

    dhcp_pool_start: Optional[str] = None
    """A valid IPv4 address."""

    dns_server: Optional[str] = None
    """A valid IPv4 address."""

    dns_servers: Optional[List[str]] = None

    reservations: Optional[Dict[str, str]] = None
    """Mapping of MAC addresses to IP addresses"""
