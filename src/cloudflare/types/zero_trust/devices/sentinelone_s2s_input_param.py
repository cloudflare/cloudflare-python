# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

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

    operator: Literal["<", "<=", ">", ">=", "=="]
    """operator"""
