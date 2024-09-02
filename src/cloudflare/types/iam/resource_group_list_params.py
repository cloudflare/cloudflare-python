# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["ResourceGroupListParams"]


class ResourceGroupListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    id: str
    """ID of the resource group to be fetched."""

    name: str
    """Name of the resource group to be fetched."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""
