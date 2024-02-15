# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from typing import Union

from datetime import datetime

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["EventLoadBalancerHealthcheckEventsListHealthcheckEventsParams"]


class EventLoadBalancerHealthcheckEventsListHealthcheckEventsParams(TypedDict, total=False):
    identifier: str

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

    pool_name: str
    """The name for the pool to filter."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start date and time of requesting data period in the ISO8601 format."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date and time of requesting data period in the ISO8601 format."""
