# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["QuotaListResponse", "Advanced"]


class Advanced(BaseModel):
    allocated: Optional[int] = None
    """Quantity Allocated."""

    used: Optional[int] = None
    """Quantity Used."""


class QuotaListResponse(BaseModel):
    advanced: Optional[Advanced] = None
