# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["RuleParam"]


class RuleParam(TypedDict, total=False):
    id: str
    """The Web Analytics rule identifier."""

    host: str
    """The hostname the rule will be applied to."""

    inclusive: bool
    """Whether the rule includes or excludes traffic from being measured."""

    is_paused: bool
    """Whether the rule is paused or not."""

    paths: List[str]
    """The paths the rule will be applied to."""

    priority: float
