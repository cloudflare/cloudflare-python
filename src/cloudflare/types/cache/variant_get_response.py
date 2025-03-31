# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["VariantGetResponse"]


class VariantGetResponse(BaseModel):
    id: object

    editable: bool
    """Whether the setting is editable"""

    value: str
    """The value of the feature"""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""
