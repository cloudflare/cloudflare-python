# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .health_check_rate import HealthCheckRate
from .health_check_type import HealthCheckType

__all__ = [
    "IPSECTunnelCreateParams",
    "BGP",
    "HealthCheck",
    "HealthCheckTarget",
    "HealthCheckTargetMagicHealthCheckTarget",
]


class IPSECTunnelCreateParams(TypedDict, total=False):
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

    automatic_return_routing: bool
    """
    True if automatic stateful return routing should be enabled for a tunnel, false
    otherwise.
    """

    bgp: BGP

    customer_endpoint: str
    """The IP address assigned to the customer side of the IPsec tunnel.

    Not required, but must be set for proactive traceroutes to work.
    """

    description: str
    """An optional description forthe IPsec tunnel."""

    health_check: HealthCheck

    interface_address6: str
    """
    A 127 bit IPV6 prefix from within the virtual_subnet6 prefix space with the
    address being the first IP of the subnet and not same as the address of
    virtual_subnet6. Eg if virtual_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 ,
    interface_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127
    """

    psk: str
    """A randomly generated or provided string for use in the IPsec tunnel."""

    replay_protection: bool
    """
    If `true`, then IPsec replay protection will be supported in the
    Cloudflare-to-customer direction.
    """

    x_magic_new_hc_target: Annotated[bool, PropertyInfo(alias="x-magic-new-hc-target")]


class BGP(TypedDict, total=False):
    customer_asn: Required[int]
    """ASN used on the customer end of the BGP session"""

    extra_prefixes: SequenceNotStr[str]
    """
    Prefixes in this list will be advertised to the customer device, in addition to
    the routes in the Magic routing table.
    """

    md5_key: str
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


class HealthCheckTargetMagicHealthCheckTarget(TypedDict, total=False):
    """The destination address in a request type health check.

    After the healthcheck is decapsulated at the customer end of the tunnel, the ICMP echo will be forwarded to this address. This field defaults to `customer_gre_endpoint address`. This field is ignored for bidirectional healthchecks as the interface_address (not assigned to the Cloudflare side of the tunnel) is used as the target.
    """

    saved: str
    """The saved health check target.

    Setting the value to the empty string indicates that the calculated default
    value will be used.
    """


HealthCheckTarget: TypeAlias = Union[HealthCheckTargetMagicHealthCheckTarget, str]


class HealthCheck(TypedDict, total=False):
    direction: Literal["unidirectional", "bidirectional"]
    """The direction of the flow of the healthcheck.

    Either unidirectional, where the probe comes to you via the tunnel and the
    result comes back to Cloudflare via the open Internet, or bidirectional where
    both the probe and result come and go via the tunnel.
    """

    enabled: bool
    """Determines whether to run healthchecks for a tunnel."""

    rate: HealthCheckRate
    """How frequent the health check is run. The default value is `mid`."""

    target: HealthCheckTarget
    """The destination address in a request type health check.

    After the healthcheck is decapsulated at the customer end of the tunnel, the
    ICMP echo will be forwarded to this address. This field defaults to
    `customer_gre_endpoint address`. This field is ignored for bidirectional
    healthchecks as the interface_address (not assigned to the Cloudflare side of
    the tunnel) is used as the target. Must be in object form if the
    x-magic-new-hc-target header is set to true and string form if
    x-magic-new-hc-target is absent or set to false.
    """

    type: HealthCheckType
    """The type of healthcheck to run, reply or request. The default value is `reply`."""
