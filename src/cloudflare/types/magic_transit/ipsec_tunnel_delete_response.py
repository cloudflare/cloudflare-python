# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .psk_metadata import PSKMetadata
from .health_check_rate import HealthCheckRate
from .health_check_type import HealthCheckType

__all__ = [
    "IPSECTunnelDeleteResponse",
    "DeletedIPSECTunnel",
    "DeletedIPSECTunnelHealthCheck",
    "DeletedIPSECTunnelHealthCheckTarget",
    "DeletedIPSECTunnelHealthCheckTargetMagicHealthCheckTarget",
]


class DeletedIPSECTunnelHealthCheckTargetMagicHealthCheckTarget(BaseModel):
    effective: Optional[str] = None
    """The effective health check target.

    If 'saved' is empty, then this field will be populated with the calculated
    default value on GET requests. Ignored in POST, PUT, and PATCH requests.
    """

    saved: Optional[str] = None
    """The saved health check target.

    Setting the value to the empty string indicates that the calculated default
    value will be used.
    """


DeletedIPSECTunnelHealthCheckTarget: TypeAlias = Union[DeletedIPSECTunnelHealthCheckTargetMagicHealthCheckTarget, str]


class DeletedIPSECTunnelHealthCheck(BaseModel):
    direction: Optional[Literal["unidirectional", "bidirectional"]] = None
    """The direction of the flow of the healthcheck.

    Either unidirectional, where the probe comes to you via the tunnel and the
    result comes back to Cloudflare via the open Internet, or bidirectional where
    both the probe and result come and go via the tunnel.
    """

    enabled: Optional[bool] = None
    """Determines whether to run healthchecks for a tunnel."""

    rate: Optional[HealthCheckRate] = None
    """How frequent the health check is run. The default value is `mid`."""

    target: Optional[DeletedIPSECTunnelHealthCheckTarget] = None
    """The destination address in a request type health check.

    After the healthcheck is decapsulated at the customer end of the tunnel, the
    ICMP echo will be forwarded to this address. This field defaults to
    `customer_gre_endpoint address`. This field is ignored for bidirectional
    healthchecks as the interface_address (not assigned to the Cloudflare side of
    the tunnel) is used as the target. Must be in object form if the
    x-magic-new-hc-target header is set to true and string form if
    x-magic-new-hc-target is absent or set to false.
    """

    type: Optional[HealthCheckType] = None
    """The type of healthcheck to run, reply or request. The default value is `reply`."""


class DeletedIPSECTunnel(BaseModel):
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

    health_check: Optional[DeletedIPSECTunnelHealthCheck] = None

    modified_on: Optional[datetime] = None
    """The date and time the tunnel was last modified."""

    psk_metadata: Optional[PSKMetadata] = None
    """The PSK metadata that includes when the PSK was generated."""

    replay_protection: Optional[bool] = None
    """
    If `true`, then IPsec replay protection will be supported in the
    Cloudflare-to-customer direction.
    """


class IPSECTunnelDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_ipsec_tunnel: Optional[DeletedIPSECTunnel] = None
