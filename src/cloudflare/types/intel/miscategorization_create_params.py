# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MiscategorizationCreateParams"]


class MiscategorizationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

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
