# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BillingUsageHistoryParams"]


class BillingUsageHistoryParams(TypedDict, total=False):
    account_id: Required[str]

    value_grouping_window: Required[Literal["day", "hour"]]
    """Grouping window for usage data."""

    end_time: Optional[float]
    """End time as Unix timestamp in milliseconds."""

    start_time: Optional[float]
    """Start time as Unix timestamp in milliseconds."""
