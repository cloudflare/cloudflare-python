# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from .schedule import Schedule

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ScheduleGetResponse"]


class ScheduleGetResponse(BaseModel):
    schedules: Optional[List[Schedule]] = None
