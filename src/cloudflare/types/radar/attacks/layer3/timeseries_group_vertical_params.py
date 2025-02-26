# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TimeseriesGroupVerticalParams"]


class TimeseriesGroupVerticalParams(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """
    Aggregation interval results should be returned in (for example, in 15 minutes
    or 1 hour intervals). Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    """

    continent: List[str]
    """Comma-separated list of continents (alpha-2 continent codes).

    Prefix with `-` to exclude continents from results. For example, `-EU,NA`
    excludes results from EU, but includes results from NA.
    """

    date_end: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[List[str], PropertyInfo(alias="dateRange")]
    """Filters results by the specified date range.

    For example, use `7d` and `7dcontrol` to compare this week with the previous
    week. Use this parameter or set specific start and end dates (`dateStart` and
    `dateEnd` parameters).
    """

    date_start: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range."""

    direction: Literal["ORIGIN", "TARGET"]
    """
    Together with the `location` parameter, will apply the filter to origin or
    target location.
    """

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filters results by IP version (Ipv4 vs. IPv6)."""

    limit_per_group: Annotated[int, PropertyInfo(alias="limitPerGroup")]
    """
    Limits the number of objects per group to the top items within the specified
    time range. If there are more items than the limit, the response will include
    the count of items, with any remaining items grouped together under an "other"
    category.
    """

    location: List[str]
    """Comma-separated list of locations (alpha-2 codes).

    Prefix with `-` to exclude locations from results. For example, `-US,PT`
    excludes results from the US, but includes results from PT.
    """

    name: List[str]
    """Array of names used to label the series in the response."""

    normalization: Literal["PERCENTAGE", "MIN0_MAX"]
    """Normalization method applied.

    Refer to
    [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
    """

    protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]]
    """Array of L3/4 attack types."""
