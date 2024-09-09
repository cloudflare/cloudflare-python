# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Seat"]


class Seat(BaseModel):
    access_seat: Optional[bool] = None
    """True if the seat is part of Access."""

    created_at: Optional[datetime] = None

    gateway_seat: Optional[bool] = None
    """True if the seat is part of Gateway."""

    seat_uid: Optional[str] = None
    """The unique API identifier for the Zero Trust seat."""

    updated_at: Optional[datetime] = None
