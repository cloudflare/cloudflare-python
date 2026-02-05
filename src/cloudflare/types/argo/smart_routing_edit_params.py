# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SmartRoutingEditParams"]


class SmartRoutingEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Specifies the zone associated with the API call."""

    value: Required[Literal["on", "off"]]
    """Specifies the enablement value of Argo Smart Routing."""
