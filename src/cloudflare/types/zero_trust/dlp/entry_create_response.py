# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .profiles.pattern import Pattern

__all__ = ["EntryCreateResponse"]


class EntryCreateResponse(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    updated_at: datetime

    profile_id: Optional[str] = None
