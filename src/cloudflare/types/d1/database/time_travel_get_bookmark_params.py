# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TimeTravelGetBookmarkParams"]


class TimeTravelGetBookmarkParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """An optional ISO 8601 timestamp.

    If provided, returns the nearest available bookmark at or before this timestamp.
    If omitted, returns the current bookmark.
    """
