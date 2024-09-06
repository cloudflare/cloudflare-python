# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from .health_check_param import HealthCheckParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["IPSECTunnelUpdateParams"]


class IPSECTunnelUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cloudflare_endpoint: Required[str]
    """The IP address assigned to the Cloudflare side of the IPsec tunnel."""

    interface_address: Required[str]
    """
    A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
    of the tunnel. Select the subnet from the following private IP space:
    10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    """

    name: Required[str]
    """The name of the IPsec tunnel. The name cannot share a name with other tunnels."""

    customer_endpoint: str
    """The IP address assigned to the customer side of the IPsec tunnel.

    Not required, but must be set for proactive traceroutes to work.
    """

    description: str
    """An optional description forthe IPsec tunnel."""

    health_check: HealthCheckParam

    psk: str
    """A randomly generated or provided string for use in the IPsec tunnel."""

    replay_protection: bool
    """
    If `true`, then IPsec replay protection will be supported in the
    Cloudflare-to-customer direction.
    """
