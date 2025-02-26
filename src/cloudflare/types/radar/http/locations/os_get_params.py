# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["OSGetParams"]


class OSGetParams(TypedDict, total=False):
    asn: List[str]
    """Comma-separated list of Autonomous System Numbers (ASNs).

    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
    """

    bot_class: Annotated[List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]], PropertyInfo(alias="botClass")]
    """Filters results by bot class.

    Refer to
    [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).
    """

    browser_family: Annotated[List[Literal["CHROME", "EDGE", "FIREFOX", "SAFARI"]], PropertyInfo(alias="browserFamily")]
    """Filters results by browser family."""

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

    device_type: Annotated[List[Literal["DESKTOP", "MOBILE", "OTHER"]], PropertyInfo(alias="deviceType")]
    """Filters results by device type."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    http_protocol: Annotated[List[Literal["HTTP", "HTTPS"]], PropertyInfo(alias="httpProtocol")]
    """Filters results by HTTP protocol (HTTP vs. HTTPS)."""

    http_version: Annotated[List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]], PropertyInfo(alias="httpVersion")]
    """Filters results by HTTP version."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filters results by IP version (Ipv4 vs. IPv6)."""

    limit: int
    """Limits the number of objects returned in the response."""

    location: List[str]
    """Comma-separated list of locations (alpha-2 codes).

    Prefix with `-` to exclude locations from results. For example, `-US,PT`
    excludes results from the US, but includes results from PT.
    """

    name: List[str]
    """Array of names used to label the series in the response."""

    tls_version: Annotated[
        List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]], PropertyInfo(alias="tlsVersion")
    ]
    """Filters results by TLS version."""
