# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Annotated

from ....._utils import PropertyInfo

from typing import List, Union

from datetime import datetime

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = ["TimeseriesGroupARCParams"]

class TimeseriesGroupARCParams(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """
    Aggregation interval results should be returned in (for example, in 15 minutes
    or 1 hour intervals). Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    """

    date_end: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateEnd", format = "iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[List[str], PropertyInfo(alias="dateRange")]
    """
    For example, use `7d` and `7dControl` to compare this week with the previous
    week. Use this parameter or set specific start and end dates (`dateStart` and
    `dateEnd` parameters).
    """

    date_start: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateStart", format = "iso8601")]
    """Array of datetimes to filter the start of a series."""

    dkim: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for dkim."""

    dmarc: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for dmarc."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    name: List[str]
    """Array of names that will be used to name the series in responses."""

    spf: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for spf."""

    tls_version: Annotated[List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]], PropertyInfo(alias="tlsVersion")]
    """Filter for tls version."""