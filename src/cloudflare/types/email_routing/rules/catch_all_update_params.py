# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .catch_all_action_param import CatchAllActionParam
from .catch_all_matcher_param import CatchAllMatcherParam

__all__ = ["CatchAllUpdateParams"]


class CatchAllUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    actions: Required[Iterable[CatchAllActionParam]]
    """List actions for the catch-all routing rule."""

    matchers: Required[Iterable[CatchAllMatcherParam]]
    """List of matchers for the catch-all routing rule."""

    enabled: Literal[True, False]
    """Routing rule status."""

    name: str
    """Routing rule name."""
