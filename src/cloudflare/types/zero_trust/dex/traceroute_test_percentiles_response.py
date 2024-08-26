# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from ..percentiles import Percentiles

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TracerouteTestPercentilesResponse"]

class TracerouteTestPercentilesResponse(BaseModel):
    hops_count: Optional[Percentiles] = FieldInfo(alias = "hopsCount", default = None)

    packet_loss_pct: Optional[Percentiles] = FieldInfo(alias = "packetLossPct", default = None)

    round_trip_time_ms: Optional[Percentiles] = FieldInfo(alias = "roundTripTimeMs", default = None)