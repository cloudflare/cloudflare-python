# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .action_param import ActionParam
from .matcher_param import MatcherParam

__all__ = ["CatchAllUpdateParams"]


class CatchAllUpdateParams(TypedDict, total=False):
    actions: Required[Iterable[ActionParam]]
    """List actions for the catch-all routing rule."""

    matchers: Required[Iterable[MatcherParam]]
    """List of matchers for the catch-all routing rule."""

    enabled: Literal[True, False]
    """Routing rule status."""

    name: str
    """Routing rule name."""
