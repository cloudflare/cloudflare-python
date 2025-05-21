# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HostnameEditParams"]


class HostnameEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Specify the identifier of the hostname."""

    description: str
    """Specify an optional description of the hostname."""

    dnslink: str
    """Specify the DNSLink value used if the target is ipfs."""
