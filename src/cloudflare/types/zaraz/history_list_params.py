# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Annotated

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["HistoryListParams"]


class HistoryListParams(TypedDict, total=False):
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
