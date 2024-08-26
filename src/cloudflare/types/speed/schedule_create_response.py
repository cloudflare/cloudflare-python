# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from .schedule import Schedule

from .pages.test import Test

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ScheduleCreateResponse"]

class ScheduleCreateResponse(BaseModel):
    schedule: Optional[Schedule] = None
    """The test schedule."""

    test: Optional[Test] = None