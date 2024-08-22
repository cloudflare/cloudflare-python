# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from .wan_static_addressing import WANStaticAddressing

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["WAN"]

class WAN(BaseModel):
    id: Optional[str] = None
    """Identifier"""

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