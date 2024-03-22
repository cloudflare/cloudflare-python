# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ACLCreateParams", "ACL", "ACLLAN1", "ACLLAN2"]


class ACLCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    acl: ACL


class ACLLAN1(TypedDict, total=False):
    lan_id: Required[str]
    """The identifier for the LAN you want to create an ACL policy with."""

    lan_name: str
    """The name of the LAN based on the provided lan_id."""

    ports: Iterable[int]
    """Array of ports on the provided LAN that will be included in the ACL.

    If no ports are provided, communication on any port on this LAN is allowed.
    """

    subnets: List[Union[str, str]]
    """Array of subnet IPs within the LAN that will be included in the ACL.

    If no subnets are provided, communication on any subnets on this LAN are
    allowed.
    """


class ACLLAN2(TypedDict, total=False):
    lan_id: Required[str]
    """The identifier for the LAN you want to create an ACL policy with."""

    lan_name: str
    """The name of the LAN based on the provided lan_id."""

    ports: Iterable[int]
    """Array of ports on the provided LAN that will be included in the ACL.

    If no ports are provided, communication on any port on this LAN is allowed.
    """

    subnets: List[Union[str, str]]
    """Array of subnet IPs within the LAN that will be included in the ACL.

    If no subnets are provided, communication on any subnets on this LAN are
    allowed.
    """


class ACL(TypedDict, total=False):
    lan_1: Required[ACLLAN1]

    lan_2: Required[ACLLAN2]

    name: Required[str]
    """The name of the ACL."""

    description: str
    """Description for the ACL."""

    protocols: List[Literal["tcp", "udp", "icmp"]]
