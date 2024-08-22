# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .dhcp_relay import DHCPRelay
from .dhcp_server import DHCPServer

__all__ = ["LANStaticAddressing"]


class LANStaticAddressing(BaseModel):
    address: str
    """A valid CIDR notation representing an IP range."""

    dhcp_relay: Optional[DHCPRelay] = None

    dhcp_server: Optional[DHCPServer] = None

    secondary_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""

    virtual_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""
