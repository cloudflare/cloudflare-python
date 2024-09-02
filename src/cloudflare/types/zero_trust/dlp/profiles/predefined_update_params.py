# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable, Optional

from ..context_awareness_param import ContextAwarenessParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = ["PredefinedUpdateParams", "Entry"]


class PredefinedUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    entries: Required[Iterable[Entry]]

    allowed_match_count: Optional[int]

    context_awareness: ContextAwarenessParam
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    ocr_enabled: bool


class Entry(TypedDict, total=False):
    id: Required[str]

    enabled: Required[bool]
