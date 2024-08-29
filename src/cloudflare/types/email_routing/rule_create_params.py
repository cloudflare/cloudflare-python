# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .action_param import ActionParam
from .matcher_param import MatcherParam

__all__ = ["RuleCreateParams"]


class RuleCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    actions: Required[Iterable[ActionParam]]
    """List actions patterns."""

    matchers: Required[Iterable[MatcherParam]]
    """Matching patterns to forward to your actions."""

    enabled: Literal[True, False]
    """Routing rule status."""

    name: str
    """Routing rule name."""

    priority: float
    """Priority of the routing rule."""
