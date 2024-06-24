# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ConnectionTamperingTimeseriesGroupsResponse",
    "Meta",
    "MetaDateRange",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "Serie0",
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
    agg_interval: str = FieldInfo(alias="aggInterval")

    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")

    last_updated: datetime = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Serie0(BaseModel):
    later_in_flow: List[str]
    """
    Connections matching signatures for tampering later in the connection, after the
    transfer of multiple data packets.
    """

    no_match: List[str]
    """Connections that do not match any tampering signatures."""

    post_ack: List[str]
    """
    Connections matching signatures for tampering after the receipt of a SYN packet
    and ACK packet, meaning the TCP connection was successfully established but the
    server did not receive any subsequent packets.
    """

    post_psh: List[str]
    """
    Connections matching signatures for tampering after the receipt of a packet with
    PSH flag set, following connection establishment.
    """

    post_syn: List[str]
    """
    Connections matching signatures for tampering after the receipt of only a single
    SYN packet, and before the handshake completes.
    """

    timestamps: List[datetime]


class ConnectionTamperingTimeseriesGroupsResponse(BaseModel):
    meta: Meta

    serie_0: Serie0
