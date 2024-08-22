# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["InvestigateTraceResponse", "Inbound", "InboundLine", "Outbound", "OutboundLine"]

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

class InvestigateTraceResponse(BaseModel):
    inbound: Inbound

    outbound: Outbound