# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["RobotsTXTDomainsParams"]


class RobotsTXTDomainsParams(TypedDict, total=False):
    domain_category: Annotated[str, PropertyInfo(alias="domainCategory")]
    """Filter domains by category"""

    domain_name: Annotated[str, PropertyInfo(alias="domainName")]
    """Filter domains by name"""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit: int
    """Limit the number of objects in the response."""

    offset: int
    """Number of objects to skip before grabbing results."""
