# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SearchGlobalParams"]


class SearchGlobalParams(TypedDict, total=False):
    query: Required[str]
    """Search for locations, autonomous systems and reports."""

    exclude: List[Literal["SPECIAL_EVENTS", "NOTEBOOKS", "LOCATIONS", "ASNS"]]
    """Search types to be excluded from results."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    include: List[Literal["SPECIAL_EVENTS", "NOTEBOOKS", "LOCATIONS", "ASNS"]]
    """Search types to be included in results."""

    limit: int
    """Limits the number of objects returned in the response."""

    limit_per_group: Annotated[float, PropertyInfo(alias="limitPerGroup")]
    """Limit the number of objects per search category."""
