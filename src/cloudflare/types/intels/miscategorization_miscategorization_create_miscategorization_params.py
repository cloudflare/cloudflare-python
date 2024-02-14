# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["MiscategorizationMiscategorizationCreateMiscategorizationParams"]


class MiscategorizationMiscategorizationCreateMiscategorizationParams(TypedDict, total=False):
    content_adds: object
    """Content category IDs to add."""

    content_removes: object
    """Content category IDs to remove."""

    indicator_type: Literal["domain", "ipv4", "ipv6", "url"]

    ip: object
    """Provide only if indicator_type is `ipv4` or `ipv6`."""

    security_adds: object
    """Security category IDs to add."""

    security_removes: object
    """Security category IDs to remove."""

    url: str
    """Provide only if indicator_type is `domain` or `url`.

    Example if indicator_type is `domain`: `example.com`. Example if indicator_type
    is `url`: `https://example.com/news/`.
    """
