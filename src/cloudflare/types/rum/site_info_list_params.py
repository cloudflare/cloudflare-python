# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["SiteInfoListParams"]


class SiteInfoListParams(TypedDict, total=False):
    order_by: Literal["host", "created"]
    """The property used to sort the list of results."""

    page: float
    """Current page within the paginated list of results."""

    per_page: float
    """Number of items to return per page of results."""
