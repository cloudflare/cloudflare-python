# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .health_check import HealthCheck

__all__ = ["CfInterconnectGetResponse", "Interconnect", "InterconnectBGP", "InterconnectGRE"]


class InterconnectBGP(BaseModel):
    as_no: Optional[int] = None
    """Deprecated. Use customer_asn."""

    cloudflare_endpoint: Optional[str] = None
    """Read-only for v1.5; derived from interface_address."""

    customer_asn: Optional[int] = None
    """ASN used on the customer end of the BGP session."""

    customer_endpoint: Optional[str] = None
    """Read-only for v1.5; derived from interface_address."""

    export_filter_id: Optional[str] = None
    """ID of the BGP filter profile applied to routes advertised to the customer."""

    extra_prefixes: Optional[List[str]] = None
    """
    Prefixes in this list will be advertised to the customer device, in addition to
    the routes in the Magic routing table.
    """

    import_filter_id: Optional[str] = None
    """ID of the BGP filter profile applied to routes received from the customer."""

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


class InterconnectGRE(BaseModel):
    """The configuration specific to GRE interconnects."""

    cloudflare_endpoint: Optional[str] = None
    """
    The IP address assigned to the Cloudflare side of the GRE tunnel created as part
    of the Interconnect.
    """


class Interconnect(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    automatic_return_routing: Optional[bool] = None
    """
    True if automatic stateful return routing should be enabled for a tunnel, false
    otherwise. Requires the `coupler_integration` account flag to be enabled;
    requests setting this to `true` without that flag will be rejected.
    """

    bgp: Optional[InterconnectBGP] = None

    colo_name: Optional[str] = None
    """The name of the interconnect. The name cannot share a name with other tunnels."""

    created_on: Optional[datetime] = None
    """The date and time the tunnel was created."""

    description: Optional[str] = None
    """An optional description of the interconnect."""

    gre: Optional[InterconnectGRE] = None
    """The configuration specific to GRE interconnects."""

    health_check: Optional[HealthCheck] = None

    interface_address: Optional[str] = None
    """The IPv4 interface address for the interconnect.

    For MPLS Interconnects, use a /30 or /31 prefix. For GRE Interconnects, a /29,
    /30, or /31 prefix may be used. A /29 prefix is only allowed for v1.5
    interconnects, and the address must be the .3 host of the subnet (the fourth
    address overall; the network address is not usable). Select the subnet from RFC
    1918 or the approved link-local ranges.
    """

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
    """The Maximum Transmission Unit (MTU) in bytes for the interconnect.

    The minimum value is 576.
    """

    name: Optional[str] = None
    """The name of the interconnect. The name cannot share a name with other tunnels."""

    version: Optional[str] = None
    """Immutable interconnect version configured at creation time. One of:

    - "1"
    - "1.5"
    - "2"
    """

    virtual_port_reservation_id: Optional[str] = None
    """
    An identifier that correlates this interconnect with the corresponding V2 CNI
    interconnect resource.
    """


class CfInterconnectGetResponse(BaseModel):
    interconnect: Optional[Interconnect] = None
