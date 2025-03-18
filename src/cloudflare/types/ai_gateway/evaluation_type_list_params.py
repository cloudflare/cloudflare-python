# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EvaluationTypeListParams"]


class EvaluationTypeListParams(TypedDict, total=False):
    account_id: Required[str]

    order_by: str

    order_by_direction: Literal["asc", "desc"]

    page: int

    per_page: int
