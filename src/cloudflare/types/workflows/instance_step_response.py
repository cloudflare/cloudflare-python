# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InstanceStepResponse", "Error"]


class Error(BaseModel):
    """Error details when status='errored'; null otherwise."""

    message: str

    name: str


class InstanceStepResponse(BaseModel):
    error: Optional[Error] = None
    """Error details when status='errored'; null otherwise."""

    status: Literal[
        "queued", "running", "paused", "errored", "terminated", "complete", "waitingForPause", "waiting", "rollingBack"
    ]

    event_type: Optional[str] = None
    """The event type the step is waiting on, as supplied to step.waitForEvent.

    Only present when type='waitForEvent'.
    """

    output: Optional[object] = None
    """Contains the full step output or waitForEvent payload without truncation.

    Uses '[REDACTED]' for sensitive outputs. Contains a value when
    status='complete'. May contain a ReadableStream when step.do returns one; the
    response serves stream outputs as application/octet-stream rather than JSON.
    """
