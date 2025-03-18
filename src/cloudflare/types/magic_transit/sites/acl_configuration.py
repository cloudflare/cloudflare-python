# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .subnet import Subnet
from ...._models import BaseModel

__all__ = ["ACLConfiguration"]


class ACLConfiguration(BaseModel):
    lan_id: str
    """The identifier for the LAN you want to create an ACL policy with."""

    lan_name: Optional[str] = None
    """The name of the LAN based on the provided lan_id."""

    port_ranges: Optional[List[str]] = None
    """Array of port ranges on the provided LAN that will be included in the ACL.

    If no ports or port rangess are provided, communication on any port on this LAN
    is allowed.
    """

    ports: Optional[List[int]] = None
    """Array of ports on the provided LAN that will be included in the ACL.

    If no ports or port ranges are provided, communication on any port on this LAN
    is allowed.
    """

    subnets: Optional[List[Subnet]] = None
    """Array of subnet IPs within the LAN that will be included in the ACL.

    If no subnets are provided, communication on any subnets on this LAN are
    allowed.
    """
