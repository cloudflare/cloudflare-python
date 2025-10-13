# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["LeakedCredentialTimeseriesGroupsV2Params"]


class LeakedCredentialTimeseriesGroupsV2Params(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).

    Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    """

    asn: SequenceNotStr[str]
    """Filters results by Autonomous System.

    Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list.
    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
    """

    bot_class: Annotated[List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]], PropertyInfo(alias="botClass")]
    """Filters results by bot class.

    Refer to
    [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).
    """

    check_result: Annotated[
        List[
            Literal[
                "CLEAN",
                "USERNAME_LEAKED",
                "USERNAME_PASSWORD_SIMILAR",
                "USERNAME_AND_PASSWORD_LEAKED",
                "PASSWORD_LEAKED",
            ]
        ],
        PropertyInfo(alias="checkResult"),
    ]
    """Filters results by leaked credential check result."""

    compromised: List[Literal["CLEAN", "COMPROMISED"]]
    """Filters results by compromised credential status (clean vs. compromised)."""

    continent: SequenceNotStr[str]
    """Filters results by continent.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    continents from results. For example, `-EU,NA` excludes results from EU, but
    includes results from NA.
    """

    date_end: Annotated[SequenceNotStr[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[SequenceNotStr[str], PropertyInfo(alias="dateRange")]
    """Filters results by date range.

    For example, use `7d` and `7dcontrol` to compare this week with the previous
    week. Use this parameter or set specific start and end dates (`dateStart` and
    `dateEnd` parameters).
    """

    date_start: Annotated[SequenceNotStr[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit_per_group: Annotated[int, PropertyInfo(alias="limitPerGroup")]
    """
    Limits the number of objects per group to the top items within the specified
    time range. When item count exceeds the limit, extra items appear grouped under
    an "other" category.
    """

    location: SequenceNotStr[str]
    """Filters results by location.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    locations from results. For example, `-US,PT` excludes results from the US, but
    includes results from PT.
    """

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""

    normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"]
    """Normalization method applied to the results.

    Refer to
    [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
    """
