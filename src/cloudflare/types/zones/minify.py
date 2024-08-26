# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Minify", "Value"]

class Value(BaseModel):
    css: Optional[Literal["on", "off"]] = None
    """Automatically minify all CSS files for your website."""

    html: Optional[Literal["on", "off"]] = None
    """Automatically minify all HTML files for your website."""

    js: Optional[Literal["on", "off"]] = None
    """Automatically minify all JavaScript files for your website."""

class Minify(BaseModel):
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