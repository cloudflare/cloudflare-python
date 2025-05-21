# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ScheduleGetResponse", "Schedule"]


class Schedule(BaseModel):
    cron: str

    created_on: Optional[str] = None

    modified_on: Optional[str] = None


class ScheduleGetResponse(BaseModel):
    schedules: List[Schedule]
