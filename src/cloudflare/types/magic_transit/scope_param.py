# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .colo_names_item import ColoNamesItem
from .colo_regions_item import ColoRegionsItem

__all__ = ["ScopeParam"]


class ScopeParam(TypedDict, total=False):
    colo_names: List[ColoNamesItem]
    """List of colo names for the ECMP scope."""

    colo_regions: List[ColoRegionsItem]
    """List of colo regions for the ECMP scope."""
