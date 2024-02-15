# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable, Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = [
    "CustomUpdateParams",
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

    description: str
    """The description of the profile."""

    entries: Iterable[Entry]
    """The custom entries for this profile.

    Array elements with IDs are modifying the existing entry with that ID. Elements
    without ID will create new entries. Any entry not in the list will be deleted.
    """

    name: str
    """The name of the profile."""

    shared_entries: Iterable[SharedEntry]
    """Entries from other profiles (e.g.

    pre-defined Cloudflare profiles, or your Microsoft Information Protection
    profiles).
    """


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
