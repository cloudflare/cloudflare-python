# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["V1ListParams"]

class V1ListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""