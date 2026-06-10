# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DataClassUpdateParams", "SensitivityLevel"]


class DataClassUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    data_tags: Optional[SequenceNotStr[str]]

    description: Optional[str]

    expression: Optional[str]

    name: Optional[str]

    sensitivity_levels: Optional[Iterable[SensitivityLevel]]


class SensitivityLevel(TypedDict, total=False):
    """
    A reference pairing a sensitivity group with a specific level within that group.
    """

    group_id: Required[str]

    level_id: Required[str]
