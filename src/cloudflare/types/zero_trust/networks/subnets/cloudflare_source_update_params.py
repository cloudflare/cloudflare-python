# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CloudflareSourceUpdateParams"]


class CloudflareSourceUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    comment: str
    """An optional description of the subnet."""

    name: str
    """A user-friendly name for the subnet."""

    network: str
    """The private IPv4 or IPv6 range defining the subnet, in CIDR notation."""
