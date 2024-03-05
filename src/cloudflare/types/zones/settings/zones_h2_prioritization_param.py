# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesH2PrioritizationParam"]


class ZonesH2PrioritizationParam(TypedDict, total=False):
    id: Required[Literal["h2_prioritization"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off", "custom"]]
    """Current value of the zone setting."""
