# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReportListParams"]


class ReportListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of the time range (RFC3339). Takes precedence over to_date."""

    from_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Deprecated, use `start` instead. Start date in YYYY-MM-DD format."""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of the time range (RFC3339). Takes precedence over from_date."""

    to_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Deprecated, use `end` instead. End date in YYYY-MM-DD format."""
