# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RandomSteering", "PoolWeights"]


class PoolWeights(BaseModel):
    key: Optional[str] = None
    """Pool ID"""

    value: Optional[float] = None
    """Weight"""


class RandomSteering(BaseModel):
    default_weight: Optional[float] = None
    """
    The default weight for pools in the load balancer that are not specified in the
    pool_weights map.
    """

    pool_weights: Optional[PoolWeights] = None
    """A mapping of pool IDs to custom weights.

    The weight is relative to other pools in the load balancer.
    """