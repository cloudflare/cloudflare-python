# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ....._types import SequenceNotStr
from .pattern_param import PatternParam
from ..context_awareness_param import ContextAwarenessParam

__all__ = [
    "CustomUpdateParams",
    "Entry",
    "EntryDLPNewCustomEntryWithID",
    "EntryDLPNewCustomEntry",
    "SensitivityLevel",
    "SharedEntry",
]


class CustomUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    ai_context_enabled: bool

    allowed_match_count: Optional[int]

    confidence_threshold: Optional[str]

    context_awareness: ContextAwarenessParam
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    data_classes: Optional[SequenceNotStr[str]]
    """Data class IDs to associate with the profile.

    If omitted, existing associations are unchanged.
    """

    data_tags: Optional[SequenceNotStr[str]]
    """Data tag IDs to associate with the profile.

    If omitted, existing associations are unchanged.
    """

    description: Optional[str]
    """The description of the profile."""

    entries: Optional[Iterable[Entry]]
    """
    Custom entries from this profile. If this field is omitted, entries owned by
    this profile will not be changed.
    """

    ocr_enabled: bool

    sensitivity_levels: Optional[Iterable[SensitivityLevel]]
    """Sensitivity levels to associate with the profile.

    If omitted, existing associations are unchanged.
    """

    shared_entries: Iterable[SharedEntry]
    """Other entries, e.g. predefined or integration."""


class EntryDLPNewCustomEntryWithID(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    name: Required[str]

    pattern: Required[PatternParam]

    description: Optional[str]


class EntryDLPNewCustomEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    pattern: Required[PatternParam]

    description: Optional[str]


Entry: TypeAlias = Union[EntryDLPNewCustomEntryWithID, EntryDLPNewCustomEntry]


class SensitivityLevel(TypedDict, total=False):
    """
    A reference pairing a sensitivity group with a specific level within that group.
    """

    group_id: Required[str]

    level_id: Required[str]


class SharedEntry(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]
