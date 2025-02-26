# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SpeedHistogramParams"]


class SpeedHistogramParams(TypedDict, total=False):
    asn: List[str]
    """Comma-separated list of Autonomous System Numbers (ASNs).

    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
    """

    bucket_size: Annotated[int, PropertyInfo(alias="bucketSize")]
    """Width for every bucket in the histogram."""

    continent: List[str]
    """Comma-separated list of continents (alpha-2 continent codes).

    Prefix with `-` to exclude continents from results. For example, `-EU,NA`
    excludes results from EU, but includes results from NA.
    """

    date_end: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    location: List[str]
    """Comma-separated list of locations (alpha-2 codes).

    Prefix with `-` to exclude locations from results. For example, `-US,PT`
    excludes results from the US, but includes results from PT.
    """

    metric_group: Annotated[Literal["BANDWIDTH", "LATENCY", "JITTER"], PropertyInfo(alias="metricGroup")]
    """Metrics to be returned."""

    name: List[str]
    """Array of names used to label the series in the response."""
