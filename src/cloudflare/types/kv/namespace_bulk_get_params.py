# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NamespaceBulkGetParams"]


class NamespaceBulkGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    keys: Required[List[str]]
    """Array of keys to retrieve (maximum 100)"""

    type: Literal["text", "json"]
    """Whether to parse JSON values in the response"""

    with_metadata: Annotated[bool, PropertyInfo(alias="withMetadata")]
    """Whether to include metadata in the response"""
