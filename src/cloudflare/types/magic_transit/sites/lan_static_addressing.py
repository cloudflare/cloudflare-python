# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .dhcp_relay import DHCPRelay
from .dhcp_server import DHCPServer

__all__ = ["LANStaticAddressing"]


class LANStaticAddressing(BaseModel):
    """
    If the site is not configured in high availability mode, this configuration is optional (if omitted, use DHCP). However, if in high availability mode, static_address is required along with secondary and virtual address.
    """

    address: str
    """A valid CIDR notation representing an IP range."""

    dhcp_relay: Optional[DHCPRelay] = None

    dhcp_server: Optional[DHCPServer] = None

    secondary_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""

    virtual_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""
