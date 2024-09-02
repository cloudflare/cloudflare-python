# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["FirewallListParams"]


class FirewallListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of clusters per page."""
