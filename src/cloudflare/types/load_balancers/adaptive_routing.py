# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AdaptiveRouting"]


class AdaptiveRouting(BaseModel):
    failover_across_pools: Optional[bool] = None
    """
    Extends zero-downtime failover of requests to healthy origins from alternate
    pools, when no healthy alternate exists in the same pool, according to the
    failover order defined by traffic and origin steering. When set false (the
    default) zero-downtime failover will only occur between origins within the same
    pool. See `session_affinity_attributes` for control over when sessions are
    broken or reassigned.
    """
