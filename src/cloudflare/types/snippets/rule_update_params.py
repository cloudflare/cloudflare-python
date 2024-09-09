# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

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
