# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from .health_check_rate import HealthCheckRate

from .health_check_type import HealthCheckType

from datetime import datetime

from .psk_metadata import PSKMetadata

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IPSECTunnelGetResponse", "IPSECTunnel", "IPSECTunnelTunnelHealthCheck"]


class IPSECTunnelTunnelHealthCheck(BaseModel):
    enabled: Optional[bool] = None
    """Determines whether to run healthchecks for a tunnel."""

    rate: Optional[HealthCheckRate] = None
    """How frequent the health check is run. The default value is `mid`."""

    target: Optional[str] = None
    """The destination address in a request type health check.

    After the healthcheck is decapsulated at the customer end of the tunnel, the
    ICMP echo will be forwarded to this address. This field defaults to
    `customer_gre_endpoint address`.
    """

    type: Optional[HealthCheckType] = None
    """The type of healthcheck to run, reply or request. The default value is `reply`."""


class IPSECTunnel(BaseModel):
    cloudflare_endpoint: str
    """The IP address assigned to the Cloudflare side of the IPsec tunnel."""

    interface_address: str
    """
    A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
    of the tunnel. Select the subnet from the following private IP space:
    10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    """

    name: str
    """The name of the IPsec tunnel. The name cannot share a name with other tunnels."""

    id: Optional[str] = None
    """Tunnel identifier tag."""

    allow_null_cipher: Optional[bool] = None
    """
    When `true`, the tunnel can use a null-cipher (`ENCR_NULL`) in the ESP tunnel
    (Phase 2).
    """

    created_on: Optional[datetime] = None
    """The date and time the tunnel was created."""

    customer_endpoint: Optional[str] = None
    """The IP address assigned to the customer side of the IPsec tunnel.

    Not required, but must be set for proactive traceroutes to work.
    """

    description: Optional[str] = None
    """An optional description forthe IPsec tunnel."""

    modified_on: Optional[datetime] = None
    """The date and time the tunnel was last modified."""

    psk_metadata: Optional[PSKMetadata] = None
    """The PSK metadata that includes when the PSK was generated."""

    replay_protection: Optional[bool] = None
    """
    If `true`, then IPsec replay protection will be supported in the
    Cloudflare-to-customer direction.
    """

    tunnel_health_check: Optional[IPSECTunnelTunnelHealthCheck] = None


class IPSECTunnelGetResponse(BaseModel):
    ipsec_tunnel: Optional[IPSECTunnel] = None
