# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .pattern_param import PatternParam
from ..context_awareness_param import ContextAwarenessParam

__all__ = [
    "CustomCreateParams",
    "Variant0",
    "Variant0Profile",
    "Variant0ProfileEntry",
    "Variant0ProfileEntryDLPNewCustomEntry",
    "Variant0ProfileEntryDLPNewWordListEntry",
    "Variant0ProfileSharedEntry",
    "Variant0ProfileSharedEntryUnionMember0",
    "Variant0ProfileSharedEntryUnionMember1",
    "Variant0ProfileSharedEntryUnionMember2",
    "Variant0ProfileSharedEntryUnionMember3",
    "DLPNewCustomProfile",
    "DLPNewCustomProfileEntry",
    "DLPNewCustomProfileEntryDLPNewCustomEntry",
    "DLPNewCustomProfileEntryDLPNewWordListEntry",
    "DLPNewCustomProfileSharedEntry",
    "DLPNewCustomProfileSharedEntryUnionMember0",
    "DLPNewCustomProfileSharedEntryUnionMember1",
    "DLPNewCustomProfileSharedEntryUnionMember2",
    "DLPNewCustomProfileSharedEntryUnionMember3",
]


class Variant0(TypedDict, total=False):
    account_id: Required[str]

    profiles: Required[Iterable[Variant0Profile]]


class Variant0ProfileEntryDLPNewCustomEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    pattern: Required[PatternParam]


class Variant0ProfileEntryDLPNewWordListEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    words: Required[List[str]]


Variant0ProfileEntry: TypeAlias = Union[Variant0ProfileEntryDLPNewCustomEntry, Variant0ProfileEntryDLPNewWordListEntry]


class Variant0ProfileSharedEntryUnionMember0(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["custom"]]


class Variant0ProfileSharedEntryUnionMember1(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["predefined"]]


class Variant0ProfileSharedEntryUnionMember2(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["integration"]]


class Variant0ProfileSharedEntryUnionMember3(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["exact_data"]]


Variant0ProfileSharedEntry: TypeAlias = Union[
    Variant0ProfileSharedEntryUnionMember0,
    Variant0ProfileSharedEntryUnionMember1,
    Variant0ProfileSharedEntryUnionMember2,
    Variant0ProfileSharedEntryUnionMember3,
]


class Variant0Profile(TypedDict, total=False):
    entries: Required[Iterable[Variant0ProfileEntry]]

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
    """The description of the profile"""

    ocr_enabled: bool

    shared_entries: Iterable[Variant0ProfileSharedEntry]
    """Entries from other profiles (e.g.

    pre-defined Cloudflare profiles, or your Microsoft Information Protection
    profiles).
    """


class DLPNewCustomProfile(TypedDict, total=False):
    account_id: Required[str]

    entries: Required[Iterable[DLPNewCustomProfileEntry]]

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
    """The description of the profile"""

    ocr_enabled: bool

    shared_entries: Iterable[DLPNewCustomProfileSharedEntry]
    """Entries from other profiles (e.g.

    pre-defined Cloudflare profiles, or your Microsoft Information Protection
    profiles).
    """


class DLPNewCustomProfileEntryDLPNewCustomEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    pattern: Required[PatternParam]


class DLPNewCustomProfileEntryDLPNewWordListEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    words: Required[List[str]]


DLPNewCustomProfileEntry: TypeAlias = Union[
    DLPNewCustomProfileEntryDLPNewCustomEntry, DLPNewCustomProfileEntryDLPNewWordListEntry
]


class DLPNewCustomProfileSharedEntryUnionMember0(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["custom"]]


class DLPNewCustomProfileSharedEntryUnionMember1(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["predefined"]]


class DLPNewCustomProfileSharedEntryUnionMember2(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["integration"]]


class DLPNewCustomProfileSharedEntryUnionMember3(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["exact_data"]]


DLPNewCustomProfileSharedEntry: TypeAlias = Union[
    DLPNewCustomProfileSharedEntryUnionMember0,
    DLPNewCustomProfileSharedEntryUnionMember1,
    DLPNewCustomProfileSharedEntryUnionMember2,
    DLPNewCustomProfileSharedEntryUnionMember3,
]

CustomCreateParams: TypeAlias = Union[Variant0, DLPNewCustomProfile]
