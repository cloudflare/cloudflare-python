# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LivestreamGetAllLivestreamsParams"]


class LivestreamGetAllLivestreamsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Specify the end time range in ISO format to access the live stream."""

    exclude_meetings: bool
    """Exclude the RealtimeKit meetings that are livestreamed."""

    page_no: int
    """The page number from which you want your page search results to be displayed."""

    per_page: int
    """Number of results per page."""

    sort_order: Literal["ASC", "DSC"]
    """Specifies the sorting order for the results."""

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Specify the start time range in ISO format to access the live stream."""

    status: Literal["LIVE", "IDLE", "ERRORED", "INVOKED"]
    """Specifies the status of the operation."""
