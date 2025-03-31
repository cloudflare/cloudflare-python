# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TCPResetsTimeoutSummaryResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")

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
