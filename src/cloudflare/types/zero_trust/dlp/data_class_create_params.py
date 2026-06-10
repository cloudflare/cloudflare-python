# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DataClassCreateParams", "SensitivityLevel"]


class DataClassCreateParams(TypedDict, total=False):
    account_id: Required[str]

    data_tags: Required[SequenceNotStr[str]]

    expression: Required[str]

    name: Required[str]

    sensitivity_levels: Required[Iterable[SensitivityLevel]]

    description: Optional[str]


class SensitivityLevel(TypedDict, total=False):
    """
    A reference pairing a sensitivity group with a specific level within that group.
    """

    group_id: Required[str]

    level_id: Required[str]
