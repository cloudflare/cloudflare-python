# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["TargetBulkUpdateParams", "Body", "BodyIP", "BodyIPIPV4", "BodyIPIPV6"]


class TargetBulkUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    body: Required[Iterable[Body]]


class BodyIPIPV4(TypedDict, total=False):
    ip_addr: str
    """IP address of the target"""

    virtual_network_id: str
    """(optional) Private virtual network identifier for the target.

    If omitted, the default virtual network ID will be used.
    """


class BodyIPIPV6(TypedDict, total=False):
    ip_addr: str
    """IP address of the target"""

    virtual_network_id: str
    """(optional) Private virtual network identifier for the target.

    If omitted, the default virtual network ID will be used.
    """


class BodyIP(TypedDict, total=False):
    ipv4: BodyIPIPV4
    """The target's IPv4 address"""

    ipv6: BodyIPIPV6
    """The target's IPv6 address"""


class Body(TypedDict, total=False):
    hostname: Required[str]
    """A non-unique field that refers to a target.

    Case insensitive, maximum length of 255 characters, supports the use of special
    characters dash and period, does not support spaces, and must start and end with
    an alphanumeric character.
    """

    ip: Required[BodyIP]
    """The IPv4/IPv6 address that identifies where to reach a target"""
