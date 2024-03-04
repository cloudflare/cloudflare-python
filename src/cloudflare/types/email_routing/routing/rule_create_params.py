# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleCreateParams", "Action", "Matcher"]


class RuleCreateParams(TypedDict, total=False):
    actions: Required[Iterable[Action]]
    """List actions patterns."""

    matchers: Required[Iterable[Matcher]]
    """Matching patterns to forward to your actions."""

    enabled: Literal[True, False]
    """Routing rule status."""

    name: str
    """Routing rule name."""

    priority: float
    """Priority of the routing rule."""


class Action(TypedDict, total=False):
    type: Required[Literal["drop", "forward", "worker"]]
    """Type of supported action."""

    value: Required[List[str]]


class Matcher(TypedDict, total=False):
    field: Required[Literal["to"]]
    """Field for type matcher."""

    type: Required[Literal["literal"]]
    """Type of matcher."""

    value: Required[str]
    """Value for matcher."""
