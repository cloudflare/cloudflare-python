# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AccessRequestListParams"]


class AccessRequestListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    direction: Literal["desc", "asc"]
    """The chronological sorting order for the logs."""

    email: str
    """Filter by user email.

    Defaults to substring matching. To force exact matching, set `email_exact=true`.
    Example (default): `email=@example.com` returns all events with that domain.
    Example (exact): `email=user@example.com&email_exact=true` returns only that
    user.
    """

    email_exact: bool
    """When true, `email` is matched exactly instead of substring matching."""

    limit: int
    """The maximum number of log entries to retrieve."""

    page: int
    """Page number of results."""

    per_page: int
    """Number of results per page."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The earliest event timestamp to query."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The latest event timestamp to query."""

    user_id: str
    """Filter by user UUID."""
