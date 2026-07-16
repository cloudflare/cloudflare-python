# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["TimeseriesGroupARCParams"]


class TimeseriesGroupARCParams(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).

    Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    When omitted, the interval is auto-selected from the requested date range; finer
    intervals are only available for shorter ranges. If the requested interval is
    too granular for the date range, the request is rejected.
    """

    date_end: Annotated[SequenceNotStr[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateStart`. When requesting
    comparison series, every series must resolve to the same duration as the main
    series. Each `dateStart`/`dateEnd` is floored to the nearest 15 minutes before
    evaluation, so windows whose durations match only before alignment may be
    rejected.
    """

    date_range: Annotated[SequenceNotStr[str], PropertyInfo(alias="dateRange")]
    """
    Filters results by relative date range ending at the current time, with each
    value producing a separate series. Use `<n>d` for days (up to `364d`) or `<n>w`
    for weeks (up to `52w`). Append `control` to request the equivalent previous
    period for comparison: the comparison window is shifted back by the current
    window's length rounded up to a whole number of weeks, so it keeps the same
    weekday alignment and does not overlap the current window (e.g. `7dcontrol`
    covers days -14 to -7, `10dcontrol` covers days -24 to -14). For example, pass
    `7d` and `7dcontrol` to compare this week with the previous week. All series
    must resolve to the same duration as the main series; relative ranges (including
    `control`) satisfy this automatically. Use this parameter or set specific start
    and end dates (`dateStart` and `dateEnd` parameters).
    """

    date_start: Annotated[SequenceNotStr[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range.

    Alternative to `dateRange`; provide together with `dateEnd`. When requesting
    comparison series, every series must resolve to the same duration as the main
    series. Each `dateStart`/`dateEnd` is floored to the nearest 15 minutes before
    evaluation, so windows whose durations match only before alignment may be
    rejected.
    """

    dkim: List[Literal["PASS", "NONE", "FAIL"]]
    """Filters results by DKIM (DomainKeys Identified Mail) validation status."""

    dmarc: List[Literal["PASS", "NONE", "FAIL"]]
    """
    Filters results by DMARC (Domain-based Message Authentication, Reporting and
    Conformance) validation status.
    """

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""

    spf: List[Literal["PASS", "NONE", "FAIL"]]
    """Filters results by SPF (Sender Policy Framework) validation status."""

    tls_version: Annotated[List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]], PropertyInfo(alias="tlsVersion")]
    """Filters results by TLS version."""
