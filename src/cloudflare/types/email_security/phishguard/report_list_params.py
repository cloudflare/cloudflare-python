# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReportListParams"]


class ReportListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end of the search date range (RFC3339 format)."""

    from_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The beginning of the search date range (RFC3339 format)."""

    to_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
