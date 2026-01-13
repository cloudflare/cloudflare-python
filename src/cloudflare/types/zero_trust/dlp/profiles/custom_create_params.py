# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ....._types import SequenceNotStr
from .pattern_param import PatternParam
from ..context_awareness_param import ContextAwarenessParam

__all__ = ["CustomCreateParams", "Entry", "EntryDLPNewCustomEntry", "EntryDLPNewWordListEntry", "SharedEntry"]


class CustomCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    ai_context_enabled: bool

    allowed_match_count: int
    """Related DLP policies will trigger when the match count exceeds the number set."""

    confidence_threshold: Optional[str]

    context_awareness: ContextAwarenessParam
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    description: Optional[str]
    """The description of the profile."""

    entries: Iterable[Entry]

    ocr_enabled: bool

    shared_entries: Iterable[SharedEntry]
    """Entries from other profiles (e.g.

    pre-defined Cloudflare profiles, or your Microsoft Information Protection
    profiles).
    """


class EntryDLPNewCustomEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    pattern: Required[PatternParam]


class EntryDLPNewWordListEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    words: Required[SequenceNotStr[str]]


Entry: TypeAlias = Union[EntryDLPNewCustomEntry, EntryDLPNewWordListEntry]


class SharedEntry(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]
