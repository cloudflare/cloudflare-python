# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PoolAccountLoadBalancerPoolsPatchPoolsParams"]


class PoolAccountLoadBalancerPoolsPatchPoolsParams(TypedDict, total=False):
    notification_email: Literal['""']
    """The email address to send health status notifications to.

    This field is now deprecated in favor of Cloudflare Notifications for Load
    Balancing, so only resetting this field with an empty string `""` is accepted.
    """
