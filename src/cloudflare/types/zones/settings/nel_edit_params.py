# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .zone_setting_nel_param import ZoneSettingNELParam

__all__ = ["NELEditParams"]


class NELEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[ZoneSettingNELParam]
    """Enable Network Error Logging reporting on your zone. (Beta)"""
