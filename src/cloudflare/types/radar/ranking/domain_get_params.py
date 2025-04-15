# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DomainGetParams"]


class DomainGetParams(TypedDict, total=False):
    date: Annotated[List[Union[str, datetime.date]], PropertyInfo(format="iso8601")]
    """Filters results by the specified array of dates."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    include_top_locations: Annotated[bool, PropertyInfo(alias="includeTopLocations")]
    """Includes top locations in the response."""

    limit: int
    """Limits the number of objects returned in the response."""

    name: List[str]
    """Array of names used to label the series in the response."""

    ranking_type: Annotated[Literal["POPULAR", "TRENDING_RISE", "TRENDING_STEADY"], PropertyInfo(alias="rankingType")]
    """The ranking type."""
