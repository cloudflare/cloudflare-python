# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CatchAllAction"]


class CatchAllAction(BaseModel):
    type: Literal["drop", "forward", "worker"]
    """Type of action for catch-all rule."""

    value: Optional[List[str]] = None
