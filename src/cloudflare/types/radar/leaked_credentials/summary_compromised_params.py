# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SummaryCompromisedParams"]


class SummaryCompromisedParams(TypedDict, total=False):
    bot_class: Annotated[List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]], PropertyInfo(alias="botClass")]
    """Filters results by bot class.

    Refer to
    [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).
    """

    date_end: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[List[str], PropertyInfo(alias="dateRange")]
    """Filters results by the specified date range.

    For example, use `7d` and `7dcontrol` to compare this week with the previous
    week. Use this parameter or set specific start and end dates (`dateStart` and
    `dateEnd` parameters).
    """

    date_start: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    name: List[str]
    """Array of names used to label the series in the response."""
