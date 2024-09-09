# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RiskScoringGetResponse", "Event"]


class Event(BaseModel):
    id: str

    name: str

    risk_level: Literal["low", "medium", "high"]

    timestamp: datetime

    event_details: Optional[object] = None


class RiskScoringGetResponse(BaseModel):
    email: str

    events: List[Event]

    name: str

    last_reset_time: Optional[datetime] = None

    risk_level: Optional[Literal["low", "medium", "high"]] = None
