# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .static_addressing import StaticAddressing

__all__ = ["WAN"]


class WAN(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    description: Optional[str] = None

    physport: Optional[int] = None

    priority: Optional[int] = None
    """Priority of WAN for traffic loadbalancing."""

    site_id: Optional[str] = None
    """Identifier"""

    static_addressing: Optional[StaticAddressing] = None
    """(optional) if omitted, use DHCP.

    Submit secondary_address when site is in high availability mode.
    """

    vlan_tag: Optional[int] = None
    """VLAN port number."""
