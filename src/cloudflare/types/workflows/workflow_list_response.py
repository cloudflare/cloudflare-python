# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WorkflowListResponse", "Instances"]


class Instances(BaseModel):
    complete: Optional[float] = None

    errored: Optional[float] = None

    paused: Optional[float] = None

    queued: Optional[float] = None

    running: Optional[float] = None

    terminated: Optional[float] = None

    unknown: Optional[float] = None

    waiting: Optional[float] = None

    waiting_for_pause: Optional[float] = FieldInfo(alias="waitingForPause", default=None)


class WorkflowListResponse(BaseModel):
    id: str

    class_name: str

    created_on: datetime

    instances: Instances

    modified_on: datetime

    name: str

    script_name: str

    triggered_on: Optional[datetime] = None
