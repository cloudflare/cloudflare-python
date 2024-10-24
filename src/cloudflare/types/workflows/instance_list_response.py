# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InstanceListResponse"]


class InstanceListResponse(BaseModel):
    id: str

    created_on: datetime

    modified_on: datetime

    status: Literal["queued", "running", "paused", "errored", "terminated", "complete", "waitingForPause", "unknown"]

    version_id: str

    workflow_id: str
