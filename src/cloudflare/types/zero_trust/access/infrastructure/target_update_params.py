# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TargetUpdateParams", "IP", "IPIPV4", "IPIPV6"]


class TargetUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    hostname: Required[str]
    """A non-unique field that refers to a target.

    Case insensitive, maximum length of 255 characters, supports the use of special
    characters dash and period, does not support spaces, and must start and end with
    an alphanumeric character.
    """

    ip: Required[IP]
    """The IPv4/IPv6 address that identifies where to reach a target"""


class IPIPV4(TypedDict, total=False):
    ip_addr: str
    """IP address of the target"""

    virtual_network_id: str
    """(optional) Private virtual network identifier for the target.

    If omitted, the default virtual network ID will be used.
    """


class IPIPV6(TypedDict, total=False):
    ip_addr: str
    """IP address of the target"""

    virtual_network_id: str
    """(optional) Private virtual network identifier for the target.

    If omitted, the default virtual network ID will be used.
    """


class IP(TypedDict, total=False):
    ipv4: IPIPV4
    """The target's IPv4 address"""

    ipv6: IPIPV6
    """The target's IPv6 address"""
