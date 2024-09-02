# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["HoldDeleteParams"]


class HoldDeleteParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    hold_after: str
    """
    If `hold_after` is provided, the hold will be temporarily disabled, then
    automatically re-enabled by the system at the time specified in this
    RFC3339-formatted timestamp. Otherwise, the hold will be disabled indefinitely.
    """
