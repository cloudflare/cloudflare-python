# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..percentiles import Percentiles

__all__ = ["TracerouteTestPercentilesResponse"]


class TracerouteTestPercentilesResponse(BaseModel):
    hops_count: Optional[Percentiles] = FieldInfo(alias="hopsCount", default=None)

    packet_loss_pct: Optional[Percentiles] = FieldInfo(alias="packetLossPct", default=None)

    round_trip_time_ms: Optional[Percentiles] = FieldInfo(alias="roundTripTimeMs", default=None)
