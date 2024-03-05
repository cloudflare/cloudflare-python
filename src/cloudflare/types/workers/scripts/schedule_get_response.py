# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ScheduleGetResponse", "Schedule"]


class Schedule(BaseModel):
    created_on: Optional[object] = None

    cron: Optional[object] = None

    modified_on: Optional[object] = None


class ScheduleGetResponse(BaseModel):
    schedules: Optional[List[Schedule]] = None
