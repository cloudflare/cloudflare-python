# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..unnamed_schema_ref_174 import UnnamedSchemaRef174
from ..unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["ConnectionTamperingSummaryResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRef174]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")

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
