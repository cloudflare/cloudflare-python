# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ContentPolicyEditResponse"]


class ContentPolicyEditResponse(BaseModel):
    """A content policy pattern that matches against the subject or body of an email."""

    id: Optional[str] = None
    """Content policy identifier."""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Whether the policy is active."""

    modified_at: Optional[datetime] = None

    name: Optional[str] = None
    """Human-readable name of the policy."""

    notes: Optional[str] = None
    """Optional note describing the purpose of the policy."""

    pattern: Optional[str] = None
    """Regular expression the policy matches against."""

    targets: Optional[List[Literal["SUBJECT", "BODY"]]] = None
    """Parts of the email the pattern is matched against."""
