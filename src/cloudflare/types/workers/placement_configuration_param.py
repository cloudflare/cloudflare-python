# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PlacementConfigurationParam"]

class PlacementConfigurationParam(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    Only `"smart"` is currently supported
    """