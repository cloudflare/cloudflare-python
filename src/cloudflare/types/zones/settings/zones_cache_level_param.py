# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesCacheLevelParam"]


class ZonesCacheLevelParam(TypedDict, total=False):
    id: Required[Literal["cache_level"]]
    """ID of the zone setting."""

    value: Required[Literal["aggressive", "basic", "simplified"]]
    """Current value of the zone setting."""
