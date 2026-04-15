# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["ItemListResponse"]


class ItemListResponse(BaseModel):
    id: str

    checksum: str

    chunks_count: Optional[int] = None

    created_at: datetime

    file_size: Optional[float] = None

    key: str

    last_seen_at: datetime

    namespace: str

    next_action: Optional[Literal["INDEX", "DELETE"]] = None

    source_id: Optional[str] = None
    """Identifies which data source this item belongs to.

    "builtin" for uploaded files, "{type}:{source}" for external sources, null for
    legacy items.
    """

    status: Literal["queued", "running", "completed", "error", "skipped", "outdated"]

    error: Optional[str] = None
