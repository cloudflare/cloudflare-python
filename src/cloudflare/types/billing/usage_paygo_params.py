# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsagePaygoParams"]


class UsagePaygoParams(TypedDict, total=False):
    account_id: Required[str]
    """Represents a Cloudflare resource identifier tag."""

    from_: Annotated[Union[str, date], PropertyInfo(alias="from", format="iso8601")]
    """Defines the start date for the usage query (e.g., 2025-02-01)."""

    last_month_period_start: int
    """Specifies the month of the billing period to query (1-12).

    Must be provided together with last_year_period_start. Mutually exclusive with
    from/to.
    """

    last_year_period_start: int
    """Specifies the year of the billing period to query (e.g., 2025).

    Must be provided together with last_month_period_start. Mutually exclusive with
    from/to.
    """

    to: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Defines the end date for the usage query (e.g., 2025-03-01)."""
