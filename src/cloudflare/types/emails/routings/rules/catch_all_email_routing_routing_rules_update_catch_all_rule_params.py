# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable, List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo
from .....types import shared_params

__all__ = ["CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleParams", "Action", "Matcher"]


class CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleParams(TypedDict, total=False):
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
