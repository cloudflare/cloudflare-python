# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CustomUpdateParams",
    "ContextAwareness",
    "ContextAwarenessSkip",
    "Entry",
    "EntryPattern",
    "SharedEntry",
    "SharedEntryDLPSharedEntryUpdatePredefined",
    "SharedEntryDLPSharedEntryUpdateIntegration",
]


class CustomUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    allowed_match_count: float
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: ContextAwareness
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    description: str
    """The description of the profile."""

    entries: Iterable[Entry]
    """The custom entries for this profile.

    Array elements with IDs are modifying the existing entry with that ID. Elements
    without ID will create new entries. Any entry not in the list will be deleted.
    """

    name: str
    """The name of the profile."""

    ocr_enabled: bool
    """If true, scan images via OCR to determine if any text present matches filters."""

    shared_entries: Iterable[SharedEntry]
    """Entries from other profiles (e.g.

    pre-defined Cloudflare profiles, or your Microsoft Information Protection
    profiles).
    """


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


class EntryPattern(TypedDict, total=False):
    regex: Required[str]
    """The regex pattern."""

    validation: Literal["luhn"]
    """Validation algorithm for the pattern.

    This algorithm will get run on potential matches, and if it returns false, the
    entry will not be matched.
    """


class Entry(TypedDict, total=False):
    enabled: bool
    """Whether the entry is enabled or not."""

    name: str
    """The name of the entry."""

    pattern: EntryPattern
    """A pattern that matches an entry"""

    profile_id: object
    """ID of the parent profile"""


class SharedEntryDLPSharedEntryUpdatePredefined(TypedDict, total=False):
    enabled: bool
    """Whether the entry is enabled or not."""


class SharedEntryDLPSharedEntryUpdateIntegration(TypedDict, total=False):
    enabled: bool
    """Whether the entry is enabled or not."""


SharedEntry = Union[SharedEntryDLPSharedEntryUpdatePredefined, SharedEntryDLPSharedEntryUpdateIntegration]
