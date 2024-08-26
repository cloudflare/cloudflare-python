# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .catch_all_action import CatchAllAction
from .catch_all_matcher import CatchAllMatcher

__all__ = ["CatchAllUpdateResponse"]


class CatchAllUpdateResponse(BaseModel):
    id: Optional[str] = None
    """Routing rule identifier."""

    actions: Optional[List[CatchAllAction]] = None
    """List actions for the catch-all routing rule."""

    enabled: Optional[Literal[True, False]] = None
    """Routing rule status."""

    matchers: Optional[List[CatchAllMatcher]] = None
    """List of matchers for the catch-all routing rule."""

    name: Optional[str] = None
    """Routing rule name."""

    tag: Optional[str] = None
    """Routing rule tag. (Deprecated, replaced by routing rule identifier)"""
