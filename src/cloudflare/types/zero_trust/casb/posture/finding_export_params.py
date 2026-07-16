# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["FindingExportParams", "Order"]


class FindingExportParams(TypedDict, total=False):
    account_id: Required[str]

    ignored: bool
    """Filter for only the ignored findings. Set to false to only see active items."""

    integration_id: SequenceNotStr[str]
    """Filter by multiple integration IDs."""

    max_affliction_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view findings that occurred on or before the affliction date.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    min_affliction_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view findings that occurred on or after the affliction date.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    orders: Iterable[Order]
    """Which fields to use when ordering the findings."""

    product: Optional[Literal["SaaS", "Cloud"]]
    """Filter by finding's category product."""

    search: str
    """A search term."""

    severities: List[Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"]]
    """Filter by severity levels."""

    vendors: List[
        Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT",
            "MICROSOFT_INTERNAL",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
        ]
    ]
    """Filter by vendor types."""


class Order(TypedDict, total=False):
    """Order specification for finding exports."""

    direction: Required[Literal["asc", "desc"]]
    """Sort direction."""

    name: Required[Literal["instance_count", "finding.name", "integration.name", "latest_affliction_date", "severity"]]
    """Which field to use when ordering the findings."""
