# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["WANStaticAddressing"]


class WANStaticAddressing(BaseModel):
    address: str
    """A valid CIDR notation representing an IP range."""

    gateway_address: str
    """A valid IPv4 address."""

    secondary_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""
