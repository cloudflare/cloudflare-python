# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConnectorUpdateResponse", "Device"]


class Device(BaseModel):
    id: str

    serial_number: Optional[str] = None


class ConnectorUpdateResponse(BaseModel):
    id: str

    activated: bool

    interrupt_window_duration_hours: float

    interrupt_window_hour_of_day: float

    last_updated: str

    notes: str

    timezone: str

    device: Optional[Device] = None

    last_heartbeat: Optional[str] = None

    last_seen_version: Optional[str] = None
