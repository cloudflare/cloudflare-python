# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = ["AsePrefixesParams"]

class AsePrefixesParams(TypedDict, total=False):
    country: str
    """Alpha-2 country code."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit: int
    """Maximum number of ASes to return"""