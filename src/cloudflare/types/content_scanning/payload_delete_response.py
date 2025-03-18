# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PayloadDeleteResponse"]


class PayloadDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The unique ID for this custom scan expression"""

    payload: Optional[str] = None
    """Ruleset expression to use in matching content objects"""
