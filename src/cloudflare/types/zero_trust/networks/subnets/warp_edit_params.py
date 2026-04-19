# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WARPEditParams"]


class WARPEditParams(TypedDict, total=False):
    account_id: str
    """Cloudflare account ID"""

    comment: str
    """An optional description of the subnet."""

    is_default_network: bool
    """If `true`, this is the default subnet for the account.

    There can only be one default subnet per account.
    """

    name: str
    """A user-friendly name for the subnet."""

    network: str
    """The private IPv4 or IPv6 range defining the subnet, in CIDR notation."""
