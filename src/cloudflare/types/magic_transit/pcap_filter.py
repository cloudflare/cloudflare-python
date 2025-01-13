# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PCAPFilter"]


class PCAPFilter(BaseModel):
    destination_address: Optional[str] = None
    """The destination IP address of the packet."""

    destination_port: Optional[float] = None
    """The destination port of the packet."""

    protocol: Optional[float] = None
    """The protocol number of the packet."""

    source_address: Optional[str] = None
    """The source IP address of the packet."""

    source_port: Optional[float] = None
    """The source port of the packet."""
