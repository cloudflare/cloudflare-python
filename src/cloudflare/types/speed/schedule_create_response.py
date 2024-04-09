# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .test import Test
from .schedule import Schedule
from ..._models import BaseModel

__all__ = ["ScheduleCreateResponse"]


class ScheduleCreateResponse(BaseModel):
    schedule: Optional[Schedule] = None
    """The test schedule."""

    test: Optional[Test] = None
