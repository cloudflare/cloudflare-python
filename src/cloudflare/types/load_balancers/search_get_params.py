# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["SearchGetParams", "SearchParams"]


class SearchGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    page: float

    per_page: float

    search_params: SearchParams


class SearchParams(TypedDict, total=False):
    query: str
    """Search query term."""

    references: Literal["", "*", "referral", "referrer"]
    """The type of references to include ("\\**" for all)."""
