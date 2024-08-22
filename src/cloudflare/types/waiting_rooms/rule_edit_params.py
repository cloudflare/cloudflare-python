# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["RuleEditParams", "Position", "PositionIndex", "PositionBefore", "PositionAfter"]


class RuleEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    waiting_room_id: Required[str]

    action: Required[Literal["bypass_waiting_room"]]
    """The action to take when the expression matches."""

    expression: Required[str]
    """Criteria defining when there is a match for the current rule."""

    description: str
    """The description of the rule."""

    enabled: bool
    """When set to true, the rule is enabled."""

    position: Position
    """Reorder the position of a rule"""


class PositionIndex(TypedDict, total=False):
    index: int
    """
    Places the rule in the exact position specified by the integer number
    <POSITION_NUMBER>. Position numbers start with 1. Existing rules in the ruleset
    from the specified position number onward are shifted one position (no rule is
    overwritten).
    """


class PositionBefore(TypedDict, total=False):
    before: str
    """Places the rule before rule <RULE_ID>.

    Use this argument with an empty rule ID value ("") to set the rule as the first
    rule in the ruleset.
    """


class PositionAfter(TypedDict, total=False):
    after: str
    """Places the rule after rule <RULE_ID>.

    Use this argument with an empty rule ID value ("") to set the rule as the last
    rule in the ruleset.
    """


Position: TypeAlias = Union[PositionIndex, PositionBefore, PositionAfter]
