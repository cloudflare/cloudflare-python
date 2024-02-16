# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["OverTimeListParams"]


class OverTimeListParams(TypedDict, total=False):
    time_end: Required[str]
    """Timestamp in ISO format"""

    time_start: Required[str]
    """Timestamp in ISO format"""

    colo: str
    """Cloudflare colo"""

    device_id: str
    """Device-specific ID, given as UUID v4"""
