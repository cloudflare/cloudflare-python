# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Tag"]


class Tag(BaseModel):
    name: str
    """The name of the tag"""

    app_count: Optional[int] = None
    """The number of applications that have this tag"""

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None
