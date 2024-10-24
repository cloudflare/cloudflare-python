# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["InstanceCreateResponse", "InstanceCreateResponseItem"]


class InstanceCreateResponseItem(BaseModel):
    id: str

    status: Literal[
        "queued", "running", "paused", "errored", "terminated", "complete", "waitingForPause", "waiting", "unknown"
    ]

    version_id: str

    workflow_id: str


InstanceCreateResponse: TypeAlias = List[InstanceCreateResponseItem]
