# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TCPResetsTimeoutSummaryResponse",
    "Meta",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "MetaDateRange",
    "MetaUnit",
    "Summary0",
]


class MetaConfidenceInfoAnnotation(BaseModel):
    """Annotation associated with the result (e.g. outage or other type of event)."""

    data_source: Literal[
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
    ] = FieldInfo(alias="dataSource")
    """Data source for annotations."""

    description: str

    end_date: datetime = FieldInfo(alias="endDate")

    event_type: Literal["EVENT", "GENERAL", "OUTAGE", "PARTIAL_PROJECTION", "PIPELINE", "TRAFFIC_ANOMALY"] = FieldInfo(
        alias="eventType"
    )
    """Event type for annotations."""

    is_instantaneous: bool = FieldInfo(alias="isInstantaneous")
    """Whether event is a single point in time or a time range."""

    linked_url: str = FieldInfo(alias="linkedUrl")

    start_date: datetime = FieldInfo(alias="startDate")


class MetaConfidenceInfo(BaseModel):
    annotations: List[MetaConfidenceInfoAnnotation]

    level: int
    """Provides an indication of how much confidence Cloudflare has in the data."""


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class MetaUnit(BaseModel):
    name: str

    value: str


class Meta(BaseModel):
    """Metadata for the results."""

    confidence_info: MetaConfidenceInfo = FieldInfo(alias="confidenceInfo")

    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp of the last dataset update."""

    normalization: Literal[
        "PERCENTAGE",
        "MIN0_MAX",
        "MIN_MAX",
        "RAW_VALUES",
        "PERCENTAGE_CHANGE",
        "ROLLING_AVERAGE",
        "OVERLAPPED_PERCENTAGE",
        "RATIO",
    ]
    """Normalization method applied to the results.

    Refer to
    [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
    """

    units: List[MetaUnit]
    """Measurement units for the results."""


class Summary0(BaseModel):
    later_in_flow: str
    """
    Connection resets within the first 10 packets from the client, but after the
    server has received multiple data packets.
    """

    no_match: str
    """All other connections."""

    post_ack: str
    """
    Connection resets or timeouts after the server received both a SYN packet and an
    ACK packet, meaning the connection was successfully established.
    """

    post_psh: str
    """
    Connection resets or timeouts after the server received a packet with PSH flag
    set, following connection establishment.
    """

    post_syn: str
    """
    Connection resets or timeouts after the server received only a single SYN
    packet.
    """


class TCPResetsTimeoutSummaryResponse(BaseModel):
    meta: Meta
    """Metadata for the results."""

    summary_0: Summary0
