# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SentineloneInputParam"]


class SentineloneInputParam(TypedDict, total=False):
    operating_system: Required[object]

    path: Required[str]
    """File path."""

    sha256: str
    """SHA-256."""

    thumbprint: str
    """Signing certificate thumbprint."""
