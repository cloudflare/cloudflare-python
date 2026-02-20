# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["ASPATimeseriesParams"]


class ASPATimeseriesParams(TypedDict, total=False):
    date_end: Annotated[Union[str, datetime], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_start: Annotated[Union[str, datetime], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range (inclusive)."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    location: SequenceNotStr[str]
    """Filters results by location.

    Specify a comma-separated list of alpha-2 location codes.
    """

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""

    rir: List[Literal["RIPE_NCC", "ARIN", "APNIC", "LACNIC", "AFRINIC"]]
    """Filter by Regional Internet Registry (RIR).

    Multiple RIRs generate multiple series.
    """
