# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["RandomSteeringParam"]


class RandomSteeringParam(TypedDict, total=False):
    default_weight: float
    """
    The default weight for pools in the load balancer that are not specified in the
    pool_weights map.
    """

    pool_weights: Dict[str, float]
    """A mapping of pool IDs to custom weights.

    The weight is relative to other pools in the load balancer.
    """
