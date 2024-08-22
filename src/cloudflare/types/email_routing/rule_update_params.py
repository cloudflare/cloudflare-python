# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable

from .action_param import ActionParam

from .matcher_param import MatcherParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["RuleUpdateParams"]

class RuleUpdateParams(TypedDict, total=False):
    zone_identifier: Required[str]
    """Identifier"""

    actions: Required[Iterable[ActionParam]]
    """List actions patterns."""

    matchers: Required[Iterable[MatcherParam]]
    """Matching patterns to forward to your actions."""

    enabled: Literal[True, False]
    """Routing rule status."""

    name: str
    """Routing rule name."""

    priority: float
    """Priority of the routing rule."""