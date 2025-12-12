# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["InstanceStatsResponse"]


class InstanceStatsResponse(BaseModel):
    completed: Optional[int] = None

    error: Optional[int] = None

    file_embed_errors: Optional[Dict[str, object]] = None

    index_source_errors: Optional[Dict[str, object]] = None

    last_activity: Optional[datetime] = None

    queued: Optional[int] = None

    running: Optional[int] = None

    skipped: Optional[int] = None
