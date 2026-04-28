# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DHCPServerParam", "DHCPOption"]


class DHCPOption(TypedDict, total=False):
    """A custom DHCP option to include in DHCP responses."""

    code: Required[int]
    """DHCP option number (1-254).

    Options 0 and 255 are reserved by RFC 2132. Options 3, 6, and 51 are not allowed
    because they conflict with connector-managed configuration.
    """

    type: Required[Literal["text", "hex", "ip", "byte", "short", "integer"]]
    """The type of the option value.

    text: a string (max 255 bytes). hex: colon-separated hex bytes (e.g.
    "01:04:aa:bb:cc", max 255 bytes). ip: an IPv4 address (e.g. "10.20.30.40").
    byte: an unsigned integer 0-255 (1 byte). short: an unsigned integer 0-65535 (2
    bytes). integer: an unsigned integer 0-4294967295 (4 bytes).
    """

    value: Required[str]
    """The option value, interpreted according to the type field."""


class DHCPServerParam(TypedDict, total=False):
    dhcp_options: Iterable[DHCPOption]
    """Optional list of custom DHCP options to include in DHCP responses.

    Only valid when DHCP server is enabled.
    """

    dhcp_pool_end: str
    """A valid IPv4 address."""

    dhcp_pool_start: str
    """A valid IPv4 address."""

    dns_server: str
    """A valid IPv4 address."""

    dns_servers: SequenceNotStr[str]

    reservations: Dict[str, str]
    """Mapping of MAC addresses to IP addresses"""
