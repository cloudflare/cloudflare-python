# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["ByDatasetListParams"]


class ByDatasetListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    indicator_type: Annotated[str, PropertyInfo(alias="indicatorType")]

    name: str
    """Filter by indicator value (substring match)"""

    page: float

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]

    related_event: Annotated[SequenceNotStr[str], PropertyInfo(alias="relatedEvent")]
    """Filter indicators by related event UUID(s).

    Multiple UUIDs can be provided by repeating the parameter.
    """
