# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["InternetServiceCategoriesParams"]


class InternetServiceCategoriesParams(TypedDict, total=False):
    date: Annotated[SequenceNotStr[Union[str, datetime.date]], PropertyInfo(format="iso8601")]
    """Filters results by the specified array of dates."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""
