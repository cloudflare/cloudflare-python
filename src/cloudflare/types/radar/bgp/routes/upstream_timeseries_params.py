# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["UpstreamTimeseriesParams"]


class UpstreamTimeseriesParams(TypedDict, total=False):
    date_end: Annotated[Union[str, datetime], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateStart`.
    """

    date_start: Annotated[Union[str, datetime], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateEnd`.
    """

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    ip_version: Annotated[Literal["IPv4", "IPv6"], PropertyInfo(alias="ipVersion")]
    """Address family of the observed paths. Defaults to IPv4."""

    limit: int
    """Number of upstream ASNs to return as separate series, ranked by the first
    bucket.

    Remaining upstreams are grouped into an "OTHER" series. Defaults to 5.
    """
