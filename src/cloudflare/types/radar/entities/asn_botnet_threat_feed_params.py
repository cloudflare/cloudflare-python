# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ASNBotnetThreatFeedParams"]


class ASNBotnetThreatFeedParams(TypedDict, total=False):
    asn: SequenceNotStr[str]
    """Filters results by Autonomous System.

    Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list.
    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
    """

    compare_date_range: Annotated[str, PropertyInfo(alias="compareDateRange")]
    """Relative date range for rank change comparison (e.g., "1d", "7d", "30d")."""

    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """The date to retrieve (YYYY-MM-DD format).

    If not specified, returns the most recent available data. Note: This is the date
    the report was generated. The report is generated from information collected
    from the previous day (e.g., the 2026-02-23 entry contains data from
    2026-02-22).
    """

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    location: str
    """Filters results by location. Specify an alpha-2 location code."""

    metric: Literal["OFFENSE_COUNT", "NUMBER_OF_OFFENDING_IPS"]
    """Metric to rank ASNs by."""

    offset: int
    """Skips the specified number of objects before fetching the results."""

    sort_order: Annotated[Literal["ASC", "DESC"], PropertyInfo(alias="sortOrder")]
    """Sort order."""
