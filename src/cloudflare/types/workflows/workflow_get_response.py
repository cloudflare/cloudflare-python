# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WorkflowGetResponse", "Schedule"]


class Schedule(BaseModel):
    cron: str

    next_instance: str


class WorkflowGetResponse(BaseModel):
    id: str

    class_name: str

    created_on: datetime

    instances: Dict[str, float]

    modified_on: datetime

    name: str

    script_name: str

    triggered_on: Optional[datetime] = None

    jurisdiction: Optional[Literal["eu", "fedramp", "us"]] = None
    """Jurisdiction where instances of this workflow run and store data.

    Set when the workflow is created and cannot be changed.
    """

    schedules: Optional[List[Schedule]] = None

    script_deleted: Optional[bool] = None
    """Whether the bound Worker was deleted, leaving this Workflow inactive."""
