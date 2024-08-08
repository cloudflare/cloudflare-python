# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AllowPatternGetResponse"]


class AllowPatternGetResponse(BaseModel):
    id: int

    created_at: datetime

    is_recipient: bool

    is_regex: bool

    is_sender: bool

    is_spoof: bool

    last_modified: datetime

    pattern: str

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]

    verify_sender: bool

    comments: Optional[str] = None
