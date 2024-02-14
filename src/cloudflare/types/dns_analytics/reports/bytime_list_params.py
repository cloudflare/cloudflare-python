# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from typing import Union

from datetime import datetime

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["BytimeListParams"]


class BytimeListParams(TypedDict, total=False):
    dimensions: str
    """A comma-separated list of dimensions to group results by."""

    filters: str
    """Segmentation filter in 'attribute operator value' format."""

    limit: int
    """Limit number of returned metrics."""

    metrics: str
    """A comma-separated list of metrics to query."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start date and time of requesting data period in ISO 8601 format."""

    sort: str
    """
    A comma-separated list of dimensions to sort by, where each dimension may be
    prefixed by - (descending) or + (ascending).
    """

    time_delta: Literal["all", "auto", "year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"]
    """Unit of time to group data by."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date and time of requesting data period in ISO 8601 format."""
