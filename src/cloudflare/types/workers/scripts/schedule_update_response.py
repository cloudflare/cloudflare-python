# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ScheduleUpdateResponse", "Schedule"]


class Schedule(BaseModel):
    created_on: Optional[object] = None

    cron: Optional[object] = None

    modified_on: Optional[object] = None


class ScheduleUpdateResponse(BaseModel):
    schedules: Optional[List[Schedule]] = None
