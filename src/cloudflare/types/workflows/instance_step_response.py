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

    output: Optional[object] = None
    """Full step output or waitForEvent payload without truncation.

    Sensitive outputs are returned as '[REDACTED]'. Populated when
    status='complete'. May be a ReadableStream when the step returned one from
    step.do; stream outputs are served as application/octet-stream rather than JSON.
    """
