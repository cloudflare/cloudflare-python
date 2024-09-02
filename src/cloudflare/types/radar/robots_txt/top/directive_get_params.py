# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Annotated

from ....._utils import PropertyInfo

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = ["DirectiveGetParams"]


class DirectiveGetParams(TypedDict, total=False):
    agent_category: Annotated[Literal["AI"], PropertyInfo(alias="agentCategory")]
    """Filter by user agent category."""

    date: str
    """Date to filter the ranking."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit: int
    """Limit the number of objects in the response."""

    name: List[str]
    """Array of names that will be used to name the series in responses."""
