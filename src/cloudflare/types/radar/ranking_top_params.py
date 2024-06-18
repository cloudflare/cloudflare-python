# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RankingTopParams"]


class RankingTopParams(TypedDict, total=False):
    date: List[str]
    """Array of dates to filter the ranking."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit: int
    """Limit the number of objects in the response."""

    location: List[str]
    """Array of locations (alpha-2 country codes)."""

    name: List[str]
    """Array of names that will be used to name the series in responses."""

    ranking_type: Annotated[Literal["POPULAR", "TRENDING_RISE", "TRENDING_STEADY"], PropertyInfo(alias="rankingType")]
    """The ranking type."""
