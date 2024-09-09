# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WANStaticAddressingParam"]


class WANStaticAddressingParam(TypedDict, total=False):
    address: Required[str]
    """A valid CIDR notation representing an IP range."""

    gateway_address: Required[str]
    """A valid IPv4 address."""

    secondary_address: str
    """A valid CIDR notation representing an IP range."""
