# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .pcap_filter import PCAPFilter

__all__ = ["PCAP"]


class PCAP(BaseModel):
    id: Optional[str] = None
    """The ID for the packet capture."""

    filter_v1: Optional[PCAPFilter] = None
    """The packet capture filter. When this field is empty, all packets are captured."""

    offset_time: Optional[datetime] = None
    """The RFC 3339 offset timestamp from which to query backwards for packets.

    Must be within the last 24h. When this field is empty, defaults to time of
    request.
    """

    status: Optional[
        Literal[
            "unknown", "success", "pending", "running", "conversion_pending", "conversion_running", "complete", "failed"
        ]
    ] = None
    """The status of the packet capture request."""

    submitted: Optional[str] = None
    """The RFC 3339 timestamp when the packet capture was created."""

    system: Optional[Literal["magic-transit"]] = None
    """The system used to collect packet captures."""

    time_limit: Optional[float] = None
    """The packet capture duration in seconds."""

    type: Optional[Literal["simple", "full"]] = None
    """The type of packet capture.

    `Simple` captures sampled packets, and `full` captures entire payloads and
    non-sampled packets.
    """
