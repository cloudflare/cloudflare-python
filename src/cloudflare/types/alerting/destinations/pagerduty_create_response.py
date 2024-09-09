# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["PagerdutyCreateResponse"]


class PagerdutyCreateResponse(BaseModel):
    id: Optional[str] = None
    """token in form of UUID"""
