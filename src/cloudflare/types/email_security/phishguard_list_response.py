# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PhishguardListResponse", "Fields", "Tag"]


class Fields(BaseModel):
    postfix_id: str

    to: List[str]

    ts: datetime

    from_: Optional[str] = FieldInfo(alias="from", default=None)


class Tag(BaseModel):
    category: str

    value: str


class PhishguardListResponse(BaseModel):
    id: int

    content: str

    disposition: Literal[
        "MALICIOUS", "MALICIOUS-BEC", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "ENCRYPTED", "EXTERNAL", "UNKNOWN", "NONE"
    ]

    fields: Fields

    priority: str

    title: str

    ts: datetime

    tags: Optional[List[Tag]] = None
