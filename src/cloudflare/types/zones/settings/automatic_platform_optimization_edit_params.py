# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .zone_setting_automatic_platform_optimization_param import ZoneSettingAutomaticPlatformOptimizationParam

__all__ = ["AutomaticPlatformOptimizationEditParams"]


class AutomaticPlatformOptimizationEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[ZoneSettingAutomaticPlatformOptimizationParam]
