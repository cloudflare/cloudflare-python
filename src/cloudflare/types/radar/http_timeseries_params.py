# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HTTPTimeseriesParams"]


class HTTPTimeseriesParams(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """
    Aggregation interval results should be returned in (for example, in 15 minutes
    or 1 hour intervals). Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    """

    asn: List[str]
    """Array of comma separated list of ASNs, start with `-` to exclude from results.

    For example, `-174, 3356` excludes results from AS174, but includes results from
    AS3356.
    """

    bot_class: Annotated[List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]], PropertyInfo(alias="botClass")]
    """Filter for bot class.

    Refer to
    [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).
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

    device_type: Annotated[List[Literal["DESKTOP", "MOBILE", "OTHER"]], PropertyInfo(alias="deviceType")]
    """Filter for device type."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    http_protocol: Annotated[List[Literal["HTTP", "HTTPS"]], PropertyInfo(alias="httpProtocol")]
    """Filter for http protocol."""

    http_version: Annotated[List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]], PropertyInfo(alias="httpVersion")]
    """Filter for http version."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filter for ip version."""

    location: List[str]
    """Array of comma separated list of locations (alpha-2 country codes).

    Start with `-` to exclude from results. For example, `-US,PT` excludes results
    from the US, but includes results from PT.
    """

    name: List[str]
    """Array of names that will be used to name the series in responses."""

    normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"]
    """Normalization method applied.

    Refer to
    [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
    """

    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]]
    """Filter for os name."""

    tls_version: Annotated[
        List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]], PropertyInfo(alias="tlsVersion")
    ]
    """Filter for tls version."""
