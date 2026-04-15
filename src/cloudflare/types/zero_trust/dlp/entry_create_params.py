# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .profiles.pattern_param import PatternParam

__all__ = ["EntryCreateParams"]


class EntryCreateParams(TypedDict, total=False):
    account_id: str

    enabled: Required[bool]

    name: Required[str]

    pattern: Required[PatternParam]

    description: Optional[str]

    profile_id: str
