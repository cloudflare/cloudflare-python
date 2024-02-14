# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["SeatZeroTrustSeatsUpdateAUserSeatResponse", "SeatZeroTrustSeatsUpdateAUserSeatResponseItem"]


class SeatZeroTrustSeatsUpdateAUserSeatResponseItem(BaseModel):
    access_seat: Optional[bool] = None
    """True if the seat is part of Access."""

    created_at: Optional[datetime] = None

    gateway_seat: Optional[bool] = None
    """True if the seat is part of Gateway."""

    seat_uid: Optional[str] = None
    """Identifier"""

    updated_at: Optional[datetime] = None


SeatZeroTrustSeatsUpdateAUserSeatResponse = List[SeatZeroTrustSeatsUpdateAUserSeatResponseItem]
