# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ContentListParams"]


class ContentListParams(TypedDict, total=False):
    account_id: Required[str]

    direction: Literal["asc", "desc"]
    """Direction to order results."""

    dlp_profile_id: str
    """Filter by an DLP profile ID"""

    integration_id: str
    """Filter by an integration ID"""

    max_affliction_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view findings that occurred on or before the affliction date.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    min_affliction_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view findings that occurred on or after the affliction date.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    order: Literal["asset_name", "dlp_profile_count", "integration_name", "latest_affliction_date"]
    """Which field to use when ordering content assets."""

    page: int
    """A page number within the paginated result set."""

    per_page: int
    """Number of results to return per page."""

    search: str
    """A search term."""

    vendor: Literal[
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
    """Filter by vendor"""
