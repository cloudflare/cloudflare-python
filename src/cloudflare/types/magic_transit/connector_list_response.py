# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConnectorListResponse", "Device"]


class Device(BaseModel):
    id: str

    serial_number: Optional[str] = None


class ConnectorListResponse(BaseModel):
    id: str

    activated: bool

    interrupt_window_days_of_week: List[
        Literal["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    ]
    """Allowed days of the week for upgrades. Default is all days."""

    interrupt_window_duration_hours: float

    interrupt_window_embargo_dates: List[str]
    """List of dates (YYYY-MM-DD) when upgrades are blocked."""

    interrupt_window_hour_of_day: float

    last_updated: str

    notes: str

    timezone: str

    device: Optional[Device] = None

    last_heartbeat: Optional[str] = None

    last_seen_version: Optional[str] = None

    license_key: Optional[str] = None
