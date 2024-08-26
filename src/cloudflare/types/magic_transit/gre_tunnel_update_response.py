# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from .health_check import HealthCheck

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["GRETunnelUpdateResponse", "ModifiedGRETunnel"]

class ModifiedGRETunnel(BaseModel):
    cloudflare_gre_endpoint: str
    """The IP address assigned to the Cloudflare side of the GRE tunnel."""

    customer_gre_endpoint: str
    """The IP address assigned to the customer side of the GRE tunnel."""

    interface_address: str
    """
    A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
    of the tunnel. Select the subnet from the following private IP space:
    10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    """

    name: str
    """The name of the tunnel.

    The name cannot contain spaces or special characters, must be 15 characters or
    less, and cannot share a name with another GRE tunnel.
    """

    id: Optional[str] = None
    """Tunnel identifier tag."""

    created_on: Optional[datetime] = None
    """The date and time the tunnel was created."""

    description: Optional[str] = None
    """An optional description of the GRE tunnel."""

    health_check: Optional[HealthCheck] = None

    modified_on: Optional[datetime] = None
    """The date and time the tunnel was last modified."""

    mtu: Optional[int] = None
    """Maximum Transmission Unit (MTU) in bytes for the GRE tunnel.

    The minimum value is 576.
    """

    ttl: Optional[int] = None
    """Time To Live (TTL) in number of hops of the GRE tunnel."""

class GRETunnelUpdateResponse(BaseModel):
    modified: Optional[bool] = None

    modified_gre_tunnel: Optional[ModifiedGRETunnel] = None