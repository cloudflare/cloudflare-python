# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .schedule import Schedule
from ..._models import BaseModel
from .pages.test import Test

__all__ = ["ScheduleCreateResponse"]


class ScheduleCreateResponse(BaseModel):
    schedule: Optional[Schedule] = None
    """The test schedule."""

    test: Optional[Test] = None
