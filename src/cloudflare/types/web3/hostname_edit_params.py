# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HostnameEditParams"]


class HostnameEditParams(TypedDict, total=False):
    zone_identifier: Required[str]
    """Identifier"""

    description: str
    """An optional description of the hostname."""

    dnslink: str
    """DNSLink value used if the target is ipfs."""
