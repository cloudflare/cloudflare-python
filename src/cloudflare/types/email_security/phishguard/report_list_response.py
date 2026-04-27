# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ReportListResponse", "Fields", "Tag"]


class Fields(BaseModel):
    to: List[str]

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    occurred_at: Optional[datetime] = None

    postfix_id: Optional[str] = None

    ts: Optional[datetime] = None
    """Deprecated, use `occurred_at` instead"""


class Tag(BaseModel):
    category: str

    value: str


class ReportListResponse(BaseModel):
    id: int

    content: str

    disposition: Literal[
        "MALICIOUS", "MALICIOUS-BEC", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "ENCRYPTED", "EXTERNAL", "UNKNOWN", "NONE"
    ]

    fields: Fields

    priority: str

    title: str

    created_at: Optional[datetime] = None

    tags: Optional[List[Tag]] = None

    ts: Optional[datetime] = None
    """Deprecated, use `created_at` instead"""

    updated_at: Optional[datetime] = None
