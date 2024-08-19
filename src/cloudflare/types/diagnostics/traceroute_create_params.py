# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TracerouteCreateParams", "Options"]


class TracerouteCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    targets: Required[List[str]]

    colos: List[str]
    """If no source colo names specified, all colos will be used.

    China colos are unavailable for traceroutes.
    """

    options: Options


class Options(TypedDict, total=False):
    max_ttl: int
    """Max TTL."""

    packet_type: Literal["icmp", "tcp", "udp", "gre", "gre+icmp"]
    """Type of packet sent."""

    packets_per_ttl: int
    """Number of packets sent at each TTL."""

    port: int
    """For UDP and TCP, specifies the destination port.

    For ICMP, specifies the initial ICMP sequence value. Default value 0 will choose
    the best value to use for each protocol.
    """

    wait_time: int
    """Set the time (in seconds) to wait for a response to a probe."""
