# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["TopVerticalParams"]


class TopVerticalParams(TypedDict, total=False):
    asn: SequenceNotStr[str]
    """Filters results by Autonomous System.

    Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list.
    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
    """

    continent: SequenceNotStr[str]
    """Filters results by continent.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    continents from results. For example, `-EU,NA` excludes results from EU, but
    includes results from NA.
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

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    http_method: Annotated[
        List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ],
        PropertyInfo(alias="httpMethod"),
    ]
    """Filters results by HTTP method."""

    http_version: Annotated[List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]], PropertyInfo(alias="httpVersion")]
    """Filters results by HTTP version."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filters results by IP version (Ipv4 vs. IPv6)."""

    limit: int
    """Limits the number of objects returned in the response."""

    location: SequenceNotStr[str]
    """Filters results by location.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    locations from results. For example, `-US,PT` excludes results from the US, but
    includes results from PT.
    """

    mitigation_product: Annotated[
        List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ],
        PropertyInfo(alias="mitigationProduct"),
    ]
    """Filters the results by layer 7 mitigation product."""

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""
