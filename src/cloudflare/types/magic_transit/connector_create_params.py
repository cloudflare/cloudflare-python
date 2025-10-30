# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectorCreateParams", "Device"]


class ConnectorCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    device: Required[Device]

    activated: bool

    interrupt_window_duration_hours: float

    interrupt_window_hour_of_day: float

    notes: str

    timezone: str


class Device(TypedDict, total=False):
    id: str

    serial_number: str
