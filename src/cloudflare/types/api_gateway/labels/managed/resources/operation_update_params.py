# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ......_types import SequenceNotStr

__all__ = ["OperationUpdateParams", "Selector", "SelectorInclude"]


class OperationUpdateParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    selector: Required[Selector]
    """Operation IDs selector"""


class SelectorInclude(TypedDict, total=False):
    operation_ids: Required[SequenceNotStr[str]]


class Selector(TypedDict, total=False):
    """Operation IDs selector"""

    include: Required[SelectorInclude]
