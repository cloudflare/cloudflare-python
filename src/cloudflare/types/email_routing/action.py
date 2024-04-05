# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Action"]


class Action(BaseModel):
    type: Literal["drop", "forward", "worker"]
    """Type of supported action."""

    value: List[str]
