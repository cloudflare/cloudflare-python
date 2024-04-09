# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .colo_name import ColoName
from .colo_region import ColoRegion

__all__ = ["ScopeParam"]


class ScopeParam(TypedDict, total=False):
    colo_names: List[ColoName]
    """List of colo names for the ECMP scope."""

    colo_regions: List[ColoRegion]
    """List of colo regions for the ECMP scope."""
