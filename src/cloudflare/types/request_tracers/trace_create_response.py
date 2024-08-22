# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["TraceCreateResponse"]


class TraceCreateResponse(BaseModel):
    status_code: Optional[int] = None
    """HTTP Status code of zone response"""

    trace: Optional["Trace"] = None


from .trace import Trace

if PYDANTIC_V2:
    TraceCreateResponse.model_rebuild()
else:
    TraceCreateResponse.update_forward_refs()  # type: ignore
