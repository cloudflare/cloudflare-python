# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BlockSenderGetResponse"]


class BlockSenderGetResponse(BaseModel):
    id: int
    """The unique identifier for the allow policy."""

    created_at: datetime

    is_regex: bool

    last_modified: datetime

    pattern: str

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]

    comments: Optional[str] = None
