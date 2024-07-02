# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DevelopmentMode"]


class DevelopmentMode(BaseModel):
    id: Literal["development_mode"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    time_remaining: Optional[float] = None
    """
    Value of the zone setting. Notes: The interval (in seconds) from when
    development mode expires (positive integer) or last expired (negative integer)
    for the domain. If development mode has never been enabled, this value is false.
    """
