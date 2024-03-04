# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

__all__ = ["RuleCreateParams", "Position", "PositionBeforePosition", "PositionAfterPosition", "PositionIndexPosition"]


class RuleCreateParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    position: Position
    """An object configuring where the rule will be placed."""


class PositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class PositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class PositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


Position = Union[PositionBeforePosition, PositionAfterPosition, PositionIndexPosition]
