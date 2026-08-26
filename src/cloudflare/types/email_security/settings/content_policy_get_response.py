# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ContentPolicyGetResponse"]


class ContentPolicyGetResponse(BaseModel):
    """A content policy pattern that matches against the subject or body of an email."""

    id: Optional[str] = None
    """Content policy identifier."""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None

    modified_at: Optional[datetime] = None

    name: Optional[str] = None

    notes: Optional[str] = None

    pattern: Optional[str] = None

    targets: Optional[List[Literal["SUBJECT", "BODY"]]] = None
