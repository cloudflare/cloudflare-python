# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SentineloneS2sInput"]


class SentineloneS2sInput(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    active_threats: Optional[float] = None
    """The Number of active threats."""

    infected: Optional[bool] = None
    """Whether device is infected."""

    is_active: Optional[bool] = None
    """Whether device is active."""

    network_status: Optional[Literal["connected", "disconnected", "disconnecting", "connecting"]] = None
    """Network status of device."""

    operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = None
    """operator"""
