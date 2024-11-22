# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SortQueryStringForCacheParam"]


class SortQueryStringForCacheParam(TypedDict, total=False):
    id: Literal["sort_query_string_for_cache"]
    """Turn on or off the reordering of query strings.

    When query strings have the same structure, caching improves.
    """

    value: Literal["on", "off"]
    """The status of Query String Sort"""
