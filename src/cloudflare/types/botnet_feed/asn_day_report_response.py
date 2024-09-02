# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ASNDayReportResponse"]


class ASNDayReportResponse(BaseModel):
    cidr: Optional[str] = None

    date: Optional[datetime] = None

    offense_count: Optional[int] = None
