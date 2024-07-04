# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IPTimeseriesParams"]


class IPTimeseriesParams(TypedDict, total=False):
    asn: str
    """Comma separated list of ASNs."""

    date_end: Annotated[Union[str, datetime], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[str, PropertyInfo(alias="dateRange")]
    """
    Shorthand date ranges for the last X days - use when you don't need specific
    start and end dates.
    """

    date_start: Annotated[Union[str, datetime], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range (inclusive)."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    include_delay: Annotated[bool, PropertyInfo(alias="includeDelay")]
    """Include data delay meta information"""

    location: str
    """Comma separated list of locations."""

    name: List[str]
    """Array of names that will be used to name the series in responses."""
