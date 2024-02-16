# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["SearchListParams", "SearchParams"]


class SearchListParams(TypedDict, total=False):
    page: object

    per_page: object

    search_params: SearchParams


class SearchParams(TypedDict, total=False):
    query: str
    """Search query term."""

    references: Literal["", "*", "referral", "referrer"]
    """The type of references to include ("\\**" for all)."""
