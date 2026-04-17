# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ManagedGetParams"]


class ManagedGetParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    with_mapped_resource_counts: bool
    """Include `mapped_resources` for each label"""
