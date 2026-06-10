# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SensitivityGroupUpdateParams", "Level"]


class SensitivityGroupUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    description: Optional[str]

    levels: Optional[Iterable[Level]]
    """The desired final state of levels.

    - `None` (omitted): no level changes.
    - `Some([])`: delete all levels.
    - `Some([...])`: desired final set + order.
    """

    name: Optional[str]


class Level(TypedDict, total=False):
    id: Optional[str]
    """If `None` (omitted), a new level will be created.

    Otherwise, an existing level will be updated.
    """

    description: Optional[str]

    name: Optional[str]
