# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    enabled: Required[bool]
    """Indicates whether zone-level authenticated origin pulls is enabled."""
