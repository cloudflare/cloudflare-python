# File generated from our OpenAPI spec by Stainless.

from typing import List

from ...._models import BaseModel

__all__ = ["FullGetResponse"]


class FullGetResponse(BaseModel):
    default_sampling: float
    """Fallback sampling rate of flow messages being sent in packets per second.

    This should match the packet sampling rate configured on the router.
    """

    name: str
    """The account name."""

    router_ips: List[str]
