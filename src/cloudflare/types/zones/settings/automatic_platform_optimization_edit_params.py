# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .zones_automatic_platform_optimization_param import ZonesAutomaticPlatformOptimizationParam

__all__ = ["AutomaticPlatformOptimizationEditParams"]


class AutomaticPlatformOptimizationEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[ZonesAutomaticPlatformOptimizationParam]
