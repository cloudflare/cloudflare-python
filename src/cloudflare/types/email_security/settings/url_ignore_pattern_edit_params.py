# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["URLIgnorePatternEditParams"]


class URLIgnorePatternEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    comments: Optional[str]
    """Optional note describing the reason for the ignore pattern."""

    pattern: str
    """Regular expression matching URLs that should not be rewritten."""
