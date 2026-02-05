# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .health_check_rate import HealthCheckRate
from .health_check_type import HealthCheckType

__all__ = [
    "GRETunnelGetResponse",
    "GRETunnel",
    "GRETunnelBGP",
    "GRETunnelBGPStatus",
    "GRETunnelHealthCheck",
    "GRETunnelHealthCheckTarget",
    "GRETunnelHealthCheckTargetMagicHealthCheckTarget",
]


class GRETunnelBGP(BaseModel):
    customer_asn: int
    """ASN used on the customer end of the BGP session"""

    extra_prefixes: Optional[List[str]] = None
    """
    Prefixes in this list will be advertised to the customer device, in addition to
    the routes in the Magic routing table.
    """

    md5_key: Optional[str] = None
    """MD5 key to use for session authentication.

    Note that _this is not a security measure_. MD5 is not a valid security
    mechanism, and the key is not treated as a secret value. This is _only_
    supported for preventing misconfiguration, not for defending against malicious
    attacks.

    The MD5 key, if set, must be of non-zero length and consist only of the
    following types of character:

    - ASCII alphanumerics: `[a-zA-Z0-9]`
    - Special characters in the set `'!@#$%^&*()+[]{}<>/.,;:_-~`= \\||`

    In other words, MD5 keys may contain any printable ASCII character aside from
    newline (0x0A), quotation mark (`"`), vertical tab (0x0B), carriage return
    (0x0D), tab (0x09), form feed (0x0C), and the question mark (`?`). Requests
    specifying an MD5 key with one or more of these disallowed characters will be
    rejected.
    """


class GRETunnelBGPStatus(BaseModel):
    state: Literal["BGP_DOWN", "BGP_UP", "BGP_ESTABLISHING"]

    tcp_established: bool

    updated_at: datetime

    bgp_state: Optional[str] = None

    cf_speaker_ip: Optional[str] = None

    cf_speaker_port: Optional[int] = None

    customer_speaker_ip: Optional[str] = None

    customer_speaker_port: Optional[int] = None


class GRETunnelHealthCheckTargetMagicHealthCheckTarget(BaseModel):
    """The destination address in a request type health check.

    After the healthcheck is decapsulated at the customer end of the tunnel, the ICMP echo will be forwarded to this address. This field defaults to `customer_gre_endpoint address`. This field is ignored for bidirectional healthchecks as the interface_address (not assigned to the Cloudflare side of the tunnel) is used as the target.
    """

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


GRETunnelHealthCheckTarget: TypeAlias = Union[GRETunnelHealthCheckTargetMagicHealthCheckTarget, str]


class GRETunnelHealthCheck(BaseModel):
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

    target: Optional[GRETunnelHealthCheckTarget] = None
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


class GRETunnel(BaseModel):
    id: str
    """Identifier"""

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

    automatic_return_routing: Optional[bool] = None
    """
    True if automatic stateful return routing should be enabled for a tunnel, false
    otherwise.
    """

    bgp: Optional[GRETunnelBGP] = None

    bgp_status: Optional[GRETunnelBGPStatus] = None

    created_on: Optional[datetime] = None
    """The date and time the tunnel was created."""

    description: Optional[str] = None
    """An optional description of the GRE tunnel."""

    health_check: Optional[GRETunnelHealthCheck] = None

    interface_address6: Optional[str] = None
    """
    A 127 bit IPV6 prefix from within the virtual_subnet6 prefix space with the
    address being the first IP of the subnet and not same as the address of
    virtual_subnet6. Eg if virtual_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 ,
    interface_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127
    """

    modified_on: Optional[datetime] = None
    """The date and time the tunnel was last modified."""

    mtu: Optional[int] = None
    """Maximum Transmission Unit (MTU) in bytes for the GRE tunnel.

    The minimum value is 576.
    """

    ttl: Optional[int] = None
    """Time To Live (TTL) in number of hops of the GRE tunnel."""


class GRETunnelGetResponse(BaseModel):
    gre_tunnel: Optional[GRETunnel] = None
