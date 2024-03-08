# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ZonesMinify", "Value"]


class Value(BaseModel):
    css: Optional[Literal["on", "off"]] = None
    """Automatically minify all CSS files for your website."""

    html: Optional[Literal["on", "off"]] = None
    """Automatically minify all HTML files for your website."""

    js: Optional[Literal["on", "off"]] = None
    """Automatically minify all JavaScript files for your website."""


class ZonesMinify(BaseModel):
    id: Literal["minify"]
    """Zone setting identifier."""

    value: Value
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
