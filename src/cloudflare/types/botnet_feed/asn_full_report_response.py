# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ASNFullReportResponse"]


class ASNFullReportResponse(BaseModel):
    cidr: Optional[str] = None

    date: Optional[datetime] = None

    offense_count: Optional[int] = None
