# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "RuleEmailRoutingRoutingRulesListRoutingRulesResponse",
    "RuleEmailRoutingRoutingRulesListRoutingRulesResponseItem",
    "RuleEmailRoutingRoutingRulesListRoutingRulesResponseItemAction",
    "RuleEmailRoutingRoutingRulesListRoutingRulesResponseItemMatcher",
]


class RuleEmailRoutingRoutingRulesListRoutingRulesResponseItemAction(BaseModel):
    type: Literal["drop", "forward", "worker"]
    """Type of supported action."""

    value: List[str]


class RuleEmailRoutingRoutingRulesListRoutingRulesResponseItemMatcher(BaseModel):
    field: Literal["to"]
    """Field for type matcher."""

    type: Literal["literal"]
    """Type of matcher."""

    value: str
    """Value for matcher."""


class RuleEmailRoutingRoutingRulesListRoutingRulesResponseItem(BaseModel):
    id: Optional[str] = None
    """Routing rule identifier."""

    actions: Optional[List[RuleEmailRoutingRoutingRulesListRoutingRulesResponseItemAction]] = None
    """List actions patterns."""

    enabled: Optional[Literal[True, False]] = None
    """Routing rule status."""

    matchers: Optional[List[RuleEmailRoutingRoutingRulesListRoutingRulesResponseItemMatcher]] = None
    """Matching patterns to forward to your actions."""

    name: Optional[str] = None
    """Routing rule name."""

    priority: Optional[float] = None
    """Priority of the routing rule."""

    tag: Optional[str] = None
    """Routing rule tag. (Deprecated, replaced by routing rule identifier)"""


RuleEmailRoutingRoutingRulesListRoutingRulesResponse = List[RuleEmailRoutingRoutingRulesListRoutingRulesResponseItem]
