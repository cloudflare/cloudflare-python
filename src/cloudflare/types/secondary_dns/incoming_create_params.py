# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["IncomingCreateParams"]

class IncomingCreateParams(TypedDict, total=False):
    zone_id: Required[str]

    auto_refresh_seconds: Required[float]
    """
    How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
    applicable for primary zones.
    """

    name: Required[str]
    """Zone name."""

    peers: Required[List[str]]
    """A list of peer tags."""