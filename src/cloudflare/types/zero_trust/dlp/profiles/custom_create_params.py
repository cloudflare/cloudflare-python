# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAlias, Literal

from typing import Iterable, Optional, List, Union

from ..context_awareness_param import ContextAwarenessParam

from .pattern_param import PatternParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = [
    "CustomCreateParams",
    "Profile",
    "ProfileEntry",
    "ProfileEntryDLPNewCustomEntry",
    "ProfileEntryDLPNewWordListEntry",
    "ProfileSharedEntry",
    "ProfileSharedEntryCustom",
    "ProfileSharedEntryPredefined",
    "ProfileSharedEntryIntegration",
    "ProfileSharedEntryExactData",
]


class CustomCreateParams(TypedDict, total=False):
    account_id: Required[str]

    profiles: Required[Iterable[Profile]]


class ProfileEntryDLPNewCustomEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    pattern: Required[PatternParam]


class ProfileEntryDLPNewWordListEntry(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    words: Required[List[str]]


ProfileEntry: TypeAlias = Union[ProfileEntryDLPNewCustomEntry, ProfileEntryDLPNewWordListEntry]


class ProfileSharedEntryCustom(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["custom"]]


class ProfileSharedEntryPredefined(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["predefined"]]


class ProfileSharedEntryIntegration(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["integration"]]


class ProfileSharedEntryExactData(TypedDict, total=False):
    enabled: Required[bool]

    entry_id: Required[str]

    entry_type: Required[Literal["exact_data"]]


ProfileSharedEntry: TypeAlias = Union[
    ProfileSharedEntryCustom, ProfileSharedEntryPredefined, ProfileSharedEntryIntegration, ProfileSharedEntryExactData
]


class Profile(TypedDict, total=False):
    entries: Required[Iterable[ProfileEntry]]

    name: Required[str]

    allowed_match_count: int
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: ContextAwarenessParam
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    description: Optional[str]
    """The description of the profile"""

    ocr_enabled: bool

    shared_entries: Iterable[ProfileSharedEntry]
    """Entries from other profiles (e.g.

    pre-defined Cloudflare profiles, or your Microsoft Information Protection
    profiles).
    """
