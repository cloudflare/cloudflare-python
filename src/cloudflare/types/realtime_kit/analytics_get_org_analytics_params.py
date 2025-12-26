# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AnalyticsGetOrgAnalyticsParams"]


class AnalyticsGetOrgAnalyticsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    end_date: str
    """end date in YYYY-MM-DD format"""

    start_date: str
    """start date in YYYY-MM-DD format"""
