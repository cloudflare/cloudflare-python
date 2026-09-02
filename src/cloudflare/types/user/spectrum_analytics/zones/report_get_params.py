# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ReportGetParams"]


class ReportGetParams(TypedDict, total=False):
    cdn_traffic: bool
    """Include CDN traffic in the bandwidth aggregation."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of time interval to query, defaults to `until` - 6 hours.

    Timestamp must be in RFC3339 format and uses UTC unless otherwise specified.
    """

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of time interval to query, defaults to current time.

    Timestamp must be in RFC3339 format and uses UTC unless otherwise specified.
    """
