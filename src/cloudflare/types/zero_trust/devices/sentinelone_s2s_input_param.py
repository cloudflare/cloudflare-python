# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SentineloneS2sInputParam"]


class SentineloneS2sInputParam(TypedDict, total=False):
    connection_id: Required[str]
    """Posture Integration ID."""

    active_threats: float
    """The Number of active threats."""

    infected: bool
    """Whether device is infected."""

    is_active: bool
    """Whether device is active."""

    network_status: Literal["connected", "disconnected", "disconnecting", "connecting"]
    """Network status of device."""

    operational_state: Literal[
        "na",
        "partially_disabled",
        "auto_fully_disabled",
        "fully_disabled",
        "auto_partially_disabled",
        "disabled_error",
        "db_corruption",
    ]
    """Agent operational state."""

    operator: Literal["<", "<=", ">", ">=", "=="]
    """operator"""
