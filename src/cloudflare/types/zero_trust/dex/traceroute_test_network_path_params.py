# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TracerouteTestNetworkPathParams"]


class TracerouteTestNetworkPathParams(TypedDict, total=False):
    account_id: Required[str]

    device_id: Required[Annotated[str, PropertyInfo(alias="deviceId")]]
    """Device to filter tracroute result runs to"""

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start time for aggregate metrics in ISO ms"""

    interval: Required[Literal["minute", "hour"]]
    """Time interval for aggregate time slots."""

    to: Required[str]
    """End time for aggregate metrics in ISO ms"""
