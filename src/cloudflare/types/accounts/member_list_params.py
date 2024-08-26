# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["MemberListParams"]

class MemberListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    direction: Literal["asc", "desc"]
    """Direction to order results."""

    order: Literal["user.first_name", "user.last_name", "user.email", "status"]
    """Field to order results by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""

    status: Literal["accepted", "pending", "rejected"]
    """A member's status in the account."""