# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SummaryTaskParams"]


class SummaryTaskParams(TypedDict, total=False):
    date_end: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[List[str], PropertyInfo(alias="dateRange")]
    """
    For example, use `7d` and `7dControl` to compare this week with the previous
    week. Use this parameter or set specific start and end dates (`dateStart` and
    `dateEnd` parameters).
    """

    date_start: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Array of datetimes to filter the start of a series."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit_per_group: Annotated[int, PropertyInfo(alias="limitPerGroup")]
    """
    Limit the number of objects (e.g., browsers, verticals, etc.) to the top items
    within the specified time range. If the limitPerGroup is set, the response will
    include that number of items, with the remaining items grouped together under an
    "other" category.
    """

    name: List[str]
    """Array of names that will be used to name the series in responses."""
