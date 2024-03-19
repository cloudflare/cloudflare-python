# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..observatory_schedule import ObservatorySchedule
from .observatory_page_test import ObservatoryPageTest

__all__ = ["ScheduleCreateResponse"]


class ScheduleCreateResponse(BaseModel):
    schedule: Optional[ObservatorySchedule] = None
    """The test schedule."""

    test: Optional[ObservatoryPageTest] = None
