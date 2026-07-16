# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ......_types import SequenceNotStr
from ......_utils import PropertyInfo

__all__ = ["JobExportParams", "Order"]


class JobExportParams(TypedDict, total=False):
    account_id: Required[str]

    integration_id: SequenceNotStr[str]
    """Filter by multiple integration IDs."""

    max_updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view remediation jobs updated on or before this datetime.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    min_updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view remediation jobs updated on or after this datetime.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    orders: Iterable[Order]
    """Ordering specifications for the export."""

    search: str
    """A search term."""

    status: List[Literal["pending", "processing", "completed", "failed", "validating"]]
    """Filter by remediation job status."""


class Order(TypedDict, total=False):
    """Order specification for remediation jobs exports."""

    direction: Required[Literal["asc", "desc"]]
    """Sort direction."""

    name: Required[
        Literal["asset_name", "finding_type_name", "integration_name", "status", "last_updated_at", "affliction_date"]
    ]
    """Which field to use when ordering the remediation jobs."""
