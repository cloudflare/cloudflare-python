# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ACLListResponse", "ACL", "ACLLAN1", "ACLLAN2"]


class ACLLAN1(BaseModel):
    lan_id: str
    """The identifier for the LAN you want to create an ACL policy with."""

    lan_name: Optional[str] = None
    """The name of the LAN based on the provided lan_id."""

    ports: Optional[List[int]] = None
    """Array of ports on the provided LAN that will be included in the ACL.

    If no ports are provided, communication on any port on this LAN is allowed.
    """

    subnets: Optional[List[Union[str, str]]] = None
    """Array of subnet IPs within the LAN that will be included in the ACL.

    If no subnets are provided, communication on any subnets on this LAN are
    allowed.
    """


class ACLLAN2(BaseModel):
    lan_id: str
    """The identifier for the LAN you want to create an ACL policy with."""

    lan_name: Optional[str] = None
    """The name of the LAN based on the provided lan_id."""

    ports: Optional[List[int]] = None
    """Array of ports on the provided LAN that will be included in the ACL.

    If no ports are provided, communication on any port on this LAN is allowed.
    """

    subnets: Optional[List[Union[str, str]]] = None
    """Array of subnet IPs within the LAN that will be included in the ACL.

    If no subnets are provided, communication on any subnets on this LAN are
    allowed.
    """


class ACL(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    description: Optional[str] = None
    """Description for the ACL."""

    lan_1: Optional[ACLLAN1] = None

    lan_2: Optional[ACLLAN2] = None

    name: Optional[str] = None
    """The name of the ACL."""

    protocols: Optional[List[Literal["tcp", "udp", "icmp"]]] = None


class ACLListResponse(BaseModel):
    acls: Optional[List[ACL]] = None
