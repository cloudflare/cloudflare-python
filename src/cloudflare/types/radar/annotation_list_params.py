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
    """End of the date range (inclusive)."""

    date_range: Annotated[str, PropertyInfo(alias="dateRange")]
    """Filters results by date range."""

    date_start: Annotated[Union[str, datetime], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range (inclusive)."""

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
