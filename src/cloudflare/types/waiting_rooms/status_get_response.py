# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StatusGetResponse"]


class StatusGetResponse(BaseModel):
    estimated_queued_users: Optional[int] = None

    estimated_total_active_users: Optional[int] = None

    event_id: Optional[str] = None

    max_estimated_time_minutes: Optional[int] = None

    status: Optional[Literal["event_prequeueing", "not_queueing", "queueing", "suspended"]] = None
