# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["ContentExportParams", "DLPProfileInformation", "DLPProfileInformationEntry", "Order"]


class ContentExportParams(TypedDict, total=False):
    account_id: Required[str]

    dlp_profile_information: Required[Iterable[DLPProfileInformation]]
    """DLP profile metadata for the export."""

    dlp_profile_id: SequenceNotStr[str]
    """Filter by DLP profile IDs."""

    integration_id: SequenceNotStr[str]
    """Filter by integration IDs."""

    max_affliction_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view content flagged on or before this date."""

    min_affliction_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view content flagged on or after this date."""

    orders: Iterable[Order]
    """Ordering specifications for the export."""

    search: str
    """Search term to filter content."""

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


class DLPProfileInformationEntry(TypedDict, total=False):
    """Entry within a DLP profile."""

    id: Required[str]
    """Unique identifier for the DLP profile entry."""

    name: Required[str]
    """Name of the DLP profile entry."""

    profile_id: Required[str]
    """ID of the parent DLP profile."""


class DLPProfileInformation(TypedDict, total=False):
    """DLP profile configuration."""

    id: Required[str]
    """Unique identifier for the DLP profile."""

    entries: Required[Iterable[DLPProfileInformationEntry]]
    """Entries contained within this DLP profile."""

    name: Required[str]
    """Name of the DLP profile."""


class Order(TypedDict, total=False):
    """Generic ordering specification."""

    direction: Required[Literal["asc", "desc"]]
    """Sort direction."""

    name: Required[Literal["asset_name", "dlp_profile_count", "integration_name", "latest_affliction_date"]]
    """Content-specific field names for ordering."""
