# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MiscategorizationCreateParams"]


class MiscategorizationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    content_adds: Iterable[int]
    """Content category IDs to add."""

    content_removes: Iterable[int]
    """Content category IDs to remove."""

    indicator_type: Literal["domain", "ipv4", "ipv6", "url"]

    ip: Optional[str]
    """Provide only if indicator_type is `ipv4` or `ipv6`."""

    security_adds: Iterable[int]
    """Security category IDs to add."""

    security_removes: Iterable[int]
    """Security category IDs to remove."""

    url: str
    """Provide only if indicator_type is `domain` or `url`.

    Example if indicator_type is `domain`: `example.com`. Example if indicator_type
    is `url`: `https://example.com/news/`.
    """
