# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleUpdateParams", "Body"]


class RuleUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    action: Required[Literal["bypass_waiting_room"]]
    """The action to take when the expression matches."""

    expression: Required[str]
    """Criteria defining when there is a match for the current rule."""

    description: str
    """The description of the rule."""

    enabled: bool
    """When set to true, the rule is enabled."""
