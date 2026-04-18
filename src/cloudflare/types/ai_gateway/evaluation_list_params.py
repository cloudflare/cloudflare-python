# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EvaluationListParams"]


class EvaluationListParams(TypedDict, total=False):
    account_id: Required[str]

    name: str

    page: int

    per_page: int

    processed: bool

    search: str
    """Search by id, name"""
