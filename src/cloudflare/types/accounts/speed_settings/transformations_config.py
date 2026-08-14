# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["TransformationsConfig"]


class TransformationsConfig(BaseModel):
    """A configuration item for a specific zone and feature."""

    id: Optional[str] = None
    """Feature identifier."""

    cf_zone_tag: Optional[str] = None
    """Zone tag identifier."""

    editable: Optional[bool] = None
    """Whether this setting can be modified."""

    modified_on: Optional[datetime] = None
    """When this setting was last modified."""

    value: Optional[str] = None
    """Current value of the feature setting."""
