# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .content_lists import DistributedWebConfigContentListEntryParam

__all__ = ["ContentListUpdateParams"]


class ContentListUpdateParams(TypedDict, total=False):
    zone_identifier: Required[str]
    """Identifier"""

    action: Required[Literal["block"]]
    """Behavior of the content list."""

    entries: Required[Iterable[DistributedWebConfigContentListEntryParam]]
    """Content list entries."""
