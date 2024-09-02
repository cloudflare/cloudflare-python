# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from .issue_type import IssueType

from typing_extensions import Literal

from datetime import datetime

from ...shared.response_info import ResponseInfo

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IssueListResponse", "Result", "ResultIssue"]


class ResultIssue(BaseModel):
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


class Result(BaseModel):
    count: Optional[int] = None
    """Total number of results"""

    issues: Optional[List[ResultIssue]] = None

    page: Optional[int] = None
    """Current page within paginated list of results"""

    per_page: Optional[int] = None
    """Number of results per page of results"""


class IssueListResponse(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    success: Literal[True]
    """Whether the API call was successful"""

    result: Optional[Result] = None
