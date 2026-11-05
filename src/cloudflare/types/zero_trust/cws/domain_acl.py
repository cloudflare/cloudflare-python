# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DomainACL", "Entry"]


class Entry(BaseModel):
    action: Literal["ALLOW", "BLOCK"]
    """Per-domain decision overriding the parent ACL's default_action"""

    domain: str
    """Hostname or domain pattern, capped at 255 UTF-8 bytes"""


class DomainACL(BaseModel):
    id: str
    """Server-assigned UUID"""

    created_at: datetime

    default_action: Literal["ALLOW", "BLOCK"]
    """Action applied when no entry matches the request domain"""

    entries: Optional[List[Entry]] = None
    """Per-domain action overrides. Each domain appears at most once."""

    name: str
    """Human-readable name; unique per account"""

    updated_at: datetime
