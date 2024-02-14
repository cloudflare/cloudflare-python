# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["StatusWaitingRoomGetWaitingRoomStatusResponse"]


class StatusWaitingRoomGetWaitingRoomStatusResponse(BaseModel):
    estimated_queued_users: Optional[int] = None

    estimated_total_active_users: Optional[int] = None

    event_id: Optional[str] = None

    max_estimated_time_minutes: Optional[int] = None

    status: Optional[Literal["event_prequeueing", "not_queueing", "queueing"]] = None
