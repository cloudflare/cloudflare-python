# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HijackEventsParams"]


class HijackEventsParams(TypedDict, total=False):
    date_end: Annotated[Union[str, datetime], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[
        Literal[
            "1d",
            "2d",
            "7d",
            "14d",
            "28d",
            "12w",
            "24w",
            "52w",
            "1dControl",
            "2dControl",
            "7dControl",
            "14dControl",
            "28dControl",
            "12wControl",
            "24wControl",
        ],
        PropertyInfo(alias="dateRange"),
    ]
    """
    Shorthand date ranges for the last X days - use when you don't need specific
    start and end dates.
    """

    date_start: Annotated[Union[str, datetime], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range (inclusive)."""

    event_id: Annotated[int, PropertyInfo(alias="eventId")]
    """The unique identifier of a event"""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    hijacker_asn: Annotated[int, PropertyInfo(alias="hijackerAsn")]
    """The potential hijacker AS of a BGP hijack event"""

    involved_asn: Annotated[int, PropertyInfo(alias="involvedAsn")]
    """The potential hijacker or victim AS of a BGP hijack event"""

    involved_country: Annotated[str, PropertyInfo(alias="involvedCountry")]
    """The country code of the potential hijacker or victim AS of a BGP hijack event"""

    max_confidence: Annotated[int, PropertyInfo(alias="maxConfidence")]
    """The maximum confidence score to filter events (1-4 low, 5-7 mid, 8+ high)"""

    min_confidence: Annotated[int, PropertyInfo(alias="minConfidence")]
    """The minimum confidence score to filter events (1-4 low, 5-7 mid, 8+ high)"""

    page: int
    """Current page number, starting from 1"""

    per_page: int
    """Number of entries per page"""

    prefix: str
    """The prefix hijacked during a BGP hijack event"""

    sort_by: Annotated[Literal["ID", "TIME", "CONFIDENCE"], PropertyInfo(alias="sortBy")]
    """Sort events by field"""

    sort_order: Annotated[Literal["ASC", "DESC"], PropertyInfo(alias="sortOrder")]
    """Sort order"""

    victim_asn: Annotated[int, PropertyInfo(alias="victimAsn")]
    """The potential victim AS of a BGP hijack event"""
