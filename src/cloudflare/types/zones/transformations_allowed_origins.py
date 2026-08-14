# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TransformationsAllowedOrigins"]


class TransformationsAllowedOrigins(BaseModel):
    """Controls which origins are allowed to request image and video transformations."""

    id: Optional[Literal["image_resizing_allowed_origins"]] = None
    """ID of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Optional[Literal["on", "off"]] = None
    """
    Comma-separated list of allowed origin domains for image and video
    transformations. Use "\\**" to allow all origins (default).
    """
