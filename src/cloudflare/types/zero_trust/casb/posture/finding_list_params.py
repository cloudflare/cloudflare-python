# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["FindingListParams"]


class FindingListParams(TypedDict, total=False):
    account_id: Required[str]

    cursor: str
    """A cursor for pagination.

    Obtained from the `result_info.cursor` field of a previous response.
    """

    direction: Literal["asc", "desc"]
    """Direction to order results."""

    finding_type_ids: str
    """A comma separated list of UUIDs identifying the finding type(s)."""

    ignored: bool
    """Filter for only the ignored findings. Set to false to only see "active" items"""

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

    observation: Literal["Activity", "Insight", "Issue"]
    """Filter by observation type of the finding"""

    order: Literal["finding.name", "instance_count", "integration.name", "latest_affliction_date", "severity"]
    """Which field to use when ordering the findings."""

    page: int
    """A page number within the paginated result set."""

    per_page: int
    """Number of results to return per page."""

    product: Literal["Cloud", "Saas"]
    """Filter by product category of the finding"""

    search: str
    """A search term."""

    severity: Literal["Critical", "High", "Medium", "Low"]
    """Filter by severity"""

    type: Literal["Content", "Posture"]
    """Filter by type of the finding"""

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
