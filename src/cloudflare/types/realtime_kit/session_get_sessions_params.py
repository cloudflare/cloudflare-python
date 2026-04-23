# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SessionGetSessionsParams"]


class SessionGetSessionsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    associated_id: str
    """ID of the meeting that sessions should be associated with"""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end time range for which you want to retrieve the meetings.

    The time must be specified in ISO format.
    """

    page_no: float
    """The page number from which you want your page search results to be displayed."""

    participants: str

    per_page: float
    """Number of results per page"""

    search: str
    """
    Search string that matches sessions based on meeting title, meeting ID, and
    session ID
    """

    sort_by: Literal["minutesConsumed", "createdAt"]

    sort_order: Literal["ASC", "DESC"]

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The start time range for which you want to retrieve the meetings.

    The time must be specified in ISO format.
    """

    status: Literal["LIVE", "ENDED"]
