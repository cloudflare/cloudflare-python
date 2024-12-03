# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["TraceGetResponse", "Inbound", "InboundLine", "Outbound", "OutboundLine"]


class InboundLine(BaseModel):
    lineno: int

    message: str

    ts: datetime


class Inbound(BaseModel):
    lines: Optional[List[InboundLine]] = None


class OutboundLine(BaseModel):
    lineno: int

    message: str

    ts: datetime


class Outbound(BaseModel):
    lines: Optional[List[OutboundLine]] = None


class TraceGetResponse(BaseModel):
    inbound: Inbound

    outbound: Outbound
