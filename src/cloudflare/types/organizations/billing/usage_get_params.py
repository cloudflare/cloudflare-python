# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UsageGetParams"]


class UsageGetParams(TypedDict, total=False):
    from_: Annotated[Union[str, date], PropertyInfo(alias="from", format="iso8601")]
    """Start date for the usage query (ISO 8601).

    Required if `to` is set. When omitted along with `to`, defaults to the start of
    the current month. Filters by charge period (when consumption happened), not
    billing period. The maximum date range is 31 days.
    """

    metric: str
    """Filter results by billable metric id (e.g., workers_standard_requests)."""

    to: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """End date for the usage query (ISO 8601).

    Required if `from` is set. When omitted along with `from`, defaults to today.
    Filters by charge period (when consumption happened), not billing period. The
    maximum date range is 31 days.
    """
