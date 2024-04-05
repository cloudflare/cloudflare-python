# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MatcherItem"]


class MatcherItem(BaseModel):
    field: Literal["to"]
    """Field for type matcher."""

    type: Literal["literal"]
    """Type of matcher."""

    value: str
    """Value for matcher."""
