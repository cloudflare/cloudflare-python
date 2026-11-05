# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr
from ..profiles.pattern_param import PatternParam

__all__ = ["CustomCreateParams"]


class CustomCreateParams(TypedDict, total=False):
    account_id: Required[str]

    enabled: Required[bool]

    name: Required[str]

    pattern: Required[PatternParam]

    description: Optional[str]

    profile_id: str

    validator_ids: SequenceNotStr[str]
    """Validators the new entry should reference, by id, at most 10."""
