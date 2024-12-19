# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InstanceListParams"]


class InstanceListParams(TypedDict, total=False):
    account_id: Required[str]

    date_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """In ISO 8601 with no timezone offsets and in UTC."""

    date_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """In ISO 8601 with no timezone offsets and in UTC."""

    page: float

    per_page: float

    status: Literal[
        "queued", "running", "paused", "errored", "terminated", "complete", "waitingForPause", "waiting", "unknown"
    ]
