# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ItemListResponse"]


class ItemListResponse(BaseModel):
    id: str

    key: str

    status: Literal["queued", "running", "completed", "error", "skipped"]

    error: Optional[str] = None

    last_seen_at: Optional[datetime] = None

    next_action: Optional[str] = None
