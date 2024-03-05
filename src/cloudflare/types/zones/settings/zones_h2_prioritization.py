# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ZonesH2Prioritization"]


class ZonesH2Prioritization(BaseModel):
    id: Literal["h2_prioritization"]
    """ID of the zone setting."""

    value: Literal["on", "off", "custom"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
