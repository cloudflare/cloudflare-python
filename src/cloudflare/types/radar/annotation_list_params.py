# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AnnotationListParams"]


class AnnotationListParams(TypedDict, total=False):
    asn: int
    """Filters results by Autonomous System.

    Specify a single Autonomous System Number (ASN) as integer.
    """

    data_source: Annotated[
        Literal[
            "ALL",
            "AI_BOTS",
            "AI_GATEWAY",
            "BGP",
            "BOTS",
            "CONNECTION_ANOMALY",
            "CT",
            "DNS",
            "DNS_MAGNITUDE",
            "DNS_AS112",
            "DOS",
            "EMAIL_ROUTING",
            "EMAIL_SECURITY",
            "FW",
            "FW_PG",
            "HTTP",
            "HTTP_CONTROL",
            "HTTP_CRAWLER_REFERER",
            "HTTP_ORIGINS",
            "IQI",
            "LEAKED_CREDENTIALS",
            "NET",
            "ROBOTS_TXT",
            "SPEED",
            "WORKERS_AI",
        ],
        PropertyInfo(alias="dataSource"),
    ]
    """Filters results by data source."""

    date_end: Annotated[Union[str, datetime], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateStart`.
    """

    date_range: Annotated[str, PropertyInfo(alias="dateRange")]
    """Filters results by a relative date range ending at the current time.

    Use `<n>d` for days (up to `364d`) or `<n>w` for weeks (up to `52w`), e.g. `7d`.
    Append `control` to request the equivalent previous period for comparison: the
    comparison window is shifted back by the current window's length rounded up to a
    whole number of weeks, so it keeps the same weekday alignment and does not
    overlap the current window (e.g. `3dcontrol` covers days -10 to -7, `7dcontrol`
    covers days -14 to -7, `28dcontrol` covers days -56 to -28, and `10dcontrol`
    covers days -24 to -14). Mutually exclusive with `dateStart`/`dateEnd`.
    """

    date_start: Annotated[Union[str, datetime], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateEnd`.
    """

    event_type: Annotated[
        Literal["EVENT", "GENERAL", "OUTAGE", "PARTIAL_PROJECTION", "PIPELINE", "TRAFFIC_ANOMALY"],
        PropertyInfo(alias="eventType"),
    ]
    """Filters results by event type."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    location: str
    """Filters results by location. Specify an alpha-2 location code."""

    offset: int
    """Skips the specified number of objects before fetching the results."""

    origin: str
    """Filters results by origin."""
