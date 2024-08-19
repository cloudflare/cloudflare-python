# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ActivityLogSettings"]


class ActivityLogSettings(BaseModel):
    enabled: Optional[bool] = None
    """Enable activity logging."""
