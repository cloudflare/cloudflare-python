# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["EntityGetParams"]


class EntityGetParams(TypedDict, total=False):
    ip: Required[str]
    """IP address."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""
