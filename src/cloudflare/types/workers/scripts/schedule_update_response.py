# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .unnamed_schema_ref_c8302c265937f9d6f96fd69644e56b26 import UnnamedSchemaRefC8302c265937f9d6f96fd69644e56b26

__all__ = ["ScheduleUpdateResponse"]


class ScheduleUpdateResponse(BaseModel):
    schedules: Optional[List[UnnamedSchemaRefC8302c265937f9d6f96fd69644e56b26]] = None
