# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecordingGetRecordingsParams"]


class RecordingGetRecordingsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end time range for which you want to retrieve the meetings.

    The time must be specified in ISO format.
    """

    expired: bool
    """If passed, only shows expired/non-expired recordings on RealtimeKit's bucket"""

    meeting_id: str
    """ID of a meeting. Optional. Will limit results to only this meeting if passed."""

    page_no: float
    """The page number from which you want your page search results to be displayed."""

    per_page: float
    """Number of results per page"""

    search: str
    """The search query string. You can search using the meeting ID or title."""

    sort_by: Literal["invokedTime"]

    sort_order: Literal["ASC", "DESC"]

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The start time range for which you want to retrieve the meetings.

    The time must be specified in ISO format.
    """

    status: List[Literal["INVOKED", "RECORDING", "UPLOADING", "UPLOADED"]]
    """Filter by one or more recording status"""
