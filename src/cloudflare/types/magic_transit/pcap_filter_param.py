# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PCAPFilterParam"]


class PCAPFilterParam(TypedDict, total=False):
    destination_address: str
    """The destination IP address of the packet."""

    destination_port: float
    """The destination port of the packet."""

    protocol: float
    """The protocol number of the packet."""

    source_address: str
    """The source IP address of the packet."""

    source_port: float
    """The source port of the packet."""
