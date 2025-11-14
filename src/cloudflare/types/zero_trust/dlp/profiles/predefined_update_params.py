# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["PredefinedUpdateParams", "Entry"]


class PredefinedUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    ai_context_enabled: bool

    allowed_match_count: Optional[int]

    confidence_threshold: Optional[str]

    enabled_entries: Optional[SequenceNotStr[str]]

    entries: Iterable[Entry]

    ocr_enabled: bool


class Entry(TypedDict, total=False):
    id: Required[str]

    enabled: Required[bool]
