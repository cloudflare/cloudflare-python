# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["TimeseriesGroupTimeseriesParams"]


class TimeseriesGroupTimeseriesParams(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).

    Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    When omitted, the interval is auto-selected from the requested date range; finer
    intervals are only available for shorter ranges. If the requested interval is
    too granular for the date range, the request is rejected.
    """

    asn: SequenceNotStr[str]
    """Filters results by Autonomous System.

    Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list.
    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
    """

    content_type: Annotated[
        List[
            Literal[
                "HTML",
                "IMAGES",
                "JSON",
                "JAVASCRIPT",
                "CSS",
                "PLAIN_TEXT",
                "FONTS",
                "XML",
                "YAML",
                "VIDEO",
                "AUDIO",
                "MARKDOWN",
                "DOCUMENTS",
                "BINARY",
                "SERIALIZATION",
                "OTHER",
            ]
        ],
        PropertyInfo(alias="contentType"),
    ]
    """Filters results by content type category.

    When set, results can only be further filtered by location, continent, or
    Autonomous System.
    """

    continent: SequenceNotStr[str]
    """Filters results by continent.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    continents from results. For example, `-EU,NA` excludes results from EU, but
    includes results from NA.
    """

    crawl_purpose: Annotated[SequenceNotStr[str], PropertyInfo(alias="crawlPurpose")]
    """Filters results by bot crawl purpose."""

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

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    industry: SequenceNotStr[str]
    """Filters results by industry."""

    limit_per_group: Annotated[int, PropertyInfo(alias="limitPerGroup")]
    """
    Limits the number of objects per group to the top items within the specified
    time range. When item count exceeds the limit, extra items appear grouped under
    an "other" category. Only supported on high-cardinality dimensions; otherwise
    the request is rejected. Minimum value is 2.
    """

    location: SequenceNotStr[str]
    """Filters results by location.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    locations from results. For example, `-US,PT` excludes results from the US, but
    includes results from PT.
    """

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""

    response_status: Annotated[SequenceNotStr[str], PropertyInfo(alias="responseStatus")]
    """Filters results by HTTP response status code (e.g.

    200, 403, 404). Only
    [IANA-registered codes](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)
    are accepted.
    """

    response_status_category: Annotated[
        List[Literal["INFORMATIONAL", "SUCCESS", "REDIRECTION", "CLIENT_ERROR", "SERVER_ERROR"]],
        PropertyInfo(alias="responseStatusCategory"),
    ]
    """Filters results by HTTP response status code category."""

    user_agent: Annotated[SequenceNotStr[str], PropertyInfo(alias="userAgent")]
    """Filters results by user agent."""

    vertical: SequenceNotStr[str]
    """Filters results by vertical."""
