# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable

from .catch_all_action_param import CatchAllActionParam

from .catch_all_matcher_param import CatchAllMatcherParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["CatchAllUpdateParams"]

class CatchAllUpdateParams(TypedDict, total=False):
    actions: Required[Iterable[CatchAllActionParam]]
    """List actions for the catch-all routing rule."""

    matchers: Required[Iterable[CatchAllMatcherParam]]
    """List of matchers for the catch-all routing rule."""

    enabled: Literal[True, False]
    """Routing rule status."""

    name: str
    """Routing rule name."""