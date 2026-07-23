# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["URLIgnorePatternCreateParams"]


class URLIgnorePatternCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    pattern: Required[str]
    """Regular expression identifying URLs to exempt from rewriting."""

    comments: Optional[str]
    """Optional note describing the reason for the ignore pattern."""
