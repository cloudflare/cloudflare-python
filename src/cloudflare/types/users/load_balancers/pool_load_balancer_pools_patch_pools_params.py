# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["PoolLoadBalancerPoolsPatchPoolsParams"]


class PoolLoadBalancerPoolsPatchPoolsParams(TypedDict, total=False):
    notification_email: Literal['""']
    """The email address to send health status notifications to.

    This field is now deprecated in favor of Cloudflare Notifications for Load
    Balancing, so only resetting this field with an empty string `""` is accepted.
    """
