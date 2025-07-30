# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RuleUpdateParams", "Body"]


class RuleUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """The unique ID of the zone."""

    body: Required[Iterable[Body]]
    """A list of snippet rules."""


class Body(TypedDict, total=False):
    expression: Required[str]
    """The expression defining which traffic will match the rule."""

    snippet_name: Required[str]
    """The identifying name of the snippet."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""
