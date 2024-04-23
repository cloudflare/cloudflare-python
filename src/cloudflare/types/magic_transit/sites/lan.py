# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .nat import Nat
from ...._models import BaseModel
from .routed_subnet import RoutedSubnet
from .lan_static_addressing import LANStaticAddressing

__all__ = ["LAN"]


class LAN(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    ha_link: Optional[bool] = None
    """mark true to use this LAN for HA probing.

    only works for site with HA turned on. only one LAN can be set as the ha_link.
    """

    name: Optional[str] = None

    nat: Optional[Nat] = None

    physport: Optional[int] = None

    routed_subnets: Optional[List[RoutedSubnet]] = None

    site_id: Optional[str] = None
    """Identifier"""

    static_addressing: Optional[LANStaticAddressing] = None
    """
    If the site is not configured in high availability mode, this configuration is
    optional (if omitted, use DHCP). However, if in high availability mode,
    static_address is required along with secondary and virtual address.
    """

    vlan_tag: Optional[int] = None
    """VLAN port number."""
