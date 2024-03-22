# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RuleUpdateResponse", "Action", "Matcher"]


class Action(BaseModel):
    type: Literal["drop", "forward", "worker"]
    """Type of supported action."""

    value: List[str]


class Matcher(BaseModel):
    field: Literal["to"]
    """Field for type matcher."""

    type: Literal["literal"]
    """Type of matcher."""

    value: str
    """Value for matcher."""


class RuleUpdateResponse(BaseModel):
    id: Optional[str] = None
    """Routing rule identifier."""

    actions: Optional[List[Action]] = None
    """List actions patterns."""

    enabled: Optional[Literal[True, False]] = None
    """Routing rule status."""

    matchers: Optional[List[Matcher]] = None
    """Matching patterns to forward to your actions."""

    name: Optional[str] = None
    """Routing rule name."""

    priority: Optional[float] = None
    """Priority of the routing rule."""

    tag: Optional[str] = None
    """Routing rule tag. (Deprecated, replaced by routing rule identifier)"""
