# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RuleDeleteResponse"]


class RuleDeleteResponse(BaseModel):
    errors: List[object]

    messages: List[object]

    success: Literal[True]
    """Whether the API call was successful"""
