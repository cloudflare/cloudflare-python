# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HistoryNotificationHistoryListHistoryParams"]


class HistoryNotificationHistoryListHistoryParams(TypedDict, total=False):
    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Limit the returned results to history records older than the specified date.

    This must be a timestamp that conforms to RFC3339.
    """

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Limit the returned results to history records newer than the specified date.

    This must be a timestamp that conforms to RFC3339.
    """
