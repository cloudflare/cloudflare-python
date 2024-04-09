# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    origin_healthy: bool
    """If true, filter events where the origin status is healthy.

    If false, filter events where the origin status is unhealthy.
    """

    origin_name: str
    """The name for the origin to filter."""

    pool_healthy: bool
    """If true, filter events where the pool status is healthy.

    If false, filter events where the pool status is unhealthy.
    """

    pool_id: str

    pool_name: str
    """The name for the pool to filter."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start date and time of requesting data period in the ISO8601 format."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date and time of requesting data period in the ISO8601 format."""
