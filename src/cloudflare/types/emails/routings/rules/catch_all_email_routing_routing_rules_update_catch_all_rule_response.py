# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = ["CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse", "Action", "Matcher"]


class Action(BaseModel):
    type: Literal["drop", "forward", "worker"]
    """Type of action for catch-all rule."""

    value: Optional[List[str]] = None


class Matcher(BaseModel):
    type: Literal["all"]
    """Type of matcher. Default is 'all'."""


class CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse(BaseModel):
    id: Optional[str] = None
    """Routing rule identifier."""

    actions: Optional[List[Action]] = None
    """List actions for the catch-all routing rule."""

    enabled: Optional[Literal[True, False]] = None
    """Routing rule status."""

    matchers: Optional[List[Matcher]] = None
    """List of matchers for the catch-all routing rule."""

    name: Optional[str] = None
    """Routing rule name."""

    tag: Optional[str] = None
    """Routing rule tag. (Deprecated, replaced by routing rule identifier)"""
