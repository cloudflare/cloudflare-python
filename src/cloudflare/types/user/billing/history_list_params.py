# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from typing import Union

from datetime import datetime

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["HistoryListParams"]


class HistoryListParams(TypedDict, total=False):
    action: str
    """The billing item action."""

    occurred_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When the billing item was created."""

    order: Literal["type", "occurred_at", "action"]
    """Field to order billing history by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""

    type: str
    """The billing item type."""
