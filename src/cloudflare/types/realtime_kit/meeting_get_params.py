# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MeetingGetParams"]


class MeetingGetParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end time range for which you want to retrieve the meetings.

    The time must be specified in ISO format.
    """

    page_no: float
    """The page number from which you want your page search results to be displayed."""

    per_page: float
    """Number of results per page"""

    search: str
    """The search query string. You can search using the meeting ID or title."""

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The start time range for which you want to retrieve the meetings.

    The time must be specified in ISO format.
    """
