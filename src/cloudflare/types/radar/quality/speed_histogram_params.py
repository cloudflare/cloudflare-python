# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SpeedHistogramParams"]


class SpeedHistogramParams(TypedDict, total=False):
    asn: List[str]
    """Array of comma separated list of ASNs, start with `-` to exclude from results.

    For example, `-174, 3356` excludes results from AS174, but includes results from
    AS3356.
    """

    bucket_size: Annotated[int, PropertyInfo(alias="bucketSize")]
    """The width for every bucket in the histogram."""

    continent: List[str]
    """Array of comma separated list of continents (alpha-2 continent codes).

    Start with `-` to exclude from results. For example, `-EU,NA` excludes results
    from Europe, but includes results from North America.
    """

    date_end: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    location: List[str]
    """Array of comma separated list of locations (alpha-2 country codes).

    Start with `-` to exclude from results. For example, `-US,PT` excludes results
    from the US, but includes results from PT.
    """

    metric_group: Annotated[Literal["BANDWIDTH", "LATENCY", "JITTER"], PropertyInfo(alias="metricGroup")]
    """Metrics to be returned."""

    name: List[str]
    """Array of names that will be used to name the series in responses."""
