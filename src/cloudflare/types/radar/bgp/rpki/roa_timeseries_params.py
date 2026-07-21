# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["RoaTimeseriesParams"]


class RoaTimeseriesParams(TypedDict, total=False):
    asn: SequenceNotStr[str]
    """Filters results by Autonomous System Number.

    Specify one or more ASNs. Multiple values generate one series per ASN.
    """

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

    location: SequenceNotStr[str]
    """Filters results by location.

    Specify a comma-separated list of alpha-2 location codes.
    """

    metric: Literal[
        "validPfxsRatio", "validPfxsV4Ratio", "validPfxsV6Ratio", "validIpsRatio", "validIpsV4Ratio", "validIpsV6Ratio"
    ]
    """Which RPKI ROA validation metric to return.

    validPfxsRatio = ratio of RPKI-valid prefixes (IPv4+IPv6 combined).
    validPfxsV4Ratio / validPfxsV6Ratio = same, split by IP version. validIpsRatio =
    ratio of RPKI-valid address space (IPv4 /24s + IPv6 /48s). validIpsV4Ratio /
    validIpsV6Ratio = same, split by IP version.
    """

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""
