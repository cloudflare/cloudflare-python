# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PredefinedUpdateParams", "Entry"]


class PredefinedUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    allowed_match_count: float
    """Related DLP policies will trigger when the match count exceeds the number set."""

    entries: Iterable[Entry]
    """The entries for this profile."""


class Entry(TypedDict, total=False):
    enabled: bool
    """Whether the entry is enabled or not."""
