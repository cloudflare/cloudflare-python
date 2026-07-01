# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IntegrationListParams"]


class IntegrationListParams(TypedDict, total=False):
    account_id: Required[str]

    application: str
    """Filter by application/vendor (e.g., GOOGLE_WORKSPACE, MICROSOFT_INTERNAL)."""

    direction: Literal["asc", "desc"]
    """Direction to order results."""

    dlp_enabled: bool
    """Filter by DLP enabled status (true/false)."""

    order: Literal["application", "created", "name", "status"]
    """Field to order results by."""

    page: int
    """Page number within the paginated result set."""

    page_size: int
    """Number of results per page."""

    search: str
    """Search integrations by name or application."""

    status: Literal["Healthy", "Initializing", "Offline", "Unhealthy"]
    """Filter by integration status."""

    use_cases: str
    """Filter by enabled use cases (e.g., casb, ces).

    Matches integrations enrolled in any of the specified values. Can be specified
    multiple times.
    """
