# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["DatabaseListParams"]


class DatabaseListParams(TypedDict, total=False):
    name: str
    """a database name to search for."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""
