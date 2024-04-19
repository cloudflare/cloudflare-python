# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SummaryGetParams"]


class SummaryGetParams(TypedDict, total=False):
    direction: Literal["desc", "asc"]

    order_by: Literal["timestamp", "event_count", "max_risk_level"]

    page: int

    per_page: int
