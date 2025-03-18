# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List
from typing_extensions import TypeAlias, TypeAliasType

from ..._compat import PYDANTIC_V2

__all__ = ["Trace"]

if TYPE_CHECKING or PYDANTIC_V2:
    Trace = TypeAliasType("Trace", List["TraceItem"])
else:
    Trace: TypeAlias = List["TraceItem"]

from .trace_item import TraceItem
