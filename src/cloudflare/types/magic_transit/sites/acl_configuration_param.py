# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from .subnet import Subnet

__all__ = ["ACLConfigurationParam"]


class ACLConfigurationParam(TypedDict, total=False):
    lan_id: Required[str]
    """The identifier for the LAN you want to create an ACL policy with."""

    lan_name: str
    """The name of the LAN based on the provided lan_id."""

    port_ranges: List[str]
    """Array of port ranges on the provided LAN that will be included in the ACL.

    If no ports or port rangess are provided, communication on any port on this LAN
    is allowed.
    """

    ports: Iterable[int]
    """Array of ports on the provided LAN that will be included in the ACL.

    If no ports or port ranges are provided, communication on any port on this LAN
    is allowed.
    """

    subnets: List[Subnet]
    """Array of subnet IPs within the LAN that will be included in the ACL.

    If no subnets are provided, communication on any subnets on this LAN are
    allowed.
    """
