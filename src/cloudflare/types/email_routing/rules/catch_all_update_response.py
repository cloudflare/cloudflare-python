# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from .catch_all_action import CatchAllAction

from typing_extensions import Literal

from .catch_all_matcher import CatchAllMatcher

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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