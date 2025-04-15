# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TimeseriesGroupThreatCategoryParams"]


class TimeseriesGroupThreatCategoryParams(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).

    Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    """

    arc: List[Literal["PASS", "NONE", "FAIL"]]
    """Filters results by ARC (Authenticated Received Chain) validation."""

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

    dkim: List[Literal["PASS", "NONE", "FAIL"]]
    """Filters results by DKIM (DomainKeys Identified Mail) validation status."""

    dmarc: List[Literal["PASS", "NONE", "FAIL"]]
    """
    Filters results by DMARC (Domain-based Message Authentication, Reporting and
    Conformance) validation status.
    """

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    name: List[str]
    """Array of names used to label the series in the response."""

    spf: List[Literal["PASS", "NONE", "FAIL"]]
    """Filters results by SPF (Sender Policy Framework) validation status."""

    tls_version: Annotated[List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]], PropertyInfo(alias="tlsVersion")]
    """Filters results by TLS version."""
