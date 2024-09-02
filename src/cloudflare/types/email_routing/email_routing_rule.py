# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from .action import Action

from typing_extensions import Literal

from .matcher import Matcher

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["EmailRoutingRule"]


class EmailRoutingRule(BaseModel):
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
