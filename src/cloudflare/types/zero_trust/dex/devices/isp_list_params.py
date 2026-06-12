# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ISPListParams"]


class ISPListParams(TypedDict, total=False):
    account_id: Required[str]
    """Unique identifier linked to an account."""

    per_page: Required[int]
    """Number of items per page"""

    cursor: str
    """Cursor for cursor-based pagination. Mutually exclusive with page."""

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Start time for the query in ISO 8601 format."""

    page: int
    """Page number of paginated results. Mutually exclusive with cursor."""

    sort_by: Literal["time_start"]
    """The field to sort results by."""

    sort_order: Literal["ASC", "DESC"]
    """The order to sort results."""

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End time for the query in ISO 8601 format."""
