# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InstanceListParams"]


class InstanceListParams(TypedDict, total=False):
    account_id: Required[str]

    cursor: str
    """`page` and `cursor` are mutually exclusive, use one or the other."""

    date_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Accepts ISO 8601 with no timezone offsets and in UTC."""

    date_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Accepts ISO 8601 with no timezone offsets and in UTC."""

    page: float
    """`page` and `cursor` are mutually exclusive, use one or the other."""

    per_page: float

    status: Literal["queued", "running", "paused", "errored", "terminated", "complete", "waitingForPause", "waiting"]
