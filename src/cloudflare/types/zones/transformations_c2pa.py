# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TransformationsC2pa"]


class TransformationsC2pa(BaseModel):
    """
    Controls C2PA signing for images processed through Cloudflare Image Transformations.
    """

    id: Optional[Literal["image_resizing_c2pa"]] = None
    """ID of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Optional[Literal["on", "off"]] = None
    """Current value of the zone setting."""
