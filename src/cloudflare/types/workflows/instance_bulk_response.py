# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InstanceBulkResponse"]


class InstanceBulkResponse(BaseModel):
    id: str

    status: Literal[
        "queued", "running", "paused", "errored", "terminated", "complete", "waitingForPause", "waiting", "unknown"
    ]

    version_id: str

    workflow_id: str
