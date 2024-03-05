# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["BytimeGetParams"]


class BytimeGetParams(TypedDict, total=False):
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
