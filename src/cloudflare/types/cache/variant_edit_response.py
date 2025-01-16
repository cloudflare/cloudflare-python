# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VariantEditResponse"]


class VariantEditResponse(BaseModel):
    id: Literal["variants"]
    """ID of the zone setting."""

    editable: bool
    """Whether the setting is editable"""

    value: str
    """The value of the feature"""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""
