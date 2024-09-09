# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LanguageUpdateParams"]


class LanguageUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    identifier: Required[str]
    """A Cloudflare-generated unique identifier for a media item."""

    file: Required[str]
    """The WebVTT file containing the caption or subtitle content."""
