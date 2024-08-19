# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CatchAllMatcher"]


class CatchAllMatcher(BaseModel):
    type: Literal["all"]
    """Type of matcher. Default is 'all'."""
