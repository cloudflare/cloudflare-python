# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DNSParam", "ReverseRecord"]


class ReverseRecord(TypedDict, total=False):
    first_seen: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """First seen date of the DNS record during the time period."""

    hostname: object
    """Hostname that the IP was observed resolving to."""

    last_seen: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Last seen date of the DNS record during the time period."""


class DNSParam(TypedDict, total=False):
    count: float
    """Total results returned based on your search parameters."""

    page: float
    """Current page within paginated list of results."""

    per_page: float
    """Number of results per page of results."""

    reverse_records: Iterable[ReverseRecord]
    """Reverse DNS look-ups observed during the time period."""
