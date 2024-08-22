# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["LocationListParams"]

class LocationListParams(TypedDict, total=False):
    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit: int
    """Limit the number of objects in the response."""

    location: str
    """Comma separated list of locations."""

    offset: int
    """Number of objects to skip before grabbing results."""