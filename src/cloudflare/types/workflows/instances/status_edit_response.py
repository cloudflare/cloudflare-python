# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["StatusEditResponse"]


class StatusEditResponse(BaseModel):
    status: Literal[
        "queued", "running", "paused", "errored", "terminated", "complete", "waitingForPause", "waiting", "unknown"
    ]

    timestamp: datetime
    """In ISO 8601 with no timezone offsets and in UTC."""
