# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .trace import Trace
from ..._models import BaseModel

__all__ = ["TraceCreateResponse"]


class TraceCreateResponse(BaseModel):
    status_code: Optional[int] = None
    """HTTP Status code of zone response"""

    trace: Optional[List[Trace]] = None
