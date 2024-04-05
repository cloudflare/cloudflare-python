# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .action_item import ActionItem
from .matcher_item import MatcherItem

__all__ = ["Properties"]


class Properties(BaseModel):
    id: Optional[str] = None
    """Routing rule identifier."""

    actions: Optional[List[ActionItem]] = None
    """List actions patterns."""

    enabled: Optional[Literal[True, False]] = None
    """Routing rule status."""

    matchers: Optional[List[MatcherItem]] = None
    """Matching patterns to forward to your actions."""

    name: Optional[str] = None
    """Routing rule name."""

    priority: Optional[float] = None
    """Priority of the routing rule."""

    tag: Optional[str] = None
    """Routing rule tag. (Deprecated, replaced by routing rule identifier)"""
