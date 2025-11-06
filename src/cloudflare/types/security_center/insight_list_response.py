# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..intel.attack_surface_report.issue_type import IssueType

__all__ = ["InsightListResponse", "Issue"]


class Issue(BaseModel):
    id: Optional[str] = None

    dismissed: Optional[bool] = None

    issue_class: Optional[str] = None

    issue_type: Optional[IssueType] = None

    payload: Optional[object] = None

    resolve_link: Optional[str] = None

    resolve_text: Optional[str] = None

    severity: Optional[Literal["Low", "Moderate", "Critical"]] = None

    since: Optional[datetime] = None

    subject: Optional[str] = None

    timestamp: Optional[datetime] = None


class InsightListResponse(BaseModel):
    count: Optional[int] = None
    """Total number of results"""

    issues: Optional[List[Issue]] = None

    page: Optional[int] = None
    """Current page within paginated list of results"""

    per_page: Optional[int] = None
    """Number of results per page of results"""
