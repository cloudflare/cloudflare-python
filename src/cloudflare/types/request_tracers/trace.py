# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAliasType

__all__ = ["Trace"]

Trace = TypeAliasType('Trace', List["TraceItem"])

from .trace_item import TraceItem
