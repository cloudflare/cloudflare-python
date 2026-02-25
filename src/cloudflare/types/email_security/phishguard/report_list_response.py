# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ReportListResponse", "Fields", "Tag"]


class Fields(BaseModel):
    to: List[str]

    ts: datetime

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    postfix_id: Optional[str] = None


class Tag(BaseModel):
    category: str

    value: str


class ReportListResponse(BaseModel):
    id: int

    content: str

    created_at: datetime

    disposition: Literal[
        "MALICIOUS", "MALICIOUS-BEC", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "ENCRYPTED", "EXTERNAL", "UNKNOWN", "NONE"
    ]

    fields: Fields

    priority: str

    title: str

    ts: datetime

    updated_at: datetime

    tags: Optional[List[Tag]] = None
