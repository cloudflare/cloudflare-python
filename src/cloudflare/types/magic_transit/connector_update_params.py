# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ConnectorUpdateParams"]


class ConnectorUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    activated: bool

    interrupt_window_days_of_week: List[
        Literal["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    ]
    """Allowed days of the week for upgrades. Default is all days."""

    interrupt_window_duration_hours: float

    interrupt_window_embargo_dates: SequenceNotStr[str]
    """List of dates (YYYY-MM-DD) when upgrades are blocked."""

    interrupt_window_hour_of_day: float

    notes: str

    provision_license: bool
    """When true, regenerate license key for the connector."""

    timezone: str
