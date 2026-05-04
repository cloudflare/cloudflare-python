# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuditLogListByInsightParams"]


class AuditLogListByInsightParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter entries changed before this timestamp (RFC 3339)."""

    changed_by: str
    """Filter by the actor that made the change."""

    cursor: str
    """Opaque cursor for pagination.

    Use the cursor value from result_info of the previous response.
    """

    field_changed: Literal["status", "user_classification"]
    """Filter by the field that was changed."""

    order: Literal["asc", "desc"]
    """Sort order for results. Use 'asc' for oldest first or 'desc' for newest first."""

    per_page: int
    """Number of results per page."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter entries changed at or after this timestamp (RFC 3339)."""
