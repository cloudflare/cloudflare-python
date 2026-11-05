# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Workload"]


class Workload(BaseModel):
    id: str
    """Server-assigned UUID"""

    created_at: datetime

    filter: str
    """Filter expression selecting the requests this workload matches.

    Maximum 4096 UTF-8 bytes.
    """

    name: str
    """Human-readable handle; unique per account."""

    tags: Dict[str, str]
    """Tags attached to this workload"""

    updated_at: datetime

    description: Optional[str] = None
    """Optional free-form description."""
