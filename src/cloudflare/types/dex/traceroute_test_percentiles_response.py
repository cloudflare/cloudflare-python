# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["TracerouteTestPercentilesResponse", "HopsCount", "PacketLossPct", "RoundTripTimeMs"]


class HopsCount(BaseModel):
    p50: Optional[float] = None
    """p50 observed in the time period"""

    p90: Optional[float] = None
    """p90 observed in the time period"""

    p95: Optional[float] = None
    """p95 observed in the time period"""

    p99: Optional[float] = None
    """p99 observed in the time period"""


class PacketLossPct(BaseModel):
    p50: Optional[float] = None
    """p50 observed in the time period"""

    p90: Optional[float] = None
    """p90 observed in the time period"""

    p95: Optional[float] = None
    """p95 observed in the time period"""

    p99: Optional[float] = None
    """p99 observed in the time period"""


class RoundTripTimeMs(BaseModel):
    p50: Optional[float] = None
    """p50 observed in the time period"""

    p90: Optional[float] = None
    """p90 observed in the time period"""

    p95: Optional[float] = None
    """p95 observed in the time period"""

    p99: Optional[float] = None
    """p99 observed in the time period"""


class TracerouteTestPercentilesResponse(BaseModel):
    hops_count: Optional[HopsCount] = FieldInfo(alias="hopsCount", default=None)

    packet_loss_pct: Optional[PacketLossPct] = FieldInfo(alias="packetLossPct", default=None)

    round_trip_time_ms: Optional[RoundTripTimeMs] = FieldInfo(alias="roundTripTimeMs", default=None)
