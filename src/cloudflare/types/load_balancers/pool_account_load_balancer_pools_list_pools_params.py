# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PoolAccountLoadBalancerPoolsListPoolsParams"]


class PoolAccountLoadBalancerPoolsListPoolsParams(TypedDict, total=False):
    monitor: object
    """
    The ID of the Monitor to use for checking the health of origins within this
    pool.
    """
