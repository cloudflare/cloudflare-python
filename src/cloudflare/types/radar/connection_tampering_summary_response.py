# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ConnectionTamperingSummaryResponse",
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
    Connections matching signatures for tampering later in the connection, after the
    transfer of multiple data packets.
    """

    no_match: str
    """Connections that do not match any tampering signatures."""

    post_ack: str
    """
    Connections matching signatures for tampering after the receipt of a SYN packet
    and ACK packet, meaning the TCP connection was successfully established but the
    server did not receive any subsequent packets.
    """

    post_psh: str
    """
    Connections matching signatures for tampering after the receipt of a packet with
    PSH flag set, following connection establishment.
    """

    post_syn: str
    """
    Connections matching signatures for tampering after the receipt of only a single
    SYN packet, and before the handshake completes.
    """


class ConnectionTamperingSummaryResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
