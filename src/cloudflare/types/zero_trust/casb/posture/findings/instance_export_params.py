# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["InstanceExportParams", "Order"]


class InstanceExportParams(TypedDict, total=False):
    account_id: Required[str]

    archived: bool
    """Filter for archived status."""

    max_affliction_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view findings that occurred on or before the affliction date.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    min_affliction_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view findings that occurred on or after the affliction date.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    orders: Iterable[Order]
    """Ordering specifications for the export."""

    search: str
    """A search term."""


class Order(TypedDict, total=False):
    """Order specification for finding instance exports."""

    direction: Required[Literal["asc", "desc"]]
    """Sort direction."""

    name: Required[Literal["asset.name", "affliction_date"]]
    """Which field to use when ordering the finding instances."""
