# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LoadSheddingParam"]


class LoadSheddingParam(TypedDict, total=False):
    default_percent: float
    """The percent of traffic to shed from the pool, according to the default policy.

    Applies to new sessions and traffic without session affinity.
    """

    default_policy: Literal["random", "hash"]
    """The default policy to use when load shedding.

    A random policy randomly sheds a given percent of requests. A hash policy
    computes a hash over the CF-Connecting-IP address and sheds all requests
    originating from a percent of IPs.
    """

    session_percent: float
    """
    The percent of existing sessions to shed from the pool, according to the session
    policy.
    """

    session_policy: Literal["hash"]
    """
    Only the hash policy is supported for existing sessions (to avoid exponential
    decay).
    """
