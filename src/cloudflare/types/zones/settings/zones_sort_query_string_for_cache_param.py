# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesSortQueryStringForCacheParam"]


class ZonesSortQueryStringForCacheParam(TypedDict, total=False):
    id: Required[Literal["sort_query_string_for_cache"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""
