# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["ScopeParam"]


class ScopeParam(TypedDict, total=False):
    colo_names: List[str]
    """List of colo names for the ECMP scope."""

    colo_regions: List[str]
    """List of colo regions for the ECMP scope."""
