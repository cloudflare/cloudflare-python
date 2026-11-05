# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["FindingTypeListParams"]


class FindingTypeListParams(TypedDict, total=False):
    account_id: Required[str]

    direction: Literal["asc", "desc"]
    """Sort direction for the primary field.

    Defaults to 'desc'. Ties are resolved by case-insensitive name, then ID, both
    ascending regardless of direction.
    """

    max_updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return only finding types updated at or before this RFC 3339 timestamp
    (inclusive).
    """

    min_updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return only finding types updated at or after this RFC 3339 timestamp
    (inclusive).
    """

    order: Literal["created", "updated", "match_count", "name", "vendor", "type", "origin", "severity"]
    """Field to sort by (case-insensitive).

    Defaults to 'created'. Name and vendor sorting is case-insensitive; vendor uses
    friendly provider names. Ascending order: type Content then Posture; origin
    custom then system; severity Low, Medium, High, Critical.
    """

    origins: List[Literal["custom", "system"]]
    """Filter finding types by origin.

    Supports multiple comma-separated, case-insensitive values.
    """

    page: int
    """A page number within the paginated result set."""

    per_page: int
    """Number of results to return per page."""

    quarantined: bool
    """
    When true, return only quarantined finding types; when false, return only
    non-quarantined finding types. Omit to return both.
    """

    search: str
    """Filter finding types by name or ID (case-insensitive substring match)."""

    severities: List[Literal["critical", "high", "medium", "low"]]
    """Filter finding types by severity.

    Supports multiple comma-separated, case-insensitive values.
    """

    types: List[Literal["Content", "Posture"]]
    """Filter finding types by category type.

    Supports multiple comma-separated, case-insensitive values.
    """

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
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
            "ZOOM",
        ]
    ]
    """Filter finding types by vendor.

    Supports multiple comma-separated values. Each value may be either the vendor
    enum (GOOGLE_WORKSPACE) or the friendly name returned by the read routes (Google
    Workspace).
    """
