# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["WorkflowListResponse", "Schedule"]


class Schedule(BaseModel):
    cron: str

    next_instance: str


class WorkflowListResponse(BaseModel):
    id: str

    class_name: str

    created_on: datetime

    instances: Dict[str, float]

    modified_on: datetime

    name: str

    script_name: str

    triggered_on: Optional[datetime] = None

    schedules: Optional[List[Schedule]] = None
