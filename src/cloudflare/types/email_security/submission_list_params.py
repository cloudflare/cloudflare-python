# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubmissionListParams"]


class SubmissionListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    customer_status: Literal["escalated", "reviewed", "unreviewed"]

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end of the search date range. Defaults to `now` if not provided."""

    original_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]

    outcome_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]

    page: int
    """The page number of paginated results."""

    per_page: int
    """The number of results per page."""

    query: Optional[str]

    requested_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The beginning of the search date range. Defaults to `now - 30 days` if not
    provided.
    """

    status: str

    submission_id: str

    type: Literal["TEAM", "USER"]
