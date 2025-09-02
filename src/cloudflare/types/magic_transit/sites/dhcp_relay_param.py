# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["DHCPRelayParam"]


class DHCPRelayParam(TypedDict, total=False):
    server_addresses: SequenceNotStr[str]
    """List of DHCP server IPs."""
