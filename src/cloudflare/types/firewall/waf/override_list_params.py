# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OverrideListParams"]


class OverrideListParams(TypedDict, total=False):
    page: float
    """The page number of paginated results."""

    per_page: float
    """The number of WAF overrides per page."""
