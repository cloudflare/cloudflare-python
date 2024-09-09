# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPV6NetworkParam"]


class IPV6NetworkParam(TypedDict, total=False):
    network: Required[str]
    """The IPv6 address or IPv6 CIDR."""
