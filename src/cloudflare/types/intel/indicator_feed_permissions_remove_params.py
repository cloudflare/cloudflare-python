# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["IndicatorFeedPermissionsRemoveParams"]


class IndicatorFeedPermissionsRemoveParams(TypedDict, total=False):
    account_tag: str
    """The Cloudflare account tag of the account to change permissions on"""

    feed_id: int
    """The ID of the feed to add/remove permissions on"""
