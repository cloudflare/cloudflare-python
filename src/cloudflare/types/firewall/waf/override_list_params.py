# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OverrideListParams"]


class OverrideListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    page: float
    """The page number of paginated results."""

    per_page: float
    """The number of WAF overrides per page."""
