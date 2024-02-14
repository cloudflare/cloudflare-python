# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomDLPProfilesCreateCustomProfilesParams", "Profile", "ProfileEntry", "ProfileEntryPattern"]


class CustomDLPProfilesCreateCustomProfilesParams(TypedDict, total=False):
    profiles: Required[Iterable[Profile]]


class ProfileEntryPattern(TypedDict, total=False):
    regex: Required[str]
    """The regex pattern."""

    validation: Literal["luhn"]
    """Validation algorithm for the pattern.

    This algorithm will get run on potential matches, and if it returns false, the
    entry will not be matched.
    """


class ProfileEntry(TypedDict, total=False):
    enabled: Required[bool]
    """Whether the entry is enabled or not."""

    name: Required[str]
    """The name of the entry."""

    pattern: Required[ProfileEntryPattern]
    """A pattern that matches an entry"""


class Profile(TypedDict, total=False):
    allowed_match_count: float
    """Related DLP policies will trigger when the match count exceeds the number set."""

    description: str
    """The description of the profile."""

    entries: Iterable[ProfileEntry]
    """The entries for this profile."""

    name: str
    """The name of the profile."""
