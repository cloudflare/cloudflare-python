# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["IndicatorListResponse", "Indicator", "Pagination"]


class Indicator(BaseModel):
    id: str

    article_id: str

    article_title: Optional[str] = None

    dataset_id: Optional[str] = None
    """Threat Events dataset identifier for navigating from this indicator.

    Null when the account feeds dataset mapping is unavailable.
    """

    feed_display_name: Optional[str] = None

    feed_id: str

    type: str

    value: str


class Pagination(BaseModel):
    count: int

    cursor: Optional[str] = None

    has_more: bool

    page: int
    """Ordinal of this cursor page; not a total-results offset."""

    per_page: int

    total_count: Optional[int] = None

    total_count_is_exact: bool


class IndicatorListResponse(BaseModel):
    indicators: List[Indicator]

    pagination: Pagination
