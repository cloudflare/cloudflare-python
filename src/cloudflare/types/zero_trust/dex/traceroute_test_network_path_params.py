# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TracerouteTestNetworkPathParams"]


class TracerouteTestNetworkPathParams(TypedDict, total=False):
    account_id: Required[str]

    device_id: Required[Annotated[str, PropertyInfo(alias="deviceId")]]
    """Device to filter tracroute result runs to"""

    interval: Required[Literal["minute", "hour"]]
    """Time interval for aggregate time slots."""

    time_end: Required[Annotated[str, PropertyInfo(alias="timeEnd")]]
    """End time for aggregate metrics in ISO ms"""

    time_start: Required[Annotated[str, PropertyInfo(alias="timeStart")]]
    """Start time for aggregate metrics in ISO ms"""
