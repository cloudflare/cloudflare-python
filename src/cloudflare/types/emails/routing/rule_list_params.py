# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RuleListParams"]


class RuleListParams(TypedDict, total=False):
    enabled: Literal[True, False]
    """Filter by enabled routing rules."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""
