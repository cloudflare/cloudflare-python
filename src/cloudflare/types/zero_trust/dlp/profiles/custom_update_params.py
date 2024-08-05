# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .pattern_param import PatternParam
from ..context_awareness_param import ContextAwarenessParam

__all__ = [
    "CustomUpdateParams",
    "Entry",
    "SharedEntry",
    "SharedEntryDLPSharedEntryUpdatePredefined",
    "SharedEntryDLPSharedEntryUpdateIntegration",
]


class CustomUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    allowed_match_count: float
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: ContextAwarenessParam
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


class Entry(TypedDict, total=False):
    enabled: bool
    """Whether the entry is enabled or not."""

    name: str
    """The name of the entry."""

    pattern: PatternParam
    """A pattern that matches an entry"""


class SharedEntryDLPSharedEntryUpdatePredefined(TypedDict, total=False):
    enabled: bool
    """Whether the entry is enabled or not."""


class SharedEntryDLPSharedEntryUpdateIntegration(TypedDict, total=False):
    enabled: bool
    """Whether the entry is enabled or not."""


SharedEntry: TypeAlias = Union[SharedEntryDLPSharedEntryUpdatePredefined, SharedEntryDLPSharedEntryUpdateIntegration]
