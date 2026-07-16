# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    account_id: Required[str]

    cursor: str
    """A cursor for pagination."""

    direction: Literal["asc", "desc"]
    """Direction to order results."""

    integration_id: str
    """Filter by an integration ID"""

    max_updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view remediations updated on or before the max updated datetime.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    min_updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view remediations updated on or after the min updated datetime.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    order: Literal[
        "created_at",
        "affliction_date",
        "integration_name",
        "status",
        "last_updated_at",
        "asset_name",
        "finding_type_name",
    ]
    """An optional param to sort the results by the given field."""

    page: int
    """A page number within the paginated result set."""

    per_page: int
    """Number of results to return per page."""

    search: str
    """A search term."""

    status: Literal["pending", "processing", "completed", "failed", "validating"]
    """Filter to view remediations with the given status."""

    triggered_by_actor: List[Literal["user", "account_token"]]
    """Filter remediations by what kind of actor triggered them.

    Supports multiple comma-separated values.
    """
