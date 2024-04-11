# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .colo_name_param import ColoNameParam
from .colo_region_param import ColoRegionParam

__all__ = ["ScopeParam"]


class ScopeParam(TypedDict, total=False):
    colo_names: ColoNameParam
    """List of colo names for the ECMP scope."""

    colo_regions: ColoRegionParam
    """List of colo regions for the ECMP scope."""
