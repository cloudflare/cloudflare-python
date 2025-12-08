# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectorCreateParams", "Device"]


class ConnectorCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    device: Required[Device]
    """Exactly one of id, serial_number, or provision_license must be provided."""

    activated: bool

    interrupt_window_duration_hours: float

    interrupt_window_hour_of_day: float

    notes: str

    timezone: str


class Device(TypedDict, total=False):
    """Exactly one of id, serial_number, or provision_license must be provided."""

    id: str

    provision_license: bool
    """When true, create and provision a new licence key for the connector."""

    serial_number: str
