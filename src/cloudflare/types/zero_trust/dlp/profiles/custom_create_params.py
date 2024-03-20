# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CustomCreateParams",
    "Profile",
    "ProfileContextAwareness",
    "ProfileContextAwarenessSkip",
    "ProfileEntry",
    "ProfileEntryPattern",
]


class CustomCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    profiles: Required[Iterable[Profile]]


class ProfileContextAwarenessSkip(TypedDict, total=False):
    files: Required[bool]
    """If the content type is a file, skip context analysis and return all matches."""


class ProfileContextAwareness(TypedDict, total=False):
    enabled: Required[bool]
    """
    If true, scan the context of predefined entries to only return matches
    surrounded by keywords.
    """

    skip: Required[ProfileContextAwarenessSkip]
    """Content types to exclude from context analysis and return all matches."""


class ProfileEntryPattern(TypedDict, total=False):
    regex: Required[str]
    """The regex pattern."""

    validation: Literal["luhn"]
    """Validation algorithm for the pattern.

    This algorithm will get run on potential matches, and if it returns false, the
    entry will not be matched.
    """


class ProfileEntry(TypedDict, total=False):
    enabled: Required[bool]
    """Whether the entry is enabled or not."""

    name: Required[str]
    """The name of the entry."""

    pattern: Required[ProfileEntryPattern]
    """A pattern that matches an entry"""


class Profile(TypedDict, total=False):
    allowed_match_count: float
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: ProfileContextAwareness
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
