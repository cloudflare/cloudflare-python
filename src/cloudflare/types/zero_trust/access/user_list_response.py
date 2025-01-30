# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    id: Optional[str] = None
    """UUID"""

    access_seat: Optional[bool] = None
    """True if the user has authenticated with Cloudflare Access."""

    active_device_count: Optional[float] = None
    """The number of active devices registered to the user."""

    created_at: Optional[datetime] = None

    email: Optional[str] = None
    """The email of the user."""

    gateway_seat: Optional[bool] = None
    """True if the user has logged into the WARP client."""

    last_successful_login: Optional[datetime] = None
    """The time at which the user last successfully logged in."""

    name: Optional[str] = None
    """The name of the user."""

    seat_uid: Optional[str] = None
    """The unique API identifier for the Zero Trust seat."""

    uid: Optional[str] = None
    """The unique API identifier for the user."""

    updated_at: Optional[datetime] = None
