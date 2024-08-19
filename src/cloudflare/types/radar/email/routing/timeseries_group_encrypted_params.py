# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TimeseriesGroupEncryptedParams"]


class TimeseriesGroupEncryptedParams(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """
    Aggregation interval results should be returned in (for example, in 15 minutes
    or 1 hour intervals). Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    """

    arc: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for arc (Authenticated Received Chain)."""

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

    dkim: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for dkim."""

    dmarc: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for dmarc."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filter for ip version."""

    name: List[str]
    """Array of names that will be used to name the series in responses."""

    spf: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for spf."""
