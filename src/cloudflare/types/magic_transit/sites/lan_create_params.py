# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from .nat_param import NatParam

from typing import Iterable

from .routed_subnet_param import RoutedSubnetParam

from .lan_static_addressing_param import LANStaticAddressingParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["LANCreateParams"]

class LANCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    physport: Required[int]

    vlan_tag: Required[int]
    """VLAN port number."""

    ha_link: bool
    """mark true to use this LAN for HA probing.

    only works for site with HA turned on. only one LAN can be set as the ha_link.
    """

    name: str

    nat: NatParam

    routed_subnets: Iterable[RoutedSubnetParam]

    static_addressing: LANStaticAddressingParam
    """
    If the site is not configured in high availability mode, this configuration is
    optional (if omitted, use DHCP). However, if in high availability mode,
    static_address is required along with secondary and virtual address.
    """