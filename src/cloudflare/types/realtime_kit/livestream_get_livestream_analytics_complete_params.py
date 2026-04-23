# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LivestreamGetLivestreamAnalyticsCompleteParams"]


class LivestreamGetLivestreamAnalyticsCompleteParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Specify the end time range in ISO format to access the livestream analytics."""

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Specify the start time range in ISO format to access the livestream analytics."""
