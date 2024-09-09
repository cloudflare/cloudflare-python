# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .pattern_param import PatternParam
from ..context_awareness_param import ContextAwarenessParam

__all__ = [
    "CustomUpdateParams",
    "Entry",
    "EntryDLPNewCustomEntryWithID",
    "EntryDLPNewCustomEntry",
    "SharedEntry",
    "SharedEntryPredefined",
    "SharedEntryIntegration",
    "SharedEntryExactData",
]


class CustomUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    entries: Required[Iterable[Entry]]
    """Custom entries from this profile"""

    name: Required[str]

    allowed_match_count: Optional[int]

    context_awareness: ContextAwarenessParam
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    description: Optional[str]
    """The description of the profile"""

    ocr_enabled: bool

    shared_entries: Iterable[SharedEntry]
    """Other entries, e.g. predefined or integration."""


class EntryDLPNewCustomEntryWithID(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    name: Required[str]

    pattern: Required[PatternParam]


class EntryDLPNewCustomEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    pattern: Required[PatternParam]


Entry: TypeAlias = Union[EntryDLPNewCustomEntryWithID, EntryDLPNewCustomEntry]


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


SharedEntry: TypeAlias = Union[SharedEntryPredefined, SharedEntryIntegration, SharedEntryExactData]
