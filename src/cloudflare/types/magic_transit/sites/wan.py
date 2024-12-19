# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .wan_static_addressing import WANStaticAddressing

__all__ = ["WAN"]


class WAN(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    health_check_rate: Optional[Literal["low", "mid", "high"]] = None
    """Magic WAN health check rate for tunnels created on this link.

    The default value is `mid`.
    """

    name: Optional[str] = None

    physport: Optional[int] = None

    priority: Optional[int] = None
    """Priority of WAN for traffic loadbalancing."""

    site_id: Optional[str] = None
    """Identifier"""

    static_addressing: Optional[WANStaticAddressing] = None
    """(optional) if omitted, use DHCP.

    Submit secondary_address when site is in high availability mode.
    """

    vlan_tag: Optional[int] = None
    """VLAN port number."""
