# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EvaluationListParams"]


class EvaluationListParams(TypedDict, total=False):
    account_id: Required[str]

    id: str

    name: str

    order_by: str
    """Order By Column Name"""

    order_by_direction: Literal["asc", "desc"]
    """Order By Direction"""

    page: int

    per_page: int

    processed: bool

    search: str
    """Search by id, name"""

    total_logs: float
