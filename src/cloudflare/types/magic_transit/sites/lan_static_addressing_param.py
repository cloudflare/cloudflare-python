# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .dhcp_relay_param import DHCPRelayParam
from .dhcp_server_param import DHCPServerParam

__all__ = ["LANStaticAddressingParam"]


class LANStaticAddressingParam(TypedDict, total=False):
    address: Required[str]
    """A valid CIDR notation representing an IP range."""

    dhcp_relay: DHCPRelayParam

    dhcp_server: DHCPServerParam

    secondary_address: str
    """A valid CIDR notation representing an IP range."""

    virtual_address: str
    """A valid CIDR notation representing an IP range."""
