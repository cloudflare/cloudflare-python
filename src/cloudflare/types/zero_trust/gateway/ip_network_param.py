# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["IPNetworkParam"]

class IPNetworkParam(TypedDict, total=False):
    network: Required[str]
    """The IP address or IP CIDR."""