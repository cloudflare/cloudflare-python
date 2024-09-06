# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["RuleUpdateParams", "Rule"]


class RuleUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    rules: Iterable[Rule]
    """List of snippet rules"""


class Rule(TypedDict, total=False):
    description: str

    enabled: bool

    expression: str

    snippet_name: str
    """Snippet identifying name"""
