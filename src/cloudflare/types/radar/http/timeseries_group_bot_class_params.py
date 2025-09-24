# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["TimeseriesGroupBotClassParams"]


class TimeseriesGroupBotClassParams(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).

    Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    """

    asn: SequenceNotStr[str]
    """Filters results by Autonomous System.

    Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list.
    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
    """

    browser_family: Annotated[List[Literal["CHROME", "EDGE", "FIREFOX", "SAFARI"]], PropertyInfo(alias="browserFamily")]
    """Filters results by browser family."""

    continent: SequenceNotStr[str]
    """Filters results by continent.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    continents from results. For example, `-EU,NA` excludes results from EU, but
    includes results from NA.
    """

    date_end: Annotated[SequenceNotStr[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[SequenceNotStr[str], PropertyInfo(alias="dateRange")]
    """Filters results by date range.

    For example, use `7d` and `7dcontrol` to compare this week with the previous
    week. Use this parameter or set specific start and end dates (`dateStart` and
    `dateEnd` parameters).
    """

    date_start: Annotated[SequenceNotStr[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range."""

    device_type: Annotated[List[Literal["DESKTOP", "MOBILE", "OTHER"]], PropertyInfo(alias="deviceType")]
    """Filters results by device type."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    geo_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="geoId")]
    """Filters results by Geolocation.

    Specify a comma-separated list of GeoNames IDs. Prefix with `-` to exclude
    geoIds from results. For example, `-2267056,360689` excludes results from the
    2267056 (Lisbon), but includes results from 5128638 (New York).
    """

    http_protocol: Annotated[List[Literal["HTTP", "HTTPS"]], PropertyInfo(alias="httpProtocol")]
    """Filters results by HTTP protocol (HTTP vs. HTTPS)."""

    http_version: Annotated[List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]], PropertyInfo(alias="httpVersion")]
    """Filters results by HTTP version."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filters results by IP version (Ipv4 vs. IPv6)."""

    location: SequenceNotStr[str]
    """Filters results by location.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    locations from results. For example, `-US,PT` excludes results from the US, but
    includes results from PT.
    """

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""

    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]]
    """Filters results by operating system."""

    tls_version: Annotated[
        List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]], PropertyInfo(alias="tlsVersion")
    ]
    """Filters results by TLS version."""
