# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["TraceGetResponse", "Inbound", "InboundLine", "Outbound", "OutboundLine"]


class InboundLine(BaseModel):
    lineno: Optional[int] = None
    """Line number in the trace log"""

    logged_at: Optional[datetime] = None

    message: Optional[str] = None

    ts: Optional[str] = None
    """Deprecated, use `logged_at` instead. End of life: November 1, 2026."""


class Inbound(BaseModel):
    lines: Optional[List[InboundLine]] = None

    pending: Optional[bool] = None


class OutboundLine(BaseModel):
    lineno: Optional[int] = None
    """Line number in the trace log"""

    logged_at: Optional[datetime] = None

    message: Optional[str] = None

    ts: Optional[str] = None
    """Deprecated, use `logged_at` instead. End of life: November 1, 2026."""


class Outbound(BaseModel):
    lines: Optional[List[OutboundLine]] = None

    pending: Optional[bool] = None


class TraceGetResponse(BaseModel):
    inbound: Inbound

    outbound: Outbound
