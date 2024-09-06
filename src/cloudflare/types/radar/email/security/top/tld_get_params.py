# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Annotated

from typing import List, Union

from datetime import datetime

from ......_utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ......_types import FileTypes
from ......_utils import PropertyInfo

__all__ = ["TldGetParams"]


class TldGetParams(TypedDict, total=False):
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

    dmarc: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for dmarc."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit: int
    """Limit the number of objects in the response."""

    name: List[str]
    """Array of names that will be used to name the series in responses."""

    spf: List[Literal["PASS", "NONE", "FAIL"]]
    """Filter for spf."""

    tld_category: Annotated[Literal["CLASSIC", "COUNTRY"], PropertyInfo(alias="tldCategory")]
    """Filter for TLDs by category."""

    tls_version: Annotated[List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]], PropertyInfo(alias="tlsVersion")]
    """Filter for tls version."""
