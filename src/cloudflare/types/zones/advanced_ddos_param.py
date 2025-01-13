# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AdvancedDDoSParam"]


class AdvancedDDoSParam(TypedDict, total=False):
    id: Required[Literal["advanced_ddos"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""
