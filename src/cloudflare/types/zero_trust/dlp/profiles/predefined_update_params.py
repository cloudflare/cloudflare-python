# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..context_awareness_param import ContextAwarenessParam

__all__ = ["PredefinedUpdateParams", "Entry"]


class PredefinedUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    entries: Required[Iterable[Entry]]

    ai_context_enabled: bool

    allowed_match_count: Optional[int]

    confidence_threshold: Optional[str]

    context_awareness: ContextAwarenessParam
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    ocr_enabled: bool


class Entry(TypedDict, total=False):
    id: Required[str]

    enabled: Required[bool]
