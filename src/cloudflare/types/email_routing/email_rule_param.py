# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .action_param import ActionParam
from .matcher_param import MatcherParam

__all__ = ["EmailRuleParam"]


class EmailRuleParam(TypedDict, total=False):
    actions: Iterable[ActionParam]
    """List actions patterns."""

    enabled: Literal[True, False]
    """Routing rule status."""

    matchers: Iterable[MatcherParam]
    """Matching patterns to forward to your actions."""

    name: str
    """Routing rule name."""

    priority: float
    """Priority of the routing rule."""
