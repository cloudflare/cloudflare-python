# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["InternetServiceTopParams"]


class InternetServiceTopParams(TypedDict, total=False):
    date: Annotated[List[Union[str, datetime.date]], PropertyInfo(format="iso8601")]
    """Array of dates to filter the ranking."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit: int
    """Limit the number of objects in the response."""

    name: List[str]
    """Array of names that will be used to name the series in responses."""

    service_category: Annotated[List[str], PropertyInfo(alias="serviceCategory")]
    """Filter for services category."""
