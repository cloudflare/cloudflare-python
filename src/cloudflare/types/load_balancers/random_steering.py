# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["RandomSteering"]


class RandomSteering(BaseModel):
    """
    Configures pool weights.
    - `steering_policy="random"`: A random pool is selected with probability proportional to pool weights.
    - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each pool's outstanding requests.
    - `steering_policy="least_connections"`: Use pool weights to scale each pool's open connections.
    """

    default_weight: Optional[float] = None
    """
    The default weight for pools in the load balancer that are not specified in the
    pool_weights map.
    """

    pool_weights: Optional[Dict[str, float]] = None
    """A mapping of pool IDs to custom weights.

    The weight is relative to other pools in the load balancer.
    """
