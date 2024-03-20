# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PredefinedUpdateParams", "ContextAwareness", "ContextAwarenessSkip", "Entry"]


class PredefinedUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    allowed_match_count: float
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: ContextAwareness
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    entries: Iterable[Entry]
    """The entries for this profile."""

    ocr_enabled: bool
    """If true, scan images via OCR to determine if any text present matches filters."""


class ContextAwarenessSkip(TypedDict, total=False):
    files: Required[bool]
    """If the content type is a file, skip context analysis and return all matches."""


class ContextAwareness(TypedDict, total=False):
    enabled: Required[bool]
    """
    If true, scan the context of predefined entries to only return matches
    surrounded by keywords.
    """

    skip: Required[ContextAwarenessSkip]
    """Content types to exclude from context analysis and return all matches."""


class Entry(TypedDict, total=False):
    enabled: bool
    """Whether the entry is enabled or not."""
