# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InstanceListResponse"]


class InstanceListResponse(BaseModel):
    id: str

    created_on: datetime

    ended_on: Optional[datetime] = None

    modified_on: datetime

    started_on: Optional[datetime] = None

    status: Literal[
        "queued", "running", "paused", "errored", "terminated", "complete", "waitingForPause", "waiting", "unknown"
    ]

    version_id: str

    workflow_id: str
