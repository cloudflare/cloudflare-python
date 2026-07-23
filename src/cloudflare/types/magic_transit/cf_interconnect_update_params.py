# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .health_check_param import HealthCheckParam

__all__ = ["CfInterconnectUpdateParams", "GRE"]


class CfInterconnectUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    automatic_return_routing: bool
    """
    True if automatic stateful return routing should be enabled for a tunnel, false
    otherwise. Requires the `coupler_integration` account flag to be enabled;
    requests setting this to `true` without that flag will be rejected.
    """

    description: str
    """An optional description of the interconnect."""

    gre: GRE
    """The configuration specific to GRE interconnects."""

    health_check: HealthCheckParam

    interface_address: str
    """The IPv4 interface address for the interconnect.

    For MPLS Interconnects, use a /30 or /31 prefix. For GRE Interconnects, a /29,
    /30, or /31 prefix may be used. A /29 prefix is only allowed for v1.5
    interconnects, and the address must be the .3 host of the subnet (the fourth
    address overall; the network address is not usable). Select the subnet from RFC
    1918 or the approved link-local ranges.
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


class GRE(TypedDict, total=False):
    """The configuration specific to GRE interconnects."""

    cloudflare_endpoint: str
    """
    The IP address assigned to the Cloudflare side of the GRE tunnel created as part
    of the Interconnect.
    """
