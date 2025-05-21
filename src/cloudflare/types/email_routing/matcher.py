# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Matcher"]


class Matcher(BaseModel):
    type: Literal["all", "literal"]
    """Type of matcher."""

    field: Optional[Literal["to"]] = None
    """Field for type matcher."""

    value: Optional[str] = None
    """Value for matcher."""
