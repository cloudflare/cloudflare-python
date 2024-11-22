# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SortQueryStringForCache"]


class SortQueryStringForCache(BaseModel):
    id: Optional[Literal["sort_query_string_for_cache"]] = None
    """Turn on or off the reordering of query strings.

    When query strings have the same structure, caching improves.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of Query String Sort"""
