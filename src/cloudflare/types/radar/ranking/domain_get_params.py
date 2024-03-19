# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DomainGetParams"]


class DomainGetParams(TypedDict, total=False):
    date: List[Optional[str]]
    """Array of dates to filter the ranking."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit: int
    """Limit the number of objects in the response."""

    name: List[str]
    """Array of names that will be used to name the series in responses."""

    ranking_type: Annotated[Literal["POPULAR", "TRENDING_RISE", "TRENDING_STEADY"], PropertyInfo(alias="rankingType")]
    """The ranking type."""
