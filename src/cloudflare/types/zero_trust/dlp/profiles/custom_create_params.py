# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .pattern_param import PatternParam
from ..context_awareness_param import ContextAwarenessParam

__all__ = ["CustomCreateParams", "Profile", "ProfileEntry"]


class CustomCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    profiles: Required[Iterable[Profile]]


class ProfileEntry(TypedDict, total=False):
    enabled: Required[bool]
    """Whether the entry is enabled or not."""

    name: Required[str]
    """The name of the entry."""

    pattern: Required[PatternParam]
    """A pattern that matches an entry"""


class Profile(TypedDict, total=False):
    allowed_match_count: float
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: ContextAwarenessParam
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    description: str
    """The description of the profile."""

    entries: Iterable[ProfileEntry]
    """The entries for this profile."""

    name: str
    """The name of the profile."""

    ocr_enabled: bool
    """If true, scan images via OCR to determine if any text present matches filters."""
