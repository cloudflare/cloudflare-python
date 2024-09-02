# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ......_types import FileTypes
from ......_utils import PropertyInfo

__all__ = ["EntryCreateParams"]


class EntryCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: Required[str]
    """CID or content path of content to block."""

    type: Required[Literal["cid", "content_path"]]
    """Type of content list entry to block."""

    description: str
    """An optional description of the content list entry."""
