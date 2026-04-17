# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ....._types import SequenceNotStr
from .pattern_param import PatternParam
from ..context_awareness_param import ContextAwarenessParam

__all__ = [
    "CustomCreateParams",
    "Entry",
    "EntryDLPNewCustomEntry",
    "EntryDLPNewWordListEntry",
    "SensitivityLevel",
    "SharedEntry",
]


class CustomCreateParams(TypedDict, total=False):
    account_id: str

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

    data_classes: SequenceNotStr[str]
    """Data class IDs to associate with the profile."""

    data_tags: SequenceNotStr[str]
    """Data tag IDs to associate with the profile."""

    description: Optional[str]
    """The description of the profile."""

    entries: Iterable[Entry]

    ocr_enabled: bool

    sensitivity_levels: Iterable[SensitivityLevel]
    """Sensitivity levels to associate with the profile."""

    shared_entries: Iterable[SharedEntry]
    """Entries from other profiles (e.g.

    pre-defined Cloudflare profiles, or your Microsoft Information Protection
    profiles).
    """


class EntryDLPNewCustomEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    pattern: Required[PatternParam]

    description: Optional[str]


class EntryDLPNewWordListEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    words: Required[SequenceNotStr[str]]


Entry: TypeAlias = Union[EntryDLPNewCustomEntry, EntryDLPNewWordListEntry]


class SensitivityLevel(TypedDict, total=False):
    """
    A reference pairing a sensitivity group with a specific level within that group.
    """

    group_id: Required[str]

    level_id: Required[str]


class SharedEntry(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]
