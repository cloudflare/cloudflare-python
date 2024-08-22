# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SummaryDMARCParams"]


class SummaryDMARCParams(TypedDict, total=False):
    arc: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for arc (Authenticated Received Chain)."""

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

    dkim: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for dkim."""

    encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]]
    """Filter for encrypted emails."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filter for ip version."""

    name: List[str]
    """Array of names that will be used to name the series in responses."""

    spf: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for spf."""
