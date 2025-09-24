# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SmartShieldUpdateResponse", "SmartTieredCache"]


class SmartTieredCache(BaseModel):
    id: Optional[str] = None
    """The id of the Smart Tiered Cache setting."""

    editable: Optional[bool] = None
    """Whether the setting is editable."""

    modified_on: Optional[str] = None
    """The last time the setting was modified."""

    value: Optional[Literal["on", "off"]] = None
    """Specifies the enablement value of Tiered Cache."""


class SmartShieldUpdateResponse(BaseModel):
    smart_tiered_cache: Optional[SmartTieredCache] = None
