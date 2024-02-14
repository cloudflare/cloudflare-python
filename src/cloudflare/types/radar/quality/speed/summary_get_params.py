# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from typing import List, Union

from datetime import datetime

from ....._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo
from .....types import shared_params

__all__ = ["SummaryGetParams"]


class SummaryGetParams(TypedDict, total=False):
    asn: List[str]
    """Array of comma separated list of ASNs, start with `-` to exclude from results.

    For example, `-174, 3356` excludes results from AS174, but includes results from
    AS3356.
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

    name: List[str]
    """Array of names that will be used to name the series in responses."""
