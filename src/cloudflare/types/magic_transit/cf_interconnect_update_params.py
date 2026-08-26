# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .health_check_rate import HealthCheckRate
from .health_check_type import HealthCheckType

__all__ = [
    "CfInterconnectUpdateParams",
    "BGP",
    "GRE",
    "HealthCheck",
    "HealthCheckTarget",
    "HealthCheckTargetMagicHealthCheckTarget",
]


class CfInterconnectUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    automatic_return_routing: bool
    """
    True if automatic stateful return routing should be enabled for a tunnel, false
    otherwise. Requires the `coupler_integration` account flag to be enabled;
    requests setting this to `true` without that flag will be rejected.
    """

    bgp: BGP

    description: str
    """An optional description of the interconnect."""

    gre: GRE
    """Not configurable for version 1.5 interconnects; supplying it returns an error."""

    health_check: HealthCheck

    interface_address: str
    """The IPv4 interface address for the interconnect.

    For MPLS Interconnects, use a /30 or /31 prefix. For GRE Interconnects, a /30 or
    /31 prefix may be used. Version 1.5 interconnects require a /31 prefix and may
    also use a prefix from the account's authorized prefixes; otherwise, select the
    subnet from RFC 1918 or the approved link-local ranges.
    """

    interface_address6: str
    """
    A 127 bit IPV6 prefix from within the virtual_subnet6 prefix space with the
    address being the first IP of the subnet and not same as the address of
    virtual_subnet6. Eg if virtual_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 ,
    interface_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127
    """

    mtu: int
    """The Maximum Transmission Unit (MTU) in bytes for the interconnect.

    The minimum value is 576.
    """

    name: str
    """The name of the interconnect. The name cannot share a name with other tunnels."""

    x_magic_new_hc_target: Annotated[bool, PropertyInfo(alias="x-magic-new-hc-target")]


class BGP(TypedDict, total=False):
    as_no: int
    """Deprecated. Use customer_asn."""

    cloudflare_endpoint: str
    """Read-only for v1.5; derived from interface_address."""

    customer_asn: int
    """ASN used on the customer end of the BGP session."""

    customer_endpoint: str
    """Read-only for v1.5; derived from interface_address."""

    export_filter_id: str
    """ID of the BGP filter profile applied to routes advertised to the customer."""

    extra_prefixes: SequenceNotStr[str]
    """
    Prefixes in this list will be advertised to the customer device, in addition to
    the routes in the Magic routing table.
    """

    import_filter_id: str
    """ID of the BGP filter profile applied to routes received from the customer."""

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


class GRE(TypedDict, total=False):
    """Not configurable for version 1.5 interconnects; supplying it returns an error."""

    cloudflare_endpoint: str
    """
    The IP address assigned to the Cloudflare side of the GRE tunnel created as part
    of the Interconnect.
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

    Either unidirectional, where the probe comes to you via the interconnect and the
    result comes back to Cloudflare via the open Internet, or bidirectional where
    both the probe and result come and go via the interconnect.
    """

    enabled: bool
    """Determines whether to run healthchecks for a tunnel."""

    rate: HealthCheckRate
    """How frequent the health check is run. The default value is `mid`."""

    source: str
    """The source IPv4 address used for bidirectional health checks.

    Supported only for version 1.5 interconnects. It is required when `direction` is
    `bidirectional` and must be omitted (and is cleared) when `direction` is
    `unidirectional`. The address must be within RFC1918 space, the approved
    link-local range 169.254.240.0/20, or the Cloudflare reserved range
    198.41.199.224/27.
    """

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
