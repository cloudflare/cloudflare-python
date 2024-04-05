# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OriginDNSParam"]


class OriginDNSParam(TypedDict, total=False):
    name: str
    """The name of the DNS record associated with the origin."""

    ttl: int
    """The TTL of our resolution of your DNS record in seconds."""

    type: Literal["", "A", "AAAA", "SRV"]
    """The type of DNS record associated with the origin.

    "" is used to specify a combination of A/AAAA records.
    """
