# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .action_item_param import ActionItemParam
from .matcher_item_param import MatcherItemParam

__all__ = ["RuleUpdateParams"]


class RuleUpdateParams(TypedDict, total=False):
    zone_identifier: Required[str]
    """Identifier"""

    actions: Required[Iterable[ActionItemParam]]
    """List actions patterns."""

    matchers: Required[Iterable[MatcherItemParam]]
    """Matching patterns to forward to your actions."""

    enabled: Literal[True, False]
    """Routing rule status."""

    name: str
    """Routing rule name."""

    priority: float
    """Priority of the routing rule."""
