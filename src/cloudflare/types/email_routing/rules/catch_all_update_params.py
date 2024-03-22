# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CatchAllUpdateParams", "Action", "Matcher"]


class CatchAllUpdateParams(TypedDict, total=False):
    actions: Required[Iterable[Action]]
    """List actions for the catch-all routing rule."""

    matchers: Required[Iterable[Matcher]]
    """List of matchers for the catch-all routing rule."""

    enabled: Literal[True, False]
    """Routing rule status."""

    name: str
    """Routing rule name."""


class Action(TypedDict, total=False):
    type: Required[Literal["drop", "forward", "worker"]]
    """Type of action for catch-all rule."""

    value: List[str]


class Matcher(TypedDict, total=False):
    type: Required[Literal["all"]]
    """Type of matcher. Default is 'all'."""
