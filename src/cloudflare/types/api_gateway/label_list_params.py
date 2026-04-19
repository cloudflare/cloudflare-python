# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LabelListParams"]


class LabelListParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    direction: Literal["asc", "desc"]
    """Direction to order results."""

    filter: str
    """Filter for labels where the name or description matches using substring match"""

    order: Literal["name", "description", "created_at", "last_updated", "mapped_resources.operations"]
    """Field to order by"""

    page: int
    """Page number of paginated results."""

    per_page: int
    """Maximum number of results per page."""

    source: Literal["user", "managed"]
    """Filter for labels with source"""

    with_mapped_resource_counts: bool
    """Include `mapped_resources` for each label"""
