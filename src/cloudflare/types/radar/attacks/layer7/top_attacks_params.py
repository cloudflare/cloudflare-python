# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TopAttacksParams"]


class TopAttacksParams(TypedDict, total=False):
    asn: List[str]
    """Comma-separated list of Autonomous System Numbers (ASNs).

    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
    """

    continent: List[str]
    """Comma-separated list of continents (alpha-2 continent codes).

    Prefix with `-` to exclude continents from results. For example, `-EU,NA`
    excludes results from EU, but includes results from NA.
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

    limit: int
    """Limits the number of objects returned in the response."""

    limit_direction: Annotated[Literal["ORIGIN", "TARGET"], PropertyInfo(alias="limitDirection")]
    """Array of attack origin/target location attack limits.

    Together with `limitPerLocation`, limits how many objects will be fetched per
    origin/target location.
    """

    limit_per_location: Annotated[int, PropertyInfo(alias="limitPerLocation")]
    """
    Limits the number of attacks per origin/target (refer to `limitDirection`
    parameter) location.
    """

    location: List[str]
    """Comma-separated list of locations (alpha-2 codes).

    Prefix with `-` to exclude locations from results. For example, `-US,PT`
    excludes results from the US, but includes results from PT.
    """

    magnitude: Literal["AFFECTED_ZONES", "MITIGATED_REQUESTS"]
    """This parameter is deprecated.

    In the future, we will only support attack magnitude defined by the total number
    of mitigated requests (MITIGATED_REQUESTS).
    """

    mitigation_product: Annotated[
        List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ],
        PropertyInfo(alias="mitigationProduct"),
    ]
    """Array of L7 mitigation products."""

    name: List[str]
    """Array of names used to label the series in the response."""

    normalization: Literal["PERCENTAGE", "MIN_MAX"]
    """Normalization method applied.

    Refer to
    [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
    """
