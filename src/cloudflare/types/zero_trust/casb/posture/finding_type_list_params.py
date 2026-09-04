# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FindingTypeListParams"]


class FindingTypeListParams(TypedDict, total=False):
    account_id: Required[str]

    page: int
    """A page number within the paginated result set."""

    per_page: int
    """Number of results to return per page."""

    search: str
    """Filter finding types by name or ID (case-insensitive substring match)."""

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
    """Filter finding types by vendor. Supports multiple comma-separated values."""
