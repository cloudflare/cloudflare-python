# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["JitRequestListParams"]


class JitRequestListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    page: int
    """Page number of results."""

    per_page: int
    """Number of results per page."""

    search: str
    """
    Case-insensitive search over request ID, requester email, application audience,
    and application hostname.
    """

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The earliest request timestamp to query.

    Defaults to 366 days before the current time.
    """

    status: Literal["PENDING", "APPROVED", "DENIED", "CANCELED", "SPENT"]
    """JIT request status. `SPENT` is deprecated and interpreted as `APPROVED`."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The latest request timestamp to query. Defaults to the current time."""
