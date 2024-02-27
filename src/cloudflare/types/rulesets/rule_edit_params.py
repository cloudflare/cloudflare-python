# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["RuleEditParams", "Position", "PositionPosition"]


class RuleEditParams(TypedDict, total=False):
    account_id: Required[str]
    """The unique ID of the account."""

    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    position: Position
    """An object configuring where the rule will be placed."""


class PositionPosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class PositionPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class PositionPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


Position = Union[PositionPosition, PositionPosition, PositionPosition]
