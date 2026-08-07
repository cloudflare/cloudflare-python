# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["PathListParams"]


class PathListParams(TypedDict, total=False):
    collector: str
    """Scope to a single RouteViews collector (e.g.

    "route-views3"). Omit to merge across all active collectors (identical path
    segments are deduplicated, observation counts summed, and every contributing
    collector listed).
    """

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    ip_version: Annotated[Literal["IPv4", "IPv6"], PropertyInfo(alias="ipVersion")]
    """Address family of the observed paths. Defaults to IPv4."""
