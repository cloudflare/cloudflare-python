# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RequestListParams"]


class RequestListParams(TypedDict, total=False):
    page: Required[int]
    """Page number of results"""

    per_page: Required[int]
    """Number of results per page"""

    completed_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Retrieve requests completed after this time"""

    completed_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Retrieve requests completed before this time"""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Retrieve requests created after this time"""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Retrieve requests created before this time"""

    request_type: str
    """Requested information from request"""

    sort_by: str
    """Field to sort results by"""

    sort_order: Literal["asc", "desc"]
    """Sort order (asc or desc)"""

    status: Literal["open", "accepted", "reported", "approved", "completed", "declined"]
    """Request Status"""
