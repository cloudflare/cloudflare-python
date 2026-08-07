# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["QuotaGetResponse"]


class QuotaGetResponse(BaseModel):
    allocated: int
    """The allocated custom hostname quota."""

    exceeded: bool
    """Whether the current usage has exceeded the allocated quota."""

    hard_cap: int
    """
    The maximum number of custom hostnames allowed before create requests are
    rejected.
    """

    used: int
    """The number of custom hostnames currently in use."""
