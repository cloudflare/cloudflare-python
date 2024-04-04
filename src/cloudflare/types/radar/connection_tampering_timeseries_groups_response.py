# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..unnamed_schema_ref_b5f3bd1840490bc487ffef84567807b1 import UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1
from ..unnamed_schema_ref_baac9d7da12de53e99142f8ecd3982e5 import UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5

__all__ = ["ConnectionTamperingTimeseriesGroupsResponse", "Meta", "MetaConfidenceInfo", "Serie0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    agg_interval: str = FieldInfo(alias="aggInterval")

    date_range: List[UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5] = FieldInfo(alias="dateRange")

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
