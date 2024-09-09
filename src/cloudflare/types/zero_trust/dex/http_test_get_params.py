# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HTTPTestGetParams"]


class HTTPTestGetParams(TypedDict, total=False):
    account_id: Required[str]

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start time for aggregate metrics in ISO ms"""

    interval: Required[Literal["minute", "hour"]]
    """Time interval for aggregate time slots."""

    to: Required[str]
    """End time for aggregate metrics in ISO ms"""

    colo: str
    """Optionally filter result stats to a Cloudflare colo.

    Cannot be used in combination with deviceId param.
    """

    device_id: Annotated[List[str], PropertyInfo(alias="deviceId")]
    """Optionally filter result stats to a specific device(s).

    Cannot be used in combination with colo param.
    """
