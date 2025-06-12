# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .pattern_param import PatternParam
from ..context_awareness_param import ContextAwarenessParam

__all__ = [
    "CustomCreateParams",
    "Entry",
    "EntryDLPNewCustomEntry",
    "EntryDLPNewWordListEntry",
    "SharedEntry",
    "SharedEntryCustom",
    "SharedEntryPredefined",
    "SharedEntryIntegration",
    "SharedEntryExactData",
]


class CustomCreateParams(TypedDict, total=False):
    account_id: Required[str]

    entries: Required[Iterable[Entry]]

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

    words: Required[List[str]]


Entry: TypeAlias = Union[EntryDLPNewCustomEntry, EntryDLPNewWordListEntry]


class SharedEntryCustom(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["custom"]]


class SharedEntryPredefined(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["predefined"]]


class SharedEntryIntegration(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["integration"]]


class SharedEntryExactData(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["exact_data"]]


SharedEntry: TypeAlias = Union[SharedEntryCustom, SharedEntryPredefined, SharedEntryIntegration, SharedEntryExactData]
