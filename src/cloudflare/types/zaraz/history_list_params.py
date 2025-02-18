# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoryListParams"]


class HistoryListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    limit: int
    """Maximum amount of results to list. Default value is 10."""

    offset: int
    """Ordinal number to start listing the results with. Default value is 0."""

    sort_field: Annotated[
        Literal["id", "user_id", "description", "created_at", "updated_at"], PropertyInfo(alias="sortField")
    ]
    """The field to sort by. Default is updated_at."""

    sort_order: Annotated[Literal["DESC", "ASC"], PropertyInfo(alias="sortOrder")]
    """Sorting order. Default is DESC."""
