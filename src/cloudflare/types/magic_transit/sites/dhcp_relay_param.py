# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["DHCPRelayParam"]


class DHCPRelayParam(TypedDict, total=False):
    server_addresses: List[str]
    """List of DHCP server IPs."""
