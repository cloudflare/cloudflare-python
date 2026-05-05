# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TopAsesParams"]


class TopAsesParams(TypedDict, total=False):
    country: str
    """Optional ISO 3166-1 alpha-2 country filter. Omit for global top-N."""

    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters results by the specified datetime (ISO 8601)."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    metric: Literal["v4_24s", "v6_48s"]
    """Ranking metric: IPv4 /24 count or IPv6 /48 count."""
