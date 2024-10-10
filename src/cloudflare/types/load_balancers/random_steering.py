# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["RandomSteering"]


class RandomSteering(BaseModel):
    default_weight: Optional[float] = None
    """
    The default weight for pools in the load balancer that are not specified in the
    pool_weights map.
    """

    pool_weights: Optional[Dict[str, float]] = None
    """A mapping of pool IDs to custom weights.

    The weight is relative to other pools in the load balancer.
    """
