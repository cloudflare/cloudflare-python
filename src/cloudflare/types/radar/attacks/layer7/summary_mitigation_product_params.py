# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SummaryMitigationProductParams"]


class SummaryMitigationProductParams(TypedDict, total=False):
    asn: List[str]
    """Array of comma separated list of ASNs, start with `-` to exclude from results.

    For example, `-174, 3356` excludes results from AS174, but includes results from
    AS3356.
    """

    continent: List[str]
    """Array of comma separated list of continents (alpha-2 continent codes).

    Start with `-` to exclude from results. For example, `-EU,NA` excludes results
    from Europe, but includes results from North America.
    """

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
    """Filter for http method."""

    http_version: Annotated[List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]], PropertyInfo(alias="httpVersion")]
    """Filter for http version."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filter for ip version."""

    limit_per_group: Annotated[int, PropertyInfo(alias="limitPerGroup")]
    """
    Limit the number of objects (e.g., browsers, verticals, etc.) to the top items
    within the specified time range. If the limitPerGroup is set, the response will
    include that number of items, with the remaining items grouped together under an
    "other" category.
    """

    location: List[str]
    """Array of comma separated list of locations (alpha-2 country codes).

    Start with `-` to exclude from results. For example, `-US,PT` excludes results
    from the US, but includes results from PT.
    """

    name: List[str]
    """Array of names that will be used to name the series in responses."""
