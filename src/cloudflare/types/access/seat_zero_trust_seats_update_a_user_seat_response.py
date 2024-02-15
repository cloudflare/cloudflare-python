# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

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
