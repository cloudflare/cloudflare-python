# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..unnamed_schema_ref_b5f3bd1840490bc487ffef84567807b1 import UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1
from ..unnamed_schema_ref_baac9d7da12de53e99142f8ecd3982e5 import UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5

__all__ = ["ConnectionTamperingSummaryResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5] = FieldInfo(alias="dateRange")

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
