# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RuleUpdateParams", "Rule"]


class RuleUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Use this field to specify the unique ID of the zone."""

    rules: Required[Iterable[Rule]]
    """Lists snippet rules."""


class Rule(TypedDict, total=False):
    """Define a snippet rule."""

    expression: Required[str]
    """Define the expression that determines which traffic matches the rule."""

    snippet_name: Required[str]
    """Identify the snippet."""

    description: str
    """Provide an informative description of the rule."""

    enabled: bool
    """Indicate whether to execute the rule."""
