# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo
from .....types import shared_params

__all__ = ["ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListParams", "Entry"]


class ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListParams(TypedDict, total=False):
    zone_identifier: Required[str]
    """Identifier"""

    action: Required[Literal["block"]]
    """Behavior of the content list."""

    entries: Required[Iterable[Entry]]
    """Content list entries."""


class Entry(TypedDict, total=False):
    content: str
    """CID or content path of content to block."""

    description: str
    """An optional description of the content list entry."""

    type: Literal["cid", "content_path"]
    """Type of content list entry to block."""
