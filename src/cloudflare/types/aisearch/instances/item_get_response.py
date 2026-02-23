# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ItemGetResponse"]


class ItemGetResponse(BaseModel):
    id: float

    checksum: str

    chunks_count: Optional[int] = None

    created_at: datetime

    file_size: Optional[float] = None

    key: str

    last_seen_at: datetime

    namespace: str

    next_action: Optional[Literal["INDEX", "DELETE"]] = None

    status: Literal["queued", "running", "completed", "error", "skipped"]

    error: Optional[str] = None

    public_id: Optional[str] = None
