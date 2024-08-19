# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TCPResetsTimeoutSummaryResponse",
    "Meta",
    "MetaDateRange",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "Summary0",
]


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class MetaConfidenceInfoAnnotation(BaseModel):
    data_source: str = FieldInfo(alias="dataSource")

    description: str

    event_type: str = FieldInfo(alias="eventType")

    is_instantaneous: bool = FieldInfo(alias="isInstantaneous")

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)

    linked_url: Optional[str] = FieldInfo(alias="linkedUrl", default=None)

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[MetaConfidenceInfoAnnotation]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


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

    summary_0: Summary0
