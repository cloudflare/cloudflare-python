# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IPTimeseriesParams"]


class IPTimeseriesParams(TypedDict, total=False):
    asn: List[str]
    """Filters results by Autonomous System.

    Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list.
    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
    """

    date_end: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[List[str], PropertyInfo(alias="dateRange")]
    """Filters results by date range.

    For example, use `7d` and `7dcontrol` to compare this week with the previous
    week. Use this parameter or set specific start and end dates (`dateStart` and
    `dateEnd` parameters).
    """

    date_start: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    include_delay: Annotated[bool, PropertyInfo(alias="includeDelay")]
    """Includes data delay meta information."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filters results by IP version (Ipv4 vs. IPv6)."""

    location: List[str]
    """Filters results by location.

    Specify a comma-separated list of alpha-2 location codes.
    """

    name: List[str]
    """Array of names used to label the series in the response."""
