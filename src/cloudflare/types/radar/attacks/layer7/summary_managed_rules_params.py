# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SummaryManagedRulesParams"]


class SummaryManagedRulesParams(TypedDict, total=False):
    asn: List[str]
    """Comma-separated list of Autonomous System Numbers (ASNs).

    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
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

    mitigation_product: Annotated[
        List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ],
        PropertyInfo(alias="mitigationProduct"),
    ]
    """Array of L7 mitigation products."""

    name: List[str]
    """Array of names used to label the series in the response."""
