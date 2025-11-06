# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RoutePfx2asParams"]


class RoutePfx2asParams(TypedDict, total=False):
    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    longest_prefix_match: Annotated[bool, PropertyInfo(alias="longestPrefixMatch")]
    """Return only results with the longest prefix match for the given prefix.

    For example, specify a /32 prefix to lookup the origin ASN for an IPv4 address.
    """

    origin: int
    """Lookup prefixes originated by the given ASN."""

    prefix: str
    """Network prefix, IPv4 or IPv6."""

    rpki_status: Annotated[Literal["VALID", "INVALID", "UNKNOWN"], PropertyInfo(alias="rpkiStatus")]
    """Return only results with matching rpki status: valid, invalid or unknown."""
