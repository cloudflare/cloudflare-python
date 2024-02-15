# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["V2ListParams"]


class V2ListParams(TypedDict, total=False):
    continuation_token: Optional[str]
    """Continuation token for a next page. List images V2 returns continuation_token"""

    per_page: float
    """Number of items per page."""

    sort_order: Literal["asc", "desc"]
    """Sorting order by upload time."""
