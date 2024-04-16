# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LoadShedding"]


class LoadShedding(BaseModel):
    default_percent: Optional[float] = None
    """The percent of traffic to shed from the pool, according to the default policy.

    Applies to new sessions and traffic without session affinity.
    """

    default_policy: Optional[Literal["random", "hash"]] = None
    """The default policy to use when load shedding.

    A random policy randomly sheds a given percent of requests. A hash policy
    computes a hash over the CF-Connecting-IP address and sheds all requests
    originating from a percent of IPs.
    """

    session_percent: Optional[float] = None
    """
    The percent of existing sessions to shed from the pool, according to the session
    policy.
    """

    session_policy: Optional[Literal["hash"]] = None
    """
    Only the hash policy is supported for existing sessions (to avoid exponential
    decay).
    """
