# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["TrustedDomainGetResponse"]


class TrustedDomainGetResponse(BaseModel):
    id: int

    created_at: datetime

    is_recent: bool

    is_regex: bool

    is_similarity: bool

    last_modified: datetime

    pattern: str

    comments: Optional[str] = None
