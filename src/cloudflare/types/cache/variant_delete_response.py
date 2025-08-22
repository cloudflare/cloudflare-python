# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VariantDeleteResponse"]


class VariantDeleteResponse(BaseModel):
    id: Literal["variants"]
    """The identifier of the caching setting."""

    editable: bool
    """Whether the setting is editable."""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""
