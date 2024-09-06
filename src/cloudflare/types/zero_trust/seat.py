# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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
