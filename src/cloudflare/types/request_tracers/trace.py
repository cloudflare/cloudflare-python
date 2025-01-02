# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

from .trace_item import TraceItem

__all__ = ["Trace"]

Trace: TypeAlias = List[TraceItem]
