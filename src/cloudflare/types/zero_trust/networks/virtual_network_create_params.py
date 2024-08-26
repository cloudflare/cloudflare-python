# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VirtualNetworkCreateParams"]


class VirtualNetworkCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    name: Required[str]
    """A user-friendly name for the virtual network."""

    comment: str
    """Optional remark describing the virtual network."""

    is_default: bool
    """If `true`, this virtual network is the default for the account."""
