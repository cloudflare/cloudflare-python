# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LivestreamGetLivestreamAnalyticsDaywiseParams"]


class LivestreamGetLivestreamAnalyticsDaywiseParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    end_time: int
    """
    Specify the end time as a Unix timestamp in seconds to access the livestream
    analytics.
    """

    filters: str
    """Optional filters for livestream analytics."""

    start_time: int
    """
    Specify the start time as a Unix timestamp in seconds to access the livestream
    analytics.
    """
